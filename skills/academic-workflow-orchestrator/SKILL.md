# academic-workflow-orchestrator

## Descripción

Coordina las skills de Academic Colombia según el tipo de actividad, artefacto, institución, cobertura disponible y estado del trabajo.

No reemplaza las skills especializadas. Decide cuáles ejecutar, en qué orden y cuándo detener el flujo.

## Fuente canónica

Leer y aplicar `core/ORCHESTRATION.md`.

## Entradas

- instrucción del usuario;
- guía/rúbrica cuando exista;
- institución;
- artefactos disponibles;
- estado del trabajo: nuevo / borrador / terminado / corregido;
- resultados previos de otras skills si existen.

## Flujo

1. Identificar el objetivo y estado del trabajo.
2. Ejecutar o reutilizar `academic-requirements-analyzer` cuando haya guía/rúbrica.
3. Determinar el tipo de artefacto y seleccionar las skills necesarias.
4. Omitir skills que no aporten al entregable.
5. Evaluar cobertura nativa.
6. Si existe un gap material, llamar `external-reference-resolver`.
7. Mantener trazabilidad entre outputs de skills.
8. Pasar por los gates de calidad correspondientes.
9. Terminar siempre en `academic-final-review` antes de declarar READY.

## Routing mínimo

### Documento nuevo
requirements → template → research/evidence → citation/APA → critical review → artifact validation → final review.

### Documento existente
academic-document-auditor → evidence/citation resolution si aplica → academic-document-repair autorizado → artifact/visual QA → final review.

### XLSX / análisis cuantitativo
requirements → source/data validation → statistical analysis → tables/charts → artifact validation → final review.

### PPTX / visual / video / web
requirements → source/evidence validation → artifact-specific validation → final review.

## Reglas críticas

- No ejecutar todas las skills por defecto.
- No usar n8n, webhooks, RAG externo o asistentes persistentes como requisito del workflow.
- No mezclar lógica de plataforma con reglas académicas.
- No introducir una referencia externa cuando la cobertura nativa sea suficiente.
- No declarar READY si queda un requisito obligatorio, evidencia crítica o QA pendiente.
- Si el contenido fue previamente validado y solo se solicita formato, activar reparación conservadora.

## Salida

Entregar un plan/rastro de ejecución con:

- skills ejecutadas;
- skills omitidas y razón;
- findings/gaps;
- fallbacks externos utilizados, si existen;
- estado final: READY / NOT READY / USER DECISION REQUIRED.
