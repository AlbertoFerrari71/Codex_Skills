# AGENTS.md Checklist

Use this checklist when creating or reviewing an AGENTS.md file.

## Review Points

- Repository purpose: one short paragraph about what the repo is for.
- Setup commands: only commands that are known and useful.
- Test commands: focused tests, full tests, and smoke checks when available.
- Build commands: local build or packaging steps, if relevant.
- Coding style: conventions that differ from defaults.
- Branch/Git rules: expected branch, commit rules, push rules, PR rules.
- Forbidden actions: destructive commands, deploys, broad refactors, or out-of-scope writes.
- Safety constraints: data handling, credential handling, external-state limits.
- Generated files policy: which outputs are committed, ignored, or regenerated.
- Environment assumptions: OS, runtime, launcher, path quirks.
- Handoff/report format: required final report structure.
- How to keep it short: move long examples to docs or skill references.

## Minimal AGENTS.md Skeleton

```markdown
# AGENTS.md

## Scope

This file applies to the whole repository.

## Repository Purpose

Short description of the project and its main workflow.

## Commands

- Test: `...`
- Build: `...`
- Verify: `...`

## Rules

- Do not commit, push, deploy, or create PRs unless explicitly requested.
- Keep changes scoped to the requested files.
- Preserve existing user changes.
- Use local project conventions.

## Safety

- Do not write credential values into tracked files.
- Report ambiguity instead of guessing.

## Final Report

Include files changed, commands run, results, risks, and next step.
```
