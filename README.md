# Agentic Data Science

A canvas, a process and a set of agent skills for doing data science with a coding agent, without handing over the judgement.

> Status: **v0.1, draft.** Developed for and tested in the course “Introduction to Data Science and Machine Learning” at [opencampus.sh](https://opencampus.sh). Expect changes after the first cohort.

## Why

Coding agents make writing analysis code cheap. What they do not make cheap is the part that decides whether an analysis is worth anything:

- asking a question that the data can actually answer,
- knowing which information is available at the moment a prediction is needed,
- checking that a merge, a split or a metric is correct, because analysis code rarely fails loudly,
- saying what a result means, and what it does not, to the people who have to act on it.

An agent left to guess produces plausible numbers. A leaking time series split or a join that duplicates rows runs without errors and often *improves* the score. Reading every line of generated code does not scale; looking at the final number is not enough.

This repository encodes a different habit: **the agent finds facts, the human makes decisions, and every result has to pass explicit checks before it counts.**

## The three parts

### 1. The canvas

The [Agentic Data Science Canvas](canvas/) is one page with eleven blocks plus a log. Each block has an owner:

- **Human decides**: decision, questions, audiences, success criteria, what is known in advance, data decisions, recommendation.
- **Agent drafts, human approves**: data inventory, checks, experiments, findings.

In a project the canvas lives as `CANVAS.md` in the repository. It is the shared state between the team and the agent: the skills read it and write to it. A printable version is in [`canvas/`](canvas/).

### 2. The process

```
question ──► data ──► plan ──► experiments ──► review ──► communication
   ▲                                │              │
   └──────── decision log ◄─────────┴── surprise ──┘
```

Each step ends at a **stop point** where a human decision is required. See [docs/process.md](docs/process.md) and the [principles](docs/principles.md) behind it.

### 3. The skills

Plain-text agent skills (`SKILL.md`) that run the process. They work with Claude Code, GitHub Copilot, Cursor, Codex and other agents that support skills.

**Core set**

| Skill | Use it to | Canvas blocks |
|---|---|---|
| `/setup-ds-project` | Set up a repository once: canvas, glossary, decision log, checks, experiment log | all |
| `/ask-ds` | Find out which skill fits your situation | – |
| `/grill-question` | Get interviewed until the decision, questions, audiences and success criteria are sharp | 1–4, 6 |
| `/explore-data` | Profile the data and surface the data decisions you need to make | 5, 7 |
| `/to-analysis-plan` | Turn the conversation into a written analysis plan with agreed checkpoints | 4, 6–8 |
| `/to-experiments` | Split the plan into experiment cards, starting with a baseline tracer bullet | 9 |
| `/implement-experiment` | Build one experiment check-first and log the result | 8, 9 |
| `/review-results` | Review a result on two axes: validity and question | 8–10 |
| `/diagnose-surprise` | Find out why a result is too good, too bad or does not add up | 8, 9 |
| `/to-memo` | Write for an audience: decision memo, README section, presentation storyline | 10, 11 |
| `/tidy-notebooks` | Turn exploratory notebooks into a reproducible pipeline without changing results | – |
| `/ds-retro` | After a milestone: turn mistakes into checks, glossary entries and rules | log |

Reference skills used by the others: `data-checks`, `leakage`, `audience`.

**Deep learning extension**

| Skill | Use it to |
|---|---|
| `debug-training` | Work through the sanity checks when a network does not learn as expected |
| `training-protocol` | Reference: seeds, repeated runs, tuning protocol, compute budget, experiment tracking |
| `/model-card` | Document a trained model for a technical audience |

See [docs/deep-learning.md](docs/deep-learning.md) for what changes when the model is a neural network.

## Install

The skills follow the same layout as [Matt Pocock's skills](https://github.com/mattpocock/skills), so the same installers work.

```bash
# Editable copies in your project (any agent; needs Node.js 22.20 or newer)
npx skills@latest add steffen74/agentic-data-science

# Claude Code plugin
claude plugin marketplace add steffen74/agentic-data-science
claude plugin install agentic-data-science@agentic-data-science
```

Then, once per project:

```
/setup-ds-project
```

## Quickstart

1. `/setup-ds-project`: creates `CANVAS.md`, `GLOSSARY.md`, `DECISIONS.md`, `checks/` and `experiments/LOG.md`.
2. `/grill-question`: answer the agent’s questions about the decision behind your project.
3. `/explore-data`: let the agent profile your data; decide the open data questions.
4. `/to-analysis-plan`, then `/to-experiments`: agree on checkpoints and the first experiments.
5. `/implement-experiment` per card; `/review-results` runs at the end of each.
6. `/to-memo` when you have something to say.

Unsure what comes next? `/ask-ds`.

## Works well with

The data science skills govern the question-and-evidence loop. For the code inside it (data loaders, training loops, packages), Matt Pocock’s engineering skills fit directly: `/tdd`, `/implement`, `/code-review`. For understanding what the agent built, his `/wait-what` and `/teach` are useful, especially in teaching.

## Credits and licenses

- Skills: [MIT](LICENSE). Several skills are adapted from [Matt Pocock’s skills](https://github.com/mattpocock/skills) (MIT); see [NOTICE.md](NOTICE.md).
- Canvas and documentation: [CC BY 4.0](LICENSE-docs.md).

Feedback and pull requests are welcome; see [CONTRIBUTING.md](CONTRIBUTING.md).
