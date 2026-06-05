# 100 Skill Authoring Release Flow

Use this flow when creating a new skill.

## Naming convention

- Use lowercase.
- Use kebab-case.
- Do not use underscores.
- Do not use spaces.
- Do not use accented or non-ASCII characters.
- Use `as-common-*` for common skills.
- Use `as-<project-key>-*` for project-specific skills.

## Recommended structure

```text
as-common-<skill-name>/
  SKILL.md
  references/
    <standard>.md
  examples/
    demo-prompts.md
```

## `SKILL.md`

The frontmatter must include:

```markdown
---
name: as-common-<skill-name>
description: Use this skill when ...
---
```

The body should stay compact:

- purpose;
- when to use it;
- workflow;
- required outputs;
- safety rules;
- references;
- examples.

## Description

A useful description should:

- describe the trigger condition;
- include the domain or workflow;
- avoid generic wording;
- stay under the validator length limit;
- match the folder name in `name:`.

## References and examples

Use `references/` for standards, templates, decision matrices, and long operating rules.

Use `examples/` for demo prompts, sample reviews, sample reports, and expected outputs.

## Release target

Aim for:

- validator score 100 for strategic/common skills;
- `references/` present;
- `examples/` present;
- `SKILLS_INDEX.md` regenerated;
- `SKILL_SCORE.md` regenerated;
- changelog updated;
- smoke trial recorded for substantial skills.

## Publication

Commit and push direct to `main` only after validator, smoke trial, diff check, staged diff check, and status review pass.
