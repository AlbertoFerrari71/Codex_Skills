---
name: as-common-agent-context-governor
description: Use this skill when reviewing, creating, or reconciling project instructions, AGENTS.md files, Codex prompts, skill usage, repository rules, handoff summaries, or context conflicts before starting or closing an agentic coding step.
---

# as-common-agent-context-governor

## Purpose

Govern the operational context for Alberto's ChatGPT and Codex work. Use it to prevent conflicts between instruction sources, repo rules, skill guidance, prompts, reports, PowerShell outputs, Git rules, tests, and verification gates.

## Use this skill when

- preparing a new Codex step;
- reviewing AGENTS.md;
- creating a project handoff;
- reconciling global and local instructions;
- diagnosing conflicting instructions;
- preparing a context map for a repo;
- deciding which skill should be used;
- cleaning project docs before an agent task.

## Workflow

1. Identify instruction sources.
2. Classify source authority.
3. Detect conflicts and duplication.
4. Decide the active instruction set.
5. Produce a context map.
6. Produce a handoff or correction prompt.
7. Record unresolved risks.

## Required outputs

- context map;
- conflict review;
- active instruction set;
- Codex-ready context summary;
- unresolved questions;
- next-step recommendation.

## Safety rules

- Never invent missing project facts.
- Do not silently override higher-authority instructions.
- Preserve safety, testing, and Git constraints.
- Flag ambiguity instead of guessing.
- Keep local/private paths and credentials out of public artifacts unless explicitly required and safe.

## References

- `references/context-governance-standard.md`
- `references/instruction-source-map.md`
- `references/agents-md-checklist.md`
- `references/skill-conflict-review.md`
- `references/context-handoff-template.md`

## Examples

- `examples/demo-prompts.md`
- `examples/sample-context-review.md`
