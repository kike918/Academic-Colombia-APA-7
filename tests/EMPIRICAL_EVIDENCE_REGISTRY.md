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
| EMP-03 | SENA | financial report + evidence review | EXECUTED | Real 2026 financial-analysis workflow compared an earlier overclaiming report with a corrected final DOCX; principal ratios independently recalculated and final DOCX rendered/inspected | Full official source package, exhaustive bibliography verification and instructor outcome not part of execution |
| EMP-04 | — | XLSX cost/budget artifact | FIXTURE_READY | Artifact validation/routing specification exists | Need real workbook execution |
| EMP-05 | — | PPTX academic presentation | FIXTURE_READY | Artifact validation/routing specification exists | Need real slide deck execution |
| EMP-06 | SENA | video + written/visual support | PARTIAL | Real recording guide and six-page visual presentation checked for cross-artifact consistency with the final financial report | Actual video playback, audio, duration and link accessibility not tested |
| EMP-07 | Colombia / legal | legislation/normative activity | PARTIAL | Real export/customs academic activity exercised with current Colombian normative verification | Preserve anonymized reusable case |
| EMP-08 | — | statistics/correlation | FIXTURE_READY | Statistical acceptance scenario exists | Need real dataset/artifact execution |
| EMP-09 | UNAD | quiz / objective assessment support | PARTIAL | Real course quizzes used to validate source-grounded academic assistance | Not an artifact-generation E2E |
| EMP-10 | ChatGPT | Custom GPT runtime | NOT_CLAIMED | Static adapter + acceptance/adversarial suites ready | Real Custom GPT deployment pending |
| EMP-11 | Gemini | Gem runtime | NOT_CLAIMED | Static adapter + cross-platform suites ready | Real Gem deployment pending |
| EMP-12 | SENA | visual presentation PDF | EXECUTED | Real six-page financial presentation inspected for hierarchy, KPI consistency, concise visual support and alignment with corrected written conclusions | Native PPTX source not inspected; this does not promote PPTX E2E coverage |
| EMP-13 | SENA | draft → critical review → corrected artifact chain | EXECUTED | Real artifact family demonstrates removal/qualification of unsupported sector benchmarks, exactness claims and absolute conclusions before final delivery | Repair transaction was not captured as a machine-verifiable change log |

## Detailed empirical records

- [`empirical/sena/EMP-SENA-2026-01-CINE-FUTURO.md`](empirical/sena/EMP-SENA-2026-01-CINE-FUTURO.md)

## Evidence rules

1. Do not convert a fixture into `EXECUTED` because the routing looks correct on paper.
2. Do not store personal identifiers, student IDs, grades linked to identities or private source files in public fixtures.
3. Real cases may be summarized rather than committed when redistribution rights are unclear.
4. A passing structural GitHub Action does not change an empirical case status.
5. Platform runtime acceptance must be recorded separately from core/skill correctness.
6. Failures are valid evidence and should be preserved when they reveal a real framework gap.
7. A PDF export of a presentation validates the inspected visual artifact; it does not automatically validate the native PPTX editing/runtime path.
8. A recording guide does not count as executed video evidence unless the actual video is played back and its access/duration/audio are checked.

## v1.0 relevance

Academic Colombia does not require every possible artifact to have exhaustive empirical coverage before v1.0. It does require that public capability claims distinguish clearly between:
- implemented capability;
- acceptance specification;
- real empirical execution;
- platform runtime validation.
