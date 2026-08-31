# academic-final-review

## Descripción
Audita un entregable académico terminado contra guía, rúbrica, fuentes, APA y presentación.

## Entradas
- documento final;
- guía;
- rúbrica;
- institución;
- resultados previos de skills cuando existan.

## Flujo
1. Comparar documento vs guía.
2. Comparar documento vs rúbrica.
3. Identificar criterios sin evidencia.
4. Revisar estructura.
5. Revisar fuentes.
6. Revisar APA.
7. Revisar consistencia interna.
8. Detectar sobreextensión y relleno.
9. Reunir los `critical_gate` recibidos de otras skills.
10. Calcular readiness sin permitir que un promedio compense un fallo crítico.
11. Priorizar correcciones por impacto en la nota y riesgo de integridad.

## Salida
### Academic QA
- Guide compliance
- Rubric coverage
- Source quality
- Citation/reference integrity
- APA
- Presentation
- Readiness score
- Blocking issues

### Acciones
Separar:
- críticas;
- recomendadas;
- opcionales.

## Skill Contract v1

Cumplir `core/SKILL-CONTRACT.md`.

- `outputs.readiness`: READY / NOT_READY / USER_DECISION_REQUIRED.
- `outputs.blocking_issues`: fallos críticos no resueltos.
- `findings`: síntesis priorizada de QA.
- `gaps`: validaciones o insumos pendientes.
- `next_recommended`: acciones correctivas concretas; vacío si READY.
- `critical_gate: fail` siempre que exista un requisito obligatorio, fallo de integridad/evidencia o gate crítico propagado sin resolver.

Esta skill es el único punto que puede declarar el estado global READY.