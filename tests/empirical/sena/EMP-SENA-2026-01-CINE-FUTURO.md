# EMP-SENA-2026-01 — Financial report + presentation workflow

## Status

`EXECUTED` for the report/review/presentation artifacts described below.

`PARTIAL` for the final video because the recording guide and visual support were available, but the published/rendered video itself was not part of this execution.

## Privacy and provenance

This record summarizes a real SENA academic workflow from 2026. Personal names, learner identifiers, instructor identifiers and private course files are intentionally omitted.

The original artifacts are not committed to the public repository. This file records only the reusable evidence needed to validate Academic Colombia behavior.

## Context

- Institution: SENA.
- Domain: financial analysis.
- Case: academic company dataset, periods 2023–2024.
- Artifact set inspected:
  - earlier PDF report version;
  - corrected final DOCX report, rendered to PDF/PNG for visual QA;
  - six-page visual presentation exported as PDF;
  - seven-page recording/review guide for a 3–5 minute explanatory video.

## Why this case matters

The artifact set contains both an earlier draft with overclaims and a later corrected version. It therefore tests whether the framework can detect evidence-integrity problems instead of merely formatting a finished answer.

## Grounded numeric checks

Using the financial values present in the final report, independent recalculation reproduced the reported metrics to normal rounding tolerance:

- current ratio: ~1.04 (2023), ~1.09 (2024);
- quick ratio: ~0.93, ~0.98;
- working capital: 3,898,758 and 9,056,866 in the case units;
- debt/assets: ~30.51%, ~30.84%;
- ROA: ~10.85%, ~11.91%;
- ROE: ~15.62%, ~17.22%;
- net margin: ~16.10%, ~16.63%;
- total-asset turnover: ~0.67x, ~0.72x.

No external sector benchmark was required to reproduce these calculations.

## Skill-level findings

### `academic-requirements-analyzer`

**Status:** `partial`

The recording guide contains an explicit rubric/checklist and delivery constraints, including a 3–5 minute video range and visual/communication requirements. However, the complete official source package for the activity was not independently available in this execution, so full requirements coverage is not claimed.

### `academic-template-selector`

**Status:** `success`

The artifacts correctly remain artifact-sensitive:
- a written financial report is treated as a report;
- the visual deck is concise support for oral explanation rather than an essay copied onto slides;
- the recording guide manages timing and delivery rather than imposing document formatting rules on the video.

### `academic-source-evaluator`

**Status:** `success`

The earlier report included claims that exceeded the evidence visible in the case, including sector-quality judgments and other comparative assertions without a cited benchmark. The corrected workflow removed or weakened those assertions rather than preserving them as facts.

### `academic-evidence-mapper`

**Status:** `success`

The case exposed a useful distinction between:
- calculations directly reproducible from the supplied financial statements;
- estimates requiring methodological qualification;
- external comparative claims that need independent evidence.

A particularly important example is days-sales/collection analysis: the corrected report states that exact portfolio turnover cannot be calculated rigorously without credit-sales information and average receivables, instead of presenting a simple closing-balance estimate as an exact ratio.

### `academic-citation-manager`

**Status:** `partial`

The final report identifies SENA course materials and the academic case as sources. This is sufficient to show source awareness, but this empirical execution did not include authoritative metadata verification for every bibliographic entry. Therefore bibliographic correctness is not promoted to a full PASS claim.

### `academic-critical-review`

**Status:** `success`

The recording/review guide explicitly corrected multiple overstatements before the final presentation:
- wrong absolute revenue figures while preserving the correct growth rate;
- unsupported sector benchmark language;
- equating quick-ratio coverage with cash-on-hand;
- recommending new debt as a first response;
- treating an estimated 27.1-day collection period as exact;
- absolute viability language.

The corrected conclusion became conditional and managerial rather than absolute.

### `academic-statistical-analysis`

**Status:** `not_applicable`

This activity uses financial-ratio calculations, not inferential statistical analysis. Correct routing means this Skill should not be invoked merely because the artifact contains numbers.

### `academic-tables-figures`

**Status:** `partial`

Tables and figures are readable, numbered and integrated into the argument. Some figure/source attribution is present in the artifact family, but source-note consistency is not uniform enough in this execution to claim exhaustive APA/figure compliance.

### `academic-artifact-validator`

**Status:** `success` for report + visual presentation; `partial` for video.

The final DOCX was rendered to nine pages and visually inspected. No clipping, overlap, broken tables or missing-glyph defects were observed in the rendered pages reviewed.

The six-page presentation uses KPI cards, comparisons, a financing-composition bar, liquidity comparisons, three actions and an executive conclusion. It behaves as presentation support rather than a dense written report.

The video path remains partial because only its script/recording guide and visual support were available; playback, audio, duration and link accessibility were not tested.

### `academic-document-auditor`

**Status:** `success` for layout + evidence-risk identification.

The final DOCX renders cleanly, while comparison with the earlier PDF demonstrates that a visually polished document may still contain unsupported claims. This validates the auditor principle that visual QA is necessary but not sufficient.

### `academic-document-repair`

**Status:** `partial`

A corrected final artifact exists after substantive review, but this execution did not preserve a machine-verifiable repair transaction showing every change as `SAFE_AUTOFIX`, `EVIDENCE_REQUIRED` or `CONTENT_DECISION`. The case therefore supports the repair workflow concept without claiming a full automated repair trace.

### `academic-final-review`

**Status:** `success` with bounded claim.

The final report and presentation resolve the major evidence-integrity issues identified in the earlier version and are internally consistent on the principal financial indicators. No course grade or instructor acceptance was supplied as part of this execution, so the registry does not claim institutional approval or a perfect score.

## Cross-artifact consistency

The final written report, recording guide and visual presentation converge on the same main narrative:

1. revenue and net income grew;
2. profitability improved;
3. financing remains predominantly equity-based;
4. quick-ratio liquidity is the principal short-term attention point;
5. recommendations prioritize liquidity, working-capital discipline and collection management.

This supports the framework's multi-artifact consistency goal.

## Demonstrated framework behaviors

This real case provides empirical support for:

- SENA institutional routing without inheriting UNAD-specific structure;
- evidence-first correction of unsupported claims;
- numeric verification before interpretation;
- separation of exact metrics from estimates;
- artifact-sensitive output design;
- omission of irrelevant Skills;
- visual QA for DOCX;
- bounded readiness claims when the final video or official grading evidence is unavailable.

## Remaining gaps

- official source package/rubric was not independently reconstructed in full;
- video runtime was not available;
- bibliographic metadata was not exhaustively verified;
- no spreadsheet source workbook was inspected in this execution;
- no instructor grade/feedback is used as validation evidence.

## Empirical decision

This case is sufficient to promote SENA from `FIXTURE_READY` to **real executed coverage for written financial-report workflows**, and to record **partial multi-artifact video coverage**. It does not justify claiming exhaustive SENA, XLSX, PPTX or video validation.
