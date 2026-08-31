# Compatibility and Release Policy

Academic Colombia is a **declarative academic-agent framework**. Its behavior is defined by Markdown instructions, institutional profiles, skill contracts, routing rules, QA gates, adapters and acceptance evidence rather than by an executable application runtime.

Semantic Versioning therefore applies to **observable agent behavior and public contracts**, not only to file formats or source-code APIs.

## Version format

Academic Colombia uses `MAJOR.MINOR.PATCH`.

### MAJOR

Increment MAJOR when a change can reasonably break a previously compatible installation, workflow, adapter or expected academic behavior.

Examples:

- changing the authority hierarchy in a way that changes conflict resolution;
- introducing Skill Contract v2 with incompatible fields or status semantics;
- changing `critical_gate` propagation so previously blocked work can become READY, or vice versa;
- renaming/removing a native Skill without a compatibility path;
- materially changing routing semantics relied on by platform adapters;
- redefining the meaning of an institutional profile in an incompatible way;
- changing the canonical package layout expected by documented installation flows.

A declarative wording change is MAJOR when it predictably changes public behavior in an incompatible way, even if only Markdown changed.

### MINOR

Increment MINOR for backward-compatible capability or behavioral additions.

Examples:

- adding a new optional Skill;
- adding a new institution profile without changing existing profiles;
- supporting an additional artifact or platform adapter;
- adding a new optional output field while preserving Skill Contract v1 compatibility;
- expanding routing for a new case without changing existing expected routes;
- materially improving a Skill while preserving its declared inputs, outputs, gates and compatibility expectations.

### PATCH

Increment PATCH for backward-compatible corrections and evidence/documentation maintenance that do not intentionally change public contracts.

Examples:

- correcting a broken internal link;
- clarifying ambiguous wording without changing intended behavior;
- fixing stale metadata or a factual typo;
- adding empirical evidence records;
- improving examples or documentation;
- fixing an adapter packaging issue without changing the core contract;
- correcting a regression so behavior returns to the documented contract.

If a seemingly small wording edit changes how an agent routes, blocks or approves work, it is **not automatically a PATCH**.

## Stable v1 contracts

Starting with v1.0.0, the following are stable public contracts unless changed through a future MAJOR release:

1. `core/SKILL-CONTRACT.md` — Skill Contract v1 envelope and gate semantics.
2. `core/ORCHESTRATION.md` — core routing and readiness principles.
3. authority hierarchy — user instruction → activity guide → rubric → tutor → institution → APA → general convention, subject to the safeguards documented by the core.
4. `READY / NOT READY / USER DECISION REQUIRED` final-state model.
5. separation between implemented capability, acceptance fixture, empirical execution and platform runtime validation.
6. canonical-source principle: GitHub `main` is the source of truth; platform packages are adapters/distribution layers.
7. native Skill package convention: `skills/<skill-name>/SKILL.md`.

## Compatibility of Skills

A Skill is compatible with v1 when it:

- declares compatibility with Skill Contract v1;
- preserves the documented semantics of `status`, `findings`, `outputs`, `gaps`, `next_recommended`, `confidence` and `critical_gate`;
- does not silently override higher-authority requirements;
- does not declare final readiness unless it is the designated final-review capability;
- preserves evidence/integrity gates applicable to its domain.

## Platform adapter compatibility

ChatGPT, Gemini and future adapters are consumers of the canonical core.

An adapter MAY vary in:

- installation steps;
- file-loading strategy;
- platform-specific Instructions syntax;
- context-loading strategy;
- available product features.

An adapter MUST NOT redefine:

- authority hierarchy;
- evidence integrity rules;
- Skill Contract semantics;
- critical-gate behavior;
- institutional rules;
- final readiness meaning.

A platform-specific product limitation is documented as an adapter boundary, not used to mutate the core silently.

## Institutional compatibility

Institution profiles are isolated.

A change to UNAD must not silently change SENA behavior, and vice versa.

Institutional updates caused by new official guidance should:

1. identify the new authority/source;
2. document the previous rule when behavior changes materially;
3. add/update regression cases;
4. choose PATCH/MINOR/MAJOR according to behavioral impact, not according to how many lines changed.

## Evidence and factual updates

External facts, regulations, product limits and institutional sources can become stale without implying a core-breaking release.

A freshness correction is normally PATCH when it restores intended evidence quality without changing public workflow contracts.

A new evidence rule that changes whether a class of work is considered READY may require MINOR or MAJOR depending on compatibility impact.

## Deprecation policy

Before removing or renaming a public Skill, path, output field or documented behavior in a stable major line:

1. mark it deprecated in documentation;
2. provide the replacement path when practical;
3. keep the compatibility path for at least one MINOR release when feasible;
4. remove it only in a MAJOR release unless the old behavior creates a material integrity/safety defect.

Critical academic-integrity defects may be corrected immediately; the CHANGELOG must explain the compatibility impact.

## Changelog requirements

Every release must document **behavioral impact**, not only changed filenames.

For material prompt/Skill changes, record:

- what behavior changed;
- why it changed;
- which skills/adapters/institutions are affected;
- whether expected routing/readiness changed;
- relevant regression/acceptance evidence.

## Release gates

A stable release should not be published unless:

- declarative CI is green;
- VERSION and CHANGELOG agree;
- required internal links and Skill manifests validate;
- no known unresolved critical evidence/governance defect exists;
- coverage claims match the empirical registry;
- platform runtime claims are clearly marked validated or not claimed;
- license and third-party scope remain accurate.

## v1 support boundary

v1.0.0 stabilizes the framework architecture and contracts. It does **not** claim exhaustive empirical validation for every institution, artifact, academic domain or AI platform.

New evidence and additional institutional/platform coverage may continue in backward-compatible v1.x releases.
