# Sample Context Review

Project: AI Software Factory

Step: 050

Repository: Codex_Skills

## Instruction Sources

| Source | Status | Notes |
|---|---|---|
| Current user request | Active | Defines step 050 and required files. |
| Repository AGENTS.md | Active | Defines naming, structure, safety, and workflow. |
| Validator output | Active evidence | Confirms skill catalog health before edits. |
| SKILL.md files | Relevant | Existing skill authoring rules guide naming and structure. |
| CHANGELOG.md | Relevant | Needs a new 050 section. |
| docs/roadmap.md | Relevant | Needs next strategic skill order. |

## Conflicts

| Conflict ID | Severity | Source A | Source B | Conflict | Decision | Action |
|---|---|---|---|---|---|---|
| C-001 | note | Current request | Existing roadmap | Roadmap lists the new skill as future work. | Current step activates it. | Mark 050 completed and keep 060/070 as next items. |

## Active Constraints

- Do not commit, push, or create a PR.
- Create one new common skill with `references/` and `examples/`.
- Keep `SKILL.md` compact.
- Use validator and regenerate catalog files.
- Preserve existing skill names and content outside required updates.

## Open Questions

- None blocking in this sample.

## Next Step

060) Verification Gate Test Eval Pack Skill.

Objective: create a strategic skill for tests, smoke checks, verification gates, evals, and golden samples.
