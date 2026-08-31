# Academic Colombia — APA 7

**Academic Colombia** es un framework modular de skills para asistentes de IA orientado a planificar, investigar, construir, auditar y corregir entregables académicos en el contexto colombiano, con foco inicial en **APA 7, UNAD y SENA**.

El repositorio es la **fuente canónica**. Las implementaciones en ChatGPT, Gemini, Sparks u otras plataformas deben consumir esta lógica sin crear reglas paralelas.

> **Principio central:** la guía y la rúbrica gobiernan el trabajo; APA y las reglas institucionales ayudan a implementarlo correctamente, pero nunca reemplazan requisitos explícitos de la actividad.

## ¿Qué problema resuelve?

Academic Colombia evita que un asistente académico funcione como un único prompt gigante. Divide el trabajo en capacidades pequeñas, auditables y reutilizables:

- analizar guías y rúbricas;
- seleccionar la estructura adecuada;
- investigar y evaluar fuentes;
- mapear afirmaciones a evidencia;
- gestionar citas y referencias;
- aplicar APA 7 y perfiles institucionales;
- analizar datos cuantitativos;
- revisar tablas y figuras;
- validar DOCX, XLSX, PPTX, video, web, infografías y gráficos;
- auditar documentos terminados;
- corregirlos sin alterar silenciosamente contenido validado;
- ejecutar QA final antes de declarar un entregable listo.

## Estado

**Versión estable actual:** `0.10.2`

El motor académico ya cuenta con orquestación declarativa, contrato común entre skills, trazabilidad de evidencia, gates críticos, pruebas de routing y escenarios E2E. Los adapters de plataforma aún están en proceso de empaquetado y validación.

## Skills

Academic Colombia incluye actualmente **16 skills nativas**.

| Área | Skills principales |
|---|---|
| Orquestación | `academic-workflow-orchestrator` |
| Requisitos y estructura | `academic-requirements-analyzer`, `academic-template-selector` |
| Investigación y evidencia | `academic-research-ideation`, `academic-source-evaluator`, `academic-evidence-mapper`, `academic-citation-manager` |
| Análisis | `academic-statistical-analysis`, `academic-critical-review` |
| APA y artefactos | `apa7-academic-style`, `academic-tables-figures`, `academic-artifact-validator` |
| Auditoría y reparación | `academic-document-auditor`, `academic-document-repair` |
| Gate final | `academic-final-review` |
| Fallback controlado | `external-reference-resolver` |

➡️ **[Ver directorio completo de skills](docs/SKILLS-DIRECTORY.md)**

Cada skill conserva su definición detallada en `skills/<skill-name>/SKILL.md`.

## Cómo funciona

El flujo no ejecuta todas las skills por defecto. `academic-workflow-orchestrator` selecciona las capacidades necesarias según la actividad, institución, artefacto y estado del trabajo.

```text
INPUT
  ↓
requirements analyzer
  ↓
template selector
  ↓
capability check
  ↓
research / evidence
  ↓
draft or artifact
  ↓
APA / citations / method
  ↓
critical review
  ↓
artifact validation
  ↓
document audit / repair when applicable
  ↓
final review
  ↓
READY / NOT READY / USER DECISION REQUIRED
```

El routing canónico está definido en [`core/ORCHESTRATION.md`](core/ORCHESTRATION.md).

## Contrato entre skills

Todas las skills interoperables usan el contrato definido en [`core/SKILL-CONTRACT.md`](core/SKILL-CONTRACT.md):

```yaml
skill: skill-name
status: success | partial | blocked
findings: []
outputs: {}
gaps: []
next_recommended: []
confidence: high | medium | low
critical_gate: pass | fail | not_applicable
```

Un `critical_gate: fail` no puede ser compensado por un promedio alto de otros criterios.

## Jerarquía de autoridad

Cuando exista conflicto entre reglas, se aplica este orden:

1. instrucción explícita del usuario;
2. guía oficial de la actividad;
3. rúbrica o instrumento de evaluación;
4. instrucciones del tutor/docente;
5. reglas institucionales;
6. APA 7;
7. convenciones académicas generales.

## Contextos institucionales

### UNAD

El perfil UNAD incorpora reglas verificadas de APA 7 institucional, plantilla y comportamiento esperado para actividades, guías y rúbricas.

➡️ [`institutions/UNAD.md`](institutions/UNAD.md)

### SENA

El perfil SENA adapta el flujo a competencias, resultados de aprendizaje, evidencias, criterios e instrumentos sin heredar automáticamente reglas UNAD.

➡️ [`institutions/SENA.md`](institutions/SENA.md)

## Artefactos soportados

Academic Colombia trata APA y QA de forma sensible al artefacto:

- **DOCX/PDF académico:** formato, estructura, citas, referencias, tablas/figuras y render visual;
- **XLSX:** fórmulas, unidades, fuentes, estructura, gráficos y errores;
- **PPTX:** jerarquía, legibilidad, evidencia, citación y atribución;
- **infografías:** factualidad, jerarquía, fuentes y atribución;
- **video/YouTube:** autoría, acceso, relación con la evidencia y referencia cuando aplica;
- **landing/web:** acceso, contenido requerido, evidencia y uso como fuente;
- **gráficos:** datos, escala, etiquetas, unidades, fuente y lectura no engañosa.

➡️ [`docs/ARTIFACT-VALIDATION-MATRIX.md`](docs/ARTIFACT-VALIDATION-MATRIX.md)

## Auditoría y reparación documental

Para documentos existentes se usa un flujo separado:

```text
document auditor
   ↓
SAFE_AUTOFIX / EVIDENCE_REQUIRED / CONTENT_DECISION
   ↓
authorized repair
   ↓
render + visual QA
   ↓
final review
```

Esto permite corregir implementación APA/Word sin reescribir innecesariamente contenido académico ya validado.

➡️ [`docs/DOCUMENT-AUDIT-REPAIR-WORKFLOW.md`](docs/DOCUMENT-AUDIT-REPAIR-WORKFLOW.md)

## Uso en plataformas de IA

El core es platform-neutral.

### ChatGPT

El adapter actual se encuentra en:

`platforms/chatgpt-gpt/`

El empaquetado de producción y Knowledge Manifest forman parte de la siguiente etapa del roadmap.

### Gemini

El adapter base se encuentra en:

`platforms/gemini/`

Será actualizado después de estabilizar el paquete ChatGPT.

### Sparks / otras plataformas

Podrán consumir las mismas skills y contratos mediante adapters específicos sin modificar el core académico.

## Cómo usar el repositorio

### Para leer o reutilizar una skill

1. abre [`docs/SKILLS-DIRECTORY.md`](docs/SKILLS-DIRECTORY.md);
2. identifica la capacidad necesaria;
3. abre el `SKILL.md` correspondiente;
4. incorpora esa skill al sistema/agente compatible;
5. conserva `core/ORCHESTRATION.md`, `core/SKILL-CONTRACT.md` y los perfiles institucionales relevantes como contexto común.

### Para implementar Academic Colombia completo

Usa como base:

```text
core/
institutions/
templates/
skills/
quality/
external-references/
```

Los archivos de `platforms/` son adapters, no la fuente de verdad.

## Arquitectura del repositorio

```text
Academic-Colombia-APA-7/
├── core/                 # reglas y contratos neutrales de plataforma
├── institutions/         # perfiles UNAD y SENA
├── templates/            # perfiles/plantillas académicas
├── skills/               # capacidades modulares
├── external-references/  # fallback externo controlado
├── quality/              # gates de QA académico
├── tests/                # aceptación, regresión, routing y E2E
├── platforms/            # adapters para asistentes
├── docs/                 # arquitectura, workflows y documentación
├── LICENSE
├── CONTRIBUTING.md
├── CHANGELOG.md
├── VERSION
└── README.md
```

➡️ [Arquitectura detallada](docs/ARCHITECTURE.md) · [Roadmap](docs/ROADMAP.md) · [Academic QA](quality/ACADEMIC-QA.md)

## Testing

El repositorio incluye suites para:

- motor APA;
- compatibilidad UNAD;
- templates;
- research skills;
- referencias externas;
- validación de artefactos;
- auditoría/reparación documental;
- Skill Contract;
- routing de orquestación;
- escenarios E2E.

Los escenarios E2E distinguen explícitamente entre casos realmente ejecutados y fixtures preparados para validación futura.

## Fuentes externas

Las fuentes externas no se importan silenciosamente. Se evalúan y registran por autoridad, vigencia, licencia y uso permitido.

➡️ [`external-references/REGISTRY.md`](external-references/REGISTRY.md)

La clasificación canónica es:

- **A:** autoridad primaria oficial;
- **B:** universidad / fuente académica fuerte;
- **C:** referencia técnica o metodológica;
- **D:** guía secundaria especializada;
- **E:** producto, blog, vendor o comunidad.

## Documentación web

`docs/index.md` contiene una portada mínima preparada para **GitHub Pages**. Su objetivo es explicar el proyecto, sus reglas básicas y cómo navegar las skills sin reproducir un manual completo de APA.

La documentación web debe seguir siendo una vista de los Markdown canónicos del repositorio, no una segunda fuente de verdad.

➡️ [`docs/index.md`](docs/index.md) · [`docs/DOCUMENTATION-STRATEGY.md`](docs/DOCUMENTATION-STRATEGY.md)

## Gobernanza

- `main` es la rama canónica y está protegida por ruleset;
- los cambios llegan mediante branch/fork + pull request;
- no existe bypass rutinario de la protección;
- los ejemplos académicos reales deben anonimizarse antes de convertirse en tests;
- cambios de comportamiento requieren tests y actualización de versión/changelog.

➡️ [`CONTRIBUTING.md`](CONTRIBUTING.md) · [`docs/REPOSITORY-GOVERNANCE.md`](docs/REPOSITORY-GOVERNANCE.md)

## Licencia

Academic Colombia se distribuye bajo la **MIT License** para el contenido original del proyecto.

Los materiales, normas, marcas y recursos externos o institucionales conservan sus propios derechos y condiciones. La licencia no otorga acceso de escritura al repositorio ni implica afiliación o respaldo institucional.

➡️ [`LICENSE`](LICENSE) · [`docs/LICENSE-SCOPE.md`](docs/LICENSE-SCOPE.md)
