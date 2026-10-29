---
name: data-checks
description: Rules for check-first data analysis - what a good check is, where checkpoints go, and the anti-patterns. Use when writing or reviewing checks, assertions or tests for data pipelines, analyses or models.
---

# Data checks

Analysis code rarely fails loudly. A **check** is an automated assertion that must hold before a result counts. Checks replace reading every line of generated code: they make correctness observable.

## What a good check is

A good check compares the pipeline’s state with an **independent source of truth**: something the pipeline did not compute.

| Source of truth | Example check |
|---|---|
| The raw file | Row count after loading equals the line count of the source file |
| A key definition | Exactly one row per date and product after every merge |
| A calendar | Every date of the period present once; no dates outside it |
| A submission template | Prediction IDs equal the template’s IDs, same order, no missing values |
| The split definition | Latest training date is earlier than the earliest validation date |
| Domain bounds | Temperature between −30 and 45 °C; sales non-negative |
| A known result | Baseline metric on validation equals the value recorded when it was first computed |

## Checkpoints

Checks live at **checkpoints**, the boundaries between pipeline stages:

1. **Load**: shape, columns, types, row count vs. source.
2. **Merge**: row count unchanged (for left joins), keys unique, match rate as expected.
3. **Features**: no feature uses information beyond the leakage boundary; no unexpected missing values introduced.
4. **Split**: disjoint, ordered by time or group as planned, sizes as expected.
5. **Predictions**: IDs and count match, no missing values, values in plausible range.
6. **Metrics**: computed on the intended data; baseline reproduces.

Agree the checkpoints with the user before writing checks. Not every checkpoint needs every check; the critical paths do.

## Rules of the loop

- **Red before green.** Write the check, see it fail for the right reason (or pass on a state you know is correct), then rely on it.
- **One checkpoint at a time.** Add checks where you are working, not everywhere at once.
- **Fix the data, not the check.** A failing check is changed only with the user’s agreement and a logged reason.
- **Keep the surprises.** Every bug found by hand becomes a permanent check.

## Anti-patterns

- **Tautological**: the expected value is computed the same way as the result (`assert len(df) == len(df)`, a mean compared with itself). It passes by construction.
- **Loosened to pass**: tolerances widened or conditions removed until green.
- **Output-only**: only the final metric is checked, so an upstream error that happens to help the metric survives.
- **Test-set peeking**: any decision taken while looking at test results.

## Implementation

Prefer `pytest` tests under `checks/` that load the pipeline’s intermediate outputs, run with one command. In notebook-only projects, an `assert` cell at each checkpoint with a clear message is the fallback.
