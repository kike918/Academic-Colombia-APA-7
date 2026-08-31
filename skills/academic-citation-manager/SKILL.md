# academic-citation-manager

## Descripción

Gestiona, convierte, valida y concilia citas/referencias académicas sin inventar metadatos.

## Entradas
- texto o documento;
- lista de referencias o identificadores (DOI, URL, ISBN, PMID, etc.);
- estilo requerido;
- institución/perfil;
- fuentes oficiales disponibles.

## Flujo
1. Identificar todas las citas en el texto.
2. Identificar todas las referencias finales.
3. Construir mapa cita ↔ referencia.
4. Detectar citas sin referencia, referencias huérfanas y duplicados.
5. Verificar metadatos recuperables antes de corregir formato.
6. Resolver el estilo destino y el perfil institucional.
7. Convertir formato sin alterar datos bibliográficos verificados.
8. Marcar campos no verificables como pendientes, nunca completarlos por intuición.
9. Validar DOI/URL y tipo real de fuente.
10. Emitir reporte de cambios y pendientes.

## Reglas críticas
- La conversión de estilo no autoriza inventar datos faltantes.
- Un DOI debe resolverse o verificarse antes de declararlo válido.
- Una URL de buscador o agregador no debe sustituir la fuente original cuando exista una mejor fuente recuperable.
- Bajo UNAD en español, aplicar su convención institucional validada para autores.
- Para IA generativa consultar `core/AI-USAGE-AND-CITATION.md`.

## Salida
- referencias normalizadas;
- matriz cita ↔ referencia;
- duplicados;
- metadatos pendientes;
- enlaces/DOI inválidos;
- readiness de citación.

## Skill Contract v1

Cumplir `core/SKILL-CONTRACT.md`.

- `outputs.citation_map`: correspondencia cita ↔ referencia.
- `outputs.normalized_references`: referencias cuya metadata pudo verificarse.
- `findings`: huérfanas, duplicados, DOI/URL inválidos y problemas de estilo.
- `gaps`: metadatos o evidencia no verificables.
- `next_recommended`: `academic-evidence-mapper`, `apa7-academic-style` o `academic-final-review` según el estado.
- `critical_gate: fail` si una afirmación material depende de una cita inexistente/inventada o si una referencia crítica no puede reconciliarse.