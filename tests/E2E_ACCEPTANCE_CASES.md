# End-to-End Academic Acceptance Cases

Casos reales anonimizados o representativos para validar el sistema completo. No contienen datos personales reales ni archivos privados.

## E2E-01 — UNAD DOCX: auditoría y reparación conservative
**Tipo:** documento terminado.
**Institución:** UNAD.
**Fixture conceptual:** trabajo de comercio internacional de ~20 páginas, tablas con datos, bibliografía amplia y pocas citas explícitas.
**Expected routing:** auditor → evidence mapper/citation manager para gaps → repair conservative solo SAFE_AUTOFIX → render QA → final review.
**Expected findings:** referencias sin sangría francesa; referencias huérfanas; tablas sin nota/fuente; headings con posible conflicto institucional; URLs genéricas.
**Safety:** no inventar fuentes de tablas ni citas.

## E2E-02 — UNAD infografía + análisis breve
**Expected routing:** requirements → template/artifact selection → source evaluator → evidence mapper → tables/figures → artifact validator → final review.
**Acceptance:** la infografía sigue siendo pieza central; no convertir la actividad en ensayo largo.

## E2E-03 — SENA informe corto
**Expected routing:** requirements → SENA profile → source evaluator → citation/APA → artifact validator → final review.
**Acceptance:** no heredar reglas UNAD no presentes en la guía SENA.

## E2E-04 — XLSX de costos/presupuesto
**Expected routing:** requirements → provenance/data checks → statistical/financial calculations cuando apliquen → chart/table QA → artifact validator → final review.
**Acceptance:** fórmulas críticas erróneas bloquean READY; no forzar márgenes/interlineado de documento sobre celdas.

## E2E-05 — PPTX de exposición académica
**Expected routing:** requirements → evidence map → citation handling → artifact validator → final review.
**Acceptance:** fuente cerca del claim/visual cuando corresponde, referencias finales cuando sean requeridas, jerarquía visual legible.

## E2E-06 — Video propio + URL de evidencia + DOCX
**Expected routing:** requirements → artifact validation independiente por componente → document path para DOCX → final review global.
**Acceptance:** video privado/restringido requerido = NOT READY aunque el DOCX esté perfecto.

## E2E-07 — Actividad de legislación colombiana
**Expected routing:** requirements → legal source policy → source evaluator → evidence mapper → citation manager → critical review → final review.
**Acceptance:** tipo/número/fecha/issuer/estado/URL oficial deben verificarse; no inventar artículos o vigencia.

## E2E-08 — Actividad estadística con correlación
**Expected routing:** requirements → data/source validation → statistical analysis → evidence mapper → critical review → tables/figures → final review.
**Acceptance:** no inferir causalidad desde correlación; reportar límites y supuestos.

## Matriz de aceptación común

Cada caso debe registrar:
1. inputs disponibles;
2. skills seleccionadas;
3. skills omitidas y motivo;
4. outputs bajo `core/SKILL-CONTRACT.md`;
5. gaps y critical gates;
6. resultado esperado `READY`, `NOT READY` o `USER DECISION REQUIRED`;
7. diferencias de plataforma si existieran.

## Criterio de v0.10

La versión pasa aceptación cuando los ocho casos pueden recorrerse sin:
- inventar evidencia;
- ejecutar skills innecesarias;
- perder gaps entre skills;
- permitir que un `critical_gate: fail` termine como READY;
- aplicar reglas de un artefacto a otro sin pertinencia.