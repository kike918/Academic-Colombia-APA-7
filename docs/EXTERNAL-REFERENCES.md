# External References and Fallback Policy

## Purpose

Academic Colombia uses internal skills as the primary execution layer. External references are a controlled fallback when internal skills do not fully cover the requirements of a document, analysis, artifact, or evaluation task.

External references are not automatically normative authorities. Their role may be:

- methodological reference;
- workflow reference;
- technical implementation reference;
- domain-specific reference;
- temporary gap filler while a native Academic Colombia skill is developed.

## Authority hierarchy

External references never override:

1. explicit user instruction;
2. activity guide;
3. assessment rubric/instrument;
4. tutor/teacher instruction;
5. institution-specific rules;
6. APA 7 or another required academic standard.

## Resolution order

When a task arrives, resolve capabilities in this order:

1. Use an existing Academic Colombia skill if it fully covers the task.
2. Compose multiple Academic Colombia skills when the requirement spans several domains.
3. Detect any uncovered capability gap.
4. Search the external-reference catalog for a compatible reference.
5. Evaluate authority, license, freshness, scope and conflicts.
6. Consume only the required pattern or method.
7. Re-apply Academic Colombia institutional, integrity and QA rules.
8. Record the external dependency in the task audit when it materially affects the result.
9. If the external pattern is repeatedly useful, propose a native skill or extension.

## Capability-gap definition

An internal skill is insufficient when one or more of these conditions apply:

- it lacks a required method;
- it lacks a domain-specific validation;
- it cannot process the artifact type;
- it cannot test a required assumption;
- it lacks a necessary quality-control step;
- it covers only part of a rubric criterion;
- a newer external method materially improves correctness or reproducibility.

A skill is not considered insufficient merely because an external tool offers more features.

## External reference classes

### A — Primary academic or official authority
Examples: APA Style, official institutional guidance, official legislation.

May define rules when applicable and when not superseded by activity-specific instructions.

### B — University / scholarly secondary authority
Examples: university libraries, peer-reviewed methodological guidance.

Use to clarify, teach or supplement official rules.

### C — Technical / open-source methodological reference
Examples: K-Dense-AI/scientific-agent-skills.

Use for workflows, algorithms, checklists and agent architecture. Never treat as institutional or APA authority.

### D — Product / vendor reference
Examples: Kimi Academic Skills catalog.

Use for capability discovery and UX ideas only unless independently validated.

### E — Community / secondary explanatory source
Use for orientation only; verify important claims against stronger sources.

## Consumption modes

### 1. Reference-only
Read the external method and apply a compatible pattern manually.

### 2. Adapted workflow
Translate the external workflow into Academic Colombia terminology and constraints without copying it as a normative rule.

### 3. Temporary fallback
Use the external reference for a capability that does not yet have a native skill. Mark the gap and recommend a native implementation if recurring.

### 4. Native promotion
When an external pattern proves useful through repeated tests, implement an Academic Colombia skill inspired by it, document provenance and add regression tests.

## Mandatory checks before consumption

For every external reference verify:

- source identity;
- last update or version when relevant;
- license when code or substantial workflow material may be reused;
- scope;
- known assumptions;
- conflicts with institutional rules;
- whether the method fits the user's actual evidence type;
- whether stronger primary sources exist.

## Prohibited behavior

- Do not silently import external rules.
- Do not copy a third-party skill and present it as native without attribution and license review.
- Do not let an external tool redefine UNAD/SENA/APA requirements.
- Do not use external methods to justify fabricated data, references or conclusions.
- Do not equate popularity with authority.

## Output traceability

When external fallback materially influences the result, the audit should record:

- capability gap;
- external reference used;
- consumption mode;
- adaptations made;
- conflicts checked;
- final internal QA applied.

## Promotion rule

If the same external fallback is needed in three or more meaningful tasks or becomes strategically important, evaluate promotion to a native skill or extension with:

- dedicated SKILL.md;
- references/provenance;
- tests;
- changelog entry;
- version bump when appropriate.
