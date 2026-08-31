# Skills Distribution Manifest

Academic Colombia currently distributes **16 native Skills**.

Each canonical Skill lives at `skills/<name>/SKILL.md` and must be packaged from that source.

| # | Skill | Canonical path |
|---:|---|---|
| 1 | `academic-workflow-orchestrator` | `skills/academic-workflow-orchestrator/SKILL.md` |
| 2 | `academic-requirements-analyzer` | `skills/academic-requirements-analyzer/SKILL.md` |
| 3 | `academic-template-selector` | `skills/academic-template-selector/SKILL.md` |
| 4 | `academic-research-ideation` | `skills/academic-research-ideation/SKILL.md` |
| 5 | `academic-source-evaluator` | `skills/academic-source-evaluator/SKILL.md` |
| 6 | `academic-evidence-mapper` | `skills/academic-evidence-mapper/SKILL.md` |
| 7 | `academic-citation-manager` | `skills/academic-citation-manager/SKILL.md` |
| 8 | `academic-statistical-analysis` | `skills/academic-statistical-analysis/SKILL.md` |
| 9 | `academic-critical-review` | `skills/academic-critical-review/SKILL.md` |
| 10 | `apa7-academic-style` | `skills/apa7-academic-style/SKILL.md` |
| 11 | `academic-tables-figures` | `skills/academic-tables-figures/SKILL.md` |
| 12 | `academic-artifact-validator` | `skills/academic-artifact-validator/SKILL.md` |
| 13 | `academic-document-auditor` | `skills/academic-document-auditor/SKILL.md` |
| 14 | `academic-document-repair` | `skills/academic-document-repair/SKILL.md` |
| 15 | `academic-final-review` | `skills/academic-final-review/SKILL.md` |
| 16 | `external-reference-resolver` | `skills/external-reference-resolver/SKILL.md` |

## Required package invariant

For every native Skill:

1. the canonical directory exists under `skills/`;
2. the directory contains `SKILL.md`;
3. `SKILL.md` remains compatible with `core/SKILL-CONTRACT.md`;
4. generated packages preserve the Skill directory name;
5. generated ZIPs do not alter the canonical Markdown;
6. release/version provenance is documented outside the Skill body rather than injected into its academic behavior.

## Recommended installation order

Skills are modular and may be installed independently. For a full Academic Colombia installation, install all 16.

The orchestrator should be installed together with the specialized Skills it may route to. Installing only `academic-workflow-orchestrator` does not recreate missing specialized capabilities.

## Platform-neutral note

This manifest describes the distribution inventory, not a ChatGPT-only behavior layer. Platform-specific setup remains under `platforms/`.
