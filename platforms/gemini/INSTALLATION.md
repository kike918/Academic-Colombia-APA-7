# Install Academic Colombia as a Gemini Gem

## Prerequisites

Use an account where custom Gems and Knowledge files are available. Product availability can vary by account/workspace.

## 1. Create the Gem

In the Gemini web app:

1. Open Gems.
2. Create a new Gem.
3. Name it `Academic Colombia — APA 7 | UNAD | SENA` (or another clearly versioned name).
4. Paste `GEM_INSTRUCTIONS.md` into the instructions field.
5. Do not accept an automatic instruction rewrite without comparing it to the canonical file.

## 2. Add Knowledge

Use `KNOWLEDGE_MANIFEST.md`.

Preferred order:

1. Tier A core;
2. institution profile(s) needed;
3. APA/artifact modules;
4. native Skills;
5. external fallback docs only when required.

Gemini supports uploading files from the device and adding files from Google Drive.

### Snapshot installation

Upload files from a checked-out release/tag. This is easiest to reproduce exactly.

Record:

```text
Academic Colombia version: x.y.z
Install date: YYYY-MM-DD
Knowledge source: local snapshot
```

### Drive-backed installation

Use Drive when you want the Gem to reference an updateable file copy.

Rules:
- GitHub `main`/release remains canonical;
- sync changes from GitHub to Drive, not the opposite;
- avoid silent manual edits in Drive;
- keep version/provenance notes.

## 3. Keep activity-specific files outside permanent Knowledge

Upload the following per task/chat instead:

- assignment guide;
- rubric;
- student draft;
- local template;
- dataset;
- screenshots;
- evidence files.

## 4. Preview before relying on the Gem

Run a minimum acceptance set:

1. guide + rubric conflict;
2. request for fabricated reference;
3. UNAD vs SENA rule separation;
4. infographic vs long report;
5. existing DOCX audit request;
6. missing critical evidence;
7. quantitative claim requiring method;
8. false READY request.

Expected behavior is specified in `tests/GEMINI_ADAPTER_CASES.md`.

## 5. Knowledge citations

Gemini may cite Knowledge files depending on settings. Those citations are platform provenance, not automatically APA references for the academic artifact.

Never populate a student's references section with Academic Colombia internal framework files unless the activity genuinely requires citing the framework itself.

## 6. Updating the Gem

When the canonical repository changes:

- snapshot uploads: replace/update affected Knowledge files and rerun relevant tests;
- Drive-backed files: verify that the current version is reflected and rerun relevant tests;
- if Instructions changed materially, update them manually from the canonical adapter.

## 7. Runtime validation status

Repository readiness does not prove runtime behavior. A Gem version is considered validated only after the relevant acceptance and cross-platform cases are run on the actual Gem.
