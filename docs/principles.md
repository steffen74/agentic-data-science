# Principles

Eight habits the canvas and the skills encode. Each one answers a failure mode that coding agents make more likely, not less.

## 1. The agent finds facts, the human makes decisions

Anything that can be looked up (row counts, date ranges, missing values, the distribution of a variable) is the agent’s job. Anything that involves a trade-off (which question matters, which data is legitimate, which error is worse, what to recommend) is put to a human, with the agent’s recommendation, and waits for an answer. The canvas makes the split visible: purple blocks are decided by humans, teal blocks are drafted by the agent and approved.

## 2. The decision comes before the question, the question before the data

An analysis is only useful if someone can act on it. Start from the decision (who decides what, when, how often), derive the questions, and only then look at the data. For every question, write down what the data can *not* answer as well.

## 3. Checks come before results

Analysis code fails silently. Before a result counts, it passes explicit **checks** whose expected values come from an independent source: the row count of the source file, the IDs of a submission template, a calendar, a domain bound, a baseline. Checks are agreed with the human at **checkpoints** (after loading, merging, feature creation, splitting, prediction) before the code is written. This replaces reading every line of generated code.

## 4. Known in advance is a decision, not a detail

Every feature has to be available at the moment the prediction is needed. Where that boundary lies is decided by the human and written on the canvas; the agent enforces it. Most data leakage is a violation of this one rule.

## 5. Every model starts with a baseline

The first experiment is always a complete **tracer bullet**: from raw data through the checks to a simple baseline and its evaluation. Every later model has to beat it on validation data. A high R² does not mean a model beats “same as last week”.

## 6. Limits are part of the result

A finding without its limits is incomplete. “The data contains no sales before late October, so it cannot tell us whether an earlier start pays off” is a result, not an excuse.

## 7. Communication is a deliverable

Results are written for a named audience: a decision-maker who needs an answer, a recommendation and a sense of reliability, or a technical reader who needs to reproduce and extend the work. Both are deliverables in their own right.

## 8. The canvas is the shared state

The canvas, the glossary and the decision log live in the repository. The agent reads them at the start of every skill and updates them when something is decided. Nothing important lives only in a chat window.
