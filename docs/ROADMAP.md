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
- 15 casos de routing del orquestador.
- 8 casos de aceptación end-to-end anonimizados/representativos.

## v0.11 — ChatGPT production adapter
- Definir `KNOWLEDGE_MANIFEST.md`.
- Consolidar Instructions contra v0.10.
- Empaquetado reproducible para GPT/Skills.
- Casos de aceptación específicos de ChatGPT.
- Validar límites de Knowledge y estrategia de archivos.

## v0.12 — Gemini / other platform adapters
- Gem adapter actualizado desde core v0.10+.
- Adapter Spark cuando la plataforma/forma de instalación esté definida.
- Pruebas cruzadas de routing, integridad y readiness.

## v0.13 — Repository validation / CI
- Validador de estructura del repo.
- Validación automática de VERSION/CHANGELOG/internal links/skill contract.
- GitHub Actions cuando la automatización aporte valor real.
- Tras estabilizar checks, considerar `Require status checks` en `main`.

## v1.0 — Stable academic engine
- Suite estable y documentada.
- Instalación por plataforma.
- Regression tests académicos end-to-end.
- Semántica de orquestación/contrato estable.
- Política de releases y compatibilidad.

## Fuera de alcance antes de v1.0

No convertir en dependencia obligatoria:
- n8n;
- webhooks;
- runtime autónomo;
- memoria personal externa;
- RAG o bóvedas externas.

Estas capas podrán consumir Academic Colombia después de que el motor académico sea estable, pero no formarán parte del core.