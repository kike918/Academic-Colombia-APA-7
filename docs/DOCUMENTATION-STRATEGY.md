# Documentation Strategy

## Objetivo

Definir cómo se presenta Academic Colombia a usuarios, contribuidores y plataformas sin duplicar la fuente canónica.

## Capas de documentación

### 1. `README.md` — portada del proyecto

Debe responder rápidamente:
- qué es Academic Colombia;
- qué problema resuelve;
- qué capacidades existen;
- cómo funciona la orquestación;
- cómo empezar a usarlo;
- dónde encontrar cada bloque de documentación.

El README no debe contener el detalle operativo completo de cada skill.

### 2. `docs/SKILLS-DIRECTORY.md` — catálogo funcional

Es el índice humano de las skills.

Debe indicar:
- nombre;
- propósito;
- cuándo usarla;
- relaciones con otras skills;
- flujo recomendado por escenarios.

No reemplaza el `SKILL.md` individual.

### 3. `skills/*/SKILL.md` — definición operativa

Es la fuente detallada de comportamiento de cada skill.

Debe mantenerse compatible con `core/SKILL-CONTRACT.md` y `core/ORCHESTRATION.md`.

### 4. `/docs` — arquitectura y workflows

Contiene documentación transversal: arquitectura, QA, validación de artefactos, gobernanza, roadmap, workflows y reportes de validación.

### 5. Platform adapters

`platforms/` contiene únicamente instrucciones y empaquetado específicos de cada plataforma. No debe redefinir reglas académicas canónicas.

## Landing / GitHub Pages

### Decisión actual

No crear una landing independiente en v0.10.x.

Razones:
- README + docs ya cubren descubrimiento y navegación;
- una landing manual duplicaría contenido;
- los adapters de plataforma aún están evolucionando;
- el proyecto todavía está antes de v1.0.

### Cuándo sí crearla

Evaluar GitHub Pages cuando se cumplan varios de estos criterios:
- release estable v1.x;
- adopción pública por usuarios externos;
- documentación suficientemente extensa para necesitar navegación multi-página;
- instalación diferenciada para ChatGPT, Gemini, Sparks u otras plataformas;
- necesidad de tutoriales, ejemplos y búsqueda;
- necesidad de mostrar releases y compatibilidad.

### Regla de implementación futura

Si se habilita GitHub Pages, debe generarse a partir de Markdown versionado en el repo mediante una herramienta de documentación (por ejemplo MkDocs, Material for MkDocs, Docusaurus u otra evaluada en ese momento).

No mantener una landing HTML escrita manualmente que replique README/docs.

```text
Markdown canónico
      ↓
documentation builder
      ↓
GitHub Pages
```

El sitio publicado es una vista del repositorio, no una nueva fuente de verdad.

## Principio

**Document once, render many.**

La documentación debe mantenerse en GitHub y poder reutilizarse tanto en el README como en futuras experiencias web o adapters.
