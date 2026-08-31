# Artifact Validation Acceptance Cases

## AV-01 Word UNAD
A DOCX follows UNAD base format but contains a broken figure caption.
Expected: detect caption issue even if citations are correct.

## AV-02 Word visual QA
A DOCX has correct text but a table is clipped after rendering.
Expected: not ready until layout is fixed.

## AV-03 Excel with formulas
An XLSX contains correct-looking totals but one formula uses a hardcoded value and one cell has `#REF!`.
Expected: fail artifact QA and require formula correction.

## AV-04 Excel sourced data
A workbook contains researched market data with no source column/comment.
Expected: require provenance even though APA paper formatting is not imposed on the workbook.

## AV-05 Presentation
A PPTX uses charts from external reports without attribution.
Expected: require concise citation/attribution and full references where appropriate.

## AV-06 YouTube as source
A student cites a YouTube video but only pastes the URL.
Expected: verify creator, date, title and platform and build a recoverable reference.

## AV-07 Own video evidence
The assignment requires a video created by the student; the link is private.
Expected: critical failure because evaluator cannot access the evidence.

## AV-08 Own landing page
The report links to a landing page created for the activity.
Expected: verify public access and required content; do not automatically classify it as an external scholarly source.

## AV-09 Landing page as source
A public company page is used to support a factual claim.
Expected: treat as webpage source and verify author/entity, date/title and URL.

## AV-10 Infographic as main deliverable
The rubric asks for an infographic.
Expected: do not force an essay around it; validate sources and visual hierarchy.

## AV-11 Infographic embedded in report
An infographic created by the student is inserted into Word.
Expected: treat as a figure when appropriate and identify it as own work.

## AV-12 Chart from external dataset
A chart is created by the student from DANE data.
Expected: use a note equivalent to `Elaboración propia con datos de DANE` and include the dataset/source in references when applicable.

## AV-13 Misleading chart scale
A bar chart truncates the axis and exaggerates a minor difference.
Expected: flag as analytical/presentation risk even if values are numerically correct.

## AV-14 Mixed artifact submission
The activity requires DOCX + Excel + YouTube video.
Expected: run artifact QA independently for each component, then calculate overall readiness.

## AV-15 Broken QR
A document contains a QR code to the evidence but the destination is dead.
Expected: critical failure identical to a broken hyperlink.
