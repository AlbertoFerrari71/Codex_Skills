# .github/copilot-instructions.md - Template

Use this file only when the project benefits from repository-wide Copilot or VS Code custom instructions.

```markdown
# Copilot Instructions

This repository is `[NOME_PROGETTO]`.

## Project Context

[Short project purpose and main stack.]

## Coding Style

- Prefer simple, maintainable code over clever abstractions.
- Follow existing project patterns before introducing new ones.
- Keep changes scoped to the requested files and behavior.
- Do not add dependencies unless the task explicitly requires them.

## Safety

- Do not suggest destructive Git commands.
- Do not include secrets, tokens, passwords, private keys, certificates or `.env` contents.
- Do not modify generated/runtime outputs unless the task asks for it.

## Tests

- Prefer existing test commands and verification scripts.
- When changing behavior, update or add focused tests.
- If a check cannot run, state that explicitly in the final note.

## Project-Specific Rules

- [REGOLA_1]
- [REGOLA_2]
- [REGOLA_3]
```
