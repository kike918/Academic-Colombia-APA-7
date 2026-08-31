# Documentation Strategy

## Objetivo

Definir cómo se presenta Academic Colombia a usuarios, contribuidores y plataformas sin duplicar la fuente canónica.

## Capas de documentación

### 1. `README.md` — portada del repositorio

Debe responder rápidamente:
- qué es Academic Colombia;
- qué problema resuelve;
- qué capacidades existen;
- cómo funciona la orquestación;
- cómo empezar a usarlo;
- dónde encontrar cada bloque de documentación.

El README no debe contener el detalle operativo completo de cada skill.

### 2. `docs/index.md` — portada web mínima

Es la entrada preparada para GitHub Pages.

Debe ser más corta que el README y centrarse en:
- propósito del framework;
- reglas básicas de autoridad e integridad;
- flujo general;
- acceso al directorio de skills;
- documentación principal;
- licencia y estado.

No debe convertirse en un manual teórico completo de APA.

### 3. `docs/SKILLS-DIRECTORY.md` — catálogo funcional

Es el índice humano de las skills.

Debe indicar:
- nombre;
- propósito;
- cuándo usarla;
- relaciones con otras skills;
- flujo recomendado por escenarios.

No reemplaza el `SKILL.md` individual.

### 4. `skills/*/SKILL.md` — definición operativa

Es la fuente detallada de comportamiento de cada skill.

Debe mantenerse compatible con `core/SKILL-CONTRACT.md` y `core/ORCHESTRATION.md`.

### 5. `/docs` — arquitectura y workflows

Contiene documentación transversal: arquitectura, QA, validación de artefactos, gobernanza, roadmap, workflows, licencia/alcance y reportes de validación.

### 6. Platform adapters

`platforms/` contiene únicamente instrucciones y empaquetado específicos de cada plataforma. No debe redefinir reglas académicas canónicas.

## GitHub Pages

### Decisión actual

Iniciar una **Page mínima** a partir de `docs/index.md`.

Razones:
- el repositorio ya tiene suficiente estructura para que un lector externo se beneficie de una entrada simplificada;
- la Page puede ayudar a entender el proyecto sin recorrer el árbol completo;
- la portada puede explicar solo las reglas esenciales sin extenderse en teoría APA;
- el contenido fuente permanece en Markdown dentro de `main`.

### Alcance inicial

La primera Page no necesita:
- buscador;
- framework visual complejo;
- Docusaurus/MkDocs;
- tutoriales extensos;
- HTML mantenido manualmente;
- copias de todos los `SKILL.md`.

Puede publicarse directamente desde `main/docs` usando el render de GitHub Pages/Jekyll disponible en GitHub.

### Evolución futura

Evaluar un documentation builder cuando se cumplan varios de estos criterios:
- release estable v1.x;
- adopción pública significativa;
- documentación suficientemente extensa para necesitar navegación avanzada;
- instalación diferenciada por plataforma;
- necesidad de búsqueda, versionado de docs o tutoriales numerosos.

En ese momento podrá evaluarse MkDocs, Material for MkDocs, Docusaurus u otra alternativa.

## Regla de implementación

```text
Markdown canónico
      ↓
README + docs
      ↓
GitHub Pages
      ↓
future documentation builder if needed
```

El sitio publicado es una vista del repositorio, no una nueva fuente de verdad.

## Principio

**Document once, render many.**
