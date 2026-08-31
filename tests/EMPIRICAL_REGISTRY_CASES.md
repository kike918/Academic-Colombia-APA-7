# Empirical Evidence Registry — Acceptance Cases

## ER-01 — Real executed artifact
A real anonymized artifact is run through its workflow and inspected.
Expected: may be marked `EXECUTED` with a concise evidence summary.

## ER-02 — Conceptual fixture only
Routing and expected findings exist, but no real artifact was exercised.
Expected: `FIXTURE_READY`, never `EXECUTED`.

## ER-03 — Partial real workflow
A real activity was used, but not every declared gate was exercised.
Expected: `PARTIAL`.

## ER-04 — Platform package only
Static ChatGPT/Gemini package passes specification, but no real GPT/Gem was deployed.
Expected: runtime remains `NOT_CLAIMED`.

## ER-05 — Structural CI passes
GitHub Action is green.
Expected: empirical artifact statuses do not change.

## ER-06 — Private artifact cannot be redistributed
A real case is useful but contains protected/private material.
Expected: `SUMMARY_ONLY` or `NO_PUBLIC_FIXTURE`; do not commit original content.

## ER-07 — Identifiers present
Fixture contains student name, ID, contact information or other personal identifiers.
Expected: do not promote publicly until anonymized.

## ER-08 — Failure reveals framework gap
A real case produces an incorrect routing or misses a critical issue.
Expected: preserve failure as evidence and add/update regression coverage before claiming resolution.

## ER-09 — New SENA subprofile request
One SENA case differs from another.
Expected: do not create a subprofile from a single observation; gather official authority + repeated empirical evidence.

## ER-10 — New academic-integrity Skill suggestion
A case raises a problem already covered by source evaluation/citation/final review.
Expected: do not create a duplicate Skill.

## ER-11 — New academic-integrity recurring gap
Multiple real cases expose a distinct integrity problem not handled by current capabilities.
Expected: document gap first; only then evaluate a new Skill.

## ER-12 — Detector-evasion request
A proposed empirical capability aims to evade AI/plagiarism detection.
Expected: reject as out of scope; do not add it as a capability.

## ER-13 — External institution expansion
A contributor proposes a new university profile based on generic knowledge.
Expected: require `institutions/TEMPLATE.md`, verified sources and at least one real anonymized case before stable promotion.

## ER-14 — Grade used as evidence
A real submission receives a high grade.
Expected: grade may support outcome evidence but does not by itself prove every framework decision was correct.

## ER-15 — Low grade or tutor correction
A real submission receives corrective feedback.
Expected: preserve the feedback as high-value empirical evidence and update affected acceptance/regression cases.
