#!/usr/bin/env python3
"""Build reproducible installable ZIP packages for Academic Colombia Skills.

Canonical inputs:
    skills/<skill-name>/

Generated outputs:
    dist/individual/<skill-name>.zip
    dist/academic-colombia-skills-bundle-<VERSION>.zip

Generated artifacts are disposable build outputs and must not become a second
source of truth.
"""

from __future__ import annotations

import shutil
import tempfile
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
DIST_DIR = ROOT / "dist"
INDIVIDUAL_DIR = DIST_DIR / "individual"
VERSION_FILE = ROOT / "VERSION"


def skill_dirs() -> list[Path]:
    skills = []
    for path in sorted(SKILLS_DIR.iterdir()):
        if path.is_dir() and (path / "SKILL.md").is_file():
            skills.append(path)
    return skills


def add_tree(zf: zipfile.ZipFile, source: Path, arc_root: Path) -> None:
    for path in sorted(source.rglob("*")):
        if not path.is_file():
            continue
        relative = path.relative_to(source)
        zf.write(path, (arc_root / relative).as_posix())


def build_individual(skill: Path) -> Path:
    output = INDIVIDUAL_DIR / f"{skill.name}.zip"
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        add_tree(zf, skill, Path(skill.name))
    return output


def build_bundle(version: str, packages: list[Path]) -> Path:
    output = DIST_DIR / f"academic-colombia-skills-bundle-{version}.zip"
    with tempfile.TemporaryDirectory() as tmp:
        staging = Path(tmp) / f"academic-colombia-skills-{version}"
        package_dir = staging / "individual"
        package_dir.mkdir(parents=True)

        for package in packages:
            shutil.copy2(package, package_dir / package.name)

        for doc in [
            ROOT / "distribution" / "README.md",
            ROOT / "distribution" / "SKILLS-MANIFEST.md",
            ROOT / "distribution" / "INSTALL-CHATGPT-SKILLS.md",
            ROOT / "LICENSE",
            ROOT / "docs" / "LICENSE-SCOPE.md",
        ]:
            if doc.is_file():
                target = staging / doc.name
                if doc.name == "LICENSE-SCOPE.md":
                    target = staging / "LICENSE-SCOPE.md"
                shutil.copy2(doc, target)

        with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED) as zf:
            add_tree(zf, staging, Path(staging.name))

    return output


def main() -> None:
    if not VERSION_FILE.is_file():
        raise SystemExit("VERSION file not found")

    version = VERSION_FILE.read_text(encoding="utf-8").strip()
    skills = skill_dirs()

    if not skills:
        raise SystemExit("No skills with SKILL.md found")

    DIST_DIR.mkdir(exist_ok=True)
    INDIVIDUAL_DIR.mkdir(parents=True, exist_ok=True)

    packages = [build_individual(skill) for skill in skills]
    bundle = build_bundle(version, packages)

    print(f"Packaged {len(packages)} skills")
    print(f"Individual packages: {INDIVIDUAL_DIR}")
    print(f"Bundle: {bundle}")


if __name__ == "__main__":
    main()
