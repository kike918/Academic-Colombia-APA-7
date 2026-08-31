# Roadmap

## v0.1 — Foundation ✅
- Core académico neutral.
- APA 7 operativo inicial.
- Perfiles UNAD y SENA.
- QA y adaptadores iniciales.

## v0.2 — Verified institutional sources ✅
- Fuentes oficiales UNAD/SENA.
- Registry de autoridad documental.
- Casos de regresión iniciales.

## v0.3 — APA operational engine ✅
- Motor ampliado de citas/referencias.
- Normativa colombiana.
- Tablas y figuras.

## v0.4 — Template validation ✅
- Perfil canónico de plantilla UNAD.
- Selector de templates.
- Validación de documentos reales.

## v0.5 — Artifact validation ✅
- DOCX, XLSX, PPTX.
- Video/YouTube, landing pages, infografías y gráficos.

## v0.6 — Research and evidence skills ✅
- Citación.
- Revisión crítica.
- Estadística.
- Ideación.
- Evaluación de fuentes.
- IA y citación.

## v0.7 — External reference fallback ✅
- Registry externo controlado.
- K-Dense como referencia metodológica/técnica.
- Resolver de gaps de cobertura.

## v0.8 — Document audit and repair ✅
- Auditoría integral de documentos.
- Reparación conservative/evidence-backed/full-revision.
- QA visual obligatorio para DOCX.

## v0.9 — Governance and orchestration ✅
- MIT License.
- Contribución por branch/fork + PR.
- Protección de `main` mediante ruleset.
- Core de orquestación portable.
- Skill `academic-workflow-orchestrator`.

## v0.10 — End-to-end stabilization ✅
- Skill Contract v1.
- Migración de Skills al contrato común.
- `academic-evidence-mapper`.
- Propagación de `critical_gate`.
- QA ampliado.
- Routing y E2E.
- README, directorio de Skills y documentación pública.

## v0.11 — ChatGPT production adapter package ✅
- Knowledge Manifest.
- Installation + context strategy.
- Instructions de producción.
- Few-shot + adversarial cases.
- Distribución reproducible de las 16 Skills.
- Runtime real deliberadamente no reclamado hasta despliegue.

## v0.12 — Gemini / cross-platform adapter ✅
- Gem adapter actualizado.
- Knowledge Manifest + instalación.
- Casos Gemini y cross-platform.
- Runtime real deliberadamente no reclamado hasta despliegue.

## v0.13 — Declarative repository validation ✅
- `scripts/validate_repo.py`.
- GitHub Action de validación declarativa.
- VERSION/CHANGELOG, links, contratos, manifests y packaging.
- CI delimitado como guardrail estructural.

## v0.14 — Empirical coverage / pre-release evidence ✅
- Registry `EXECUTED / PARTIAL / FIXTURE_READY / NOT_CLAIMED`.
- Plantilla para casos reales anonimizados.
- Perfil institucional extensible basado en evidencia.
- Corpus real UNAD/SENA.
- XLSX nativo ejecutado y reconciliado.
- Casos positivos y negativos de evidencia, vigencia, metodología y artifact QA.
- Runtime ChatGPT/Gemini todavía explícitamente no reclamado.

## v1.0 — Stable academic-agent framework ✅
- Core y Skill Contract v1 estabilizados.
- Política SemVer/compatibilidad para comportamiento declarativo.
- Auditoría final de repo, documentación, licencia, adapters y distribución.
- Coverage boundaries documentados.
- Release readiness documentado.
- `main` protegido mediante PR, linear history y resolution de conversaciones.
- Declarative CI estable y listo para configurarse como required status check.

➡️ Ver [`COMPATIBILITY-POLICY.md`](COMPATIBILITY-POLICY.md) y [`V1.0-RELEASE-READINESS.md`](V1.0-RELEASE-READINESS.md).

# Post-v1 direction

Después de v1.0, el proyecto cambia de construcción de framework a **uso, mantenimiento y extensión basada en evidencia**.

## v1.x — Backward-compatible evolution

Prioridades candidatas, solo cuando exista evidencia real que las justifique:

- runtime acceptance de Custom GPT y Gemini Gem;
- más casos reales de artefactos;
- PPTX nativo;
- video reproducido con audio/duración/acceso;
- dataset estadístico/inferencial real;
- actualización de perfiles cuando cambien fuentes oficiales;
- nuevas instituciones mediante `institutions/TEMPLATE.md`;
- nuevas Skills solo ante gaps recurrentes demostrados;
- mejoras de distribución/documentación.

## Future major version

Una v2 solo se justifica cuando sea necesario romper contratos estables, por ejemplo:

- Skill Contract v2 incompatible;
- nueva semántica de routing/readiness incompatible;
- cambio material de autoridad/gates;
- reorganización incompatible del package contract.

# Fuera del core estable

No convertir automáticamente en dependencia obligatoria:

- n8n;
- webhooks;
- runtime autónomo;
- memoria personal externa;
- RAG o bóvedas externas;
- telemetría;
- evasión de detectores de IA/plagio;
- expansión masiva de instituciones.

Cualquiera de estas capas debe evaluarse como consumidor/extensión del framework, no asumirse como requisito del core.
