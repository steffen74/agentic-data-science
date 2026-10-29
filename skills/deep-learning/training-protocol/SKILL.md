---
name: training-protocol
description: Reference for trustworthy neural network experiments - seeds and repeated runs, compute budget, tuning protocol, early stopping, experiment tracking and pretrained models. Use when planning, running or comparing training runs.
---

# Training protocol

Training runs are expensive and noisy. These rules make results comparable and claims defensible.

## Seeds and repeated runs

- Set and log the seed of every source of randomness (framework, NumPy, Python, data loader).
- Before claiming that configuration A beats B, run each with **at least three seeds** and report mean and spread. An improvement smaller than the spread is not an improvement.
- Report the spread in findings, not only the best run.

## Compute budget (human decision)

Before tuning starts, the user sets the budget: number of runs, maximum time or GPU hours. Record it on the experiment card. Stop when the budget is spent, and report the best result within budget.

## Tuning protocol (fixed in advance)

1. Search space: which hyperparameters, which ranges, on which scale (learning rate on a log scale).
2. Method: grid, random or Bayesian search, with the budget above.
3. Selection: by the validation metric from the analysis plan, averaged over seeds for the finalists.
4. Stopping rule: early stopping on validation loss with a fixed patience.
5. Final estimate: retrain the selected configuration as planned and evaluate on the test set **once**.

Record every run, not only the best: tuning many configurations and reporting the best one overstates performance.

## Tracking

Each run logs: date, card, commit, data version, full configuration, seed, metrics per epoch (training and validation), final metrics per segment, runtime. Use a tracking tool (e.g. MLflow, Weights & Biases) or a CSV next to `experiments/LOG.md`. Summarise in the log only runs that change a decision.

## Pretrained models

Record the model name and version, its source, its license, and what is known about its training data. Ask whether that data could overlap with the evaluation data (e.g. public benchmark images); if so, evaluate on data the model cannot have seen. Freezing and fine-tuning choices are data decisions for `DECISIONS.md`.
