---
name: to-analysis-plan
description: "Turn the canvas and the current conversation into a written analysis plan with agreed checkpoints, and publish it to the tracker: no interview, just synthesis."
disable-model-invocation: true
---

# To analysis plan

Synthesize what is already decided into a plan. Do not interview; if something essential is undecided, list it under **Open questions** and stop at step 2. Read `CANVAS.md`, `DECISIONS.md` and `GLOSSARY.md`, and use the glossary’s terms throughout. Tracker details are in the `## Agentic data science` section of `AGENTS.md`; if it is missing, tell the user to run `/setup-ds-project`.

## 1. Sketch the checkpoints

Load the `data-checks` skill. List the **checkpoints** (load, merge, features, split, predictions, metrics) and, for each, the checks with their independent source of truth.

## 2. Confirm the checkpoints

Show the checkpoints to the user and ask whether they match their expectations. No plan is published with unconfirmed checkpoints.

## 3. Write and publish the plan

Use the template below. Publish it as one issue labelled `analysis-plan` (or `issues/plan-<slug>.md` locally). Update canvas blocks 4, 6, 7 and 8 with links to the plan.

<plan-template>

## Decision and questions
From canvas blocks 1–2, in two or three sentences.

## Hypotheses
A numbered list. For each: the statement, the analysis that tests it, the expected direction, and the **decision rule** (what result would make us act, or drop it). Written before any result is seen.

## Target and unit
What is predicted or estimated, for which unit (row), at which moment.

## Data and known in advance
Sources, joins and data decisions (link `DECISIONS.md`). The leakage boundary from block 6.

## Split and evaluation
How data is split (by time, by group), which data is used for tuning, and that the test data is touched once.

## Baseline and success
The baseline, the metric(s), segments to report, and what counts as good enough (block 4).

## Checkpoints
The confirmed checkpoints and checks from step 2.

## Out of scope
What this plan deliberately does not cover.

## Open questions
Anything undecided, with who resolves it.

</plan-template>

Avoid code and file paths in the plan; they go stale. Done when the plan is published, linked from the canvas, and contains no unconfirmed checkpoint.
