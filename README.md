# Academic Colombia — APA 7

Repositorio canónico para gestionar, versionar y reutilizar reglas académicas orientadas a **APA 7**, **UNAD** y **SENA** en asistentes de inteligencia artificial.

## Objetivo

Mantener una única fuente de verdad para:

* análisis de guías de aprendizaje y rúbricas;
* aplicación de normas APA 7;
* perfiles institucionales para UNAD y SENA;
* revisión de citas y referencias;
* control de calidad académica;
* generación y auditoría de contenidos académicos;
* reutilización de las mismas reglas en diferentes plataformas de IA.

## Plataformas objetivo

La arquitectura está diseñada para soportar inicialmente:

* ChatGPT Custom GPTs;
* OpenAI Skills;
* posteriormente Gemini Gems.

La lógica académica debe mantenerse independiente de la plataforma para evitar duplicación y divergencia entre versiones.

## Principio de autoridad

Cuando exista conflicto entre requisitos, se aplica este orden:

1. Instrucción explícita del usuario.
2. Guía oficial de la actividad.
3. Rúbrica o instrumento de evaluación.
4. Instrucciones del tutor o docente.
5. Reglas institucionales.
6. APA 7.
7. Convenciones académicas generales.

Una regla genérica de APA nunca debe reemplazar un requisito explícito de la actividad.

## Principios de calidad

Este proyecto debe:

* evitar referencias o datos bibliográficos inventados;
* priorizar fuentes oficiales, primarias y académicas;
* mantener correspondencia entre citas y referencias;
* adaptar la profundidad del trabajo al tipo de evidencia solicitada;
* evitar sobredimensionar entregables;
* revisar cada trabajo contra su guía y rúbrica antes de considerarlo terminado.

## Arquitectura prevista

```text
Academic-Colombia-APA-7/
├── core/
│   ├── CORE.md
│   └── APA7.md
│
├── institutions/
│   ├── UNAD.md
│   └── SENA.md
│
├── skills/
│   ├── academic-requirements-analyzer/
│   ├── apa7-academic-style/
│   └── academic-final-review/
│
├── quality/
│   └── ACADEMIC-QA.md
│
├── platforms/
│   ├── chatgpt-gpt/
│   └── gemini/
│
├── docs/
│   ├── ARCHITECTURE.md
│   └── ROADMAP.md
│
├── CHANGELOG.md
├── VERSION
└── README.md
```

## Fuente de verdad

**GitHub es la fuente canónica del proyecto.**

Las configuraciones de Custom GPTs, Skills y Gems deben derivarse de este repositorio y no mantenerse como versiones independientes.

## Estado

Proyecto en fase inicial.

Versión prevista inicial:

`0.1.0`

Primer alcance:

* Core académico.
* APA 7 operativo.
* Perfil UNAD.
* Perfil SENA.
* Academic QA.
* Skills iniciales para ChatGPT/OpenAI.
* Adaptador para Custom GPT.
* Preparación para Gemini Gems.

## Licencia y uso

El repositorio se utiliza inicialmente como infraestructura académica reutilizable y versionada para asistentes de IA.

La política de licencia y distribución pública podrá definirse en una versión posterior.
