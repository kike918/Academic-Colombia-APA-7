# Changelog

## 0.10.2 - 2026-08-31

### Added
- `docs/index.md` como portada mínima preparada para GitHub Pages.
- `docs/LICENSE-SCOPE.md` para aclarar alcance MIT, terceros, instituciones y contribuciones.
- `docs/V0.10.2-AUDIT-REPORT.md` con auditoría de ramas, core, skills, documentación, licencia, tests y readiness.

### Changed
- README actualizado para enlazar la documentación web mínima y el alcance de licencia.
- `docs/DOCUMENTATION-STRATEGY.md` pasa de diferir una landing a iniciar una Page mínima desde `main/docs` sin duplicar la fuente canónica.

## 0.10.1 - 2026-08-31

### Added
- `docs/SKILLS-DIRECTORY.md` como catálogo funcional de las 16 skills nativas.
- `docs/DOCUMENTATION-STRATEGY.md` con la estrategia README → docs → futura GitHub Pages sin duplicar fuentes de verdad.

### Changed
- README reconstruido como puerta de entrada pública del proyecto: propósito, capacidades, skills, orquestación, artefactos, uso por plataforma, testing, gobernanza y navegación.
- La estrategia de landing queda diferida hasta una etapa de adopción pública/v1.x y deberá generarse desde Markdown canónico del repositorio.

## 0.10.0 - 2026-08-31

### Added
- `core/SKILL-CONTRACT.md` con envelope interoperable v1 para todas las skills.
- Skill `academic-evidence-mapper` para trazabilidad claim → evidence → source → citation.
- 15 casos de routing del orquestador.
- 8 casos de aceptación end-to-end anonimizados/representativos.

### Changed
- Las 15 skills existentes adoptan el contrato común sin perder su salida humana legible.
- `core/ORCHESTRATION.md` propaga `status`, gaps y `critical_gate` y solo permite que `academic-final-review` declare READY.
- `quality/ACADEMIC-QA.md` amplía gates de requisitos, evidencia, APA, artefactos, método, fallback y orquestación.
- `docs/ARCHITECTURE.md`, `docs/ROADMAP.md` y README se alinean con la arquitectura real del sistema.
- El workflow de evidencia incorpora explícitamente source evaluator → evidence mapper → citation manager → critical review.

## 0.9.0 - 2026-08-30

### Added
- MIT License para uso, modificación y distribución pública del framework.
- `core/ORCHESTRATION.md` como flujo canónico y portable entre skills.
- Skill `academic-workflow-orchestrator` para routing condicional por tipo de trabajo/artefacto.
- `CONTRIBUTING.md` con política branch/fork + pull request.
- `docs/REPOSITORY-GOVERNANCE.md` con política de `main`, merges y configuración recomendada de ruleset.

### Changed
- README actualizado al estado real del framework.
- Roadmap actualizado desde v0.1 hasta v1.0.
- Se establece explícitamente que n8n, webhooks, memoria personal externa y runtimes autónomos no son dependencias del core antes de v1.0.

## 0.8.0 - 2026-08-30

### Added
- Skill `academic-document-auditor` para auditoría académica, APA/institucional y técnica de documentos terminados.
- Skill `academic-document-repair` para regeneración controlada de documentos a partir de una auditoría validada.
- Workflow `DOCUMENT-AUDIT-REPAIR-WORKFLOW` con modos conservative, evidence-backed y full-revision.
- Casos end-to-end basados en un documento UNAD real anonimizado.

### Changed
- Las correcciones se clasifican como `SAFE_AUTOFIX`, `EVIDENCE_REQUIRED` o `CONTENT_DECISION`.
- Para documentos cuyo contenido ya fue evaluado positivamente, el modo de reparación predeterminado es `conservative`.
- DOCX exige render, inspección visual de todas las páginas y re-render antes de declararse listo.

## 0.7.0 - 2026-08-30

### Added
- Política formal de referencias externas y fallback controlado.
- Registro aprobado de fuentes externas por clase de autoridad.
- Registro específico de `K-Dense-AI/scientific-agent-skills` como referencia metodológica/técnica.
- Skill `external-reference-resolver` para detectar gaps de cobertura nativa y seleccionar fallback externo.
- 12 casos de aceptación para consumo externo, conflictos, licencias y promoción a skill nativa.

### Changed
- El consumo de fuentes externas deja de ser implícito: ahora exige clasificación, verificación, adaptación, trazabilidad y QA interno posterior.
- Se establece una regla de promoción: fallbacks externos recurrentes deben evaluarse para convertirse en skills nativas.

## 0.6.0 - 2026-08-30

### Added
- Evaluación jerárquica de fuentes externas.
- Módulo versionable `AI-USAGE-AND-CITATION`.
- Skills `academic-citation-manager`, `academic-critical-review`, `academic-statistical-analysis`, `academic-research-ideation` y `academic-source-evaluator`.
- 15 casos de aceptación para investigación, análisis y citación.

### Changed
- Separación explícita entre autoridad normativa, fuente universitaria, repositorio técnico, guía secundaria y contenido promocional.
- Política de IA desacoplada del core APA para permitir actualizaciones rápidas.

## 0.5.0 - 2026-08-30

### Added
- Matriz de validación multiartefacto para DOCX, XLSX, PPTX, video/YouTube, landing pages, infografías y gráficos.
- Skill `academic-artifact-validator`.
- 15 casos de aceptación multiartefacto.

## 0.4.0 - 2026-08-30

### Added
- Validación de plantillas académicas UNAD.
- Perfil canónico `UNAD-TEMPLATE-PROFILE`.
- Skill `academic-template-selector`.
- Casos de compatibilidad de plantillas y documentos académicos reales.

## 0.3.0 - 2026-08-30

### Added
- Workflow operativo para normativa y jurisprudencia colombiana.
- Skill `academic-tables-figures`.
- 15 casos de regresión específicos del motor APA.

### Changed
- `core/APA7.md` ampliado con reglas operativas de citas, referencias, DOI/URL, tablas, figuras, formato general y control anti-alucinación.
- Política explícita de verificación de localizadores, metadatos y fuentes jurídicas.

## 0.2.0 - 2026-08-30

### Added
- Registro de fuentes oficiales verificadas para UNAD y SENA.
- Casos de regresión académica para validar futuras versiones del GPT, skills y Gem.
- Advertencia explícita sobre el instructivo SENA APA 6 de 2019 como fuente obsoleta frente a APA 7.

### Changed
- Perfil UNAD anclado a la guía APA 7 institucional de 2023 y OVA complementario de 2025.
- Perfil SENA anclado al instructivo institucional APA 7 de 2020 y evidencia de uso vigente en publicaciones SENA.
- Política de autoridad documental reforzada para no generalizar reglas editoriales específicas.

## 0.1.0 - 2026-08-30

### Added
- Core académico neutral.
- Perfil institucional UNAD.
- Perfil SENA.
- Skill APA 7 académica.
- Skill de análisis de requisitos.
- Skill de revisión final.
- Adaptador inicial para ChatGPT Custom GPT.
- Scaffold inicial para Gemini Gem.
