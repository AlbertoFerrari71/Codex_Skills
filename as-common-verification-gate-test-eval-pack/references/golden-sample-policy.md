# Golden Sample Policy

Golden samples are approved reference outputs used to detect regressions in generated files, reports, UI snapshots, API payloads, or AI workflow artifacts.

Use them when stable output shape matters and manual review alone is too easy to miss. Do not use them when the output is intentionally creative, highly variable, or better checked by a smaller structural assertion.

## Golden Sample vs Fixture

- Fixture: input or setup data used to run a test.
- Golden sample: expected output used to compare a result.

## Versioning

- Store golden samples in the repository only when they are small and non-sensitive.
- Keep a note explaining how each sample is generated.
- Review diffs before accepting new samples.
- Regenerate only with explicit approval or a documented reason.
- Avoid exact comparisons when headings, schema, or key fields are enough.

## Golden sample checklist

- The sample is small enough to review.
- It contains no private data.
- It represents a real workflow.
- The comparison method is documented.
- The approval path for updates is clear.
- The sample is not so rigid that harmless wording changes fail.
- The final report notes whether golden samples passed, failed, or were not run.

## Recommended folder names

- `tests/golden/`
- `tests/fixtures/`
- `examples/golden/`
- `docs/golden-samples/`

## Change Documentation

When a golden sample changes, record:

- why it changed;
- which behavior changed;
- which command regenerated it;
- who approved or requested the update;
- whether the change is a regression fix or an intentional baseline update.
