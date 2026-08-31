# ChatGPT Context Strategy

## Goal

Keep Academic Colombia reliable without flooding every interaction with the full repository.

## Layers

### Always-on behavior
Represent in `INSTRUCTIONS.md`:
- authority hierarchy;
- integrity rules;
- conditional routing;
- artifact sensitivity;
- critical-gate behavior;
- final readiness authority.

### Always-available canonical knowledge
Prioritize:
- core semantics;
- orchestration;
- Skill Contract;
- Academic QA;
- capability directory.

### Conditional knowledge
Consult when relevant:
- APA rules;
- UNAD or SENA profile;
- legal rules;
- statistics;
- document repair;
- artifact-specific rules;
- external fallback.

### Task-local authority
Treat these as highest-relevance task inputs:
- guide;
- rubric;
- teacher instructions;
- required template;
- supplied sources;
- current artifact.

## Selection rule

Before using specialist knowledge ask:

1. Does this file/capability affect a mandatory requirement?
2. Does it affect evidence quality or correctness?
3. Does it affect the artifact being produced/reviewed?
4. Does it resolve a real gap?

If all answers are no, omit it from the working path.

## Decision tree

```text
Is there a guide/rubric?
├─ yes → requirements analyzer
└─ no  → infer only minimum task requirements

Is the work existing/finished?
├─ yes → audit path
└─ no  → creation path

Does the work contain externally verifiable claims?
├─ yes → source evaluator → evidence mapper → citation manager
└─ no  → do not force research

Is APA/institutional formatting relevant?
├─ yes → applicable institutional profile → APA skill
└─ no  → do not impose paper conventions

Is there quantitative analysis?
├─ yes → statistical analysis
└─ no  → omit

Is there a specialist capability gap?
├─ yes → external-reference-resolver
└─ no  → native workflow only

Did any critical gate fail?
├─ yes → NOT READY / USER DECISION REQUIRED
└─ no  → final review decides readiness
```

## Anti-duplication rule

Do not restate full canonical rules inside platform Instructions, examples, or tests. Reference the canonical file and test observable behavior.

## Output compression

Internal workflow may be detailed; user-facing answers should be proportional to the task.

Prefer:
- concise requirements maps for simple tasks;
- full audit matrices only for audit requests;
- detailed evidence tables only when evidence mapping materially helps;
- no raw Skill Contract envelope unless useful for maintainers/debugging.

## Context failure modes

Avoid:
- loading all skills for every request;
- treating Knowledge retrieval order as authority order;
- using a generic APA file when guide/rubric already specifies the format;
- letting an external fallback become default behavior;
- using examples as normative sources;
- persisting private task files as canonical Knowledge.
