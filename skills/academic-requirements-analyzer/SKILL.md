# academic-requirements-analyzer

## Descripción
Analiza una actividad académica, guía y rúbrica para convertirlas en un mapa de requisitos accionable.

## Entradas
- institución;
- guía o enunciado;
- rúbrica o instrumento de evaluación, si existe;
- instrucciones adicionales del tutor.

## Flujo
1. Identificar institución y curso.
2. Identificar resultado de aprendizaje/competencia.
3. Identificar evidencia.
4. Clasificar individual/colaborativa.
5. Extraer fechas, puntaje y formato.
6. Extraer requisitos obligatorios.
7. Convertir cada criterio de evaluación en una evidencia verificable.
8. Detectar contradicciones o vacíos.
9. Proponer estructura mínima suficiente.

## Salida
Entregar:
- resumen de actividad;
- requisitos obligatorios;
- matriz criterio → evidencia;
- estructura recomendada;
- riesgos;
- checklist de entrega.

## QA
No inventar requisitos no presentes en la guía.
No usar APA para justificar secciones que la actividad no pide.

## Skill Contract v1

Cumplir `core/SKILL-CONTRACT.md`.

- `outputs.requirements`: requisitos identificados y su autoridad.
- `outputs.rubric_map`: criterio → evidencia esperada.
- `outputs.deliverables`: artefactos y condiciones de entrega.
- `findings`: contradicciones, riesgos y requisitos críticos.
- `gaps`: guía/rúbrica/instrucciones ausentes o ambiguas.
- `next_recommended`: `academic-template-selector` y routing posterior.
- `critical_gate: fail` si un requisito obligatorio no puede determinarse de forma fiable y es necesario para construir/validar el entregable.