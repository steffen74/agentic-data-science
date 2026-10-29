---
name: debug-training
description: Sanity-check sequence for neural network training. Use when a network does not learn, learns suspiciously well, the loss behaves oddly (flat, exploding, NaN), or before trusting a first training result.
---

# Debug training

A network can train without errors and learn almost nothing useful. Work through the sequence below **in order**, one step at a time. Each step has a pass criterion; show the user the evidence and move on only when it passes. Inspired by Andrej Karpathy’s “A Recipe for Training Neural Networks”.

Load `training-protocol` for seeds and logging conventions, and `leakage` if a result looks too good.

## The sequence

1. **Fix the seed and the data.** Same seed, same data version, deterministic options where available. *Pass:* two runs give the same loss curve.
2. **Inspect a batch.** Print shapes and dtypes; show a few raw inputs next to their labels (decode images, texts, categories). *Pass:* inputs and labels belong together and look like the data you expect after preprocessing (normalised, correct encoding).
3. **Check the initial loss.** Before training, compare the loss with its expected value: for mean squared error on standardised targets about 1; for cross-entropy with k balanced classes about ln(k). *Pass:* within a small factor of the expected value.
4. **Beat a trivial baseline.** Compare with a predictor that ignores the input (mean, majority class, “same as last week”). *Pass:* you know the number the network has to beat.
5. **Overfit one small batch.** Train repeatedly on a handful of examples. *Pass:* training loss drops close to zero. If not, the model, the loss or the data pipeline is broken; do not tune anything yet.
6. **Train on the full training set without regularization.** *Pass:* training loss decreases clearly and ends below the baseline.
7. **Find a learning rate.** A coarse sweep over orders of magnitude, short runs. *Pass:* a range where loss decreases steadily without spikes or NaN.
8. **Watch training vs. validation.** Plot both curves. *Pass:* you can name the regime: underfitting (both high), overfitting (validation rises while training falls), or good fit.
9. **Only now regularise and tune**, following the tuning protocol in `training-protocol`.

## Common causes

- Labels shuffled separately from inputs, or misaligned after filtering.
- Normalisation statistics computed on all data, or not applied at prediction time.
- Wrong loss for the output (e.g. softmax applied twice, regression target not scaled back).
- Learning rate far off; exploding gradients (check gradient norms, add clipping).
- Data augmentation that destroys the signal.
- Train/eval mode not switched (dropout and batch normalisation behave differently).

Done when the step that failed passes for an understood reason, the fix is committed, and a check protecting it is added to `checks/` where possible.
