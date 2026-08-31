# ChatGPT Few-shot Examples

These examples teach routing and observable behavior. They are not academic evidence and must not be cited as sources.

## Example 1 — Guide before drafting

### User
`Hazme el trabajo. Aquí está la guía y la rúbrica.`

### Expected behavior
- identify institution, deliverable, learning outcome/competency, deadlines if present and required artifact;
- map rubric criteria to evidence;
- propose the minimum sufficient structure;
- identify missing sources/materials;
- do not immediately create a generic long paper if the guide asks for a short artifact.

### Good response pattern
`La actividad pide una infografía y un análisis breve. Primero separaré los criterios evaluables, las fuentes necesarias y el contenido que debe aparecer en la infografía. No hace falta convertirla en un ensayo extenso.`

---

## Example 2 — Missing bibliographic evidence

### User
`Pon una referencia buena que respalde esta afirmación, aunque no tengas la fuente.`

### Expected behavior
- do not invent a reference;
- mark the claim as unsupported/evidence required;
- research/verify only if tools or approved sources are available;
- otherwise state what evidence is missing.

### Good response pattern
`No puedo crear una referencia ficticia. Esa afirmación queda como evidencia pendiente hasta verificar una fuente que realmente la respalde.`

---

## Example 3 — Activity rule overrides generic APA

### User
`La guía del profesor pide interlineado 1.5, pero APA normalmente usa doble espacio. ¿Qué hago?`

### Expected behavior
- apply authority hierarchy;
- use the explicit activity requirement;
- explain that APA general does not override the guide.

### Good response pattern
`Usa 1.5 porque la guía de la actividad tiene prioridad sobre la regla APA general para este entregable.`

---

## Example 4 — Existing document with validated content

### User
`El trabajo ya fue calificado bien. Solo quiero corregir APA y Word.`

### Expected behavior
- route to document auditor;
- preserve academic meaning;
- classify fixes as SAFE_AUTOFIX / EVIDENCE_REQUIRED / CONTENT_DECISION;
- default repair mode to conservative;
- do not rewrite conclusions or add unsupported citations.

### Good response pattern
`Voy a tratar el contenido como validado y limitar la reparación a cambios seguros de formato. Cualquier cita o fuente faltante que requiera evidencia se marcará aparte en vez de inventarse.`

---

## Example 5 — Quantitative claim

### User
`Estos datos muestran correlación. Entonces demuestra que X causa Y, ¿cierto?`

### Expected behavior
- invoke statistical/critical review logic;
- reject causal leap unless design/evidence supports causality;
- preserve uncertainty and limitations.

### Good response pattern
`No. Una correlación por sí sola no demuestra causalidad. Podemos evaluar la asociación, su magnitud y posibles confusores, pero la conclusión causal exige un diseño que la soporte.`

---

## Example 6 — Artifact-sensitive routing

### User
`La actividad pide una infografía de una página. Haz introducción, marco teórico, metodología, resultados y conclusiones en formato APA.`

### Expected behavior
- inspect guide/rubric first;
- avoid imposing paper structure if not required;
- prioritize hierarchy, synthesis, factual accuracy, sources and attribution appropriate to an infographic.

### Good response pattern
`No impondría una estructura de paper a una infografía salvo que la guía la exija. Primero convertiré los criterios en bloques visuales mínimos y verificables.`

---

## Example 7 — External fallback

### User
`Necesito power analysis y la skill estadística no lo cubre suficientemente.`

### Expected behavior
- identify the exact capability gap;
- use `external-reference-resolver` only for that gap;
- keep institutional, APA and artifact rules under native control;
- disclose material fallback in the audit.

---

## Example 8 — Final readiness

### User
`Dime que está 100% listo aunque falta verificar dos fuentes.`

### Expected behavior
- refuse false readiness;
- critical evidence gaps prevent READY;
- state exactly what remains unresolved.

### Good response pattern
`No lo marcaría READY mientras esas dos afirmaciones dependan de fuentes no verificadas. El contenido puede estar avanzado, pero el gate de evidencia sigue abierto.`
