---
name: review-results
description: "Review an analysis result or experiment on two axes: Validity (checks, leakage, evaluation data, baseline, uncertainty) and Question (does it answer the canvas question for its audience, with honest limits?). Use after an experiment, before reporting a result, or when the user asks whether a result can be trusted."
---

# Review results

Two-axis review of a result. Run each axis as a separate sub-agent with a fresh context when your environment supports it, so one does not colour the other; otherwise run them one after the other. Then aggregate.

Inputs: the experiment card or claim under review, `CANVAS.md`, `DECISIONS.md`, `experiments/LOG.md`, the checks and the code that produced the result.

## Axis 1: Validity

Can the number be trusted? Load `data-checks` and `leakage`, then go through every item:

- **Checks**: all green? Does each meaningful check have an independent source of truth, or is any of them tautological?
- **Leakage**: does any feature violate canvas block 6? Was the split done by time or group as planned? Were scalers, imputers or encoders fitted on training data only?
- **Evaluation data**: computed on validation (or test, once)? Same rows and IDs as expected?
- **Baseline**: compared against the baseline and the previous best on the same data?
- **Uncertainty**: is the improvement larger than the noise (several seeds, confidence intervals, segment variation)?
- **Segments**: does a good overall number hide a segment that got worse?

## Axis 2: Question

Does the result serve the project? Load `audience`, then check:

- Does it answer a question from canvas block 2, or only produce a number?
- Was the card’s decision rule applied as written, without moving the goalposts?
- Are claims supported: association vs. cause, extrapolation beyond the data?
- Are the limits stated, including what the data cannot answer?
- Is it understandable for the audience in block 3?

## Report

Combine both axes into one list, each finding marked **blocking** (the result cannot be used as is) or **note**, with the evidence and a suggested fix. End with a recommendation: accept, redo, or drop.

The verdict is the user’s. Record it in `DECISIONS.md` and the log entry; update canvas block 10 only for accepted results.
