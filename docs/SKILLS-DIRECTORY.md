# Academic Colombia — Skills Directory

Este documento es el directorio funcional de las skills nativas de Academic Colombia. Su propósito es responder rápidamente cuatro preguntas:

1. ¿Qué skill existe?
2. ¿Para qué sirve?
3. ¿Cuándo debe usarse?
4. ¿Con qué otras skills se conecta?

La selección real de skills está gobernada por `core/ORCHESTRATION.md` y ejecutada conceptualmente por `academic-workflow-orchestrator`. No todas las skills deben ejecutarse en todos los trabajos.

## Mapa rápido

| Skill | Función principal | Úsala cuando... |
|---|---|---|
| `academic-workflow-orchestrator` | Enruta el flujo completo | hay que decidir qué skills ejecutar y en qué orden |
| `academic-requirements-analyzer` | Extrae requisitos de guía/rúbrica | inicia una actividad o hay que auditar cobertura |
| `academic-template-selector` | Selecciona estructura/formato proporcional | hay que decidir qué tipo de documento/entregable construir |
| `academic-research-ideation` | Formula preguntas, hipótesis e ideas | se necesita explorar un problema sin confundir ideas con evidencia |
| `academic-source-evaluator` | Evalúa autoridad, vigencia y recuperabilidad de fuentes | una fuente debe aceptarse, rechazarse o limitarse |
| `academic-evidence-mapper` | Mapea claim → evidence → source → citation | hay que demostrar qué evidencia respalda cada afirmación |
| `academic-citation-manager` | Concilia citas y referencias | hay citas faltantes, referencias huérfanas o metadatos que validar |
| `academic-statistical-analysis` | Analiza datos cuantitativos | la actividad incluye estadística, regresión, correlación o datos |
| `academic-tables-figures` | Revisa tablas y figuras | hay tablas, gráficos, figuras o datos visuales que atribuir |
| `apa7-academic-style` | Aplica/revisa APA 7 | hay que normalizar citas, referencias y presentación APA |
| `academic-critical-review` | Revisa razonamiento y soporte | hay que validar argumentos, inferencias y conclusiones |
| `academic-artifact-validator` | Valida el artefacto real | el entregable es DOCX, XLSX, PPTX, video, web, infografía o gráfico |
| `academic-document-auditor` | Audita documentos terminados | existe un DOCX/PDF que debe revisarse sin modificarlo |
| `academic-document-repair` | Corrige/regenera desde una auditoría | existe un audit y hay cambios autorizados |
| `academic-final-review` | Gate final READY / NOT READY | se va a declarar el trabajo listo para entregar |
| `external-reference-resolver` | Fallback externo controlado | una capacidad requerida no está cubierta por skills nativas |

---

## 1. Orquestación y requisitos

### `academic-workflow-orchestrator`

**Propósito:** dirigir el trabajo académico completo sin reemplazar las skills especializadas.

**Responsabilidades:** seleccionar skills, decidir orden, omitir capacidades innecesarias, propagar `critical_gate`, usar fallback externo solo ante un gap real y terminar en `academic-final-review`.

**Conecta con:** todas las skills.

### `academic-requirements-analyzer`

**Propósito:** convertir una guía, rúbrica o enunciado en requisitos accionables.

**Responsabilidades:** identificar institución/curso/evidencia, extraer requisitos obligatorios, convertir criterios en evidencia verificable, detectar contradicciones y proponer la estructura mínima suficiente.

**Conecta con:** `academic-template-selector`, `academic-workflow-orchestrator`, `academic-final-review`.

### `academic-template-selector`

**Propósito:** seleccionar la estructura correcta sin sobredimensionar el entregable.

**Responsabilidades:** respetar plantilla específica cuando exista, distinguir trabajos cortos/medios/extensos, activar solo secciones necesarias y aplicar perfiles institucionales.

**Conecta con:** perfiles institucionales, `academic-requirements-analyzer`, `academic-artifact-validator`.

---

## 2. Investigación, evidencia y fuentes

### `academic-research-ideation`

**Propósito:** generar preguntas, hipótesis y alternativas de análisis sin tratarlas como hechos.

**Reglas clave:** idea ≠ evidencia; hipótesis ≠ hecho; conservar explicaciones rivales e incertidumbre.

### `academic-source-evaluator`

**Propósito:** evaluar si una fuente es apta para sustentar una afirmación o regla.

**Evalúa:** autoridad, vigencia, recuperabilidad, carácter primario/secundario y conflictos.

### `academic-evidence-mapper`

**Propósito:** establecer trazabilidad explícita entre cada afirmación relevante y su evidencia.

```text
claim → evidence → source → citation → status
```

Detecta claims sin evidencia, soporte parcial, evidencia contradictoria y gaps que bloquean READY.

### `academic-citation-manager`

**Propósito:** validar y conciliar citas/referencias sin inventar metadatos.

Detecta citas sin referencia, referencias huérfanas, duplicados, DOI/URL inválidos y metadatos pendientes.

### `external-reference-resolver`

**Propósito:** resolver gaps de capacidad mediante referencias externas previamente evaluadas.

**Regla:** native-first. Solo usa fallback cuando la cobertura nativa es parcial o inexistente. Nunca puede sobreescribir guía, rúbrica, institución o APA oficial.

---

## 3. Análisis y razonamiento

### `academic-statistical-analysis`

**Propósito:** ejecutar y revisar análisis cuantitativos académicos.

**Cubre:** descriptivos, correlación, regresión, supuestos, efecto, incertidumbre y limitaciones.

**Reglas:** correlación ≠ causalidad; R² alto ≠ validez; p < .05 no es el único criterio.

### `academic-critical-review`

**Propósito:** evaluar la solidez de argumentos, métodos, evidencia e inferencias.

**Clasifica claims:** descriptivos, correlacionales, causales, normativos e interpretativos.

---

## 4. APA, tablas y artefactos

### `apa7-academic-style`

**Propósito:** aplicar/revisar APA 7 respetando primero la guía y el perfil institucional.

**Cubre:** citas narrativas/parentéticas, citas textuales, referencias, tablas/figuras y correspondencia cita ↔ referencia.

### `academic-tables-figures`

**Propósito:** revisar numeración, título, notas, fuentes, atribución y legibilidad de tablas/figuras.

**Regla:** nunca inventar procedencia ni declarar “elaboración propia” cuando existen datos de terceros sin atribución.

### `academic-artifact-validator`

**Propósito:** validar el entregable según su tipo real.

**Artefactos:** DOCX, XLSX, PPTX, video/YouTube, landing page, infografía y gráficos.

**Regla:** no imponer formato de paper a artefactos que no son papers.

---

## 5. Auditoría y reparación de documentos

### `academic-document-auditor`

**Propósito:** auditar un documento terminado sin modificarlo.

**Revisa:** estructura, formato, estilos, citas, referencias, tablas/figuras, enlaces, trazabilidad y render visual.

**Clasifica correcciones:** `SAFE_AUTOFIX`, `EVIDENCE_REQUIRED`, `CONTENT_DECISION`.

### `academic-document-repair`

**Propósito:** corregir/regenerar un documento a partir de una auditoría validada.

**Modos:** `conservative`, `evidence-backed`, `full-revision`.

**Gate obligatorio DOCX:** repair → render → inspección visual → re-render si aplica → final review.

---

## 6. Gate final

### `academic-final-review`

**Propósito:** decidir si un trabajo puede declararse listo.

**Revisa:** guía, rúbrica, evidencia, fuentes, APA, artefacto, método y riesgos críticos.

**Única skill autorizada a emitir:** `READY`, `NOT READY`, `USER DECISION REQUIRED`.

Un buen promedio no compensa un `critical_gate: fail`.

---

## Flujo recomendado por escenario

### Trabajo nuevo

```text
requirements → template → research/evidence → citations/APA → critical review → artifact validation → final review
```

### Documento ya elaborado

```text
document auditor → evidence/citation gaps → authorized repair → artifact/render QA → final review
```

### XLSX / análisis cuantitativo

```text
requirements → source/data validation → statistical analysis → tables/charts → artifact validation → final review
```

### Infografía / PPTX / video / web

```text
requirements → source/evidence validation → artifact-specific validation → final review
```

---

## Contrato común

Todas las skills deben seguir `core/SKILL-CONTRACT.md` y emitir, cuando aplique:

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

## Fuente canónica

Los `SKILL.md` individuales son la definición detallada de comportamiento. Este directorio es una capa de navegación y no reemplaza esos archivos.
