#!/usr/bin/env python3
"""Validate structural consistency of the Academic Colombia declarative framework.

This is repository linting, not execution of the academic workflow itself.
The validator uses only the Python standard library.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_ROOT = [
    "README.md",
    "VERSION",
    "CHANGELOG.md",
    "LICENSE",
    "CONTRIBUTING.md",
    "core/CORE.md",
    "core/APA7.md",
    "core/ORCHESTRATION.md",
    "core/SKILL-CONTRACT.md",
    "quality/ACADEMIC-QA.md",
    "distribution/SKILLS-MANIFEST.md",
]

CONTRACT_MARKERS = ["Skill Contract v1", "critical_gate"]
MARKDOWN_LINK = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")
VERSION_RE = re.compile(r"^\d+\.\d+\.\d+$")
CHANGELOG_VERSION_RE = re.compile(r"^##\s+(\d+\.\d+\.\d+)\b", re.MULTILINE)
MANIFEST_SKILL_RE = re.compile(r"`skills/([^/]+)/SKILL\.md`")
REGISTRY_CLASS_RE = re.compile(r"^- \*\*([A-E])\*\*\s+—\s+(.+)$", re.MULTILINE)


def error(errors: list[str], message: str) -> None:
    errors.append(message)


def validate_required_files(errors: list[str]) -> None:
    for rel in REQUIRED_ROOT:
        if not (ROOT / rel).is_file():
            error(errors, f"missing required file: {rel}")


def validate_version(errors: list[str]) -> str | None:
    version_file = ROOT / "VERSION"
    changelog = ROOT / "CHANGELOG.md"
    if not version_file.is_file() or not changelog.is_file():
        return None
    version = version_file.read_text(encoding="utf-8").strip()
    if not VERSION_RE.fullmatch(version):
        error(errors, f"VERSION is not SemVer-like x.y.z: {version!r}")
        return version
    text = changelog.read_text(encoding="utf-8")
    match = CHANGELOG_VERSION_RE.search(text)
    if not match:
        error(errors, "CHANGELOG.md has no version heading")
    elif match.group(1) != version:
        error(errors, f"VERSION ({version}) != first CHANGELOG version ({match.group(1)})")
    return version


def skill_directories() -> dict[str, Path]:
    skills_root = ROOT / "skills"
    if not skills_root.is_dir():
        return {}
    return {path.name: path for path in sorted(skills_root.iterdir()) if path.is_dir()}


def validate_skills(errors: list[str]) -> set[str]:
    dirs = skill_directories()
    if not dirs:
        error(errors, "skills/ contains no skill directories")
        return set()
    valid_names: set[str] = set()
    for name, path in dirs.items():
        skill_file = path / "SKILL.md"
        if not skill_file.is_file():
            error(errors, f"skill directory missing SKILL.md: skills/{name}")
            continue
        text = skill_file.read_text(encoding="utf-8")
        first_heading = next((line.strip() for line in text.splitlines() if line.strip()), "")
        if first_heading != f"# {name}":
            error(errors, f"skill heading mismatch in skills/{name}/SKILL.md: {first_heading!r}")
        for marker in CONTRACT_MARKERS:
            if marker not in text:
                error(errors, f"skill missing contract marker {marker!r}: {name}")
        valid_names.add(name)
    return valid_names


def validate_manifest(errors: list[str], skill_names: set[str]) -> None:
    manifest = ROOT / "distribution" / "SKILLS-MANIFEST.md"
    if not manifest.is_file():
        return
    manifest_names = {
        name for name in MANIFEST_SKILL_RE.findall(manifest.read_text(encoding="utf-8"))
        if "<" not in name and ">" not in name
    }
    missing = sorted(skill_names - manifest_names)
    stale = sorted(manifest_names - skill_names)
    if missing:
        error(errors, f"skills missing from distribution manifest: {', '.join(missing)}")
    if stale:
        error(errors, f"manifest references nonexistent skills: {', '.join(stale)}")


def normalize_link_target(raw: str) -> str:
    target = raw.strip()
    if " " in target and not target.startswith("<"):
        target = target.split(" ", 1)[0]
    target = target.strip("<>")
    return unquote(target.split("#", 1)[0])


def validate_markdown_links(errors: list[str]) -> None:
    for md in ROOT.rglob("*.md"):
        if any(part in {".git", "dist"} for part in md.parts):
            continue
        for raw in MARKDOWN_LINK.findall(md.read_text(encoding="utf-8")):
            target = normalize_link_target(raw)
            if not target:
                continue
            if target.lower().startswith(("http://", "https://", "mailto:", "tel:", "data:")):
                continue
            candidate = ROOT / target.lstrip("/") if target.startswith("/") else (md.parent / target).resolve()
            try:
                candidate.relative_to(ROOT.resolve())
            except ValueError:
                error(errors, f"link escapes repository: {md.relative_to(ROOT)} -> {raw}")
                continue
            if not candidate.exists():
                error(errors, f"broken internal link: {md.relative_to(ROOT)} -> {raw}")


def validate_external_registry(errors: list[str]) -> None:
    registry = ROOT / "external-references" / "REGISTRY.md"
    if not registry.is_file():
        error(errors, "missing external-references/REGISTRY.md")
        return
    classes = {label: description.strip() for label, description in REGISTRY_CLASS_RE.findall(registry.read_text(encoding="utf-8"))}
    if set(classes) != set("ABCDE"):
        error(errors, f"external registry must define canonical classes A-E exactly once; found {sorted(classes)}")
    for label, description in classes.items():
        if len(description) < 12:
            error(errors, f"external registry class {label} has an incomplete description")


def validate_distribution(errors: list[str]) -> None:
    if not (ROOT / "scripts" / "package_skills.py").is_file():
        error(errors, "missing scripts/package_skills.py")
    gitignore = ROOT / ".gitignore"
    if not gitignore.is_file() or "dist/" not in gitignore.read_text(encoding="utf-8"):
        error(errors, "generated dist/ is not ignored")


def main() -> int:
    errors: list[str] = []
    validate_required_files(errors)
    version = validate_version(errors)
    skills = validate_skills(errors)
    validate_manifest(errors, skills)
    validate_markdown_links(errors)
    validate_external_registry(errors)
    validate_distribution(errors)
    print("Academic Colombia repository validation")
    print(f"version: {version or 'unknown'}")
    print(f"skills discovered: {len(skills)}")
    if errors:
        print(f"FAIL: {len(errors)} issue(s)")
        for item in errors:
            print(f"- {item}")
        return 1
    print("PASS: declarative repository structure is consistent")
    return 0


if __name__ == "__main__":
    sys.exit(main())
