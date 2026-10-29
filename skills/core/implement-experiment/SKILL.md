---
name: implement-experiment
description: Build one experiment card check-first, evaluate it on validation data, log the result and hand it to review.
disable-model-invocation: true
---

# Implement an experiment

Build the card the user names. Read the card, the analysis plan, `CANVAS.md`, `DECISIONS.md` and the last entries of `experiments/LOG.md`. Load the `data-checks` and `leakage` skills; for neural networks also `training-protocol`.

## 1. Checks first

Write the card’s new checks before the code they protect, and run them: they must go **red** for the right reason. Existing checks must stay green throughout. A check is only changed with the user’s agreement, never loosened to make it pass.

## 2. Implement

Make the one change the card describes, nothing else. Follow the data decisions in `DECISIONS.md`; if the card seems to require a new data decision, stop and ask.

Run the check command regularly while you work and the full pipeline once at the end.

## 3. Evaluate

- On **validation data only**. The test data stays untouched unless the card is the final evaluation.
- Report the metric overall and for the segments named in the plan, next to the baseline and the previous best.
- Apply the card’s decision rule as written. If the result is surprisingly good, surprisingly bad or inconsistent, load `diagnose-surprise` before going on.

## 4. Log

Add an entry to `experiments/LOG.md` using its template, including the verdict and the commit. Update block 9 of `CANVAS.md`.

## 5. Review and commit

Run `/review-results` on the experiment. Commit with a message naming the card. Close or move the card according to the verdict.

Done when all checks are green, the log entry exists, the review has run, and the work is committed.
