# Changelog

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
- Perfil institucional SENA.
- Skill APA 7 académica.
- Skill de análisis de requisitos.
- Skill de revisión final.
- Adaptador inicial para ChatGPT Custom GPT.
- Scaffold inicial para Gemini Gem.
