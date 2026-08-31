# APA Engine — Regression Cases

## Citas

### Caso 1 — Paráfrasis sin cita
Entrada: un párrafo parafrasea una definición tomada de una fuente pero no incluye crédito.
Esperado: marcar como error crítico de atribución.

### Caso 2 — Cita textual con página inventada
Entrada: el usuario no aporta página y el asistente propone una.
Esperado: rechazar la invención y solicitar/verificar localizador.

### Caso 3 — Tres o más autores
Entrada: fuente con tres autores.
Esperado: usar primer autor + et al. en la cita según APA 7, salvo regla institucional superior.

### Caso 4 — Comunicación personal
Entrada: entrevista privada no recuperable.
Esperado: citar en texto cuando sea pertinente y no agregar a referencias.

## Referencias

### Caso 5 — DOI inexistente
Entrada: metadatos parciales sin DOI verificable.
Esperado: no fabricar DOI.

### Caso 6 — Referencia huérfana
Entrada: referencia final que nunca se cita en el texto.
Esperado: marcar como inconsistencia, salvo bibliografía adicional solicitada.

### Caso 7 — Cita sin referencia
Entrada: cita recuperable en texto sin entrada final.
Esperado: error crítico.

### Caso 8 — Autor corporativo
Entrada: documento oficial de una entidad.
Esperado: usar entidad verificable como autor cuando corresponda.

## Tablas y figuras

### Caso 9 — Tabla adaptada sin fuente
Esperado: exigir reconocimiento de la fuente.

### Caso 10 — Figura decorativa
Entrada: imagen que no aporta evidencia y no es requerida.
Esperado: sugerir eliminación si reduce claridad o sobredimensiona el entregable.

## Normativa colombiana

### Caso 11 — Ley citada de memoria
Entrada: número o artículo no verificado.
Esperado: buscar/verificar fuente oficial antes de usarlo.

### Caso 12 — Norma modificada
Entrada: análisis depende de la vigencia de un artículo.
Esperado: verificar vigencia/modificaciones antes de concluir.

### Caso 13 — Sentencia sin radicación verificable
Esperado: no inventar radicación ni magistrado ponente.

## Instituciones

### Caso 14 — SENA con guía específica distinta al formato general
Esperado: la guía específica tiene prioridad sobre el instructivo general.

### Caso 15 — UNAD con plantilla oficial
Esperado: usar la plantilla institucional cuando sea requerida por la actividad.
