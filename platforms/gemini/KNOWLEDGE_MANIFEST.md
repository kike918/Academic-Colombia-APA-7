# Gemini Knowledge Manifest

## Objetivo

Definir qué partes de Academic Colombia deben formar parte del Knowledge de un Gem y cuáles deben permanecer task-scoped.

## Tier A — Core siempre disponible

Priorizar:

- `core/CORE.md`
- `core/ORCHESTRATION.md`
- `core/SKILL-CONTRACT.md`
- `quality/ACADEMIC-QA.md`
- `docs/SKILLS-DIRECTORY.md`

Estos archivos contienen identidad, jerarquía, routing, contrato y gates.

## Tier B — Reglas académicas base

Añadir cuando la capacidad de Knowledge lo permita:

- `core/APA7.md`
- `core/AI-USAGE-AND-CITATION.md`
- `core/LEGAL-COLOMBIA.md`
- `docs/ARTIFACT-VALIDATION-MATRIX.md`
- `docs/DOCUMENT-AUDIT-REPAIR-WORKFLOW.md`

No todos son relevantes a todas las tareas; las Instructions deben aplicar carga conceptual selectiva.

## Tier C — Instituciones

Añadir los perfiles realmente necesarios:

- `institutions/UNAD.md`
- `institutions/SENA.md`
- `templates/UNAD-TEMPLATE-PROFILE.md`

No generalizar reglas de una institución a otra.

## Tier D — Skills

Las definiciones `skills/*/SKILL.md` son la fuente operativa de cada capacidad.

Para una instalación completa, incluir las 16 skills nativas. Si la cuenta/superficie obliga a reducir Knowledge, priorizar las skills que correspondan al caso de uso y conservar siempre el core de Tier A.

No afirmar cobertura completa si se omiten skills necesarias.

## Tier E — Fallback y referencias externas

Cargar cuando sea material:

- `external-references/REGISTRY.md`
- `docs/EXTERNAL-REFERENCES.md`

Las referencias externas nunca reemplazan la autoridad del core/institución.

## Task-scoped — no Knowledge permanente

Mantener en la conversación/actividad:

- guía de una asignatura;
- rúbrica específica;
- entregable del estudiante;
- dataset específico;
- capturas/evidencias de una actividad;
- plantillas locales no validadas;
- documentos con información personal o académica que no deba persistir.

## Drive vs upload local

Gemini permite agregar Knowledge desde dispositivo o Drive.

### Drive

Ventaja: los cambios posteriores del archivo pueden reflejarse en el Gem.

Regla: Drive es una réplica/distribución. No editar allí reglas que no hayan sido incorporadas primero al repositorio canónico.

### Upload local

Útil para snapshots reproducibles de una versión concreta.

Registrar la versión de Academic Colombia usada en la instalación.

## Límites de producto

No fijar aquí números de archivos/tokens como contrato permanente. Los límites de Gemini pueden cambiar por plan, cuenta y producto.

Durante la instalación:
1. comprobar límites vigentes;
2. aplicar minimum sufficient context;
3. no sacrificar autoridad/gates para meter contenido secundario;
4. documentar cualquier archivo omitido.

## Regla anti-confusión de fuentes

Los archivos de este manifest explican cómo trabajar. No son automáticamente fuentes académicas que deban aparecer en el entregable del estudiante.
