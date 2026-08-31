# academic-artifact-validator

## Description

Validates academic deliverables according to their actual artifact type: Word, Excel, presentations, videos/YouTube, landing pages, infographics and charts.

## Inputs

- artifact or link;
- activity guide;
- rubric/instrument;
- institution;
- related source files if any.

## Workflow

1. Identify the primary deliverable type.
2. Identify embedded/linked secondary artifacts.
3. Apply the authority hierarchy: guide → rubric → institution → artifact rules → APA.
4. Validate content requirements.
5. Validate artifact-specific quality.
6. Validate citations, sources and attribution.
7. Validate external links and permissions.
8. Validate accessibility/readability where applicable.
9. Report critical failures separately from optional improvements.

## Artifact routing

### DOCX
Check page setup, styles, citations/references, tables/figures, hyperlinks and visual rendering.

### XLSX
Check formulas, units, labels, sources, charts, workbook structure and formula errors. Do not impose paper formatting on cells.

### PPTX
Check slide hierarchy, readability, concise citations, references, image/chart attribution and working links.

### Video / YouTube
Check authorship, title, date, platform, URL, permissions and whether it is a source or the student's own evidence.

### Landing page
Check URL, access, identity, required content, usability and evidence linkage. If used as a source, format it as a webpage reference.

### Infographic
Check factual accuracy, hierarchy, sources, attribution and whether it is the central deliverable or an embedded figure.

### Charts
Check data integrity, chart choice, labels, units, scale, source and figure treatment when embedded in a report.

## External evidence rule

A URL is not enough. Verify that the destination is accessible and matches the evidence described in the academic document.

## Output

Return:
- artifact type(s);
- guide/rubric compliance;
- format QA;
- source/APA QA;
- external-link QA;
- critical issues;
- recommended fixes;
- readiness score.

## Skill Contract v1

Cumplir `core/SKILL-CONTRACT.md`.

- `outputs.artifact_checks`: resultados por artefacto/componente.
- `findings`: fallos críticos, importantes y mejoras.
- `gaps`: artefactos inaccesibles, evidencia faltante o validaciones no ejecutables.
- `next_recommended`: normalmente `academic-final-review` o una skill correctiva pertinente.
- `critical_gate: fail` si un artefacto requerido está roto/inaccesible, contiene un error crítico de fórmula/dato, o incumple un requisito obligatorio.