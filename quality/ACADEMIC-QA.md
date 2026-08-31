# Academic QA

## Propósito

Definir los gates mínimos antes de declarar un entregable READY. Los puntajes ayudan a priorizar, pero nunca compensan un fallo crítico.

## Core gates

### Requisitos
- [ ] Institución identificada cuando aplica.
- [ ] Guía revisada o ausencia declarada.
- [ ] Rúbrica/instrumento revisado o ausencia declarada.
- [ ] Entregable correcto.
- [ ] Formato/medio de entrega correcto.
- [ ] Criterios obligatorios mapeados a evidencia.

### Contenido
- [ ] Responde exactamente a la actividad.
- [ ] Cubre criterios de evaluación.
- [ ] No hay relleno que desplace requisitos prioritarios.
- [ ] Conclusiones corresponden a resultados/evidencia.

## Evidence gates

- [ ] Claims materiales identificados.
- [ ] Claims que requieren sustento tienen evidencia verificable.
- [ ] No hay referencias tratadas como evidencia por simple afinidad temática.
- [ ] Fuentes críticas tienen autoridad, vigencia y recuperabilidad adecuadas.
- [ ] No hay evidencia inventada, localizadores falsos ni metadatos completados por intuición.
- [ ] Contradicciones o evidencia negativa relevante permanecen visibles.

## Citation / APA gates

- [ ] Correspondencia cita ↔ referencia.
- [ ] Referencias huérfanas justificadas o corregidas.
- [ ] DOI/URL verificados cuando aplica.
- [ ] Citas narrativas/parentéticas/textuales compatibles con perfil institucional.
- [ ] Tablas/figuras tienen atribución cuando corresponde.
- [ ] Formato APA no contradice guía/rúbrica/institución.

## Artifact gates

Aplicar `docs/ARTIFACT-VALIDATION-MATRIX.md` según el artefacto.

### DOCX/PDF derivado
- [ ] Setup de página/estilos relevante revisado.
- [ ] Headings/TOC/captions coherentes cuando existen.
- [ ] Render completo ejecutado cuando se modifica o audita materialmente el DOCX.
- [ ] Todas las páginas inspeccionadas visualmente.

### XLSX
- [ ] Fórmulas críticas revisadas.
- [ ] Unidades/etiquetas/fuentes visibles.
- [ ] No hay errores de fórmula materiales.
- [ ] Charts no inducen a interpretación engañosa.

### PPTX / visual
- [ ] Jerarquía y legibilidad.
- [ ] Claims/datos con atribución suficiente.
- [ ] Links/medios requeridos funcionan.

### Video / web / evidencia externa
- [ ] Accesible con permisos correctos.
- [ ] URL corresponde exactamente a la evidencia descrita.
- [ ] Autoría/fecha/título/plataforma verificables cuando se cita como fuente.

## Method / statistical gates

Cuando aplique:
- [ ] Método compatible con pregunta/diseño/datos.
- [ ] Supuestos revisados.
- [ ] Limitaciones declaradas.
- [ ] Correlación no presentada como causalidad sin diseño causal adecuado.
- [ ] Resultados no reducidos únicamente a significancia estadística.

## External fallback gates

- [ ] Cobertura nativa evaluada antes del fallback.
- [ ] Referencia externa aprobada en registry o justificada bajo política.
- [ ] Autoridad/licencia/frescura/scope verificados.
- [ ] El fallback solo cubre el gap específico.
- [ ] QA nativo reaplicado después.

## Contract / orchestration gates

- [ ] Skills relevantes cumplen `core/SKILL-CONTRACT.md`.
- [ ] `status: blocked` permanece visible hasta resolución.
- [ ] Gaps se preservan entre skills.
- [ ] Todo `critical_gate: fail` está resuelto y revalidado antes de READY.
- [ ] Skills innecesarias no se ejecutaron por defecto.
- [ ] El flujo termina en `academic-final-review`.

## Readiness Score

Ponderación orientativa:
- Requisitos/rúbrica: 30
- Contenido/razonamiento: 20
- Evidencia/fuentes: 20
- Citación/APA: 15
- Artefacto/presentación: 10
- Método/consistencia técnica: 5

El score es secundario a los gates.

## Decisión final

### READY
Todos los requisitos obligatorios cubiertos y ningún `critical_gate: fail` pendiente.

### NOT READY
Existe un fallo crítico verificable: guía/rúbrica, integridad, evidencia, cálculo, artefacto, acceso o QA obligatorio.

### USER DECISION REQUIRED
La resolución exige una decisión de contenido/alcance que no debe tomarse automáticamente.

No declarar un trabajo READY por promedio si existe una falla crítica.