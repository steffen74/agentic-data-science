# Changelog

## Unreleased

- New skill `/show-canvas`: renders `CANVAS.md` as an HTML page laid out like the printed canvas (`scripts/render_canvas.py`, standard library only). Empty blocks are marked as not decided or not drafted; with `DECISIONS.md`, each block shows its decisions and those newer than the canvas version. `live` re-renders on every change. The same script as in Agentic Course Creation.

## 0.2.1 (2026-11-05)

- `audience`: the action-title example now comes from the bike-sharing example project instead of a bakery weekday analysis, so it no longer hands a course exercise its answer.

## 0.2.0 (2026-11-02)

- `grill-question`: grills the question typed after the command, and only that one; asks for it when none is given. When the canvas already holds a different decision, it asks whether to replace it or park it under Open questions. It now names the number of independent cases a comparison rests on (seasons, stores, years) as a limit, and keeps the known-in-advance probe short for one-off decisions.
- `setup-ds-project`: ends by suggesting a first commit of the new files.
- `to-experiments`: card 1 is now called the “end-to-end baseline” instead of the “tracer bullet”; the card itself is unchanged.
- Documentation: a learning path in seven lessons (`docs/lessons.md`), and instructions for working through it on the bike-sharing example.

## 0.1.0 (2026-10-30)

First public draft.

- Agentic Data Science Canvas: eleven blocks with human/agent ownership, Markdown template and printable version.
- Core skills: `setup-ds-project`, `ask-ds`, `grill-question`, `explore-data`, `to-analysis-plan`, `to-experiments`, `implement-experiment`, `review-results`, `diagnose-surprise`, `to-memo`, `tidy-notebooks`, `ds-retro`; reference skills `data-checks`, `leakage`, `audience`.
- Deep learning extension: `debug-training`, `training-protocol`, `model-card`.
- Documentation: principles, process, deep learning; worked planning example.
