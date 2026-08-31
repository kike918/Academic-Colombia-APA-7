# Academic Colombia — Orchestration Core

## Propósito

Definir cómo se coordinan las skills del repositorio sin depender de ChatGPT, Gemini, Spark, n8n u otro runtime específico.

La orquestación es declarativa y portable. Cada plataforma puede implementar este flujo usando sus propias capacidades, pero no debe cambiar la lógica académica canónica.

## Contrato común

Toda interoperabilidad debe preservar la semántica de `core/SKILL-CONTRACT.md`.

El orquestador puede transformar la representación (Markdown/JSON/YAML/objetos internos), pero no puede perder:
- status;
- findings;
- outputs;
- gaps;
- next_recommended;
- confidence;
- critical_gate.

## Principios

1. La instrucción del usuario, guía y rúbrica gobiernan el flujo.
2. No todas las skills se ejecutan en todas las actividades.
3. La selección de skills depende del tipo de evidencia, artefacto, estado del trabajo y gaps detectados.
4. Las fuentes y afirmaciones deben mantener trazabilidad.
5. Las referencias externas solo se usan mediante `external-reference-resolver`.
6. La validación final nunca se omite.
7. Si se modifica un artefacto existente, debe conservarse el contenido validado salvo autorización explícita.
8. Un `status: blocked` no se convierte en success sin resolver el gap.
9. Un `critical_gate: fail` se propaga hasta que una revalidación explícita lo resuelva.
10. Solo `academic-final-review` puede declarar el estado global READY.

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
  └─ external-reference-resolver si existe un gap de capacidad
  ↓
RESEARCH / EVIDENCE
  ├─ academic-research-ideation cuando aplica
  ├─ academic-source-evaluator
  ├─ academic-evidence-mapper cuando existen claims materiales
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
DOCUMENT PATH (si existe documento terminado)
  ├─ academic-document-auditor
  └─ academic-document-repair si se autorizan correcciones
  ↓
academic-final-review
  ↓
READY / NOT READY / USER DECISION REQUIRED
```

## Routing por tipo de trabajo

### Documento nuevo
Requirements → template → research/source evaluation → evidence mapping → citation/APA → critical review → artifact validation → final review.

### Documento ya elaborado
Document auditor → evidence/citation gaps → repair autorizado → render/artifact QA → final review.

### Infografía / pieza visual
Requirements → artifact/template selection → source evaluation → evidence mapping para claims materiales → table/figure rules → artifact validation → final review.

### XLSX / análisis cuantitativo
Requirements → source/data validation → statistical analysis → evidence mapping de claims derivados → chart/table QA → artifact validation → final review.

### PPTX / presentación
Requirements → artifact/template selection → source evaluation → evidence mapping → concise citation handling → visual/artifact QA → final review.

### Video / YouTube / landing page
Requirements → evidence classification → source evaluation cuando se use como autoridad → accessibility/link validation → artifact validation → final review.

## Propagación de gates

- Cada skill conserva los gates críticos recibidos que sigan sin resolver.
- Una skill correctiva puede resolver un gate solo si vuelve a validar el criterio que falló.
- Un score alto no puede compensar un `critical_gate: fail`.
- `USER DECISION REQUIRED` se usa cuando el bloqueo depende de una decisión de contenido/alcance que el sistema no debe tomar solo.

## Regla claim → evidence

Cuando un entregable contiene afirmaciones materiales que requieren sustento:

```text
source evaluator
      ↓
academic-evidence-mapper
      ↓
citation manager
      ↓
critical review
```

Una referencia bibliográfica no constituye automáticamente evidencia de una afirmación.

## Reglas de detención

Marcar NOT READY cuando exista cualquiera de los siguientes:
- requisito obligatorio de guía/rúbrica sin cubrir;
- fuente o dato crítico no verificable;
- claim central que requiere evidencia y permanece en `EVIDENCE_GAP`;
- cita recuperable sin referencia o referencia material falsa/no reconciliable;
- artefacto requerido inaccesible o corrupto;
- errores de cálculo/fórmula críticos;
- documento reparado sin QA visual cuando el formato lo requiera;
- cambio de contenido que requiera decisión del usuario;
- cualquier `critical_gate: fail` no resuelto.

## Independencia de plataforma

Este archivo no define webhooks, n8n, MCP, almacenamiento externo ni asistentes persistentes. Esas son capas de implementación opcionales y posteriores.

Los adaptadores de ChatGPT, Gemini y otras plataformas deben consumir esta orquestación y el skill contract desde el repositorio como fuente canónica.