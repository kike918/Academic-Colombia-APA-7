# Arquitectura — Academic Colombia

## Fuente de verdad

GitHub es la fuente canónica. Las instalaciones en plataformas de IA derivan de este repositorio y no deben convertirse en forks lógicos divergentes.

## Capas

```text
User / Activity Inputs
        ↓
Orchestration Core
        ↓
Requirements / Institution / Evidence / APA / Artifact Skills
        ↓
Quality Gates
        ↓
Platform Adapter
```

### `core/`
Reglas neutrales de plataforma:
- autoridad y comportamiento académico;
- APA 7;
- legislación colombiana;
- IA y citación;
- orquestación;
- contrato común entre skills.

### `institutions/`
Overrides y perfiles institucionales. Actualmente UNAD y SENA.

### `templates/`
Perfiles de plantilla derivados de evidencia institucional validada. Una plantilla no reemplaza guía/rúbrica.

### `skills/`
Capacidades pequeñas, reutilizables y combinables. Todas deben cumplir `core/SKILL-CONTRACT.md`.

Familias actuales:
- planificación/requisitos;
- investigación/evidencia;
- citación/APA;
- estadística;
- tablas/figuras;
- artefactos;
- auditoría/reparación;
- revisión final;
- fallback externo;
- orquestación.

### `external-references/`
Registro controlado de referencias metodológicas/técnicas externas. No son autoridad automática y solo se consumen mediante `external-reference-resolver`.

### `quality/`
Gates de readiness académica, integridad, evidencia y artefactos.

### `tests/`
Casos de regresión, compatibilidad, routing y aceptación end-to-end. Actualmente son especificaciones de aceptación ejecutables por agentes; la automatización CI es una capa posterior.

### `platforms/`
Adaptadores de instalación/ejecución. No contienen la lógica académica canónica.

### `docs/`
Arquitectura, roadmap, validaciones, workflows y gobernanza.

## Flujo de datos

Las skills intercambian resultados usando el contrato v1:

```text
skill A
  ↓ output envelope
skill B
  ↓ findings/gaps/critical gates preserved
...
  ↓
academic-final-review
```

Un `critical_gate: fail` no puede perderse ni convertirse en READY por promedio.

## Separación de responsabilidades

- El core define reglas.
- El orquestador decide routing.
- Las skills ejecutan capacidades especializadas.
- Academic QA decide gates.
- Los adaptadores traducen a una plataforma.
- Runtimes externos, RAG, automatización o memoria personal no son dependencias del core.

## Política de actualización

1. Cambiar primero core/skill correspondiente en una branch.
2. Actualizar tests afectados.
3. Actualizar VERSION y CHANGELOG.
4. Abrir PR y resolver conversaciones.
5. Fusionar a `main` mediante el flujo protegido.
6. Validar primero el adapter de referencia.
7. Sincronizar adapters secundarios cuando el comportamiento sea estable.
8. Registrar diferencias inevitables entre plataformas.

## SemVer

- PATCH: correcciones sin cambio material de comportamiento.
- MINOR: nueva regla, skill, workflow o perfil compatible.
- MAJOR: cambio incompatible de jerarquía, contrato o semántica de ejecución.