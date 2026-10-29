# The process

The process follows the canvas from left to right, but it is a loop: experiments change the questions, surprises change the checks, and every decision is logged.

## Main flow

| Step | Skill | Agent does | Stop point (human decides) | Canvas |
|---|---|---|---|---|
| 1. Sharpen the question | `/grill-question` | Asks questions in rounds, recommends answers, looks up facts itself | Decision, questions, audiences, success criteria, what is known in advance | 1–4, 6 |
| 2. Understand the data | `/explore-data` | Profiles every dataset, proposes checks for facts that must stay true | Each open data decision (e.g. impute or treat as category) | 5, 7 |
| 3. Plan | `/to-analysis-plan` | Writes the plan from the conversation | The checkpoints where checks go | 4, 6–8 |
| 4. Slice | `/to-experiments` | Splits the plan into experiment cards, baseline first | Granularity and order of the cards | 9 |
| 5. Build | `/implement-experiment` | Writes checks first, implements, evaluates on validation data, logs | – | 8, 9 |
| 6. Review | `/review-results` | Reviews validity and fit to the question | Accept, redo or drop | 8–10 |
| 7. Communicate | `/to-memo` | Drafts memo, README section or storyline | The recommendation | 10, 11 |
| 8. Improve | `/ds-retro` | Proposes new checks, glossary entries, rules | Which to adopt | log |

Steps 4–6 repeat for every experiment card.

## On-ramps

- **A result surprises you**: too good, too bad, a sudden jump, a model worse than the baseline. `/diagnose-surprise` builds a check that goes red on the surprise and tests explanations one by one, leakage first.
- **Existing notebooks**: start with `/setup-ds-project`, then `/explore-data`, then `/grill-question`. The canvas will expose what was never decided.
- **Before handing in or publishing**: `/tidy-notebooks` turns the exploratory notebooks into a pipeline and checks that results are unchanged.

## Files in a project

| File | Content | Written by |
|---|---|---|
| `CANVAS.md` | The canvas | all skills |
| `GLOSSARY.md` | Variables, units, codes, domain terms | `/grill-question`, `/explore-data` |
| `DECISIONS.md` | Dated decisions with reason and alternatives | all skills at stop points |
| `checks/` | Automated checks (e.g. pytest) | `/implement-experiment`, `/diagnose-surprise` |
| `experiments/LOG.md` | One entry per experiment run | `/implement-experiment` |
| Issue tracker | Analysis plan and experiment cards | `/to-analysis-plan`, `/to-experiments` |

`/setup-ds-project` records the locations in a short section of `AGENTS.md`, so every skill finds them.
