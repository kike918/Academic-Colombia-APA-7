# academic-critical-review

## Descripción

Revisa borradores académicos separando afirmaciones, evidencia, inferencias, limitaciones y calidad metodológica.

## Entradas
- borrador o documento;
- fuentes utilizadas;
- guía/rúbrica;
- metodología/datos cuando existan.

## Flujo
1. Identificar afirmaciones centrales.
2. Mapear cada afirmación a evidencia o cita.
3. Clasificar afirmaciones como descriptivas, correlacionales, causales, normativas o interpretativas.
4. Verificar si la evidencia realmente respalda alcance, dirección y población de la afirmación.
5. Detectar correlación tratada como causalidad, sobre-generalización y sesgos relevantes.
6. Revisar metodología, muestra, variables, comparadores y limitaciones cuando existan.
7. Revisar coherencia entre resultados y conclusiones.
8. Para análisis cuantitativo, invocar/coordinar con `academic-statistical-analysis`.
9. Priorizar hallazgos: crítico / importante / mejora.
10. Proponer correcciones concretas sin fabricar evidencia.

## Reglas
- Distinguir datos observados de interpretación.
- Distinguir significancia estadística de importancia práctica.
- No interpretar ausencia de significancia como prueba automática de ausencia de efecto.
- Conservar evidencia contradictoria o nula.
- No declarar que una hipótesis fue validada por una simple lluvia de ideas o búsqueda superficial.

## Salida
- matriz claim → evidence;
- fortalezas;
- debilidades;
- sesgos/riesgos;
- conclusiones soportadas/no soportadas;
- acciones recomendadas.

## Skill Contract v1

Cumplir `core/SKILL-CONTRACT.md`.

- `outputs.review`: evaluación de razonamiento, metodología y conclusiones.
- `findings`: claims sobreextendidos, sesgos, inferencias inválidas y limitaciones omitidas.
- `gaps`: evidencia o información metodológica faltante.
- `next_recommended`: `academic-evidence-mapper`, `academic-statistical-analysis` o `academic-final-review`.
- `critical_gate: fail` si una conclusión central excede materialmente la evidencia o existe un error metodológico que invalida la respuesta.