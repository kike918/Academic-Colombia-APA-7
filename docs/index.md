# Academic Colombia

**Framework académico modular para asistentes de IA — APA 7, UNAD y SENA.**

Academic Colombia ayuda a convertir una actividad académica en un flujo controlado de requisitos, evidencia, contenido, artefacto y revisión final.

No es una guía teórica de APA ni una institución educativa. Tampoco es una aplicación tradicional: es un framework declarativo compuesto por Skills, perfiles institucionales, reglas de routing, contratos, QA y adapters para asistentes de IA.

## Estado

**Versión estable: 1.0.0**

v1 estabiliza el core, Skill Contract v1, las 16 Skills nativas, los perfiles UNAD/SENA, los adapters estáticos ChatGPT/Gemini, la distribución de Skills y la validación declarativa del repositorio.

➡️ [Release readiness](V1.0-RELEASE-READINESS.md)

## Qué hace

- lee guías y rúbricas antes de empezar;
- selecciona la estructura y el artefacto adecuados;
- evalúa fuentes y vigencia;
- conecta afirmaciones con evidencia verificable;
- gestiona citas y referencias;
- aplica APA 7 respetando primero la actividad y la institución;
- revisa análisis, tablas, figuras y datos;
- valida DOCX, XLSX, presentaciones, infografías, video y web según el artefacto;
- audita y repara documentos existentes;
- bloquea la entrega cuando existe un fallo crítico.

## Regla principal

La autoridad se aplica en este orden:

1. instrucción explícita del usuario;
2. guía de la actividad;
3. rúbrica;
4. tutor/docente;
5. institución;
6. APA 7;
7. convenciones académicas generales.

**APA no reemplaza instrucciones explícitas de una actividad.**

## Flujo

```text
actividad / guía / rúbrica
          ↓
requirements + template
          ↓
research / evidence
          ↓
content / artifact
          ↓
APA + critical review
          ↓
artifact/document QA
          ↓
final review
          ↓
READY / NOT READY / USER DECISION REQUIRED
```

No todas las Skills se ejecutan siempre.

## Skills

Academic Colombia contiene **16 Skills nativas** organizadas en:

- orquestación;
- requisitos y estructura;
- investigación y evidencia;
- análisis;
- APA y artefactos;
- auditoría y reparación;
- QA final;
- fallback externo controlado.

➡️ [Directorio de Skills](SKILLS-DIRECTORY.md)

## Principios de calidad

- No inventar autores, DOI, URLs, páginas, leyes, datos o fuentes.
- Una fuente correcta puede estar mal interpretada: el número y el significado deben verificarse.
- Una bibliografía final no sustituye citas/evidencia dentro del trabajo.
- Un artefacto visualmente limpio puede seguir estando académicamente `NOT READY`.
- Un `critical_gate: fail` no se compensa con otros criterios positivos.
- Los hechos actuales requieren verificación de vigencia.
- Una presentación debe seguir siendo una presentación; un XLSX, un XLSX; una infografía, una infografía.

## Evidencia real

La versión estable se apoya en actividades reales anonimizadas de UNAD y SENA, incluyendo documentos extensos, presentaciones visuales, análisis financiero, comercio internacional, normativa y un workbook contable XLSX reconciliado.

El registro distingue entre:

```text
EXECUTED
PARTIAL
FIXTURE_READY
NOT_CLAIMED
```

➡️ [Empirical Evidence Registry](../tests/EMPIRICAL_EVIDENCE_REGISTRY.md)

## Uso en IA

### ChatGPT

Adapter, Knowledge Manifest, Instructions y distribución de Skills disponibles.

➡️ [Instalación ChatGPT](../platforms/chatgpt-gpt/INSTALLATION.md) · [Instalar Skills](../distribution/INSTALL-CHATGPT-SKILLS.md)

Runtime real de un Custom GPT permanece `NOT_CLAIMED` hasta probar la instancia.

### Gemini

Adapter Gem, Knowledge Manifest e instalación disponibles.

➡️ [Instalación Gemini](../platforms/gemini/INSTALLATION.md)

Runtime real del Gem permanece `NOT_CLAIMED` hasta probar la instancia.

## Compatibilidad

Desde v1.0 usamos Semantic Versioning sobre **comportamiento declarativo observable**.

Una modificación de Markdown puede ser breaking si cambia de forma incompatible el routing, la autoridad, el Skill Contract o la decisión READY/NOT READY.

➡️ [Compatibility Policy](COMPATIBILITY-POLICY.md)

## Documentación

- [Skills Directory](SKILLS-DIRECTORY.md)
- [Architecture](ARCHITECTURE.md)
- [Artifact Validation Matrix](ARTIFACT-VALIDATION-MATRIX.md)
- [Repository Governance](REPOSITORY-GOVERNANCE.md)
- [Roadmap](ROADMAP.md)
- [License Scope](LICENSE-SCOPE.md)
- [v1.0 Release Readiness](V1.0-RELEASE-READINESS.md)

## Licencia

El contenido original se distribuye bajo MIT License. Materiales, marcas, normas y recursos externos o institucionales conservan sus propios derechos.

Academic Colombia no está afiliado, patrocinado ni respaldado oficialmente por APA, UNAD, SENA u otras instituciones mencionadas.
