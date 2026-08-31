# Gemini Gem — Configuration

## Nombre sugerido

Academic Colombia — APA 7 | UNAD | SENA

## Descripción

Framework académico modular para analizar guías y rúbricas, investigar con evidencia, aplicar APA 7 y perfiles institucionales, revisar artefactos y auditar entregables académicos en Colombia.

## Superficie

Crear y administrar el Gem desde la aplicación web de Gemini. Los Gems creados allí pueden aparecer también en móvil y paneles laterales de Google Workspace, sujeto a disponibilidad de la cuenta.

## Instructions

Copiar el contenido de:

`platforms/gemini/GEM_INSTRUCTIONS.md`

No usar la función automática de reescritura de instrucciones sin revisar el resultado contra el archivo canónico: una reescritura puede cambiar jerarquías o gates.

## Knowledge

Usar el conjunto definido en `KNOWLEDGE_MANIFEST.md`.

Gemini permite añadir archivos desde el dispositivo o desde Google Drive. Cuando se use Drive, este debe actuar como capa de distribución; GitHub sigue siendo la fuente canónica del framework.

## Knowledge citations

Las citas automáticas a archivos de Knowledge son una función de plataforma y no sustituyen las citas académicas del entregable.

El Gem debe distinguir:
- archivos del framework → instrucciones/conocimiento operativo;
- fuentes académicas reales → evidencia que puede citarse en el trabajo.

## Archivos por actividad

Las guías, rúbricas, plantillas y trabajos del estudiante son task-scoped. No convertirlos en Knowledge permanente del Gem salvo que exista una razón institucional explícita y no contengan datos que no deban persistir.

## Uso de Drive

Si los archivos de Knowledge se añaden desde Drive, Gemini puede reflejar cambios posteriores del archivo. Esto permite una distribución actualizable, pero no autoriza ediciones divergentes respecto de GitHub.

Flujo recomendado:

```text
GitHub main
   ↓
export/sync controlado
   ↓
Google Drive
   ↓
Gem Knowledge
```

## Validación mínima antes de uso real

Probar:
- jerarquía de autoridad;
- routing selectivo;
- referencias inventadas;
- evidencia faltante;
- artefacto incorrecto;
- critical gate;
- documentos existentes;
- diferencias UNAD/SENA.

Ver `tests/GEMINI_ADAPTER_CASES.md` y `tests/CROSS_PLATFORM_BEHAVIOR_CASES.md`.
