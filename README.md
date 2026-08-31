# Academic Colombia — APA 7

Repositorio canónico para gestionar, versionar y reutilizar reglas académicas orientadas a **APA 7**, **UNAD**, **SENA** y documentos universitarios en asistentes de inteligencia artificial.

## Objetivo

Mantener una única fuente de verdad para:
- análisis de guías y rúbricas;
- investigación y evaluación de fuentes;
- trazabilidad claim → evidence → source → citation;
- aplicación de APA 7 y perfiles institucionales;
- citación y referencias;
- tablas, figuras y análisis estadístico;
- validación de DOCX, XLSX, PPTX, video, web, infografías y gráficos;
- auditoría y reparación controlada de documentos;
- revisión crítica y QA final;
- reutilización portable en distintas plataformas de IA.

## Plataformas objetivo

La lógica académica es independiente de plataforma. Los adaptadores pueden empaquetarla como:
- ChatGPT / Custom GPT / Skills;
- Gemini Gems;
- Sparks u otros asistentes compatibles.

Los adaptadores consumen el repositorio; no reemplazan la fuente canónica.

## Principio de autoridad

1. Instrucción explícita del usuario.
2. Guía oficial de la actividad.
3. Rúbrica o instrumento de evaluación.
4. Instrucciones del tutor o docente.
5. Reglas institucionales.
6. APA 7.
7. Convenciones académicas generales.

Una regla genérica nunca debe reemplazar un requisito explícito de la actividad.

## Orquestación y contratos

`core/ORCHESTRATION.md` define el routing canónico entre skills. `core/SKILL-CONTRACT.md` define el envelope interoperable común.

La skill `academic-workflow-orchestrator` selecciona las capacidades necesarias y `academic-evidence-mapper` mantiene la trazabilidad entre claims y evidencia.

No todas las skills se ejecutan en todas las actividades: el flujo se adapta al tipo de artefacto, estado del trabajo y gaps de cobertura.

## Arquitectura

```text
Academic-Colombia-APA-7/
├── core/
│   ├── CORE.md
│   ├── APA7.md
│   ├── LEGAL-COLOMBIA.md
│   ├── AI-USAGE-AND-CITATION.md
│   ├── ORCHESTRATION.md
│   └── SKILL-CONTRACT.md
├── institutions/
├── templates/
├── skills/
├── external-references/
├── quality/
├── tests/
├── platforms/
├── docs/
├── LICENSE
├── CONTRIBUTING.md
├── CHANGELOG.md
├── VERSION
└── README.md
```

## Fuente de verdad

**GitHub es la fuente canónica del proyecto.**

Las configuraciones instaladas en plataformas de IA deben derivarse de este repositorio y no mantenerse como versiones divergentes.

## Gobernanza

- `main` es la rama canónica y está protegida por ruleset.
- Los cambios llegan mediante branch/fork + pull request.
- Los ejemplos de estudiantes deben anonimizarse antes de convertirse en tests.
- Las fuentes externas se consumen únicamente mediante el registry y resolver definidos por el proyecto.

Ver `CONTRIBUTING.md` y `docs/REPOSITORY-GOVERNANCE.md`.

## Estado

Framework académico modular en estabilización end-to-end.

Versión actual de esta rama: `0.10.0`.

El proyecto cubre planificación, investigación, evidencia, citación, APA, perfiles institucionales, artefactos, referencias externas, auditoría/reparación documental, orquestación portable y gates de readiness.

## Licencia

Academic Colombia se distribuye bajo la **MIT License**.

Se permite usar, copiar, modificar, distribuir y adaptar el repositorio, conservando el aviso de copyright y la licencia correspondiente.