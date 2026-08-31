# External Reference Registry

Approved external references that may be consulted by `external-reference-resolver` when native Academic Colombia skills have a documented capability gap.

## Canonical source classes

The class labels are shared with `docs/EXTERNAL-SOURCE-EVALUATION.md` and `academic-source-evaluator`:

- **A** — primary official authority (standard/institution/government as appropriate).
- **B** — university, scholarly or strong institutional secondary source.
- **C** — technical/methodological repository with verifiable provenance.
- **D** — specialized secondary explanatory guide.
- **E** — product/vendor catalog, blog, promotional or community source.

Class is not a universal quality score: relevance and authority must still be evaluated for the specific claim.

## Registry fields

Each reference should define:
- identifier;
- class;
- domains/capabilities;
- authority role;
- permitted use;
- prohibited use;
- freshness/version policy;
- license/reuse notes when relevant.

---

## APA-STYLE-OFFICIAL
- Source: APA Style / American Psychological Association.
- Class: A — primary academic authority.
- Capabilities: APA style, grammar, references, AI references when officially documented.
- Permitted: normative APA guidance unless superseded by activity/institution rules.
- Prohibited: overriding explicit institutional adaptations or course templates.
- Freshness: check current official guidance for evolving topics such as generative AI.

## UNAD-OFFICIAL
- Source: Universidad Nacional Abierta y a Distancia official repository/resources.
- Class: A — institutional authority for UNAD context.
- Capabilities: institutional APA profile, templates, academic presentation rules.
- Permitted: define UNAD-specific adaptations subject to activity guide/rubric priority.
- Prohibited: generalizing UNAD rules to other institutions.

## SENA-OFFICIAL
- Source: SENA official institutional resources.
- Class: A — institutional authority for SENA context.
- Capabilities: SENA-specific academic/document guidance.
- Permitted: define SENA profile subject to evidence guide/instrument priority.
- Prohibited: using obsolete APA 6 material as current APA 7 authority.

## K-DENSE-SCIENTIFIC-AGENT-SKILLS
- Source: `K-Dense-AI/scientific-agent-skills`.
- Class: C — technical/open-source methodological reference.
- Capabilities: citation management, critical thinking, scientific brainstorming, peer review, statistical workflows, evidence mapping, reproducibility patterns.
- Permitted: workflow/method inspiration and controlled fallback.
- Prohibited: normative APA/UNAD/SENA authority; silent copying.
- License: MIT at time of registry creation; re-check before substantial reuse.
- Freshness: check repository version/commit when method materially matters.

## KIMI-ACADEMIC-SKILLS
- Source: Kimi academic skills resources/catalog.
- Class: E — product/vendor capability-discovery reference.
- Capabilities: discovery of possible academic-agent capabilities and UX patterns.
- Permitted: feature ideation and capability-gap discovery.
- Prohibited: establishing academic rules or methods without independent validation.

## UNIVERSITY-LIBGUIDES
- Source: university libraries and academic support centers, evaluated individually.
- Class: B — university/scholarly secondary authority.
- Capabilities: explanatory examples, institutional teaching guidance, source-type examples.
- Permitted: clarification and secondary support.
- Prohibited: overriding primary APA or the user's institution.

## SECONDARY-APA-GUIDES
Examples may include specialized APA websites not operated by the American Psychological Association.

- Class: D — specialized secondary explanatory reference.
- Capabilities: Spanish-language explanation, examples, orientation.
- Permitted: examples and cross-checking after primary sources.
- Prohibited: treating domain name or branding as proof of official APA authority.

---

## Adding a new external reference

Before registry admission:
1. verify identity;
2. classify authority;
3. define supported capabilities;
4. define what it may and may not influence;
5. inspect license if reusable implementation material exists;
6. define freshness policy;
7. add at least one acceptance case if it fills a critical gap.

Unregistered sources may still be researched, but should not become a default fallback until evaluated.