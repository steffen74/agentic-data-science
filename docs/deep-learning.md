# Deep learning

A neural network is a method, not a different kind of task. The decision, the questions, the audiences and the limits stay the same, and so do most skills. What changes is where effort and risk sit.

## What changes

1. **Training runs are expensive and noisy.** The same configuration gives different results with different seeds, and a run can take hours. One score proves little: compare configurations over several seeds and within a compute budget the human sets.
2. **Hyperparameter search overfits the validation set.** After many tuning runs the best validation score is optimistic. Fix the search space, budget and stopping rule in advance, tune on validation only, and touch the test set once.
3. **Failures are quieter.** A network can train without errors and learn little: wrong normalization, misaligned labels, a learning rate slightly off. Debugging follows a fixed sequence of sanity checks (inspired by Andrej Karpathy’s “A Recipe for Training Neural Networks”).
4. **Pretrained models raise data questions.** What were they trained on, could that overlap with your test data, and what does the license allow?
5. **Unstructured data needs other split rules.** Near-duplicate images or texts, or several samples from the same person, must not be spread across training and test data.
6. **More of the work is software engineering.** Data loaders, training loops and configuration are ordinary code; Matt Pocock’s `/tdd`, `/implement` and `/code-review` fit them directly.

## Canvas additions

| Block | Addition |
|---|---|
| 5 Data | Pretrained models and their training data and license; label quality |
| 8 Checks | Training sanity checks; split checks for near-duplicates and groups |
| 9 Experiments | Seeds, repeated runs, compute budget, tuning protocol, tracking |
| 10 Findings | Variance across seeds, not just the best run |

## Extension skills

- `debug-training`: the sanity-check sequence, one step at a time, each with a pass criterion.
- `training-protocol`: reference for seeds, repeated runs, tuning protocol, budgets and tracking. `/to-experiments` and `/implement-experiment` load it when the project trains neural networks.
- `/model-card`: documents a trained model for a technical audience, following Mitchell et al., “Model Cards for Model Reporting” (2019).
