# Context Handoff Template

Use this template when closing a chat, preparing a new Codex step, or transferring context between agents.

````markdown
# Context Handoff

## Project

Name:

## Current Goal

Goal:

## Repository/Path

Repository:
Local path:

## Branch

Branch:

## Last Known Commits

- `<commit>` `<message>`

## Completed Steps

- Step:
- Result:

## Active Constraints

- Git:
- Files:
- Tests:
- Safety:

## Relevant Skills

- Skill:
- Why relevant:

## Known Facts

- Fact:

## Assumptions

- Assumption:

## Open Questions

- Question:

## Files Touched

- File:

## Verification Status

- Command:
- Result:

## Next Recommended Step

Step:
Objective:

## Prompt Seed

Use this as the starting prompt for the next agentic coding step:

```text
Project:
Repository/path:
Branch:
Step:
Objective:
Current state:
Allowed changes:
Forbidden changes:
Required checks:
Final report:
```
````
