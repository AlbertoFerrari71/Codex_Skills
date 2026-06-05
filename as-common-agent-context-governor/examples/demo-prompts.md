# Demo Prompts

## 1. Review repository context before a Codex step

User request:

```text
Review this repo context before step 120. Identify active instructions, conflicts, required checks, and anything that should block implementation.
```

Expected use of this skill:

- build an instruction source map;
- classify authority;
- flag missing or conflicting facts;
- produce a Codex-ready context summary.

Expected output:

- context map;
- conflict review;
- active constraints;
- open questions;
- next-step recommendation.

## 2. Create or improve AGENTS.md

User request:

```text
Create a compact AGENTS.md for this repository using the current README, docs, tests, and Git rules.
```

Expected use of this skill:

- use `references/agents-md-checklist.md`;
- keep the file short;
- move long procedural detail to docs if needed.

Expected output:

- proposed AGENTS.md content;
- assumptions;
- verification commands.

## 3. Resolve conflicting instructions

User request:

```text
The prompt says commit at the end, but AGENTS.md says no commit. Decide how Codex should proceed and explain the active rule set.
```

Expected use of this skill:

- create a conflict matrix;
- classify severity;
- prefer the stricter active Git constraint unless explicit approval exists.

Expected output:

- conflict ID;
- decision;
- action to take;
- residual risk.

## 4. Prepare a context handoff for a new chat

User request:

```text
Prepare a handoff so I can start a fresh chat without losing repo state, constraints, tests, and next step.
```

Expected use of this skill:

- use `references/context-handoff-template.md`;
- separate known facts, assumptions, and open questions;
- include a prompt seed.

Expected output:

- context handoff;
- files touched;
- verification status;
- next recommended step.

## 5. Decide which skill should be used for a task

User request:

```text
This task involves Git commands, docs, and a Codex prompt packet. Which skill should guide the work?
```

Expected use of this skill:

- map the task to candidate skills;
- choose the narrowest primary skill;
- note secondary skills only when they add a concrete procedure.

Expected output:

- selected skill;
- why it applies;
- non-selected skills and reason;
- active workflow.
