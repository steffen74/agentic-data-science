---
name: to-experiments
description: Break an analysis plan into experiment cards, starting with a baseline tracer bullet, each with its decision rule and blocking edges, and publish them to the tracker.
disable-model-invocation: true
---

# To experiments

Break the analysis plan into **experiment cards** an agent can build one at a time. Read the plan (fetch it if the user passes a reference), `CANVAS.md` and `experiments/LOG.md`. When the project trains neural networks, also load the `training-protocol` skill.

## 1. Draft the cards

- **Card 1 is always the tracer bullet**: raw data → all checkpoints green → the baseline from the plan → evaluation on validation data → the final output format (prediction file, table or chart). Narrow but complete. Every later card builds on a working pipeline.
- Each later card changes **one thing** (a feature, a data decision, a model, a hyperparameter range) so its effect can be attributed.
- Each card fits in one fresh context window and is verifiable on its own.
- Give each card its **blocking edges**: the cards that must be done first.

## 2. Quiz the user

Present the cards as a numbered list. For each: title, hypothesis, what changes vs. the previous best, decision rule, blocked by. Ask:

- Is the granularity right (too coarse, too fine)?
- Is the order right? Which cards are worth the effort at all?
- Are the decision rules what you would actually act on?

When neural networks are trained, also agree the compute budget and tuning protocol here.

Iterate until the user approves.

## 3. Publish

One issue per card, blockers first, labelled `experiment` and `ready-for-agent` (or `issues/NN-<slug>.md` locally), using this template:

<card-template>

## Hypothesis
What we expect and why.

## Change
The one thing this card changes compared with the previous best.

## Decision rule
Adopt if … on validation data (e.g. MAPE at least 1 point lower than the current best, no segment worse by more than 2 points). Otherwise reject.

## Checks
Existing checks that must stay green; new checks this card adds.

## Blocked by
Card references, or “None (can start immediately)”.

</card-template>

Update block 9 of `CANVAS.md` with the list of cards. Done when every approved card is published and linked from the canvas.
