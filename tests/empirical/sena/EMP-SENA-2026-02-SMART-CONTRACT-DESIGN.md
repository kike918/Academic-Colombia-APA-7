# EMP-SENA-2026-02 — Smart-contract design report

## Scope

Real SENA academic artifact, anonymized for public empirical evidence.

Artifact type: PDF report, 26 pages.
Domain: blockchain / smart contracts / traceability.
Institution: SENA.

The original private artifact is not committed to the repository.

## Why this case matters

This case exercises a technical academic workflow that is neither financial analysis nor a generic essay. It requires the framework to distinguish:
- academic requirements from product design choices;
- evidence-backed technical claims from design assumptions;
- tables/figures from prose;
- a design-stage deliverable from an implementation-stage deliverable.

## Observed artifact structure

The inspected report includes:
- introduction and objectives;
- problem/need definition;
- smart-contract justification;
- network/platform selection;
- actors and permissions;
- lot data and traceability data;
- state model;
- inputs/outputs and business rules;
- suggested functions;
- flow and logical diagrams;
- implementation plan;
- conclusions, recommendations and bibliography.

## Routing exercised

| Skill | Result | Evidence |
|---|---|---|
| `academic-requirements-analyzer` | PARTIAL | Internal section headings map well to an assignment-style design brief, but the official guide/rubric was not part of this empirical input |
| `academic-template-selector` | PASS | Long technical report structure is coherent with the artifact's declared purpose |
| `academic-source-evaluator` | PASS WITH FINDINGS | Bibliography contains strong academic/institutional sources but incomplete metadata for some entries |
| `academic-evidence-mapper` | PASS WITH FINDINGS | Technical assertions and design choices can be separated; some broad blockchain claims need tighter sourcing/qualification |
| `academic-citation-manager` | FINDINGS | IBM entry lacks a visible URL in the inspected bibliography; SENA guide entry is incomplete; source-to-claim coverage is sparse in several technical sections |
| `academic-critical-review` | PASS WITH FINDINGS | Correctly distinguishes design assumptions from implemented behavior; flags overbroad wording such as absolute immutability/intermediary claims |
| `academic-tables-figures` | FINDINGS | Five tables and two diagrams are present; figures need explicit source/AI-generation attribution and reproducibility note when applicable |
| `academic-artifact-validator` | PASS | PDF is readable and logically organized; tables and diagrams support the technical narrative |
| `academic-final-review` | PARTIAL | Suitable as a design artifact, but not evidence that the smart contract was implemented/deployed/tested |

## Strong behaviors demonstrated

### 1. MVP scope discipline

The report explicitly avoids placing the entire operation on-chain and proposes keeping only trust-critical data in blockchain while external documents/images remain off-chain with hash references.

This is evidence that the workflow can preserve a realistic MVP boundary rather than maximizing technical complexity.

### 2. State and permission modeling

The artifact defines roles, permissions, lot states, business rules and proposed functions. This gives `academic-critical-review` a concrete consistency surface:
- only authorized actors create/update;
- a brand cannot be assigned to a nonexistent lot;
- relevant changes leave a trace;
- public consultation does not imply write permission.

### 3. Design ≠ implementation

The report proposes Solidity, Remix and an Ethereum test environment for later phases. The framework must not report the contract as deployed or technically validated merely because the design is detailed.

## Findings that should be caught

1. Phrases such as "inmutable" or "sin intermediarios" should be qualified rather than treated as universal blockchain guarantees.
2. A generic "Ethereum testnet" choice is a design recommendation; the current concrete test network must be verified at implementation time.
3. Bibliographic metadata is incomplete for some sources.
4. Figures/diagrams require explicit provenance/attribution, especially when generated with an AI-assisted tool.
5. Product-specific example fields (farm, variety, regulatory reference, dates) are illustrative unless backed by real lot evidence.

## Status

`PARTIAL`

Reason: real technical artifact inspected and multiple skills exercised, but the official assignment guide/rubric and implementation/runtime evidence were not included.

## Coverage contribution

This case strengthens empirical coverage for:
- SENA technical reports;
- product-linked academic work;
- technical source/evidence review;
- tables/figures;
- architecture/design reasoning;
- correct separation of design and implementation.
