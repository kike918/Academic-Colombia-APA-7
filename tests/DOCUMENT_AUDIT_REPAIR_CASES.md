# Document Audit & Repair — End-to-End Cases

## E2E-01 — UNAD DOCX bien calificado en contenido, APA parcial
Entrada: documento académico UNAD de ~20 páginas con formato material correcto, citas escasas, referencias huérfanas, tablas sin nota/fuente y referencias sin sangría francesa.
Esperado:
- `academic-document-auditor` no cuestiona el contenido disciplinar por defecto;
- detecta formato base correcto;
- marca citas faltantes como EVIDENCE_REQUIRED;
- marca referencias huérfanas;
- marca sangría francesa como SAFE_AUTOFIX;
- marca captions de tablas como SAFE_AUTOFIX cuando la estructura es inequívoca;
- marca fuentes ausentes de tablas como EVIDENCE_REQUIRED;
- ejecuta render e inspección visual;
- readiness APA/UNAD parcial, no aprobado por compensación.

## E2E-02 — Repair conservative
Entrada: reporte de E2E-01, modo conservative.
Esperado:
- corrige sangría francesa, formato de títulos/captions, estilos y TOC si aplica;
- no inserta citas nuevas sin evidencia;
- no inventa fuentes de tablas;
- no cambia conclusiones ni datos;
- produce archivo nuevo y conserva original;
- render final sin defectos.

## E2E-03 — Repair evidence-backed
Entrada: E2E-01 + fuentes verificadas para afirmaciones y tablas.
Esperado:
- añade solo citas cuyo soporte fue comprobado;
- completa notas de tabla con fuente demostrable;
- reemplaza URLs genéricas solo con enlaces específicos verificados;
- mantiene correspondencia cita ↔ referencia.

## E2E-04 — Referencia parece relacionada pero no se ha verificado
Esperado: no insertar cita; clasificar EVIDENCE_REQUIRED.

## E2E-05 — Referencia final no citada
Esperado: marcar referencia huérfana; repair no la elimina automáticamente si puede corresponder a evidencia pendiente.

## E2E-06 — Cita sin referencia
Esperado: error crítico; repair solo completa referencia si los metadatos son verificables.

## E2E-07 — Tabla propia con datos de terceros
Esperado: no aceptar “elaboración propia” como sustituto de atribución de datos; exigir fuente de datos.

## E2E-08 — Formato Word correcto pero render roto
Esperado: estado NO LISTO hasta corregir y re-renderizar.

## E2E-09 — Título nivel 1 en mitad de página bajo perfil UNAD
Esperado: detectar inconsistencia; decidir SAFE_AUTOFIX solo si la jerarquía del título es inequívoca, de lo contrario marcar para revisión estructural.

## E2E-10 — Resumen/Abstract/TOC posiblemente innecesarios
Esperado: no eliminarlos por APA; clasificar CONTENT_DECISION salvo que guía/rúbrica indiquen que no corresponden.

## E2E-11 — Documento calificado positivamente
Esperado: repair por defecto usa modo conservative para proteger contenido ya evaluado.

## E2E-12 — Auditoría sin guía/rúbrica
Esperado: declarar limitación; evaluar APA/perfil institucional conocido, pero no afirmar cumplimiento total de la actividad.

## Caso real anonimizado — patrón Tarea 5 comercio internacional
Características conocidas:
- UNAD/ECACEN;
- carta, márgenes 2,54 cm, TNR 12, doble espacio;
- TOC real y paginación correcta;
- cuerpo con pocas citas autor-fecha;
- múltiples referencias finales no citadas explícitamente;
- tablas con datos sin nota/fuente visible;
- referencias sin sangría francesa;
- algunas URLs generales;
- contenido disciplinar previamente evaluado de forma positiva.

Uso: fixture conceptual de regresión. No almacenar nombres personales ni el documento académico original en el repositorio público.
