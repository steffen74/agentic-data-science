---
name: show-canvas
description: Show the project canvas as a page in the browser, laid out like the printed canvas, with empty blocks and decisions newer than the canvas marked. Add "live" to keep it updating while you work.
disable-model-invocation: true
---

# Show canvas

Render `CANVAS.md` as one HTML page with [`scripts/render_canvas.py`](scripts/render_canvas.py). The same script renders the `COURSE-CANVAS.md` of Agentic Course Creation; it needs only the canvas grammar (`## Section` columns between `---` rules, `### N. Block 👤|🤖` blocks).

## 1. Render

Run the script on `CANVAS.md` at the root of the project (the `## Agentic data science` section of `AGENTS.md` names it if it lives elsewhere):

```
python3 <skill dir>/scripts/render_canvas.py CANVAS.md --out build/canvas.html
```

It reads `DECISIONS.md` next to the canvas when it exists (`--decisions <file>` otherwise). If `build/` is not in `.gitignore`, say so and offer to add it: the page is a view, the canvas stays the source.

With **live** after the command, add `--watch` and start it as a background process: it re-renders whenever the canvas or the decision log changes, and the open page reloads itself every few seconds. Tell the user how to stop it.

Done when the page exists and the user has its path (or it is open in a browser pane, if your agent has one).

## 2. Point out what the page shows

In at most three lines, from the page's own markers:

- **Empty blocks** (dashed, “Not decided yet” / “Not drafted yet”), by number. An empty 👤 block is a decision nobody has made yet; recommend the skill that fills it, as `/ask-ds` would.
- **Decisions newer than the canvas** (from the *Version* date): the blocks they touch may be out of date. Offer to update those blocks; the team approves each change.
- **Open questions** without an owner.

Do not change the canvas in this skill without a yes.
