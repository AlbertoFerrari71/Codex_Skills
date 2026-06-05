# Codex Command Pack Standard

Use this reference when preparing prompt packets, task packets, or handoffs for Alberto.

## Required Shape

Every pack should include:

- project or repository name;
- local path;
- expected branch;
- step number and title;
- objective;
- current context;
- files allowed to change;
- files not allowed to change;
- safety constraints;
- verification commands;
- final report format.

## Safety Baseline

Unless Alberto asks otherwise, every prompt must state:

- no commit;
- no push;
- no pull request;
- no deploy;
- no destructive commands;
- no credential or sensitive-value changes;
- stop if the branch or working tree is not as expected.

## Verification Baseline

Prefer commands that are easy to reproduce:

```powershell
git --no-pager branch --show-current
git status --short
git --no-pager log --oneline --max-count=5
git --no-pager diff --check
```

Add project-specific tests only when they are relevant to the requested change.

## Output Contract

The final Codex report should make clear:

- what step was executed;
- whether it completed or stopped;
- what files changed;
- what tests ran;
- what risks remain;
- what next step is recommended.
