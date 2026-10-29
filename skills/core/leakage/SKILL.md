---
name: leakage
description: Rules against data leakage - the known-in-advance boundary, time series and group splits, preprocessing, tuning and the test set. Use when creating features, splitting data, preprocessing, tuning, or when a result looks too good.
---

# Leakage

**Leakage** is any path by which information that would not be available at the moment of prediction reaches the model or the evaluation. It produces results that look better than they will be in use. It rarely causes errors.

## The boundary

Canvas block 6 (**known in advance**) defines what is available at the moment the result is needed. Every feature must lie inside it. When a feature’s availability is unclear, ask the user; do not decide.

Typical violations:
- Same-day or future values of other variables (same-day sales of other products, observed instead of forecast weather).
- Aggregates that include the target period (monthly totals, rolling means not shifted).
- Identifiers that encode the outcome (a status set after the event).

## Splits

- **Time series**: split by time; training strictly before validation strictly before test. Never shuffle across the boundary. Lag and rolling features are computed from the past only (`shift` before `rolling`).
- **Groups**: when several rows belong to one entity (a customer, a patient, a store, near-duplicate images or texts), keep each entity in one split.
- The split is decided before any modelling and recorded in `DECISIONS.md`.

## Preprocessing

Fit every learned transformation on training data only, then apply it to validation and test: scaling, imputation, encodings (especially target encoding), feature selection, dimensionality reduction. Fitting on all data leaks the distribution of the evaluation data.

## Tuning and the test set

- Tune on validation data. Many tuning rounds overfit the validation set; keep the search budget fixed in advance.
- The test set is used **once**, for the final estimate. A decision taken after looking at test results turns it into validation data.

## Red flags

A sudden large improvement; validation better than training; a model far better than a strong baseline; near-perfect predictions on a noisy target. Load `diagnose-surprise`.
