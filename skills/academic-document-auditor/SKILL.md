# academic-document-auditor

## Descripción
Audita documentos académicos terminados (principalmente DOCX y PDF exportado desde DOCX) contra la jerarquía usuario → guía → rúbrica → institución → APA 7, sin modificar el archivo durante la fase de diagnóstico.

## Objetivo
Detectar errores de implementación académica, APA/institucional, trazabilidad de fuentes y calidad técnica del artefacto, separando hallazgos de contenido, formato y evidencia.

## Entradas
- documento académico;
- institución;
- guía/rúbrica cuando estén disponibles;
- perfil institucional aplicable;
- referencias externas aprobadas cuando una capacidad nativa sea insuficiente.

## Flujo
1. Identificar el tipo de entregable y la institución.
2. Cargar guía/rúbrica si existen y fijar la jerarquía de autoridad.
3. Extraer estructura: portada, secciones, títulos, tablas, figuras, citas y referencias.
4. Auditar formato material: tamaño de página, márgenes, tipografía, interlineado, alineación, sangrías, numeración, encabezados/pies y saltos.
5. Auditar estilos y navegación: Heading levels, TOC, captions y numeración.
6. Auditar citas en texto y correspondencia cita ↔ referencia.
7. Detectar referencias huérfanas, citas sin referencia, DOI/URL dudosos y metadatos incompletos.
8. Auditar tablas y figuras: número, título, nota/fuente, legibilidad y trazabilidad.
9. Auditar enlaces y evidencia externa cuando existan.
10. Renderizar el DOCX a imágenes y revisar visualmente todas las páginas.
11. Clasificar cada hallazgo como crítico / recomendado / opcional.
12. Clasificar cada corrección como SAFE_AUTOFIX / EVIDENCE_REQUIRED / CONTENT_DECISION.
13. Calcular readiness global sin permitir que un área fuerte compense un fallo crítico.

## Reglas críticas
- No modificar el documento durante la auditoría.
- No reescribir contenido académico salvo que el usuario lo solicite expresamente.
- No añadir citas a afirmaciones solo porque una referencia parezca relacionada; si no puede demostrarse el soporte, marcar EVIDENCE_REQUIRED.
- No inventar DOI, URL, páginas, autores, fechas, fuentes de tablas o figuras.
- No inferir que una referencia final respalda una afirmación específica sin evidencia suficiente.
- Para DOCX, la auditoría no termina hasta ejecutar render → inspección visual de todas las páginas.
- Cuando una regla institucional contradiga APA general, aplicar la jerarquía definida.

## Tipos de hallazgo
### SAFE_AUTOFIX
Correcciones mecánicas que no alteran el significado académico, por ejemplo:
- sangría francesa;
- márgenes;
- interlineado;
- estilo/tamaño de fuente;
- alineación;
- niveles de título claramente determinados;
- formato de captions;
- actualización de TOC;
- URL visible como hipervínculo;
- encabezado de referencias.

### EVIDENCE_REQUIRED
Requiere validar una fuente antes de corregir, por ejemplo:
- insertar una cita faltante;
- atribuir una tabla sin fuente explícita;
- reemplazar una URL genérica por un recurso específico;
- completar DOI/fecha/editorial;
- afirmar que una fuente respalda una conclusión concreta.

### CONTENT_DECISION
Puede cambiar el alcance o significado del trabajo, por ejemplo:
- eliminar secciones;
- reescribir una conclusión;
- modificar una interpretación disciplinar;
- cambiar datos o resultados;
- añadir contenido no exigido.

## Salida
Entregar:
- resumen ejecutivo;
- matriz de hallazgos;
- severidad;
- ubicación;
- regla aplicable;
- clasificación de corrección;
- propuesta de corrección;
- evidencia pendiente si aplica;
- readiness por dimensión y global;
- lista de cambios autorizables para `academic-document-repair`.

## Skill Contract v1

Cumplir `core/SKILL-CONTRACT.md`.

- `outputs.audit_findings`: matriz de hallazgos y ubicación.
- `outputs.repair_classes`: SAFE_AUTOFIX / EVIDENCE_REQUIRED / CONTENT_DECISION.
- `findings`: errores técnicos, académicos, APA y de trazabilidad.
- `gaps`: evidencia o reglas no disponibles.
- `next_recommended`: `academic-evidence-mapper`, `academic-citation-manager`, `academic-document-repair` o decisión del usuario.
- `critical_gate: fail` si existe un defecto crítico de guía/rúbrica, integridad, evidencia o render.