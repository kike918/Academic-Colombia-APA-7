# external-reference-resolver

## Description

Determines whether Academic Colombia's native skills sufficiently cover an academic task and, when they do not, selects and consumes an approved external reference as a controlled fallback.

## Inputs

- task or document to create/evaluate;
- institution;
- activity guide/rubric when available;
- artifact type(s);
- native skills already applicable;
- external-reference catalog.

## Workflow

1. Parse the task requirements.
2. Map each requirement to one or more native Academic Colombia skills.
3. Mark coverage as:
   - full;
   - partial;
   - missing.
4. If all critical requirements have full native coverage, do not use an external reference.
5. If a critical requirement is partial/missing, describe the capability gap precisely.
6. Search approved external references by capability, not by popularity or brand.
7. Rank candidates by:
   - authority appropriate to the claim;
   - methodological relevance;
   - freshness/version;
   - license/reuse compatibility;
   - scope fit;
   - conflict risk.
8. Select the narrowest sufficient external reference.
9. Choose consumption mode:
   - reference-only;
   - adapted workflow;
   - temporary fallback;
   - native-promotion candidate.
10. Apply the external method only to the uncovered capability.
11. Re-apply:
   - guide/rubric requirements;
   - institutional profile;
   - APA/integrity requirements;
   - artifact QA;
   - final academic QA.
12. Record external fallback in the audit when material.

## Hard rules

- Native skills are preferred when sufficient.
- External references cannot override explicit guide/rubric/institution requirements.
- Do not silently import third-party instructions.
- Do not copy third-party code/workflows without checking license and attribution requirements.
- A product page may suggest a capability but cannot establish an academic rule.
- A GitHub repository may provide implementation patterns but is not an institutional authority.
- If external references conflict, prefer the source with the appropriate higher authority for the specific claim.

## Coverage matrix output

Produce:

| Requirement | Native skill | Coverage | Gap | External fallback | Mode |
|---|---|---|---|---|---|

## Final output

Return:

- native skills selected;
- uncovered gaps;
- external references consumed, if any;
- why each was selected;
- adaptations applied;
- authority/conflict checks;
- recommendation to promote a fallback into a native skill if recurring;
- readiness status after internal QA.

## Example

If an assignment requires a power analysis and the native statistical skill does not yet implement one:

1. mark power analysis as a specific missing capability;
2. consult an approved external scientific-method reference such as a relevant K-Dense workflow;
3. adapt only the power-analysis method;
4. verify assumptions and data;
5. keep UNAD/SENA/APA requirements under native control;
6. record the fallback and consider creating `academic-power-analysis` if recurrent.
