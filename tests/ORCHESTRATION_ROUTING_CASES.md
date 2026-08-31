# Orchestration Routing Cases

Casos de aceptación para `academic-workflow-orchestrator`.

## Regla global

El orquestador debe seleccionar el conjunto mínimo suficiente de skills, preservar la jerarquía de autoridad y terminar en `academic-final-review`. No debe ejecutar capacidades irrelevantes por defecto.

## Caso 1 — DOCX nuevo UNAD con guía y rúbrica
**Input:** guía, rúbrica, fuentes de unidad, documento por construir.
**Expected:** requirements → template → source evaluator → evidence mapper → citation manager → APA → critical review → artifact validator → final review.
**Omitir:** document repair salvo que exista artefacto previo.

## Caso 2 — DOCX terminado, contenido ya evaluado positivamente
**Input:** DOCX existente; solicitud solo de auditoría/APA.
**Expected:** document auditor → evidence/citation gaps cuando existan → conservative repair autorizado → render QA → final review.
**Gate:** no modificar argumentos, datos o conclusiones.

## Caso 3 — Infografía
**Expected:** requirements → artifact/template selection → source evaluator → evidence mapper cuando existan claims materiales → tables/figures rules → artifact validator → final review.
**Omitir:** formato de ensayo y document repair.

## Caso 4 — XLSX financiero
**Expected:** requirements → source/data validation → statistical analysis cuando corresponda → tables/figures/chart QA → artifact validator → final review.
**Omitir:** reglas materiales de DOCX que no apliquen.

## Caso 5 — PPTX
**Expected:** requirements → source evaluator → evidence mapper → concise citation handling → artifact validator → final review.
**Gate:** legibilidad, atribución y cobertura de rúbrica.

## Caso 6 — Video + documento de soporte
**Expected:** requirements → source/evidence validation → artifact validator por componente → document audit/repair solo para el documento si aplica → final review global.
**Gate:** enlace privado o roto del video requerido = NOT READY.

## Caso 7 — Actividad jurídica colombiana
**Expected:** requirements → source evaluator → `core/LEGAL-COLOMBIA.md` → evidence mapper → citation manager → critical review → final review.
**Gate:** norma/sentencia no verificable = NOT READY o partial/blocked según centralidad.

## Caso 8 — Gap metodológico no cubierto nativamente
**Expected:** capability check → external-reference-resolver → uso limitado de referencia aprobada → retorno a QA nativo.
**Gate:** no permitir override de guía/rúbrica/institución/APA.

## Caso 9 — Cobertura nativa suficiente
**Expected:** NO llamar external-reference-resolver.

## Caso 10 — Falta guía pero usuario pide corrección de formato de DOCX
**Expected:** document auditor puede operar con perfil institucional/APA disponible, debe declarar limitación y no inventar requisitos de actividad.

## Caso 11 — Claim central sin evidencia
**Expected:** evidence mapper marca `EVIDENCE_GAP`; citation manager no inventa cita; final review = NOT READY si el claim es material.

## Caso 12 — Skill bloqueada
**Input:** fuente crítica inaccesible.
**Expected:** `status: blocked`, gap explícito, no transformar silenciosamente a success.

## Caso 13 — Hallazgo crítico resuelto
**Expected:** skill re-ejecutada; `critical_gate` puede pasar solo después de nueva validación.

## Caso 14 — Usuario excluye una sección no exigida
**Expected:** instrucción del usuario prevalece si no contradice guía/rúbrica; no reinsertar por convención APA.

## Caso 15 — Artefacto correcto, rúbrica incumplida
**Expected:** artifact validator puede pasar su dimensión, pero final review = NOT READY por requisito obligatorio pendiente.