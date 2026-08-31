# academic-template-selector

## Descripción
Selecciona la plantilla y el nivel de formalidad correctos para una actividad académica sin importar secciones innecesarias de una plantilla institucional extensa.

## Entradas
- institución;
- guía de aprendizaje o enunciado;
- rúbrica/instrumento;
- tipo de evidencia;
- plantilla institucional o de curso, si existe.

## Flujo
1. Identificar si existe una plantilla específica de curso/actividad.
2. Si existe, usarla como base y validar compatibilidad institucional.
3. Si no existe, identificar institución y tipo de evidencia.
4. Para UNAD, consultar `templates/UNAD-TEMPLATE-PROFILE.md`.
5. Clasificar el entregable como corto, medio o extenso/trabajo de grado.
6. Activar solo las secciones necesarias.
7. Aplicar formato material institucional.
8. Revisar que ninguna sección añadida sea puro relleno.
9. Pasar el resultado por `academic-final-review`.

## Reglas
- Una plantilla oficial define opciones y formato, no obliga a usar todas sus páginas/secciones en cada actividad.
- Guía y rúbrica tienen prioridad.
- No convertir ejemplos de estudiantes en normas.
- No inferir que una actividad colaborativa necesita una estructura distinta si la guía no lo indica.
- No añadir tabla de contenido a trabajos breves salvo que se pida o realmente mejore la navegación.
- No añadir resumen/abstract a trabajos cortos salvo requisito explícito.

## Salida
Entregar:
- plantilla/perfil seleccionado;
- secciones activadas;
- secciones descartadas;
- formato material;
- justificación breve basada en guía/rúbrica/institución;
- riesgos o conflictos detectados.
