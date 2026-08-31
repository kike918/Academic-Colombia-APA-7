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
| EMP-04 | UNAD | native XLSX accounting workbook | EXECUTED | Real formula-driven journal → T-accounts → trial-balance workbook inspected; 14 journal blocks balanced; no formula errors; COP 117,860,000 debit/credit totals reconcile with SIIGO export | Does not claim dashboards, pivots, macros or statistical workbook coverage |
| EMP-05 | — | PPTX academic presentation | FIXTURE_READY | Artifact validation/routing specification exists | Need real native PPTX execution |
| EMP-06 | SENA | video + written/visual support | PARTIAL | Real recording guide and six-page visual presentation checked for cross-artifact consistency with the final financial report | Actual video playback, audio, duration and link accessibility not tested |
| EMP-07 | Colombia / legal | legislation/normative activity | PARTIAL | Real export/customs academic activity exercised with current Colombian normative verification | Preserve anonymized reusable case |
| EMP-08 | — | statistics/correlation | FIXTURE_READY | Statistical acceptance scenario exists | Need real inferential/statistical dataset execution |
| EMP-09 | UNAD | quiz / objective assessment support | PARTIAL | Real course quizzes used to validate source-grounded academic assistance | Not an artifact-generation E2E |
| EMP-10 | ChatGPT | Custom GPT runtime | NOT_CLAIMED | Static adapter + acceptance/adversarial suites ready | Real Custom GPT deployment pending |
| EMP-11 | Gemini | Gem runtime | NOT_CLAIMED | Static adapter + cross-platform suites ready | Real Gem deployment pending |
| EMP-12 | SENA | visual presentation PDF | EXECUTED | Real six-page financial presentation inspected for hierarchy, KPI consistency, concise visual support and alignment with corrected written conclusions | Native PPTX source not inspected; this does not promote PPTX E2E coverage |
| EMP-13 | SENA | draft → critical review → corrected artifact chain | EXECUTED | Real artifact family demonstrates removal/qualification of unsupported sector benchmarks, exactness claims and absolute conclusions before final delivery | Repair transaction was not captured as a machine-verifiable change log |
| EMP-14 | SENA | technical smart-contract design PDF | PARTIAL | Real 26-page technical design report reviewed for scope, evidence, source quality, tables/figures and design-vs-implementation boundaries | Official guide/rubric and runtime smart-contract implementation were not included |
| EMP-15 | UNAD | collaborative trade-theories paper | PARTIAL | Real 25-page paper demonstrates heterogeneous source quality, citation/reference mismatches and contributor-to-contributor rigor differences | Official guide/rubric and original timeline/infographic artifacts unavailable |
| EMP-16 | UNAD | WTO/OECD geopolitical DOCX | PARTIAL | Real 22-page DOCX rendered cleanly; current institutional claims selectively verified while inline evidence gaps and rhetorical overclaims were identified | No official guide/rubric; not every factual claim was externally verified |
| EMP-17 | UNAD | Colombia/Ecuador rice trade case | PARTIAL | Real 20-page paper used to detect non-comparable time periods, uneven source-to-number traceability and theory-vs-evidence distinctions | No official guide/rubric; exhaustive CAN legal verification pending |
| EMP-18 | — | short spreadsheet-facts DOCX | EXECUTED | Real one-page DOCX demonstrates freshness gate: obsolete Excel worksheet limits detected against current official Microsoft specifications while layout itself passes | Institution/rubric not asserted; narrow freshness case only |
| EMP-19 | UNAD | accounting visual PDF | PARTIAL | Real 14-page visual deck correctly explains core accounting elements but exposes a pedagogical double-entry ambiguity, absolute technology language and missing visible source page | Native PPTX and official guide/rubric not inspected |
| EMP-20 | UNAD | coffee-sector macroeconomic visual PDF | EXECUTED | Real 13-page deck cross-checked against official FNC 2026 data; detected a 6.9-million-sack semantic misuse, unresolved export-period statistic and conceptual externality overreach | Source artifact remains NOT READY until findings are corrected |
| EMP-21 | UNAD | inflation/IPC presentation + video reference | PARTIAL | Real 10-page deck; April 2026 Colombia/Bogotá IPC values verified against DANE; unsupported/poorly traced 2026 year-end projection identified | Video playback not verified; exact forecast provenance unresolved |

## Detailed empirical records

- [`empirical/sena/EMP-SENA-2026-01-CINE-FUTURO.md`](empirical/sena/EMP-SENA-2026-01-CINE-FUTURO.md)
- [`empirical/sena/EMP-SENA-2026-02-SMART-CONTRACT-DESIGN.md`](empirical/sena/EMP-SENA-2026-02-SMART-CONTRACT-DESIGN.md)
- [`empirical/unad/EMP-UNAD-2026-01-TRADE-THEORIES.md`](empirical/unad/EMP-UNAD-2026-01-TRADE-THEORIES.md)
- [`empirical/unad/EMP-UNAD-2026-02-GEOPOLITICAL-ORGANIZATIONS.md`](empirical/unad/EMP-UNAD-2026-02-GEOPOLITICAL-ORGANIZATIONS.md)
- [`empirical/unad/EMP-UNAD-2026-03-RICE-CAN-CASE.md`](empirical/unad/EMP-UNAD-2026-03-RICE-CAN-CASE.md)
- [`empirical/unad/EMP-UNAD-2026-04-ACCOUNTING-XLSX.md`](empirical/unad/EMP-UNAD-2026-04-ACCOUNTING-XLSX.md)
- [`empirical/unad/EMP-UNAD-2026-05-ACCOUNTING-VISUAL-DECK.md`](empirical/unad/EMP-UNAD-2026-05-ACCOUNTING-VISUAL-DECK.md)
- [`empirical/unad/EMP-UNAD-2026-06-COFFEE-MACRO-DECK.md`](empirical/unad/EMP-UNAD-2026-06-COFFEE-MACRO-DECK.md)
- [`empirical/unad/EMP-UNAD-2026-07-INFLATION-IPC-DECK.md`](empirical/unad/EMP-UNAD-2026-07-INFLATION-IPC-DECK.md)
- [`empirical/general/EMP-GENERAL-2026-01-SPREADSHEET-FRESHNESS.md`](empirical/general/EMP-GENERAL-2026-01-SPREADSHEET-FRESHNESS.md)

## Evidence rules

1. Do not convert a fixture into `EXECUTED` because the routing looks correct on paper.
2. Do not store personal identifiers, student IDs, grades linked to identities or private source files in public fixtures.
3. Real cases may be summarized rather than committed when redistribution rights are unclear.
4. A passing structural GitHub Action does not change an empirical case status.
5. Platform runtime acceptance must be recorded separately from core/skill correctness.
6. Failures are valid evidence and should be preserved when they reveal a real framework gap.
7. A PDF export of a presentation validates the inspected visual artifact; it does not automatically validate the native PPTX editing/runtime path.
8. A recording guide or video link does not count as executed video evidence unless the actual video is played back and its access/duration/audio are checked.
9. A delivered/submitted artifact is not automatically a PASS; empirical review may record `NOT READY` findings without changing the submission history.
10. Correctness of a sampled current fact does not substitute for citation/evidence traceability inside the academic artifact.
11. A number copied from a valid source can still fail if its period, unit or semantic meaning is misinterpreted.
12. Native spreadsheet execution requires formula/value inspection and error checking; a screenshot or PDF export alone does not promote XLSX coverage.

## v1.0 relevance

Academic Colombia does not require every possible artifact to have exhaustive empirical coverage before v1.0. It does require that public capability claims distinguish clearly between:
- implemented capability;
- acceptance specification;
- real empirical execution;
- platform runtime validation.
