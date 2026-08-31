# ChatGPT Installation Guide

## Objective

Install Academic Colombia as a ChatGPT Custom GPT without copying the entire repository into one monolithic prompt.

The canonical source remains the GitHub repository. The GPT is a deployment package derived from it.

## 1. Create the GPT

Suggested name:

`Academic Colombia — APA 7 | UNAD | SENA`

Suggested description:

`Framework académico para analizar guías y rúbricas, investigar con trazabilidad, aplicar reglas institucionales/APA y auditar entregables académicos en contextos colombianos.`

## 2. Configure Instructions

Copy the complete contents of:

`platforms/chatgpt-gpt/INSTRUCTIONS.md`

into the GPT Instructions field.

Do not append full skill files to the Instructions field. Skills and reference rules belong in Knowledge.

## 3. Add Knowledge

Use `platforms/chatgpt-gpt/KNOWLEDGE_MANIFEST.md` as the packaging authority.

Minimum recommended package:

```text
core/CORE.md
core/ORCHESTRATION.md
core/SKILL-CONTRACT.md
quality/ACADEMIC-QA.md
docs/SKILLS-DIRECTORY.md
core/APA7.md
institutions/UNAD.md
institutions/SENA.md
skills/academic-workflow-orchestrator/SKILL.md
skills/academic-requirements-analyzer/SKILL.md
skills/academic-source-evaluator/SKILL.md
skills/academic-evidence-mapper/SKILL.md
skills/academic-citation-manager/SKILL.md
skills/academic-artifact-validator/SKILL.md
skills/academic-final-review/SKILL.md
```

For full-framework deployment, add the remaining native skills and specialist core files listed by the manifest.

## 4. Capabilities

Enable only the capabilities useful for academic work available in the product configuration being used.

Recommended where available:

- web research for current/verify-required claims;
- file analysis for guides, rubrics and artifacts;
- data analysis for quantitative assignments;
- image generation only when an activity actually requires a visual artifact.

The platform capability does not replace Academic Colombia's evidence or QA rules.

## 5. Task-scoped materials

For each academic task, upload or provide when available:

1. activity guide;
2. rubric/evaluation instrument;
3. tutor instructions;
4. required template;
5. source materials;
6. current draft/artifact when revising existing work.

Do not add these task-specific files to permanent GPT Knowledge by default.

## 6. Expected first behavior

When a guide/rubric is supplied, the GPT should first resolve:

- institution;
- evidence/deliverable;
- learning outcome or competency when available;
- mandatory requirements;
- rubric criteria;
- artifact type;
- missing inputs;
- minimal sufficient workflow.

It should not immediately generate a long generic academic paper unless that is what the task actually requires.

## 7. Public vs internal output

The system may use Skill Contract fields internally to preserve routing and gates.

The user-facing answer should normally present natural academic assistance rather than raw envelopes such as:

```yaml
status: partial
critical_gate: fail
```

Expose those fields only when they improve an audit/debug/maintainer workflow.

## 8. Acceptance test before publishing

Run the scenarios in:

- `tests/CHATGPT_ADAPTER_CASES.md`
- `tests/CHATGPT_ADVERSARIAL_CASES.md`

Do not publish the deployment as production-ready if critical cases fail.

## 9. Update procedure

When the repository changes:

```text
canonical repo change
      ↓
version + changelog
      ↓
review Knowledge Manifest impact
      ↓
update GPT Knowledge files if needed
      ↓
update Instructions only if behavior changed
      ↓
run ChatGPT acceptance cases
      ↓
publish/update deployment
```

## Installation principle

**Instructions control behavior; Knowledge provides canonical rules; task files provide local authority.**
