# Install Academic Colombia Skills in ChatGPT

This guide explains how an eligible ChatGPT user can install the native Academic Colombia Skills.

## Eligibility

ChatGPT Skills availability depends on plan, workspace settings, role and product surface. In eligible workspaces, Skills can be created with chat, with the editor, or uploaded from a computer.

## Preferred installation method

For reproducibility, install the packaged Skill ZIP generated from this repository.

1. Obtain the release or build the packages locally with:

   ```bash
   python scripts/package_skills.py
   ```

2. In ChatGPT, open **Plugins → Skills**.
3. Select **Create**.
4. Choose **Upload from your computer**.
5. Upload the ZIP for the Skill you want to install.
6. Review the Skill contents and any product safety/review notice.
7. Install it.
8. Repeat for the remaining Skills required by your workflow.

For the full framework, install all 16 packages listed in `SKILLS-MANIFEST.md`.

## Full installation vs selective installation

### Full installation

Recommended when the user wants Academic Colombia as a general academic workflow framework.

Install:
- the orchestrator;
- requirements/template Skills;
- research/evidence/citation Skills;
- analysis/review Skills;
- APA/artifact Skills;
- audit/repair Skills;
- final review;
- external fallback resolver.

### Selective installation

Useful when only a narrow capability is needed, for example:
- citation management;
- APA review;
- document auditing;
- statistical analysis.

A selective installation should not claim capabilities whose supporting Skills are not installed.

## Custom GPT relationship

Skills and a Custom GPT solve different packaging problems.

- Skills are reusable capabilities that ChatGPT can invoke when relevant.
- A Custom GPT provides a dedicated assistant surface with instructions, conversation starters and Knowledge.

Academic Colombia supports both. Installing the Skills does not automatically create the Custom GPT, and creating the Custom GPT does not automatically install the Skills.

The Custom GPT package is documented under `platforms/chatgpt-gpt/`.

## Updating Skills

When a new Academic Colombia version changes a Skill materially:

1. build the new ZIP from the canonical repo;
2. inspect the changed `SKILL.md`;
3. update/reinstall through the supported ChatGPT Skill management flow;
4. rerun the relevant acceptance/adversarial cases before relying on the new version for high-impact academic work.

## Security and trust

Do not install a package solely because its filename says Academic Colombia.

Verify:
- repository/release origin;
- Skill contents;
- version/provenance;
- any scripts or supporting files;
- external dependencies.

The canonical public source is the Academic Colombia repository.
