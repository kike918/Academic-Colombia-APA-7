# Repository Governance

## Canonical branch

`main` is the canonical source of truth.

Changes should reach `main` only through pull requests.

## Public access model

Because the repository is public:

- anyone may read and clone it;
- anyone may fork it;
- anyone may download and reuse it under the MIT License;
- external contributors should propose changes through forks/pull requests;
- write access should be granted only to trusted maintainers.

Public visibility does not itself grant push access to arbitrary GitHub users.

## Recommended GitHub ruleset for `main`

Create a branch ruleset targeting `main` with:

- Require a pull request before merging: ON
- Required approvals: 0 while there is a single maintainer; increase to 1 when a second reviewer exists
- Require conversation resolution before merging: ON
- Block force pushes: ON
- Block branch deletion: ON
- Require linear history: ON when squash/rebase workflow is used consistently
- Restrict direct updates / bypass: no routine bypass; emergency administrative bypass only if intentionally configured

Optional later gates:

- required status checks once CI exists;
- signed commits if the project adopts that policy;
- CODEOWNERS when multiple maintainers exist.

## Merge policy

Preferred merge method: squash.

Each merged PR should leave `main` in a coherent versioned state and update tests/version/changelog when the change materially affects behavior.

## Release discipline

- `VERSION` represents the current framework version.
- `CHANGELOG.md` records material behavior changes.
- Feature work happens on branches.
- Regression tests accompany important rules and workflows.

## Scope boundaries

Academic Colombia is a standalone academic framework. It may be referenced by personal knowledge systems or platform adapters, but should not depend on them to function.

Platform-specific GPT/Gem/Spark configuration belongs under `platforms/`; the academic core remains platform-neutral.
