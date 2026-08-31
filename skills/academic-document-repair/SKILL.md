# academic-document-repair

## Descripción
Regenera o corrige un documento académico a partir de una auditoría validada, preservando el contenido académico y aplicando solo cambios autorizados y trazables.

## Objetivo
Transformar un documento auditado en una versión corregida y lista para entregar sin introducir contenido, fuentes o metadatos no verificados.

## Entradas
- documento original;
- reporte de `academic-document-auditor`;
- lista de cambios autorizados;
- guía/rúbrica/institución;
- fuentes verificadas necesarias para hallazgos EVIDENCE_REQUIRED.

## Flujo
1. Confirmar que existe auditoría previa.
2. Separar cambios SAFE_AUTOFIX, EVIDENCE_REQUIRED y CONTENT_DECISION.
3. Aplicar SAFE_AUTOFIX directamente.
4. Aplicar EVIDENCE_REQUIRED solo cuando la fuente haya sido verificada.
5. Aplicar CONTENT_DECISION solo cuando esté expresamente autorizado por el usuario o exigido por guía/rúbrica.
6. Preservar texto, datos, conclusiones y alcance no afectados.
7. Reparar estilos, sangrías, interlineado, títulos, captions, TOC, referencias y enlaces.
8. Actualizar citas/referencias únicamente con metadatos verificables.
9. Revisar tablas/figuras y añadir notas/fuentes solo cuando la procedencia sea demostrable.
10. Guardar una copia nueva; no sobrescribir silenciosamente el original.
11. Ejecutar auditoría estructural post-repair.
12. Renderizar el DOCX a PNGs y revisar todas las páginas al 100%.
13. Si hay defectos visuales, corregir y re-renderizar hasta pasar QA.
14. Ejecutar `academic-final-review` antes de declarar listo.

## Reglas críticas
- El archivo original permanece intacto salvo instrucción explícita.
- No insertar citas por afinidad temática; la evidencia debe respaldar la afirmación.
- No inventar fuentes para tablas, figuras o datos.
- No eliminar secciones únicamente para ajustarse a una plantilla mínima si la guía no lo exige.
- No cambiar datos, resultados o conclusiones durante un repair de formato.
- Toda corrección material debe poder rastrearse a un hallazgo de auditoría o a una instrucción explícita.
- Para DOCX, render → inspección visual → iteración es gate obligatorio de entrega.

## Modos
### conservative
Solo SAFE_AUTOFIX. Recomendado por defecto cuando el contenido ya fue evaluado positivamente.

### evidence-backed
SAFE_AUTOFIX + EVIDENCE_REQUIRED con fuentes verificadas.

### full-revision
Incluye CONTENT_DECISION autorizado. Requiere especial cuidado para no cambiar la respuesta académica original sin necesidad.

## Salida
- archivo corregido con nombre nuevo;
- resumen de cambios aplicados;
- cambios no aplicados y motivo;
- fuentes verificadas incorporadas;
- resultado de render QA;
- readiness final;
- comparación conceptual original → corregido.

## Skill Contract v1

Cumplir `core/SKILL-CONTRACT.md`.
- `outputs.repaired_artifact`: copia corregida, nunca sobrescritura silenciosa.
- `outputs.applied_changes` y `outputs.skipped_changes`: cambios trazables.
- `findings`: defectos post-repair o divergencias detectadas.
- `gaps`: cambios bloqueados por evidencia o decisión.
- `next_recommended`: re-auditoría/artifact QA y `academic-final-review`.
- `critical_gate: fail` si el render/QA post-repair falla o si quedó un cambio crítico obligatorio sin resolver.