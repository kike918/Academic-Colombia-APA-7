# academic-evidence-mapper

## Descripción

Construye y mantiene la trazabilidad explícita entre afirmaciones académicas, evidencia verificable, fuentes y citas.

## Objetivo

Evitar que una fuente bibliográfica sea tratada como respaldo de una afirmación solo por afinidad temática. La skill debe demostrar qué evidencia soporta qué claim y detectar afirmaciones sin respaldo suficiente.

## Entradas

- borrador, esquema o conjunto de claims;
- fuentes verificadas;
- resultados de `academic-source-evaluator` cuando existan;
- requisitos de guía/rúbrica;
- contexto institucional y disciplinar.

## Flujo

1. Identificar claims materiales del trabajo.
2. Clasificarlos como descriptivos, interpretativos, correlacionales, causales, normativos o metodológicos cuando aplique.
3. Localizar evidencia concreta dentro de fuentes verificadas.
4. Mapear claim → evidencia → fuente → cita esperada.
5. Evaluar fuerza del soporte: strong / adequate / weak / none.
6. Detectar contradicciones, evidencia parcial y límites de generalización.
7. Marcar claims sin respaldo como `EVIDENCE_GAP`.
8. Entregar el mapa a `academic-citation-manager`, `academic-critical-review` y al orquestador.

## Salida especializada

`outputs` debe incluir, cuando sea posible:

```yaml
claims:
  - id: C1
    claim: "..."
    claim_type: descriptive
    evidence:
      source_id: S1
      locator: "página/sección/tabla cuando sea verificable"
      support: strong
    citation_status: present | missing | not_required
    status: verified | partial | evidence_gap
unsupported_claims: []
contradictions: []
```

## Reglas críticas

- No inventar evidencia, páginas, secciones o localizadores.
- Una referencia en bibliografía no prueba por sí sola que respalde un claim.
- Una fuente secundaria no debe reemplazar una primaria cuando la afirmación exige autoridad primaria y esta es accesible.
- Correlación no se convierte en causalidad por redacción.
- Si solo se dispone de abstract/resumen, no atribuir detalles metodológicos no visibles.
- Cuando el soporte sea parcial, expresarlo y no elevarlo artificialmente a `strong`.

## Contrato común

Cumplir `core/SKILL-CONTRACT.md`.

Campos recomendados:
- `findings`: claims débiles, contradictorios o sin respaldo;
- `outputs.claims`: mapa claim-evidence;
- `gaps`: evidencia o fuente pendiente;
- `next_recommended`: normalmente `academic-citation-manager` y/o `academic-critical-review`;
- `critical_gate: fail` cuando una afirmación central del entregable carece de evidencia necesaria.