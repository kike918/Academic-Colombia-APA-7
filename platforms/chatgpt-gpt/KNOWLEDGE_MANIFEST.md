# ChatGPT Knowledge Manifest

## Purpose

Define which Academic Colombia files should be made available to a ChatGPT Custom GPT, which rules belong in Instructions, and which materials should remain task-scoped instead of permanent Knowledge.

This manifest is a platform adapter. It does not replace the canonical rules in `core/`, `institutions/`, `skills/`, `quality/`, or `external-references/`.

## Loading principles

1. Keep permanent Instructions compact and behavioral.
2. Put stable reference material in Knowledge instead of duplicating it in Instructions.
3. Treat activity guides, rubrics, teacher messages and student artifacts as conversation/task inputs, not permanent Knowledge.
4. Load institutional or specialist material only when it can materially affect the answer.
5. Preserve the canonical authority hierarchy from the core.
6. Do not expose internal routing/envelope details to the end user unless they help explain a result.

## Tier 0 — Instructions layer

These concepts should be represented directly in `INSTRUCTIONS.md` because they govern every interaction:

- role and scope of Academic Colombia;
- authority hierarchy;
- no fabricated evidence or bibliographic metadata;
- artifact-sensitive behavior;
- conditional routing instead of running every skill;
- critical-gate behavior;
- requirement that final readiness comes from final review;
- task files outrank generic institutional/APA rules when authority requires it.

Do not paste full skill definitions into Instructions.

## Tier 1 — Always-available Knowledge

Recommended core package:

- `core/CORE.md`
- `core/ORCHESTRATION.md`
- `core/SKILL-CONTRACT.md`
- `quality/ACADEMIC-QA.md`
- `docs/SKILLS-DIRECTORY.md`

Purpose:
- establish system semantics;
- route to the correct capability;
- propagate gaps and critical gates;
- provide a human-readable capability catalog;
- define READY / NOT READY behavior.

## Tier 2 — Academic rules and institutional profiles

Recommended Knowledge:

- `core/APA7.md`
- `core/AI-USAGE-AND-CITATION.md`
- `core/LEGAL-COLOMBIA.md`
- `institutions/UNAD.md`
- `institutions/SENA.md`
- `templates/UNAD-TEMPLATE-PROFILE.md`

These files are consulted when relevant to the task. They must not override a higher-authority activity guide or rubric.

## Tier 3 — Native skills

Recommended Knowledge:

- `skills/academic-workflow-orchestrator/SKILL.md`
- `skills/academic-requirements-analyzer/SKILL.md`
- `skills/academic-template-selector/SKILL.md`
- `skills/academic-research-ideation/SKILL.md`
- `skills/academic-source-evaluator/SKILL.md`
- `skills/academic-evidence-mapper/SKILL.md`
- `skills/academic-citation-manager/SKILL.md`
- `skills/academic-statistical-analysis/SKILL.md`
- `skills/academic-critical-review/SKILL.md`
- `skills/apa7-academic-style/SKILL.md`
- `skills/academic-tables-figures/SKILL.md`
- `skills/academic-artifact-validator/SKILL.md`
- `skills/academic-document-auditor/SKILL.md`
- `skills/academic-document-repair/SKILL.md`
- `skills/academic-final-review/SKILL.md`
- `skills/external-reference-resolver/SKILL.md`

If platform constraints require a smaller package, prioritize the orchestrator plus only the skills used by the intended deployment profile. Do not silently remove capabilities while claiming full-framework coverage.

## Tier 4 — Controlled external-reference policy

Recommended Knowledge:

- `external-references/REGISTRY.md`
- `docs/EXTERNAL-REFERENCES.md`
- `docs/EXTERNAL-SOURCE-EVALUATION.md`

External references are fallback material only. Native coverage is preferred when sufficient.

## Tier 5 — Validation material

Recommended for maintainers and acceptance testing, not necessarily permanent end-user Knowledge:

- `tests/APA_ENGINE_CASES.md`
- `tests/UNAD_COMPATIBILITY_CASES.md`
- `tests/TEMPLATE_COMPATIBILITY_CASES.md`
- `tests/ARTIFACT_VALIDATION_CASES.md`
- `tests/RESEARCH_SKILLS_CASES.md`
- `tests/EXTERNAL_REFERENCE_CASES.md`
- `tests/DOCUMENT_AUDIT_REPAIR_CASES.md`
- `tests/SKILL_CONTRACT_CASES.md`
- `tests/ORCHESTRATION_ROUTING_CASES.md`
- `tests/E2E_ACCEPTANCE_CASES.md`
- `tests/CHATGPT_ADAPTER_CASES.md`
- `tests/CHATGPT_ADVERSARIAL_CASES.md`

These files are acceptance specifications. They are not evidence sources for academic claims.

## Task-scoped files — never permanent by default

Do not add the following to persistent GPT Knowledge unless they have been deliberately anonymized and promoted into canonical tests/examples:

- a student's assignment guide for one course;
- a specific rubric from one activity;
- teacher messages for one class;
- student submissions;
- grades or feedback tied to an identifiable student;
- private institutional files;
- client/company documents used only for one assignment.

Load them in the conversation/project where they apply.

## Retrieval order for a typical activity

```text
user request / uploaded files
      ↓
activity guide + rubric + tutor instruction
      ↓
CORE / ORCHESTRATION / SKILL-CONTRACT
      ↓
institutional profile when relevant
      ↓
selected native skills
      ↓
APA / legal / statistical specialist rules when relevant
      ↓
external fallback only for a real capability gap
      ↓
final QA
```

## Context-budget rule

Do not maximize the number of files consulted. Maximize the relevance of the context.

The adapter should prefer:

```text
minimum sufficient context
      +
explicit routing
      +
verified evidence
```

over loading the entire repository into every interaction.

## Maintenance

Whenever the core, skill catalog or routing semantics change:

1. update canonical files first;
2. update this manifest only if the ChatGPT packaging strategy changes;
3. update `INSTRUCTIONS.md` only when platform-level behavior must change;
4. add or update ChatGPT acceptance cases;
5. record behavioral impact in `CHANGELOG.md`.
