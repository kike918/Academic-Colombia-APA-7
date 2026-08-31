# Academic Colombia v1.0.0

Academic Colombia v1.0.0 is the first stable release of the modular, declarative academic-agent framework for Colombian higher education workflows.

## What v1 stabilizes

- 16 native Skills.
- Skill Contract v1.
- Authority hierarchy and routing semantics.
- Evidence chain: claim → evidence → source → citation.
- Critical gates and final readiness model.
- UNAD and SENA institutional profiles with bounded empirical coverage.
- APA 7 academic style engine.
- Artifact-aware validation.
- Document audit and repair workflow.
- Controlled external-reference fallback.
- ChatGPT and Gemini static adapters.
- Reproducible Skill distribution.
- Declarative repository CI.
- Semantic compatibility/release policy.

## Why this is a stable release

The framework has moved beyond prompt design into a versioned declarative system with:

- explicit contracts;
- routing;
- acceptance suites;
- adversarial cases;
- empirical evidence;
- repository governance;
- distribution and adapters.

Real anonymized academic artifacts were used to validate both successful and failing behavior.

Examples include:

- DOCX audit and repair;
- SENA financial analysis and cross-artifact consistency;
- UNAD trade/economics papers;
- technical smart-contract design;
- visual academic presentations;
- current-fact/freshness checks;
- a native XLSX accounting workbook reconciled across journal, T-accounts, trial balance and SIIGO.

The negative cases are intentional evidence: polished artifacts with weak sourcing, stale data, semantic misuse of valid numbers or methodology problems must still be capable of ending `NOT READY`.

## Stable public contracts

Starting in v1:

- Skill Contract v1 is stable.
- `READY / NOT READY / USER DECISION REQUIRED` semantics are stable.
- critical-gate propagation is stable.
- GitHub `main` is the canonical source.
- platform adapters cannot silently redefine the core.
- native Skills remain packaged from `skills/<skill-name>/SKILL.md`.

See `docs/COMPATIBILITY-POLICY.md`.

## Coverage boundaries

v1.0.0 does **not** claim exhaustive validation for every possible environment.

Still not claimed as runtime-validated:

- native PPTX editing/runtime path;
- full video playback/audio/duration validation;
- a real inferential-statistics dataset E2E;
- deployed Custom GPT runtime acceptance;
- deployed Gemini Gem runtime acceptance.

These are explicit coverage boundaries rather than blockers to the stable core release.

## Installation / reuse

### Skills

Use `distribution/INSTALL-CHATGPT-SKILLS.md` and build packages from the canonical source with:

```bash
python scripts/package_skills.py
```

### ChatGPT adapter

See:

`platforms/chatgpt-gpt/INSTALLATION.md`

### Gemini adapter

See:

`platforms/gemini/INSTALLATION.md`

## Governance

`main` is protected by pull-request and linear-history rules with conversation resolution and no bypass actors.

Declarative CI is stable and should be configured as a required status check for `main` at release time.

Historical merged feature branches may be deleted after release; they are not release dependencies.

## License

Original Academic Colombia content is MIT licensed. Third-party and institutional materials retain their own rights and conditions.

See `LICENSE` and `docs/LICENSE-SCOPE.md`.

## Post-v1

v1.x development should be backward-compatible and evidence-driven.

Priorities include real platform-runtime acceptance, additional empirical artifact coverage and institutional freshness maintenance rather than reopening the stable core without demonstrated need.
