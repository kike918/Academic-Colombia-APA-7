# EMP-UNAD-2026-06 — Coffee-sector macroeconomics visual deck

## Status

`EXECUTED_WITH_FINDINGS`

## Artifact

Thirteen-page visual PDF on the 2026 Colombian coffee-sector shock and strategic implications for a coffee business.

The source PDF is not committed. This record preserves only anonymized findings.

## External verification sample

A current official Federación Nacional de Cafeteros April 2026 report was used to validate selected quantitative claims.

Verified official values include:
- production year-to-date variation: approximately `-28.3%`;
- production coffee-year variation: `-26.2%`;
- production 12-month variation: `-17.0%`;
- March export annual variation: `-36.4%`;
- export year-to-date variation: approximately `-28.5%`;
- export coffee-year variation: `-17.2%`;
- export 12-month variation: `-6.2%`.

## Strong behaviors observed

- presentation maps macro shock → economic principle → business response;
- scarcity, supply contraction, opportunity cost and information asymmetry are connected to a concrete strategic case;
- visual hierarchy and narrative progression are strong;
- the `-28%` production headline is directionally consistent with the official `-28.3%` year-to-date figure.

## Critical findings

### FAIL — 6.9 million sacks misinterpreted as a drop

One slide states that a `caída de 6,9 millones de sacos` shifts the supply curve.

The official source says that **current coffee-year production exceeds 6.9 million sacks**, with a 26.2% decline versus the prior coffee year. Therefore 6.9 million is the current cumulative volume, not the magnitude of the decrease.

This is a strong empirical example for `academic-evidence-mapper` and `academic-critical-review`: a number can originate from a valid source and still be semantically misused.

### FAIL / EVIDENCE GAP — export contraction of 15%

The deck states a `-15%` contraction in exports without a sufficiently precise period definition/source trace. The official April 2026 FNC report exposes several materially different export variations (`-36.4%` annual March, about `-28.5%` year-to-date, `-17.2%` coffee year, `-6.2%` 12 months). A bare `-15%` should not pass without exact period/source reconciliation.

### EVIDENCE GAP — 2.5 million sacks not produced

The deck claims `2.5 millones` fewer 60-kg sacks. The inspected official report did not directly support that number in the same framing. It must be derived transparently or removed.

### CONCEPTUAL FINDING — externality taxonomy

The deck groups rainfall, rural insecurity, high interest rates and fertilizer costs under `externalidades negativas`. These are plausibly external/exogenous pressures or cost shocks, but they are not all externalities in the strict microeconomic sense. A stronger version should distinguish:
- externalities;
- exogenous supply shocks;
- financing-cost shocks;
- input-price shocks.

### OVERCLAIM — traceability eliminates information asymmetry

The statement that traceability `elimina` information asymmetry is too absolute. Traceability may reduce or mitigate asymmetry; it does not automatically eliminate it.

## Skills empirically exercised

- `academic-source-evaluator`
- `academic-evidence-mapper`
- `academic-critical-review`
- `academic-artifact-validator`
- `academic-final-review`
- `academic-workflow-orchestrator`

## Why this is high-value evidence

This artifact demonstrates that visual polish and broadly correct economic intuition do not compensate for:
- a misinterpreted official number;
- an unresolved period definition;
- a weakly traced derived statistic;
- overly broad conceptual labels.

The correct framework outcome is `NOT READY` until those findings are resolved, even though the presentation is visually strong.
