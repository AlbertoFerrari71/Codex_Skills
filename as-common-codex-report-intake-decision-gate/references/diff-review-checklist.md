# Diff Review Checklist

Use this checklist to compare the report with actual Git evidence.

| Check | Why it matters | Command / evidence | Decision impact |
|---|---|---|---|
| Expected files | Confirms scope was respected. | `git status --short`, original prompt. | Unexpected changes can become NO_GO_FIXABLE. |
| Unexpected files | Finds edits not mentioned in report. | `git --no-pager diff --name-status` | Can block GO until explained. |
| Generated files | Ensures generated catalogs/indexes are intentional. | Diff and generation command. | Missing regeneration can be NO_GO_FIXABLE. |
| Deleted files | Detects destructive scope changes. | Name-status with `D`. | Usually NO_GO_BLOCKER unless approved. |
| Renamed files | Confirms intended moves. | Name-status with `R`. | Needs explanation and path check. |
| Large diffs | Highlights review burden and accidental scope. | `git --no-pager diff --stat` | May require targeted review. |
| Binary files | Prevents opaque changes. | `git --no-pager diff --name-status` | Needs explicit reason. |
| Sensitive values or credentials | Avoids committing private material. | Targeted diff review. | NO_GO_BLOCKER if found. |
| Line ending noise | Separates noise from real content changes. | `git --no-pager diff --check` | Non-blocking only when command passes. |
| Docs-only changes | Confirms no code changed unexpectedly. | Name-status and diff stat. | Code edits need explanation. |
| Test coverage | Confirms verification matches risk. | Commands and outputs. | Missing mandatory tests block GO. |
| Changelog update | Keeps step history current. | Diff on `CHANGELOG.md`. | Missing update can be fixable. |
| Catalog/index regeneration | Keeps generated state aligned. | Validator/generator command and diff. | Missing update can be fixable. |
| Validator output | Confirms repo-specific quality gate. | Validator command. | Failure blocks GO. |
| Migration/schema changes | Detects high-impact changes. | Diff and migration files. | Needs stronger evidence. |
| Config changes | Detects runtime behavior changes. | Targeted diff. | Needs explicit review. |

## Useful Commands

```powershell
git status --short
git --no-pager diff --stat
git --no-pager diff --check
git --no-pager diff --name-status
git --no-pager diff -- <file>
git --no-pager log --oneline --max-count=5
```
