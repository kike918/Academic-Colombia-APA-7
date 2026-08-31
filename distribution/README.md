# Academic Colombia — Skills Distribution

This directory defines how the native Academic Colombia skills are packaged for installation and replication.

## Distribution principle

The canonical source remains:

`skills/<skill-name>/SKILL.md`

Packaged ZIP files are generated artifacts. They must not become a second source of truth and are not committed to `main`.

## Supported package forms

OpenAI currently supports creating a Skill from a directory upload or a single ZIP file. Academic Colombia therefore distributes each native skill as:

```text
<skill-name>/
└── SKILL.md
```

or:

```text
<skill-name>.zip
└── <skill-name>/
    └── SKILL.md
```

A complete bundle may also contain all native skill packages plus installation documentation.

## Build packages

From the repository root:

```bash
python scripts/package_skills.py
```

The script writes generated artifacts under:

```text
dist/
├── individual/
│   ├── academic-artifact-validator.zip
│   ├── academic-citation-manager.zip
│   └── ...
└── academic-colombia-skills-bundle-<VERSION>.zip
```

`dist/` is a build output and should not be treated as canonical content.

## Installation

See [`INSTALL-CHATGPT-SKILLS.md`](INSTALL-CHATGPT-SKILLS.md).

## Package manifest

See [`SKILLS-MANIFEST.md`](SKILLS-MANIFEST.md) for the current native skill inventory and required files.

## Trust and review

Before installing Skills from any source:

- verify the repository origin;
- inspect `SKILL.md` and any supporting files;
- confirm the release/version;
- review external dependencies if a future Skill contains scripts or code;
- do not assume that a ZIP named Academic Colombia is an official package unless it can be traced to this repository or an authorized release.

## Licensing

Original Academic Colombia content is distributed under the repository MIT License. External and institutional materials retain their own rights and conditions. See `LICENSE` and `docs/LICENSE-SCOPE.md`.
