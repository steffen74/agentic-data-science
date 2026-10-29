---
name: model-card
description: Write a model card that documents a trained model for technical readers - intended use, data, evaluation, limits and how to reproduce.
disable-model-invocation: true
---

# Model card

Document a trained model in `MODEL_CARD.md`, following Mitchell et al., “Model Cards for Model Reporting” (2019). Read `CANVAS.md`, `DECISIONS.md`, `experiments/LOG.md` and the tracking records. Load `audience` (technical reader). Use only reviewed results; mark anything unknown as unknown.

## Sections

1. **Model details**: name, version, date, architecture, framework, authors, license; pretrained components with source and license.
2. **Intended use**: the decision it supports and its users (canvas blocks 1 and 3); explicitly out-of-scope uses.
3. **Data**: training, validation and test data (source, period, size, split method); preprocessing and data decisions (link `DECISIONS.md`); what is known about pretrained models’ training data.
4. **Evaluation**: metrics from the analysis plan, overall and per segment, next to the baseline; mean and spread across seeds; the test set used once.
5. **Limitations**: where the model is unreliable (segments, conditions, periods it has never seen); what the data cannot support.
6. **Ethical and practical considerations**: who could be affected by errors, and how; anything sensitive in the data.
7. **How to reproduce**: environment, the one command, expected runtime and hardware, where outputs land.

Show the draft to the user. Done when every section is filled or marked unknown and the user has approved the card.
