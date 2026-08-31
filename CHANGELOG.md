# Changelog

## 0.14.0 - 2026-08-31

### Added
- `institutions/TEMPLATE.md` para futuras extensiones institucionales basadas en evidencia.
- `tests/EMPIRICAL_EVIDENCE_REGISTRY.md` para separar casos ejecutados, parciales, fixtures y capacidades no reclamadas.
- `tests/EMPIRICAL_CASE_TEMPLATE.md` para incorporar actividades reales anonimizadas sin publicar datos personales ni asumir derechos de redistribución.
- `docs/V0.14-PRE-RELEASE-READINESS.md` con evaluación de readiness hacia v1.0 y límites de cobertura empírica.

### Changed
- v0.14 cambia el foco desde construcción de capacidades hacia pre-release basado en evidencia real.
- Se documenta explícitamente que DOCX/UNAD tiene mayor profundidad empírica que XLSX, PPTX, video y estadística.
- Runtime de Custom GPT y Gemini Gem continúa como `NOT_CLAIMED` hasta desplegar y ejecutar suites reales.
- No se crea `academic-integrity-review` porque la evidencia actual no demuestra un gap recurrente no cubierto por las skills existentes.

### Release boundary
- No se añaden nuevas skills generales ni nuevas instituciones.
- Los fixtures no se promocionan artificialmente a pruebas ejecutadas.
- Después de v0.14 el siguiente trabajo de framework es preparación de v1.0: política de compatibilidad/releases, auditoría final y runtime acceptance cuando estén disponibles las instancias reales.

## 0.13.0 - 2026-08-31

### Added
- `scripts/validate_repo.py` como validador estructural del framework declarativo.
- `.github/workflows/validate.yml` para ejecutar validación y comprobar que los paquetes de Skills puedan generarse.
- `tests/REPOSITORY_VALIDATION_CASES.md` con 20 casos de aceptación de consistencia del repositorio.

### Validation scope
- archivos canónicos obligatorios;
- formato `VERSION` y sincronización con `CHANGELOG.md`;
- presencia y nombre de `SKILL.md` por directorio;
- marcadores del Skill Contract v1 y `critical_gate`;
- consistencia entre `skills/` y `distribution/SKILLS-MANIFEST.md`;
- links Markdown internos;
- taxonomía externa A–E;
- existencia del empaquetador y exclusión de `dist/`.

### Boundaries
- CI valida estructura/consistencia, no reemplaza tests académicos, E2E, adversariales ni aceptación runtime de ChatGPT/Gemini.
- No se modifica comportamiento del core ni de las Skills.

## 0.12.0 - 2026-08-31

### Added
- `platforms/gemini/GEM_CONFIG.md` con configuración de producción del Gem.
- `platforms/gemini/KNOWLEDGE_MANIFEST.md` para separar core, instituciones, skills y archivos task-scoped.
- `platforms/gemini/INSTALLATION.md` con instalación por snapshot o Knowledge respaldado por Drive.
- `platforms/gemini/FEW-SHOT-EXAMPLES.md` con 8 ejemplos de routing, integridad y límites.
- `tests/GEMINI_ADAPTER_CASES.md` con 20 casos de aceptación.
- `tests/CROSS_PLATFORM_BEHAVIOR_CASES.md` con 15 casos de consistencia ChatGPT ↔ Gemini.
- `docs/V0.12-VALIDATION-REPORT.md` con verificación estática y runtime pendiente.

### Changed
- `platforms/gemini/GEM_INSTRUCTIONS.md` deja de ser scaffold v0.1 y pasa a adapter alineado con ORCHESTRATION, Skill Contract, evidencia, artefactos y critical gates.
- Gemini Knowledge desde Drive se documenta como capa de distribución actualizable; GitHub continúa como fuente canónica.
- No se fijan límites numéricos de producto como contrato del framework; deben verificarse al instalar.

### Validation
- Gemini static adapter readiness: PASS.
- Cross-platform behavioral specification: PASS.
- Gemini Gem runtime acceptance: PENDING.
- ChatGPT Custom GPT runtime acceptance: PENDING.

## 0.11.0 - 2026-08-31

### Added
- `platforms/chatgpt-gpt/KNOWLEDGE_MANIFEST.md` para separar Instructions, Knowledge y archivos task-scoped.
- `platforms/chatgpt-gpt/INSTALLATION.md` con instalación reproducible del Custom GPT.
- `platforms/chatgpt-gpt/CONTEXT-STRATEGY.md` con carga condicional y minimum sufficient context.
- `platforms/chatgpt-gpt/FEW-SHOT-EXAMPLES.md` con 8 ejemplos de routing e integridad.
- `tests/CHATGPT_ADAPTER_CASES.md` con 20 casos de aceptación del adapter.
- `tests/CHATGPT_ADVERSARIAL_CASES.md` con 15 casos adversariales.
- `docs/V0.11-VALIDATION-REPORT.md` con estado de validación estática y runtime pendiente.

### Changed
- `platforms/chatgpt-gpt/INSTRUCTIONS.md` pasa de configuración inicial a adapter consolidado contra core/orchestration/Skill Contract v0.10+.
- `platforms/chatgpt-gpt/GPT_CONFIG.md` se alinea con las 16 skills, evidencia, artifacts y gates reales del framework.
- Roadmap delimita v0.12–v1.0 y excluye telemetría, evasión de detectores y expansión masiva antes de v1.0.

### Validation
- Compatibilidad estática del paquete ChatGPT: PASS.
- Ejecución en una instancia real de Custom GPT: PENDING; no se declara deployment público validado hasta completar esa prueba.

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
- `quality/ACADEMIC-QA.md` amplía gates de requisitos, evidencia, APA, artefacto, método, fallback y orquestación.
- `docs/ARCHITECTURE.md`, `docs/ROADMAP.md` y README se alinean con la arquitectura real del sistema.
- El workflow de evidencia incorpora explícitamente source evaluator → evidence mapper → citation manager → critical review.

## 0.9.0 - 2026-08-30

### Added
- MIT License para uso, modificación y distribución pública del framework.
- `core/ORCHESTRATION.md` como flujo canónico y portable entre skills.
- Skill `academic-workflow-orchestrator` para routing condicional por tipo de trabajo/artefacto.
- `CONTRIBUTING.md` con política branch/fork + PR.
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
