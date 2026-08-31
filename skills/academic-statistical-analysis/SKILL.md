# academic-statistical-analysis

## Descripción

Analiza datos académicos cuantitativos con selección de método, verificación de supuestos, diagnóstico y reporte interpretable.

## Entradas
- CSV/XLSX o tabla de datos;
- pregunta o hipótesis;
- variables y unidades;
- diseño del estudio;
- nivel de medición;
- guía/rúbrica.

## Flujo
1. Validar estructura, tipos, unidades, faltantes y duplicados.
2. Definir variable objetivo, predictores, grupos y unidad de análisis.
3. Elegir método compatible con pregunta, diseño y distribución.
4. Verificar supuestos antes de interpretar resultados.
5. Ejecutar análisis descriptivo y diagnóstico.
6. Para correlación: distinguir Pearson/Spearman, revisar outliers, no inferir causalidad y considerar confusores cuando corresponda.
7. Para regresión OLS/logística: revisar especificación, multicolinealidad, residuos/ajuste, observaciones influyentes y riesgo de sobreajuste.
8. Reportar estimaciones, incertidumbre, tamaños de efecto y p-valores cuando correspondan.
9. Interpretar magnitud y relevancia práctica, no solo umbrales de significancia.
10. Documentar transformaciones, exclusiones, paquetes/versiones y decisiones relevantes.

## Reglas críticas
- No ejecutar una regresión porque el usuario la pidió sin confirmar que el diseño y los datos la permiten.
- No presentar R² alto como prueba de causalidad o validez.
- No ocultar violaciones de supuestos.
- No eliminar outliers automáticamente.
- No usar p < .05 como única medida de calidad.
- Señalar análisis exploratorios como exploratorios.

## Salida
- diagnóstico de datos;
- método y justificación;
- supuestos y resultado de chequeos;
- resultados estadísticos;
- interpretación en lenguaje académico;
- limitaciones;
- formato de reporte compatible con APA cuando aplique.
