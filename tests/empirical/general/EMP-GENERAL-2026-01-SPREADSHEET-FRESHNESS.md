# EMP-GENERAL-2026-01 — Spreadsheet facts and freshness gate

## Scope

Real one-page DOCX submitted as a short academic answer. The original private artifact is not committed.

Artifact type: DOCX, one rendered page.
Domain: digital tools / spreadsheets.
Institution: not asserted in the public empirical record.

## Why this case matters

This tiny artifact is valuable precisely because it is simple. A generic writing assistant could accept it immediately, while an evidence-aware workflow should detect that factual software claims can become obsolete.

## Execution performed

The DOCX was rendered and visually inspected. Layout was clean and readable.

A current official Microsoft specification was used to verify the Excel worksheet-size claim.

## Routing exercised

| Skill | Result | Evidence |
|---|---|---|
| `academic-requirements-analyzer` | PARTIAL | Only the short prompt/answer context is visible; no rubric |
| `academic-source-evaluator` | MATERIAL FINDING | No sources are cited for product/version-specific claims |
| `academic-evidence-mapper` | MATERIAL FINDING | Exact Excel capacity claim requires version/current evidence |
| `academic-citation-manager` | FINDING | No reference supports the numerical specifications |
| `academic-critical-review` | PASS | Detects stale/current mismatch |
| `academic-document-auditor` | PASS | Single-page layout is clean |
| `academic-final-review` | NOT READY for a current-facts task | Core factual content is outdated unless the task explicitly asks about an old Excel version |

## Key finding

The artifact states that an Excel worksheet has:
- 65,536 rows;
- 256 columns;
- about 32,000 characters per cell.

Current Microsoft documentation for modern Excel versions specifies:
- 1,048,576 rows;
- 16,384 columns;
- 32,767 characters per cell.

Therefore, the artifact demonstrates why exact software specifications require a freshness check.

## Expected framework behavior

1. Do not correct silently if the assignment/source intentionally concerns a historical Excel version.
2. If the task is current/general, flag the row/column limits as obsolete.
3. Ask for or retrieve an authoritative current source when exact specifications matter.
4. Do not infer that "most used spreadsheet applications" remains Excel + StarOffice without current evidence.
5. Keep content correctness separate from visual cleanliness.

## Status

`EXECUTED`

This case fully exercises the intended narrow capability: stale factual-content detection plus clean DOCX artifact inspection.

## Coverage contribution

Strengthens empirical coverage for:
- freshness gates;
- product/version-sensitive facts;
- short-form assignments;
- correct separation of layout PASS and content NOT READY.
