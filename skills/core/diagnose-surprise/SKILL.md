---
name: diagnose-surprise
description: Diagnosis loop for surprising analysis results. Use when a result is too good to be true, worse than the baseline, jumps unexpectedly between runs, or numbers do not add up (row counts, totals, IDs).
---

# Diagnose a surprise

A surprising result is a bug until proven otherwise. Read `CANVAS.md`, `DECISIONS.md` and the recent log entries first.

## Phase 1: Reproduce

Re-run the exact configuration (same data, code, seed). If the surprise disappears, it is noise or state: fix the seed, restart from a clean kernel or process, and compare again.

## Phase 2: Build a feedback loop

This is the core of the skill. Write a check that goes **red** on this surprise: a row count that should be N, an ID set that should match, a metric that should not beat a known ceiling, a prediction that should equal the baseline under a trivial configuration. Spend disproportionate effort here; with a tight red signal, the cause will be found.

## Phase 3: Hypotheses, one at a time

Rank explanations by likelihood and test each with the loop, one at a time.

**Too good**: usually leakage. Load the `leakage` skill and check, in order:
1. A feature that is only known after the moment of prediction (block 6).
2. Random instead of time- or group-based split; overlapping periods.
3. Preprocessing fitted on all data instead of training data.
4. Target information inside a feature (totals, ratios, lags with the wrong sign).
5. Evaluation on training data.

**Too bad or inconsistent**: usually misalignment. Check:
1. Joins that duplicate or drop rows.
2. Row order lost between features and labels; sorting.
3. Units, scales, time zones, date parsing.
4. Wrong target column or sign of a shift.
5. Missing values handled differently in training and prediction.

## Phase 4: Fix and protect

Fix the cause, keep the red check as a permanent check in `checks/`, re-run the experiment, and log the episode in `experiments/LOG.md` (what looked wrong, what it was).

Done when the original check passes for the right reason and the user agrees with the explanation. If no hypothesis survives, report what was ruled out and ask the user how to proceed.
