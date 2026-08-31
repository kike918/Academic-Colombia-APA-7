# Skill Contract v1 — Acceptance Cases

## SC-01 Success
Skill completes its objective with sufficient evidence.
Expected: `status: success`, gaps empty or non-material, confidence justified.

## SC-02 Partial
Skill produces useful output but non-critical evidence remains pending.
Expected: `status: partial`, gaps explicit, no false completion claim.

## SC-03 Blocked
Required source/file/decision is unavailable.
Expected: `status: blocked`; downstream skill cannot silently convert to success.

## SC-04 Critical gate propagation
Upstream skill emits `critical_gate: fail`.
Expected: downstream outputs preserve the unresolved gate until revalidation.

## SC-05 Critical gate resolution
Corrective skill resolves the underlying issue and revalidates it.
Expected: gate may become pass with evidence of recheck; not by assertion alone.

## SC-06 Inputs used
Skill receives five possible sources but actually reads three.
Expected: `inputs_used` lists only the three used.

## SC-07 Confidence
Evidence is incomplete.
Expected: confidence medium/low with reason; never fabricate numeric probability.

## SC-08 Next recommended
A skill suggests a next skill that the orchestrator determines is irrelevant.
Expected: orchestrator may omit it and records the reason.

## SC-09 Platform transformation
GPT renders contract as Markdown and Gem renders as structured object.
Expected: semantic fields/status/gaps/gates remain equivalent.

## SC-10 Final readiness authority
Intermediate skill produces a high readiness score.
Expected: it cannot declare global READY; only `academic-final-review` can do so.