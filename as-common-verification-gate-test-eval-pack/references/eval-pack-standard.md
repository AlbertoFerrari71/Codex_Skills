# Eval Pack Standard

An eval is a repeatable assessment of AI or Codex workflow output. It checks whether the produced answer, report, classification, or generated artifact behaves as expected for representative cases.

Software tests usually check deterministic code behavior. AI workflow evals check output quality, completeness, safety, formatting, and decision logic. They can be manual, automatic, or mixed.

## When To Use Evals

Use evals when a workflow produces:

- Codex prompts;
- final Codex reports;
- operational summaries;
- generated documents;
- risk classifications;
- delicate email drafts;
- technical analysis.

## Designing A Small Eval Pack

1. Choose representative cases, not edge cases only.
2. Keep the initial dataset small enough to maintain.
3. Define expected behavior in plain language.
4. Decide pass criteria before running the eval.
5. Record grading method: manual, checklist, script, or hybrid.
6. Track regressions across changes.
7. Update cases only with an explicit note explaining why.

## Eval Matrix

| Eval item | Input | Expected behavior | Pass criteria | Grading method | Notes |
|---|---|---|---|---|---|
| Codex prompt | Step request with constraints | Produces scoped, safe task packet | Includes branch, files, checks, report format | Manual checklist | Use real project style without sensitive data. |
| Final Codex report | Tool outputs and diff summary | Reports files, tests, risks, and next step | No unsupported claims | Manual checklist | Mark not-run checks clearly. |
| Operational summary | Long chat context | Separates facts, assumptions, and open questions | Handoff is usable in new chat | Manual review | Keep prompt seed compact. |
| Document generation | Short source notes | Produces structured doc with limits | Required sections present | Checklist or script | Compare headings, not exact wording. |
| Risk classification | Mixed warning examples | Classifies blocker/high/medium/low/note | Matches policy table | Manual or scripted | Keep severity definitions stable. |
| Delicate email | Customer-facing request | Draft is clear and safe | Tone and facts are controlled | Manual review | Avoid invented facts. |
| Technical analysis | Process or code description | Identifies assumptions and evidence gaps | Recommendations are traceable | Manual review | Cite source files or commands. |

## Regression Measurement

Track:

- pass/fail count;
- recurring failure category;
- changed expected behavior;
- cases added or retired;
- reason for any accepted warning.

## Avoiding Overfitting

Do not tune prompts only to exact sample wording. Prefer behavior criteria, multiple compact cases, and periodic review of whether cases still represent real work.
