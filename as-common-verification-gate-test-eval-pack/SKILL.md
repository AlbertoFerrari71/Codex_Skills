---
name: as-common-verification-gate-test-eval-pack
description: Use this skill when designing, reviewing, or enforcing tests, smoke checks, health checks, evals, golden samples, verification gates, stop policies, or go/no-go release decisions for Codex-driven software and documentation steps.
---

# as-common-verification-gate-test-eval-pack

## Purpose

Build and apply clear, repeatable verification gates for Codex-driven software and documentation work. Use this skill to decide which checks must run, what blocks publication, and how evidence should be reported.

## Use this skill when

- preparing a Codex step that changes code, tests, docs, scripts, or workflows;
- deciding which tests must run before commit or push;
- creating a `scripts/verify.ps1`;
- defining smoke tests or health checks;
- creating golden samples;
- designing evals for AI/Codex workflows;
- reviewing a Codex report before publication;
- deciding GO / NO-GO;
- documenting failure and corrective action.

## Workflow

1. Identify the change type and risk.
2. Define the verification matrix.
3. Select mandatory checks.
4. Add smoke / health checks.
5. Add golden samples or evals when useful.
6. Define stop conditions.
7. Run verification in a fixed order.
8. Report evidence, gaps, and go/no-go decision.

## Required outputs

- verification matrix;
- mandatory command list;
- expected results;
- stop policy;
- test/eval coverage notes;
- golden sample notes;
- final verification report;
- next-step recommendation.

## Safety rules

- Never publish if mandatory tests fail.
- Never claim a test passed if it was not executed.
- Distinguish errors, warnings, and not-run checks.
- Preserve Git status, diff, and log evidence.
- Avoid destructive test commands unless explicitly approved.
- Keep credentials and private data out of test fixtures.
- Keep verification commands reproducible.

## References

- `references/verification-gate-standard.md`
- `references/test-matrix-template.md`
- `references/eval-pack-standard.md`
- `references/golden-sample-policy.md`
- `references/failure-stop-policy.md`
- `references/final-verification-report-template.md`

## Examples

- `examples/demo-prompts.md`
- `examples/sample-verification-gate.md`
