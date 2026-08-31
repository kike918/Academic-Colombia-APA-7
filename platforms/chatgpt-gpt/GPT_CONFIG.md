# ChatGPT Custom GPT — Production Configuration

## Name

Academic Colombia — APA 7 | UNAD | SENA

## Description

Framework académico para analizar guías y rúbricas, investigar con trazabilidad, aplicar reglas institucionales/APA, validar artefactos y auditar entregables académicos en contextos colombianos.

## Conversation starters

1. Analiza esta guía y rúbrica y conviértelas en un plan de entrega.
2. Revisa este trabajo contra la rúbrica, las fuentes y APA 7.
3. Audita este DOCX sin cambiar el contenido académico validado.
4. Revisa mis citas y referencias y señala qué evidencia falta.

## Instructions

Use the complete contents of:

`platforms/chatgpt-gpt/INSTRUCTIONS.md`

Do not duplicate full canonical skill definitions inside Instructions.

## Knowledge

Follow:

`platforms/chatgpt-gpt/KNOWLEDGE_MANIFEST.md`

The deployment should preserve at minimum:

- core semantics;
- orchestration;
- Skill Contract;
- Academic QA;
- institutional profiles relevant to the deployment;
- selected native skills;
- APA/evidence rules needed for advertised capabilities.

A reduced package must not be advertised as full-framework compatibility if essential capabilities were omitted.

## Context strategy

Use:

`platforms/chatgpt-gpt/CONTEXT-STRATEGY.md`

Principle:

> minimum sufficient context + explicit routing + verified evidence.

## Capabilities

Enable appropriate ChatGPT capabilities where available for the deployment:

- web/current-source verification;
- file analysis;
- data analysis;
- image generation only for tasks requiring visual artifacts.

Capabilities are tools. They do not replace Academic Colombia's authority, evidence or QA rules.

## Permanent Knowledge exclusions

Do not permanently add by default:

- course-specific guides;
- one-off rubrics;
- teacher messages;
- identifiable student submissions;
- grades;
- confidential academic/company documents.

These belong to the task/conversation unless deliberately anonymized and promoted into canonical tests/examples.

## Acceptance package

Before treating the GPT as production-ready, run:

- `tests/CHATGPT_ADAPTER_CASES.md`;
- `tests/CHATGPT_ADVERSARIAL_CASES.md`;
- representative core E2E cases.

Critical failures block production readiness.

## Few-shot behavior

Use `platforms/chatgpt-gpt/FEW-SHOT-EXAMPLES.md` as behavioral examples when useful.

Examples never override the user's current guide/rubric or canonical rules.

## Installation

See:

`platforms/chatgpt-gpt/INSTALLATION.md`

## Release discipline

When core behavior changes:

1. update canonical source first;
2. evaluate adapter impact;
3. update manifest/instructions only when needed;
4. rerun ChatGPT acceptance tests;
5. record behavioral impact in CHANGELOG.
