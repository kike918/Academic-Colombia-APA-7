# Skill Distribution — Acceptance Cases

## SD-01 Canonical source
Input: build packages from repository.
Expected: every package is generated from `skills/<name>/` and no package becomes canonical.

## SD-02 Native inventory
Input: current repository with 16 native Skills.
Expected: packager produces 16 individual ZIP files.

## SD-03 Required SKILL.md
Input: a directory under `skills/` without `SKILL.md`.
Expected: directory is not treated as an installable Skill.

## SD-04 Directory preservation
Input: `academic-citation-manager`.
Expected ZIP layout:
`academic-citation-manager/SKILL.md`.

## SD-05 Full bundle
Input: package all Skills.
Expected: bundle includes individual Skill ZIPs, manifest, installation guide, MIT license and license scope.

## SD-06 Generated artifacts
Input: run packaging script.
Expected: output is written only under `dist/` and `dist/` is ignored by Git.

## SD-07 Selective installation
Input: user installs only `academic-citation-manager`.
Expected: documentation does not claim full Academic Colombia orchestration coverage.

## SD-08 Orchestrator dependency semantics
Input: user installs orchestrator but omits specialized Skills.
Expected: documentation warns that missing capabilities are not recreated by the orchestrator.

## SD-09 Version provenance
Input: build bundle.
Expected: bundle filename derives from root `VERSION`.

## SD-10 External package trust
Input: third-party ZIP named Academic Colombia.
Expected: installation guide instructs verification of source, contents and provenance before installation.

## SD-11 Platform separation
Input: build distribution packages.
Expected: packages contain canonical Skills; ChatGPT-specific Custom GPT instructions remain under `platforms/chatgpt-gpt/` and are not injected into every Skill package.

## SD-12 License boundary
Input: bundle distribution.
Expected: MIT license and `LICENSE-SCOPE.md` are included without relicensing external/institutional material.
