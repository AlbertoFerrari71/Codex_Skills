# Final Verification Report Template

Use this template for a final gate report.

```markdown
A. Step executed

B. Status

C. Branch

D. Files changed

E. Verification matrix

| Area | Check | Command | Expected | Result | Blocks publication |
|---|---|---|---|---|---|

F. Commands executed

G. Passed checks

H. Failed checks

I. Warnings

J. Not-run checks

K. Git status

L. Diff summary

M. Go / no-go decision

N. Risks / attention points

O. Next step

P. Final standard line

Step executed:
Status:
Next step:
```

## Synthetic Example

```markdown
A. Step executed

060) Verification gate update

B. Status

PASS_WITH_WARNINGS

C. Branch

main

D. Files changed

- `scripts/verify.ps1`
- `docs/verification.md`

E. Verification matrix

| Area | Check | Command | Expected | Result | Blocks publication |
|---|---|---|---|---|---|
| Tests | Unit tests | `python -m pytest` | Pass | Pass | Yes |
| Git | Diff check | `git --no-pager diff --check` | No errors | Pass with line-ending notice | Yes |

F. Commands executed

- `python -m pytest`
- `git --no-pager diff --check`
- `git status --short`

G. Passed checks

- Unit tests.
- Diff check.

H. Failed checks

- None.

I. Warnings

- Line-ending notice, non-blocking.

J. Not-run checks

- UI smoke: not relevant to docs-only change.

K. Git status

Expected modified files only.

L. Diff summary

Verification docs and script updated.

M. Go / no-go decision

GO for review. No publication action was performed.

N. Risks / attention points

Review generated script in the target shell before reuse.

O. Next step

Run the same gate after the next code change.

P. Final standard line

Step executed: 060
Status: PASS_WITH_WARNINGS
Next step: 070
```
