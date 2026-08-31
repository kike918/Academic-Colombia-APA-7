# Academic Colombia — Orchestration Core

## Propósito

Definir cómo se coordinan las skills del repositorio sin depender de ChatGPT, Gemini, Spark, n8n u otro runtime específico.

La orquestación es declarativa y portable. Cada plataforma puede implementar este flujo usando sus propias capacidades, pero no debe cambiar la lógica académica canónica.

## Principios

1. La instrucción del usuario, guía y rúbrica gobiernan el flujo.
2. No todas las skills se ejecutan en todas las actividades.
3. La selección de skills depende del tipo de evidencia y de los gaps detectados.
4. Las fuentes y afirmaciones deben mantener trazabilidad.
5. Las referencias externas solo se usan mediante `external-reference-resolver`.
6. La validación final nunca se omite.
7. Si se modifica un artefacto existente, debe conservarse el contenido validado salvo autorización explícita.

## Flujo maestro

```text
INPUT
  ↓
academic-requirements-analyzer
  ↓
academic-template-selector
  ↓
CAPABILITY CHECK
  ├─ cobertura nativa suficiente
  └─ external-reference-resolver si existe un gap
  ↓
RESEARCH / EVIDENCE
  ├─ academic-research-ideation cuando aplica
  ├─ academic-source-evaluator
  ├─ academic-citation-manager
  ├─ academic-statistical-analysis cuando aplica
  └─ academic-tables-figures cuando aplica
  ↓
DRAFT / ARTIFACT
  ↓
apa7-academic-style
  ↓
academic-critical-review
  ↓
academic-artifact-validator
  ↓
DOCUMENT PATH (si existe DOCX u otro documento terminado)
  ├─ academic-document-auditor
  └─ academic-document-repair si se autorizan correcciones
  ↓
academic-final-review
  ↓
READY / NOT READY
```

## Routing por tipo de trabajo

### Documento nuevo
Requirements → template → research/evidence → drafting → APA → critical review → artifact validation → final review.

### Documento ya elaborado
Document auditor → evidence/citation gaps → repair autorizado → render/QA → final review.

### Infografía / pieza visual
Requirements → template/artifact selection → source evaluation → citation/table-figure rules → artifact validation → final review.

### XLSX / análisis cuantitativo
Requirements → source/data validation → statistical analysis → chart/table QA → artifact validation → final review.

### PPTX / presentación
Requirements → template/artifact selection → source evaluation → concise citation handling → visual/artifact QA → final review.

### Video / YouTube / landing page
Requirements → evidence classification → source evaluation when used as authority → accessibility/link validation → artifact validation → final review.

## Contrato mínimo entre skills

Cada skill debería producir, cuando sea aplicable:

```yaml
skill: skill-name
status: success | partial | blocked
findings: []
outputs: {}
gaps: []
next_recommended: []
confidence: high | medium | low
```

Los adaptadores de plataforma pueden transformar este envelope, pero deben conservar su semántica.

## Reglas de detención

Marcar `NOT READY` cuando exista cualquiera de los siguientes:

- requisito obligatorio de guía/rúbrica sin cubrir;
- fuente o dato crítico no verificable;
- cita recuperable sin referencia o referencia material sin respaldo;
- artefacto requerido inaccesible o corrupto;
- errores de cálculo/fórmula críticos;
- documento reparado sin QA visual cuando el formato lo requiera;
- cambio de contenido que requiera decisión del usuario.

## Independencia de plataforma

Este archivo no define webhooks, n8n, MCP, almacenamiento externo ni asistentes persistentes. Esas son capas de implementación opcionales y posteriores.

Los adaptadores de ChatGPT, Gemini y otras plataformas deben consumir esta orquestación desde el repositorio como fuente canónica.
