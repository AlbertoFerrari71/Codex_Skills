# Context Governance Standard

Context governance is the practice of making the active instruction set explicit before an agentic coding step starts or closes. It keeps project facts, repository rules, skill guidance, prompts, reports, and runtime evidence aligned.

This matters in ChatGPT + Codex projects because work often crosses several sources: custom instructions, project instructions, AGENTS.md files, README files, docs, skills, step prompts, command output, and prior reports. Without a short governance pass, stale or lower-authority guidance can steer the work incorrectly.

## Source Types

- Global instructions: broad behavior and safety rules that apply across workspaces.
- Project instructions: project-scoped rules, goals, and preferences.
- Repository instructions: local repo rules, usually in AGENTS.md or project docs.
- AGENTS.md: operational guidance for Codex inside a folder tree.
- Skill instructions: reusable playbooks for a narrow recurring task.
- Step prompt: the current task packet and its explicit constraints.
- Codex report: evidence of what was done, verified, or left open.
- PowerShell output: local execution evidence, including Git state, tests, and generated artifacts.

## Recommended authority order

This table is a repo and prompt governance aid. Runtime platform and session instructions remain above local project artifacts.

| Level | Source | Typical scope | Notes |
|---:|---|---|---|
| 1 | Current user request | Current turn or step | Most direct task intent, unless it asks for an unsafe or impossible action. |
| 2 | Project or repository AGENTS.md | Folder tree or repository | Governs local workflow, safety, tests, and file boundaries. |
| 3 | Current Codex step prompt | Current implementation step | Defines files, constraints, and required checks for the active task. |
| 4 | Relevant skill SKILL.md | Reusable task workflow | Applies when the task matches the skill trigger. |
| 5 | Skill references/examples | Supporting detail | Use when needed; do not let examples override direct instructions. |
| 6 | README.md and docs/ | Project knowledge | Good for setup, architecture, and conventions. Check for staleness. |
| 7 | Git history and reports | Evidence and history | Useful for facts, but may be stale or incomplete. |
| 8 | Generated artifacts and runtime output | Local evidence | Use for verification; do not treat generated text as policy by default. |

## Conflict Handling

When two sources conflict:

1. Identify both sources and quote or summarize the conflicting point.
2. Classify severity: blocker, high, medium, low, or note.
3. Prefer the higher-authority and more recent applicable source.
4. Preserve safety, Git, test, and verification constraints.
5. If the decision is unclear, stop and ask or report the ambiguity.

## Missing Information

Never invent missing facts. Mark each gap as:

- known missing;
- assumed for this step;
- open question;
- requires user decision.

Use assumptions only when they are low-risk, reversible, and clearly stated.

## Long Context

If context is too long:

- keep constraints and safety rules first;
- keep current step scope;
- keep files and commands that affect the task;
- summarize older reports;
- drop duplicated narrative;
- preserve unresolved risks.

## Codex Prompt Inclusion

Include only what Codex needs to execute safely:

- objective and current state;
- repository path and branch;
- allowed and forbidden files;
- active constraints;
- relevant skill names;
- tests and verification gates;
- expected final report.

## Known Facts / Assumptions / Open Questions

Use this compact split:

```text
Known facts:
- Verified facts with source or command.

Assumptions:
- Low-risk working assumptions, clearly marked.

Open questions:
- Decisions or missing facts that can change the work.
```
