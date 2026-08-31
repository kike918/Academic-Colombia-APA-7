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
- Distribución reproducible de las 16 Skills como ZIP derivado mediante `scripts/package_skills.py`.
- Validación estática del paquete; runtime real permanece pendiente hasta desplegar el Custom GPT.

## v0.12 — Gemini / cross-platform adapter
- Gemini Gem actualizado desde el core y contrato actuales.
- `GEM_CONFIG.md`, `KNOWLEDGE_MANIFEST.md`, `INSTALLATION.md` y few-shot examples.
- Knowledge por upload local o Drive con GitHub como fuente canónica.
- 20 casos de aceptación específicos de Gemini.
- 15 casos de consistencia conductual ChatGPT ↔ Gemini.
- Verificación de comportamiento de producto contra documentación oficial de Gemini.
- Runtime real del Gem queda pendiente hasta configurar una instancia y ejecutar la suite.
- No se añade Spark por nombre: un nuevo adapter solo entra cuando su modelo de instalación/conocimiento esté suficientemente definido.

## v0.13 — Declarative repository validation
- `scripts/validate_repo.py` valida estructura canónica del framework.
- Validación automática de VERSION/CHANGELOG, links internos, Skill Contract, registry e inventario/distribución.
- `.github/workflows/validate.yml` ejecuta el lint declarativo y verifica que los paquetes de Skills puedan generarse.
- 20 casos de aceptación de validación estructural.
- CI queda delimitado como guardrail de consistencia; no sustituye aceptación académica, E2E ni runtime.
- El check ya demostró failure → corrección → PASS en PR real.

## v0.14 — Empirical coverage / pre-release evidence
- `tests/EMPIRICAL_EVIDENCE_REGISTRY.md` separa `EXECUTED`, `PARTIAL`, `FIXTURE_READY` y `NOT_CLAIMED`.
- `tests/EMPIRICAL_CASE_TEMPLATE.md` define cómo promover actividades reales anonimizadas a evidencia reusable.
- `institutions/TEMPLATE.md` establece un patrón de extensión institucional basado en autoridad y evidencia.
- `docs/V0.14-PRE-RELEASE-READINESS.md` delimita readiness, gaps reales y criterios mínimos para v1.0.
- UNAD/DOCX mantiene la mayor profundidad empírica actual; SENA, XLSX, PPTX, video y estadística conservan límites explícitos.
- Runtime de Custom GPT y Gemini Gem permanece no reclamado hasta ejecutar las instancias reales.
- No se crea `academic-integrity-review` sin evidencia de un gap recurrente; evasión de detectores continúa fuera de alcance.
- No se amplían instituciones por volumen antes de v1.0.

## v1.0 — Stable academic-agent framework
- Congelar core y Skill Contract v1 salvo defectos de release.
- Definir política de releases y compatibilidad semántica para cambios declarativos.
- Ejecutar auditoría final de repo, documentación, licencia, adapters y distribución.
- Documentar runtime acceptance de ChatGPT/Gemini cuando las instancias estén disponibles, o mantener claramente `NOT_CLAIMED`.
- Publicar release/tag estable con límites de cobertura explícitos.
- Activar `Require status checks` para el check declarativo una vez confirmada estabilidad adicional en PR normal.

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
