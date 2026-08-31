# Repository Validation — Acceptance Cases

These cases validate repository consistency. They do not simulate academic reasoning quality.

## RV-01 Required root files
Remove a required core/governance file.
Expected: validator FAIL with the missing path.

## RV-02 VERSION format
Set `VERSION` to a non `x.y.z` value.
Expected: FAIL.

## RV-03 VERSION / CHANGELOG mismatch
Set `VERSION` to a value different from the first release heading in `CHANGELOG.md`.
Expected: FAIL.

## RV-04 Missing SKILL.md
Create a directory under `skills/` without `SKILL.md`.
Expected: FAIL.

## RV-05 Skill heading mismatch
Rename a skill directory without updating the first `# <skill-name>` heading.
Expected: FAIL.

## RV-06 Skill Contract marker
Remove `Skill Contract v1` from a native skill.
Expected: FAIL.

## RV-07 critical gate marker
Remove `critical_gate` semantics from a native skill.
Expected: FAIL.

## RV-08 Distribution manifest missing skill
Add a canonical skill but omit it from `distribution/SKILLS-MANIFEST.md`.
Expected: FAIL.

## RV-09 Stale distribution skill
Reference a nonexistent skill in the distribution manifest.
Expected: FAIL.

## RV-10 Broken relative Markdown link
Add a link to a nonexistent local file.
Expected: FAIL and report source document + target.

## RV-11 External URL
Add a valid external `https://` link.
Expected: structural validator does not attempt network validation and does not fail solely for that link.

## RV-12 Repository escape link
Add a relative link that resolves outside the repository root.
Expected: FAIL.

## RV-13 Registry taxonomy
Remove one canonical A–E class definition from `external-references/REGISTRY.md`.
Expected: FAIL.

## RV-14 Generated packages ignored
Remove `dist/` from `.gitignore`.
Expected: FAIL.

## RV-15 Packager missing
Remove `scripts/package_skills.py`.
Expected: FAIL.

## RV-16 Clean current repository
Run `python scripts/validate_repo.py` on a valid release branch.
Expected: PASS.

## RV-17 Package generation
Run `python scripts/package_skills.py` after repository validation.
Expected: individual packages and versioned bundle are generated under ignored `dist/`.

## RV-18 CI pull request
Open a PR containing valid changes.
Expected: `declarative-validation` workflow succeeds.

## RV-19 CI catches regression
Open a PR with one controlled validation failure.
Expected: status check fails and reports the reason.

## RV-20 Scope boundary
A behavior change may pass structural validation while still being academically wrong.
Expected: documentation states that CI does not replace academic acceptance, adversarial, E2E or runtime tests.
