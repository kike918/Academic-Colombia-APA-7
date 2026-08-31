# Casos de regresión académica

Estos casos permiten comprobar que una nueva versión del GPT, skill o Gem no rompa reglas esenciales.

## Caso 1 — Guía específica vs APA genérico
Entrada: una guía UNAD pide únicamente un cuadro sinóptico de una página.
Esperado: no agregar ensayo, abstract, metodología ni conclusiones por defecto. La evidencia central debe seguir siendo el cuadro sinóptico.

## Caso 2 — Rúbrica manda
Entrada: la guía pide informe, pero la rúbrica asigna la mayor parte del puntaje a una tabla comparativa.
Esperado: la estructura debe hacer explícita y visible la tabla comparativa; no enterrarla como anexo opcional.

## Caso 3 — Referencia incompleta
Entrada: se proporciona autor y título, pero no año, DOI ni URL verificable.
Esperado: no inventar metadatos. Marcar la referencia como incompleta o buscar verificación.

## Caso 4 — SENA APA 6 obsoleto
Entrada: aparecen dos instructivos SENA, uno APA 6 de 2019 y uno APA 7 de 2020.
Esperado: priorizar APA 7 para reglas actuales salvo que una actividad específica ordene otra cosa.

## Caso 5 — Regla institucional específica
Entrada: una publicación o guía institucional exige interlineado sencillo aunque APA general sugiera otro formato.
Esperado: aplicar la instrucción institucional específica al entregable correspondiente y explicar la diferencia si es relevante.

## Caso 6 — Correspondencia cita-referencia
Entrada: documento con 8 referencias finales, pero solo 6 aparecen citadas.
Esperado: detectar las 2 referencias huérfanas y no declarar el documento conforme.

## Caso 7 — Fuente actualizable
Entrada: afirmación sobre una ley, convocatoria, fecha, estadística o norma vigente.
Esperado: verificar información actual antes de usarla como hecho académico.

## Caso 8 — Elaboración propia
Entrada: figura creada por el estudiante a partir de su propio análisis.
Esperado: no atribuir una fuente externa inexistente; indicar elaboración propia cuando corresponda y según la guía institucional.

## Criterio de aprobación
Una versión no debe considerarse estable si falla cualquiera de los casos 1, 3, 4, 6 o 7.
