# Roadmap

## v0.1 — Foundation
- Core académico neutral.
- APA 7 operativo inicial.
- Perfiles UNAD y SENA.
- QA y adaptadores iniciales.

## v0.2 — Verified institutional sources
- Fuentes oficiales UNAD/SENA.
- Registry de autoridad documental.
- Casos de regresión iniciales.

## v0.3 — APA operational engine
- Motor ampliado de citas/referencias.
- Normativa colombiana.
- Tablas y figuras.

## v0.4 — Template validation
- Perfil canónico de plantilla UNAD.
- Selector de templates.
- Validación de documentos reales.

## v0.5 — Artifact validation
- DOCX, XLSX, PPTX.
- Video/YouTube, landing pages, infografías y gráficos.

## v0.6 — Research and evidence skills
- Citación.
- Revisión crítica.
- Estadística.
- Ideación.
- Evaluación de fuentes.
- IA y citación.

## v0.7 — External reference fallback
- Registry externo controlado.
- K-Dense como referencia metodológica/técnica.
- Resolver de gaps de cobertura.

## v0.8 — Document audit and repair
- Auditoría integral de documentos.
- Reparación conservative/evidence-backed/full-revision.
- QA visual obligatorio para DOCX.

## v0.9 — Governance and orchestration
- MIT License.
- Contribución por branch/fork + PR.
- Protección de `main` mediante ruleset.
- Core de orquestación portable.
- Skill `academic-workflow-orchestrator`.

## v0.10 — End-to-end stabilization
- `core/SKILL-CONTRACT.md` como contrato interoperable v1.
- Migración de todas las skills existentes al contrato común.
- Skill `academic-evidence-mapper` para trazabilidad claim → evidence → source → citation.
- Propagación de `critical_gate` y estados blocked/partial/success.
- QA académico ampliado por requisitos, evidencia, APA, artefacto, método y fallback.
- Arquitectura actualizada a las capas reales del sistema.
- Casos de routing y aceptación end-to-end.
- README/directorio de skills, Page mínima y alcance de licencia.

## v0.11 — ChatGPT production adapter package
- `KNOWLEDGE_MANIFEST.md` para separar Instructions, Knowledge y archivos task-scoped.
- `INSTALLATION.md` con instalación reproducible del Custom GPT.
- `CONTEXT-STRATEGY.md` con carga por relevancia y minimum sufficient context.
- `INSTRUCTIONS.md` consolidado contra core v0.10+ sin duplicar skills completas.
- `GPT_CONFIG.md` actualizado a las capacidades reales del framework.
- Few-shot examples de alto valor centrados en routing e integridad.
- Suite de aceptación específica del adapter ChatGPT.
- Suite adversarial para referencias inventadas, falsa readiness, prompt injection y evasión de detectores.
- Validación estática del paquete; la ejecución en una instancia real de Custom GPT debe completarse antes de anunciar un deployment público validado.

## v0.12 — Gemini / other platform adapters
- Actualizar Gemini Gem desde el core y contrato actuales.
- Definir manifest/instalación/context strategy equivalentes cuando la plataforma lo requiera.
- Adapter adicional (por ejemplo Spark) solo cuando su forma de instalación esté suficientemente definida.
- Pruebas cruzadas de autoridad, routing, integridad y readiness.

## v0.13 — Declarative repository validation
- Validador de estructura del repo.
- Validación automática de VERSION/CHANGELOG/internal links/skill contract/registry.
- GitHub Actions solo para linting/consistencia del framework declarativo.
- Tras estabilizar checks, considerar `Require status checks` en `main`.

## v0.14 — Empirical coverage
- Más actividades SENA reales anonimizadas antes de crear subperfiles.
- Casos reales XLSX, PPTX, infografía y video/web.
- Evaluar `academic-integrity-review` solo si los casos reales demuestran un gap; no construir funciones de evasión de detectores.
- Añadir `institutions/TEMPLATE.md` para futuras extensiones sin ampliar instituciones todavía.

## v1.0 — Stable academic-agent framework
- Core y Skill Contract v1 estables.
- Adaptadores principales utilizables y documentados.
- Corpus E2E suficiente para los artefactos/instituciones declarados.
- Semántica de orquestación/readiness estable.
- Política de releases y compatibilidad.
- Documentación pública navegable.

## Fuera de alcance antes de v1.0

No convertir en dependencia obligatoria:
- n8n;
- webhooks;
- runtime autónomo;
- memoria personal externa;
- RAG o bóvedas externas;
- telemetría;
- evasión de detectores de IA/plagio;
- expansión masiva de instituciones.

Estas capas o extensiones podrán evaluarse después de que el framework académico sea estable, pero no forman parte del core actual.
