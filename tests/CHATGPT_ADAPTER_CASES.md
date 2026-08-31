# ChatGPT Production Adapter — Acceptance Cases

## CG-01 Guide + rubric routing
Input: UNAD activity with guide and rubric.
Expected:
- requirements analysis before drafting;
- rubric criterion → evidence mapping;
- only relevant skills selected;
- final review before READY.

## CG-02 No rubric available
Input: task statement only.
Expected:
- do not fabricate rubric criteria;
- identify missing authority material;
- proceed with clearly labeled general recommendations when useful.

## CG-03 Existing DOCX, format-only request
Input: completed document with user requesting APA/Word correction only.
Expected:
- document auditor path;
- conservative repair by default;
- content preserved;
- visual QA required before final readiness.

## CG-04 Infographic
Input: guide requires infographic plus brief analysis.
Expected:
- artifact-sensitive routing;
- no unnecessary paper structure;
- factual/source/attribution checks;
- brief analysis treated separately from infographic.

## CG-05 Quantitative XLSX
Input: spreadsheet and rubric requiring analysis.
Expected:
- data/source validation;
- statistical-analysis skill when method is required;
- chart/table artifact QA;
- no paper formatting imposed on spreadsheet cells.

## CG-06 Legal/regulatory claim
Input: assignment involving current Colombian regulation.
Expected:
- use current/official verification when tools are available;
- distinguish verified law from interpretation;
- no invented decree/article numbers.

## CG-07 Evidence chain
Input: draft with several factual claims and source list.
Expected:
- source evaluator → evidence mapper → citation manager;
- unsupported claims remain gaps;
- thematic similarity alone is insufficient.

## CG-08 Native coverage sufficient
Input: ordinary APA/UNAD document task covered by native skills.
Expected:
- no external fallback.

## CG-09 Capability gap
Input: specialist method explicitly outside native coverage.
Expected:
- precise gap recorded;
- external-reference-resolver used narrowly;
- native QA reapplied afterwards.

## CG-10 Critical gate propagation
Input: mandatory source inaccessible and central to rubric evidence.
Expected:
- critical gate remains fail;
- final review cannot declare READY.

## CG-11 User-facing compression
Input: simple question about one citation.
Expected:
- concise natural answer;
- do not expose complete orchestration trace or raw Skill Contract unless requested/useful.

## CG-12 Maintainer audit mode
Input: maintainer asks which skills ran and why final status is blocked.
Expected:
- expose routing trace, gaps and relevant contract fields.

## CG-13 Institutional separation
Input: SENA activity.
Expected:
- do not import UNAD-specific template rules unless the task independently requires them.

## CG-14 Task files remain local
Input: one course's rubric uploaded.
Expected:
- treat as authority for that task;
- do not generalize it into permanent institutional rules.

## CG-15 Platform-neutral semantics
Input: same canonical case previously used by core routing tests.
Expected:
- ChatGPT adapter preserves authority, evidence and readiness semantics even if wording differs.

## CG-16 Few-shot non-authority
Input: current guide conflicts with a platform few-shot example.
Expected:
- current guide/rubric wins.

## CG-17 Citation metadata uncertainty
Input: incomplete reference metadata.
Expected:
- verify when possible;
- otherwise leave fields unresolved rather than hallucinating.

## CG-18 Artifact link/access failure
Input: required external evidence URL is inaccessible.
Expected:
- artifact/evidence gate fails when the inaccessible item is mandatory;
- do not claim it was inspected.

## CG-19 User explicitly changes objective
Input: user asks for a practice/example document that intentionally differs from the submission rubric.
Expected:
- follow the explicit objective while clearly distinguishing it from submission compliance;
- do not falsely label the alternative artifact compliant with the original rubric.

## CG-20 Production package integrity
Input: deployment package missing orchestrator or final-review semantics while advertised as full Academic Colombia.
Expected:
- mark package incomplete;
- do not claim full-framework compatibility.
