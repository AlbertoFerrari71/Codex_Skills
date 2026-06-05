# 100 Skill Modification Release Flow

Use this flow when changing an existing skill.

## Impact check

- Identify which behavior changes.
- Identify whether the trigger `description:` changes.
- Identify affected references, examples, templates, docs, and validators.
- Confirm the change does not break existing expected use.

## Keep compatibility

- Do not rename skill folders in ordinary modification steps.
- Do not change `name:` unless renaming is explicitly in scope.
- Keep `SKILL.md` compact.
- Move long changes into `references/` or `examples/`.
- Preserve existing safety, testing, and Git constraints.

## Description and trigger

Only change `description:` when:

- the old trigger is misleading;
- the skill's real use changed;
- trigger optimization is the explicit goal.

After changing it, run targeted smoke checks for activation clarity.

## References and examples

- Update references when rules change.
- Update examples when expected outputs change.
- Add a new example for every significant new workflow.
- Keep old behavior documented if users still rely on it.

## Changelog and catalog

- Add the current step to `CHANGELOG.md`.
- Regenerate `SKILLS_INDEX.md`.
- Regenerate `SKILL_SCORE.md`.
- Confirm score does not regress unexpectedly.

## Smoke trial

Run a smoke trial when:

- behavior changes;
- a safety rule changes;
- command templates change;
- validator or publication workflow changes.

## Hotfix criteria

Create a hotfix step when:

- a documented rule is wrong;
- a command template is unsafe;
- validator output is misleading;
- publication guidance conflicts with Alberto's current policy.

Hotfixes should be narrow, verified, committed, and pushed only after local gates pass.
