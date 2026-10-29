---
name: grill-question
description: Interview the team until the decision, questions, audiences, success criteria and leakage boundary of a data science project are sharp. Writes the canvas, glossary and decision log as answers come in.
disable-model-invocation: true
---

# Grill the question

Interview the user relentlessly about the decision behind the project until blocks 1–4 and 6 of `CANVAS.md` are sharp. Read `CANVAS.md`, `GLOSSARY.md` and `DECISIONS.md` first; never re-ask what is already decided.

## How to interview

Map the open points as a **decision tree**: the decision (block 1) gates the questions (2); the questions gate audiences (3), success criteria (4) and what is known in advance (6).

Work in **rounds**. The **frontier** is every point whose prerequisites are settled. Ask the whole frontier in one round, number each question, and give your recommended answer:

```
❓ **Q1** - **<title>**: <question, with options where useful>

➡️ <your recommended answer, and why>
```

Wait for the answers, write them down (below), recompute the frontier, and ask the next round.

**Facts are your job; decisions are the user’s.** When a question needs a fact (date range, which products exist, how often a value is missing), look it up in the data or repository yourself. Never ask the user for something you can find.

## What to probe

- **Decision**: who decides what, when, how often, how far ahead. What happens today.
- **Questions**: for each, what would the answer look like, and **what the data cannot answer**. Check this against the data: if the data never covers the relevant condition, say so.
- **Audiences**: the decision-maker and the technical reader at minimum; format for each.
- **Success**: the metric, the baseline to beat, which errors cost more, which segments matter.
- **Known in advance**: the moment the result is needed and what information exists then. Load the `leakage` skill for the rules.

Sharpen fuzzy terms as they come up (“sales” in units or revenue? per branch or total?) and invent concrete scenarios that force a precise answer.

## Write as you go

- Each settled answer goes into its canvas block immediately, in a few lines.
- Each term with a precise meaning goes into `GLOSSARY.md`.
- Each choice between alternatives goes into `DECISIONS.md` with reason and alternatives.
- Anything left open goes to **Open questions** on the canvas, with who resolves it.

Done when the frontier is empty: blocks 1–4 and 6 each hold a settled answer or an explicit open question, nothing silently assumed. Show the updated blocks and ask the user to confirm before suggesting `/explore-data`.
