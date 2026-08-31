# Empirical Evidence Registry

This registry tracks **real, anonymized executions** of Academic Colombia separately from conceptual fixtures and acceptance specifications.

A case may be marked `EXECUTED` only when an actual academic artifact/activity was exercised through the relevant workflow and its result was inspected.

## Status vocabulary

- `EXECUTED` — real anonymized case completed and reviewed.
- `PARTIAL` — real case used, but one or more declared gates were not fully exercised.
- `FIXTURE_READY` — acceptance specification exists, but no real artifact execution is claimed.
- `NOT_CLAIMED` — the framework intentionally makes no empirical coverage claim yet.

## Registry

| ID | Institution | Artifact / domain | Status | Evidence summary | Main gaps |
|---|---|---|---|---|---|
| EMP-01 | UNAD | DOCX audit + conservative repair | EXECUTED | Real anonymized ~20-page academic document audited, repaired, rendered and visually checked | More independent DOCX cases desirable |
| EMP-02 | UNAD | infographic + written analysis | PARTIAL | Real course workflow used for infographic correction and accompanying written submission | Preserve a reusable anonymized artifact fixture |
| EMP-03 | SENA | short academic evidence | FIXTURE_READY | Routing/profile acceptance case defined | Need real anonymized SENA artifacts |
| EMP-04 | — | XLSX cost/budget artifact | FIXTURE_READY | Artifact validation/routing specification exists | Need real workbook execution |
| EMP-05 | — | PPTX academic presentation | FIXTURE_READY | Artifact validation/routing specification exists | Need real slide deck execution |
| EMP-06 | — | video + DOCX multi-artifact | FIXTURE_READY | Multi-artifact acceptance scenario exists | Need real execution |
| EMP-07 | Colombia / legal | legislation/normative activity | PARTIAL | Real export/customs academic activity exercised with current Colombian normative verification | Preserve anonymized reusable case |
| EMP-08 | — | statistics/correlation | FIXTURE_READY | Statistical acceptance scenario exists | Need real dataset/artifact execution |
| EMP-09 | UNAD | quiz / objective assessment support | PARTIAL | Real course quizzes used to validate source-grounded academic assistance | Not an artifact-generation E2E |
| EMP-10 | ChatGPT | Custom GPT runtime | NOT_CLAIMED | Static adapter + acceptance/adversarial suites ready | Real Custom GPT deployment pending |
| EMP-11 | Gemini | Gem runtime | NOT_CLAIMED | Static adapter + cross-platform suites ready | Real Gem deployment pending |

## Evidence rules

1. Do not convert a fixture into `EXECUTED` because the routing looks correct on paper.
2. Do not store personal identifiers, student IDs, grades linked to identities or private source files in public fixtures.
3. Real cases may be summarized rather than committed when redistribution rights are unclear.
4. A passing structural GitHub Action does not change an empirical case status.
5. Platform runtime acceptance must be recorded separately from core/skill correctness.
6. Failures are valid evidence and should be preserved when they reveal a real framework gap.

## v1.0 relevance

Academic Colombia does not require every possible artifact to have exhaustive empirical coverage before v1.0. It does require that public capability claims distinguish clearly between:
- implemented capability;
- acceptance specification;
- real empirical execution;
- platform runtime validation.
