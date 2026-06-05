# 100 Skill Release Workflow Pack

## Purpose

This workflow makes skill releases in `Codex_Skills` repeatable, reviewable, and safe. Use it when creating a new skill, modifying an existing skill, applying a skill hotfix, or cleaning skill quality issues before publishing to `main`.

## When to use it

- New skill: create a new `as-common-*` or `as-<project-key>-*` folder.
- Skill modification: improve an existing skill without changing its identity.
- Skill hotfix: correct a narrow rule, template, or validator issue.
- Skill cleanup: archive backups, reduce warnings, align docs, or regenerate catalogs.

## Strategic skill sequence

1. `as-common-agent-context-governor`: map instructions, conflicts, repo state, and active constraints.
2. `as-common-verification-gate-test-eval-pack`: define mandatory checks, stop policy, and evidence.
3. `as-common-codex-report-intake-decision-gate`: compare final report claims with Git, diff, tests, and warning evidence.
4. `as-common-pwsh-command-pack`: use only when robust PowerShell command packs are needed.

## Release flow

1. Define the step name, objective, expected files, and publication policy.
2. Run preflight: branch, status, log, remote, validator tests, validator, catalog regeneration, and smoke script.
3. Perform context review and record conflicts or open questions.
4. Create or modify skill files with minimal scope.
5. Add or update `references/`, `examples/`, docs, templates, and changelog as needed.
6. Run validator and targeted smoke trial.
7. Regenerate `SKILLS_INDEX.md` and `SKILL_SCORE.md`.
8. Run final gate: tests, validator, smoke script, release checker, diff check, status, diff stat, and log.
9. Stage files and run `git --no-pager diff --cached --check`.
10. Commit and push only when all mandatory local gates pass.
11. Produce final report with files, tests, commit, push, risks, and next step.

## GO / NO-GO criteria

| Condition | Decision |
|---|---|
| Validator PASS, smoke PASS, diff checks PASS, expected files only | GO |
| LF/CRLF warning with exit code 0 | GO_WITH_WARNINGS |
| Missing catalog regeneration | NO_GO_FIXABLE |
| Missing smoke trial for a major skill change | GO_WITH_WARNINGS or NO_GO_FIXABLE by risk |
| Validator fail, staged diff fail, wrong branch, or failed mandatory test | NO_GO_BLOCKER |
| Scope or publication policy unclear | NEEDS_CLARIFICATION |

## Publication policy

Alberto decision D3-C applies: direct `git push origin main` is allowed when all local gates pass and the current step authorizes publication.

Branch plus PR is an alternative when:

- the repository is protected;
- Alberto explicitly requests review;
- the change is risky enough to need review before publication.
