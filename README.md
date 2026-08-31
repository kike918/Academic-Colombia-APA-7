# Academic Colombia — APA 7

**Academic Colombia** es un framework académico declarativo y modular para asistentes de IA. Ayuda a analizar, investigar, construir, auditar y revisar entregables académicos con foco inicial en **APA 7, UNAD y SENA**.

No es una aplicación tradicional ni un único prompt gigante. El repositorio organiza conocimiento, perfiles institucionales, Skills, routing, evidencia, QA, adapters y pruebas de aceptación para que un asistente pueda aplicar un flujo académico consistente.

> **Principio central:** la guía y la rúbrica gobiernan el trabajo. APA y las reglas institucionales ayudan a implementarlo correctamente, pero no reemplazan requisitos explícitos de la actividad.

## Estado

**Versión estable:** `1.0.0`

v1.0.0 estabiliza:

- Skill Contract v1;
- jerarquía de autoridad;
- routing y readiness;
- cadena claim → evidence → source → citation;
- critical gates;
- separación core / platform adapters;
- 16 Skills nativas;
- perfiles UNAD y SENA;
- distribución reproducible;
- validación declarativa del repositorio.

La cobertura empírica es real pero deliberadamente acotada. El registro distingue entre capacidad implementada, fixture de aceptación, ejecución real y runtime de plataforma.

➡️ [Release readiness](docs/V1.0-RELEASE-READINESS.md) · [Empirical Evidence Registry](tests/EMPIRICAL_EVIDENCE_REGISTRY.md) · [Compatibility policy](docs/COMPATIBILITY-POLICY.md)

## Qué resuelve

Academic Colombia divide el trabajo académico en capacidades pequeñas y auditables:

- leer guías y rúbricas;
- decidir estructura y artefacto;
- investigar y evaluar fuentes;
- verificar hechos actuales;
- mapear afirmaciones a evidencia;
- gestionar citas y referencias;
- aplicar APA 7;
- adaptar reglas UNAD/SENA;
- revisar tablas, figuras y análisis cuantitativo;
- validar DOCX, XLSX, PPTX, video, web, infografías y gráficos;
- auditar documentos terminados;
- reparar sin alterar silenciosamente contenido validado;
- ejecutar QA final antes de declarar un entregable listo.

## Cómo funciona

```text
INPUT
  ↓
requirements analyzer
  ↓
template selector
  ↓
capability / evidence check
  ↓
research + source evaluation
  ↓
evidence mapping + citations
  ↓
draft / artifact
  ↓
APA / method / artifact validation
  ↓
critical review
  ↓
document audit / repair when applicable
  ↓
final review
  ↓
READY / NOT READY / USER DECISION REQUIRED
```

No todas las Skills se ejecutan siempre. `academic-workflow-orchestrator` selecciona únicamente las capacidades necesarias para la actividad.

➡️ [Routing canónico](core/ORCHESTRATION.md)

## Jerarquía de autoridad

Cuando exista conflicto entre reglas:

1. instrucción explícita del usuario;
2. guía oficial de la actividad;
3. rúbrica o instrumento de evaluación;
4. instrucciones del tutor/docente;
5. reglas institucionales;
6. APA 7;
7. convenciones académicas generales.

Esta jerarquía opera junto con los gates de integridad y evidencia del core; una instrucción no convierte automáticamente una afirmación falsa o una fuente inventada en válida.

## Skills

Academic Colombia incluye **16 Skills nativas**.

| Área | Skills |
|---|---|
| Orquestación | `academic-workflow-orchestrator` |
| Requisitos / estructura | `academic-requirements-analyzer`, `academic-template-selector` |
| Investigación / evidencia | `academic-research-ideation`, `academic-source-evaluator`, `academic-evidence-mapper`, `academic-citation-manager` |
| Análisis | `academic-statistical-analysis`, `academic-critical-review` |
| APA / artefactos | `apa7-academic-style`, `academic-tables-figures`, `academic-artifact-validator` |
| Auditoría / reparación | `academic-document-auditor`, `academic-document-repair` |
| Gate final | `academic-final-review` |
| Fallback | `external-reference-resolver` |

➡️ [Directorio completo de Skills](docs/SKILLS-DIRECTORY.md)

Cada Skill mantiene su fuente canónica en:

```text
skills/<skill-name>/SKILL.md
```

## Skill Contract v1

Las Skills interoperables usan:

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

Un `critical_gate: fail` no puede ser compensado por un buen promedio en otros criterios.

➡️ [Skill Contract](core/SKILL-CONTRACT.md)

## Perfiles institucionales

### UNAD

Perfil institucional con fuentes verificadas, reglas de plantilla y comportamiento sensible a guía/rúbrica.

➡️ [UNAD](institutions/UNAD.md)

### SENA

Perfil separado, orientado a resultados de aprendizaje, evidencias, criterios e instrumentos. No hereda automáticamente reglas UNAD.

➡️ [SENA](institutions/SENA.md)

Las coberturas UNAD/SENA son **bounded coverage**: suficientes para uso estable del framework, no una afirmación de que todos los centros, programas, tutores o plantillas locales hayan sido probados.

## Evidencia empírica

Antes de v1.0 el framework fue probado con trabajos reales anonimizados, incluyendo:

- auditoría/reparación de DOCX;
- informes UNAD y SENA;
- presentaciones visuales;
- actividades de comercio internacional y normativa;
- diseño técnico de smart contract;
- workbook XLSX contable con reconciliación entre diario, cuentas T, balance y comprobante SIIGO;
- casos negativos de fuentes débiles, cifras mal interpretadas, periodos no comparables y datos obsoletos.

Esto permitió validar una regla clave:

```text
Visual PASS + Evidence FAIL = NOT READY
```

➡️ [Registro empírico](tests/EMPIRICAL_EVIDENCE_REGISTRY.md)

## Artefactos

El QA es sensible al tipo de artefacto:

- **DOCX/PDF** — estructura, APA, referencias, tablas/figuras, render;
- **XLSX** — fórmulas, unidades, consistencia, gráficos, reconciliación;
- **PPTX / presentaciones** — jerarquía, legibilidad, evidencia, citación;
- **infografías** — síntesis, factualidad, fuentes, atribución;
- **video** — evidencia, acceso, autoría y referencia cuando aplica;
- **web/landing** — contenido requerido, acceso y trazabilidad;
- **gráficos** — escala, etiquetas, unidades y fuente.

➡️ [Artifact Validation Matrix](docs/ARTIFACT-VALIDATION-MATRIX.md)

## Plataformas

El core es platform-neutral.

### ChatGPT

`platforms/chatgpt-gpt/` contiene Instructions, configuración, Knowledge Manifest, estrategia de contexto, instalación y suites específicas.

La distribución de las 16 Skills puede generarse como ZIPs individuales y bundle reproducible.

➡️ [Instalar Skills](distribution/INSTALL-CHATGPT-SKILLS.md) · [Custom GPT adapter](platforms/chatgpt-gpt/INSTALLATION.md)

**Runtime real del Custom GPT:** todavía `NOT_CLAIMED` hasta ejecutar una instancia real.

### Gemini

`platforms/gemini/` contiene el adapter de Gem, Knowledge Manifest, instalación y casos cross-platform.

➡️ [Gemini adapter](platforms/gemini/INSTALLATION.md)

**Runtime real del Gem:** todavía `NOT_CLAIMED` hasta ejecutar una instancia real.

## Testing y CI

El repositorio incluye suites declarativas para:

- APA;
- UNAD/SENA;
- research/evidence;
- Skill Contract;
- routing;
- artefactos;
- auditoría/reparación;
- distribución;
- ChatGPT/Gemini;
- adversarial prompts;
- evidencia empírica.

`.github/workflows/validate.yml` ejecuta validación estructural del framework: VERSION/CHANGELOG, links, manifests, Skills, contratos, registry y packaging.

CI no decide si un argumento académico es verdadero; protege la consistencia del framework.

## Arquitectura

```text
Academic-Colombia-APA-7/
├── core/
├── institutions/
├── templates/
├── skills/
├── distribution/
├── external-references/
├── quality/
├── tests/
├── platforms/
├── scripts/
├── docs/
├── LICENSE
├── CONTRIBUTING.md
├── CHANGELOG.md
├── VERSION
└── README.md
```

➡️ [Arquitectura](docs/ARCHITECTURE.md) · [Roadmap](docs/ROADMAP.md)

## Compatibilidad y releases

Desde v1.0, Semantic Versioning se aplica al **comportamiento observable** del framework, no solo a los archivos.

Un cambio de Markdown que rompa routing, readiness, autoridad o Skill Contract puede ser un cambio MAJOR aunque no exista código ejecutable.

➡️ [Compatibility and Release Policy](docs/COMPATIBILITY-POLICY.md)

## Documentación web

`docs/index.md` es una portada mínima compatible con GitHub Pages. La web debe ser una vista de la documentación canónica, no una segunda fuente de verdad.

➡️ [Landing Markdown](docs/index.md)

## Gobernanza

- `main` es la rama canónica;
- cambios por branch/fork + pull request;
- linear history;
- conversaciones de PR deben resolverse;
- no se permiten bypass rutinarios;
- cambios de comportamiento requieren pruebas y release note;
- artefactos reales solo se registran de forma anonimizada.

➡️ [Repository Governance](docs/REPOSITORY-GOVERNANCE.md)

## Licencia

El contenido original de Academic Colombia se distribuye bajo **MIT License**.

Materiales, marcas, normas y recursos de terceros o instituciones conservan sus propios derechos. La licencia no implica afiliación ni respaldo de APA, UNAD, SENA u otras organizaciones mencionadas.

➡️ [LICENSE](LICENSE) · [License scope](docs/LICENSE-SCOPE.md)
