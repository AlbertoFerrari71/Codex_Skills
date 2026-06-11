# AGENTS.md - Template

```markdown
# AGENTS.md

Scope: entire repository unless a nested AGENTS.md overrides this file.

## Project Goal

[Describe the project in 2-5 lines.]

## Roles

- Alberto decides strategy, scope changes, publication and irreversible actions.
- ChatGPT plans, reviews, clarifies tradeoffs and prepares prompts or docs.
- Codex works locally on scoped tasks, edits only authorized files and reports evidence.

## Operating Rules

- Work in Italian unless requested otherwise.
- Keep changes small, explicit, testable and documented.
- Read relevant README/docs before editing files.
- Do not silently expand scope.
- If a step is read-only, do not write files.
- If a step is document-only, do not implement code.
- If a task is fix-only, do not publish in the same step.

## Git Rules

- Before edits, check branch and `git status --short`.
- Use `git --no-pager` for long output.
- Do not commit, push, open PRs, merge, tag, deploy, reset, clean, rebase, force push or run destructive checkout unless Alberto explicitly authorizes it.
- Treat LF/CRLF warnings as warnings when tests and `git diff --check` pass.

## Verification

- Run the checks that match the change.
- Prefer the repository's existing verification commands.
- Never claim a test passed if it was not executed.
- If a required check fails, fix within scope or stop and report the blocker.

## Security

- Do not store secrets, tokens, passwords, private keys, certificates or `.env` files.
- Do not print sensitive values in logs or reports.
- Do not modify external repositories or systems unless explicitly requested.

## Final Report

Every implementation step must report:

- step executed;
- final status;
- branch;
- files created or modified;
- checks run and result;
- warnings;
- residual risks;
- next recommended step.
```
