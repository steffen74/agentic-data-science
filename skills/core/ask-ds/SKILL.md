---
name: ask-ds
description: Ask which data science skill fits your situation. A router over the skills in this repo.
disable-model-invocation: true
---

# Ask DS

Read `CANVAS.md` (and the `## Agentic data science` section of `AGENTS.md`). If either is missing, the answer is `/setup-ds-project`.

Then recommend **one** next skill, with one sentence on why, based on the first gap you find:

| If … | Recommend |
|---|---|
| Blocks 1–4 or 6 are empty or vague | `/grill-question` |
| Block 5 is empty, or new data was added | `/explore-data` |
| Questions are sharp but there is no written plan with checkpoints | `/to-analysis-plan` |
| A plan exists but no experiment cards | `/to-experiments` |
| A card is `ready-for-agent` | `/implement-experiment` (one card per fresh session) |
| A result looks too good, too bad or inconsistent | `diagnose-surprise` |
| A result exists but has not been reviewed | `/review-results` |
| Findings exist but the audiences have not received anything | `/to-memo` |
| The project is about to be handed in or published | `/tidy-notebooks` |
| A milestone just ended | `/ds-retro` |
| The model is a neural network that does not learn as expected | `debug-training` |
| A trained model needs documenting | `/model-card` |

If the user describes a situation instead, map it to the table. When two rows apply, recommend the earlier one: an unclear question makes every later step wasted work.
