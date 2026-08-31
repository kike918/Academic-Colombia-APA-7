# Academic Colombia — Skill Contract v1

## Propósito

Definir un contrato semántico común para que todas las skills de Academic Colombia puedan interoperar sin depender de una plataforma o runtime específico.

## Envelope obligatorio

Cuando una skill produzca una salida estructurada, debe poder expresarse con este envelope mínimo:

```yaml
skill: skill-name
contract_version: "1.0"
status: success | partial | blocked
inputs_used: []
findings: []
outputs: {}
gaps: []
next_recommended: []
confidence: high | medium | low
critical_gate: pass | fail | not_applicable
```

## Semántica

### `status`
- `success`: la skill completó su objetivo con evidencia suficiente.
- `partial`: produjo resultados útiles, pero quedan gaps no críticos o trabajo posterior.
- `blocked`: no puede completar su objetivo sin una fuente, archivo, decisión o capacidad faltante.

### `inputs_used`
Lista de insumos realmente utilizados. No debe declarar archivos o fuentes no consultados.

### `findings`
Hallazgos verificables producidos por la skill. Cuando aplique, cada finding debe incluir ubicación, severidad, regla/evidencia y acción propuesta.

### `outputs`
Resultado específico de la skill. Su forma interna depende de la capacidad especializada.

### `gaps`
Información, evidencia, requisito o capacidad pendiente. Un gap material debe impedir una falsa declaración de completitud.

### `next_recommended`
Skills o acciones que razonablemente deberían seguir. Es una recomendación de routing, no una obligación si el orquestador determina que no aplica.

### `confidence`
Refleja la fortaleza de la evidencia y completitud de los insumos, no una probabilidad matemática inventada.

### `critical_gate`
- `pass`: no existe un fallo crítico dentro del alcance de la skill.
- `fail`: existe al menos un fallo crítico que debe bloquear READY.
- `not_applicable`: la skill no es un gate crítico para ese caso.

## Reglas de interoperabilidad

1. Ninguna skill debe asumir que todas las demás se ejecutarán.
2. Los outputs deben ser consumibles por otra skill sin reinterpretar silenciosamente los hechos.
3. La trazabilidad de fuente/evidencia debe conservarse cuando un output pasa a otra skill.
4. `blocked` no puede convertirse en `success` por simple reformulación.
5. `critical_gate: fail` se propaga hasta `academic-final-review` salvo que el hallazgo sea resuelto y revalidado.
6. Las plataformas pueden representar el contrato en Markdown, JSON, YAML u objetos internos, pero deben conservar su semántica.
7. Las skills heredadas deben mantener su salida humana legible y, adicionalmente, cumplir este contrato.

## Contratos especializados

Cada skill puede extender `outputs` con campos propios. Ejemplos:

- requirements analyzer → `requirements`, `rubric_map`, `deliverables`;
- source evaluator → `sources`, `authority`, `verification`;
- evidence mapper → `claims`, `evidence_links`, `unsupported_claims`;
- document auditor → `audit_findings`, `repair_classes`;
- artifact validator → `artifact_checks`;
- final review → `readiness`, `blocking_issues`.

El contrato común no reemplaza la especialización; evita que cada skill hable un idioma incompatible.