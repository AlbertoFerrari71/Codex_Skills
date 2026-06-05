# Demo Prompts

## Minimal Implementation Step

```text
Step: 120) Add focused validation
Branch: main
Scope: modify only validators/check_example.py and tests/test_check_example.py
Rules: no commit, no push, no PR, no destructive commands
Checks: python tests/test_check_example.py, git --no-pager diff --check
Final report: files changed, checks run, residual risks, next step
```

## Read-Only Review Step

```text
Step: 210) Repository readiness review
Scope: read-only
Rules: do not modify files, do not commit, do not push
Checks: branch, status, recent log, relevant docs, available tests
Final report: readiness, blockers, recommended next action
```
