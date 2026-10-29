---
name: setup-ds-project
description: "Set up a repository for the agentic data science skills: canvas, glossary, decision log, checks, experiment log and issue tracker. Run once per project before the other skills."
disable-model-invocation: true
---

# Setup a data science project

Scaffold the project files every other skill reads. This is prompt-driven, not a script: explore, present what you found, confirm, then write.

## 1. Explore

Read what exists; assume nothing:

- `git remote -v`: is this a GitHub repository?
- `AGENTS.md` / `CLAUDE.md`: is there already an `## Agentic data science` section?
- `CANVAS.md`, `GLOSSARY.md`, `DECISIONS.md`, `checks/`, `experiments/` at the root.
- Data files (`*.csv`, `*.parquet`, `*.xlsx`, `data/`) and notebooks (`*.ipynb`).
- The Python environment (`pyproject.toml`, `requirements.txt`, `environment.yml`) and whether `pytest` is available.

## 2. Present findings and ask

Summarise what is present and missing. Then take the sections in order, one answer each, leading with your recommendation so the user can accept it in a word. Skip a section when exploration already settled it.

- **A. Issue tracker.** Where analysis plans and experiment cards live. Recommend GitHub Issues when the remote is on GitHub (labels `analysis-plan`, `experiment`, `ready-for-agent`); otherwise local files under `issues/`.
- **B. Checks.** Recommend `pytest` tests under `checks/`, run with one command. If the team works only in notebooks, an `assert` cell per checkpoint is the fallback.
- **C. Project context.** Ask for the project name, team members and, in one sentence, the decision the project should support. Keep the rest for `/grill-question`.

## 3. Write

- Copy the templates in [`templates/`](templates/) to the repository root (`CANVAS.md`, `GLOSSARY.md`, `DECISIONS.md`) and to `experiments/LOG.md`. Never overwrite an existing file; report it instead.
- Fill the canvas header and put the one-sentence decision into block 1 as a draft.
- Create `checks/` with one trivial passing check that loads the main dataset, so the command works from day one.
- Add this section to `AGENTS.md` (create the file if needed):

```markdown
## Agentic data science

- Canvas: `CANVAS.md` (read before any analysis work; update when something is decided)
- Glossary: `GLOSSARY.md`; decisions: `DECISIONS.md`
- Checks: `checks/`, run with `<command>`; experiment log: `experiments/LOG.md`
- Tracker: <GitHub Issues with labels ... | local files under issues/>
- Data: <paths>. Raw data is read-only.
```

Done when every file exists, the check command passes, and the user has confirmed the `AGENTS.md` section. Suggest `/grill-question` as the next step.
