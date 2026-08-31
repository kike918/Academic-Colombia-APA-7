# Template Compatibility Cases

## TC-01 Plantilla UNAD formal
Entrada: actividad UNAD que exige documento formal sin plantilla específica.
Esperado: seleccionar perfil UNAD, carta, márgenes 2,54 cm, TNR 12 recomendado, doble espacio, sangría 1,27 cm.

## TC-02 Actividad corta UNAD
Entrada: foro o ensayo breve de 2 páginas.
Esperado: no añadir automáticamente resumen, abstract, tabla de contenido, dedicatoria ni nota de aceptación.

## TC-03 Trabajo de grado
Entrada: proyecto de grado UNAD.
Esperado: consultar plantilla institucional completa y lineamientos de Escuela/programa antes de generar estructura.

## TC-04 Trabajo colaborativo
Entrada: actividad colaborativa con una plantilla institucional idéntica a la individual.
Esperado: no inventar una estructura APA colaborativa diferente; aplicar requisitos específicos de guía/rúbrica.

## TC-05 Ejemplo con ampersand
Entrada: documento de estudiante con `(Autor & Autor, año)` bajo perfil UNAD en español.
Esperado: detectar diferencia con convención institucional validada y proponer `y` cuando corresponda.

## TC-06 Título en mayúsculas sostenidas
Entrada: portada de ejemplo con título completamente en mayúsculas.
Esperado: no adoptar automáticamente esa convención; preferir el perfil institucional salvo instrucción específica.

## TC-07 Tabla de ejemplo
Entrada: tabla con `Tabla 1` y título combinados en un solo párrafo.
Esperado: normalizar número y título conforme al perfil de tablas/figuras.

## TC-08 Referencia jurídica de ejemplo
Entrada: ley o decreto copiado desde un trabajo previo.
Esperado: no reutilizar sin verificar; pasar por `LEGAL-COLOMBIA.md`.

## TC-09 Herramienta de IA en referencias
Entrada: Gemini/Copilot/NotebookLM incluidos en referencias de un ejemplo.
Esperado: mantener solo si realmente se usaron/citaron y validar el tipo de referencia aplicable; no copiar por defecto.

## TC-10 Entrega de video
Entrada: actividad cuyo entregable principal es video + breve documento de soporte.
Esperado: usar estructura mínima necesaria; no convertirla en informe extenso por defecto.

## TC-11 Plantilla institucional vs guía específica
Entrada: plantilla UNAD completa y guía de actividad que pide exclusivamente portada + infografía + referencias.
Esperado: seguir la guía y utilizar solo esos componentes.

## TC-12 Ejemplo académico real
Entrada: trabajo previo bien presentado pero con pequeñas desviaciones.
Esperado: clasificar como `reference example`, extraer patrones útiles y rechazar convenciones incompatibles.
