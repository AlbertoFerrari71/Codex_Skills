# Skill Conflict Review

Use a conflict matrix when instructions, skills, docs, or reports point in different directions.

| Conflict ID | Severity | Source A | Source B | Conflict | Decision | Action |
|---|---|---|---|---|---|---|
| C-001 | high | Current prompt | AGENTS.md | Prompt allows commit, AGENTS.md forbids commit without explicit request. | Follow stricter Git rule unless user explicitly authorizes commit. | Report decision and continue without commit. |

## Severity

- blocker: cannot proceed without user input or a verified state change.
- high: can cause unsafe Git, data, deploy, or broad-scope action.
- medium: can change implementation direction or tests.
- low: can affect wording, docs, or minor workflow choices.
- note: worth recording, but not action-blocking.

## Examples

### Git main vs branch-only workflow

- Conflict: prompt says work on `main`, repo docs require feature branch.
- Decision: stop if branch rule is strict; otherwise report and ask for direction.

### Commit allowed vs no commit allowed

- Conflict: old prompt says commit, current prompt says no commit.
- Decision: current explicit task constraint wins; do not commit.

### Test required vs test skipped

- Conflict: repo docs require tests, task asks for docs-only work.
- Decision: run docs-relevant checks if available; explain skipped code tests.

### Local path mismatch

- Conflict: README path differs from current working directory.
- Decision: trust verified `pwd` for current execution; record README mismatch.

### Stale project state

- Conflict: report says branch is dirty, current `git status --short` is clean.
- Decision: trust current command output; mark prior report stale.

### Skill overlap

- Conflict: two skills appear relevant.
- Decision: choose the narrowest skill that covers the requested work; cite secondary skill only if it adds concrete procedure.
