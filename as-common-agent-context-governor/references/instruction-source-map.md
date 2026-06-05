# Instruction Source Map

Use this table to identify which sources are relevant before a Codex step starts.

| Source | Location example | Scope | Volatility | Typical use | Risk |
|---|---|---|---|---|---|
| ChatGPT custom instructions | Account-level settings | Broad assistant behavior | Medium | Baseline preferences | May be too broad for a repo. |
| ChatGPT project instructions | Project workspace | Project-level guidance | Medium | Project goals and stable rules | Can drift from repo state. |
| Codex global AGENTS.md | User or workspace config | Global Codex guidance | Low/medium | Cross-repo workflow rules | May conflict with repo-specific rules. |
| Repository AGENTS.md | `AGENTS.md` | Repo or subtree | Medium | Local rules, tests, safety | Can be stale after process changes. |
| README.md | `README.md` | Project overview | Medium | Setup and usage | Often incomplete for agent work. |
| docs/ | `docs/*.md` | Project details | Medium/high | Runbooks, decisions, roadmap | May contain outdated decisions. |
| SKILL.md | `as-common-*/SKILL.md` | Skill workflow | Low/medium | Reusable procedure | Can overlap another skill. |
| references/ | `skill/references/*.md` | Supporting detail | Low/medium | Deep rules and templates | Should not override the main task. |
| examples/ | `skill/examples/*.md` | Demonstrations | Low | Prompt and output examples | Examples may not match the current repo. |
| prompt Codex | Current task packet | Current step | High | Scope and constraints | Can omit important repo facts. |
| report Codex | Prior final report | Prior step | Medium | Evidence and handoff | May be incomplete or stale. |
| Git history | `git log`, `git show` | Version history | Medium | Confirm commits and sequencing | Commit messages can be vague. |
| issue/PR description | GitHub issue or PR | Work item | High | Acceptance criteria | May not include local constraints. |
| local runtime output | Tests, scripts, shell output | Current machine | High | Verification evidence | Output can depend on environment. |
| generated artifacts | Reports, indexes, build output | Generated state | High | Evidence and derived docs | Can be stale if not regenerated. |

## Source triage checklist

- Which source defines the current task?
- Which source defines safety and Git limits?
- Which source defines tests or verification gates?
- Which source is most recent?
- Which source is local to this repository?
- Which source is generated and needs refresh?
- Which facts are verified by commands?
- Which facts are assumptions?
- Which sources conflict or duplicate each other?
- Which skill, if any, should guide the work?
