---
name: to-memo
description: "Write results for an audience from the canvas: a decision memo, a README section for technical readers, or a presentation storyline. Always with limits; the recommendation is signed off by the team."
disable-model-invocation: true
---

# To memo

Write for one named audience from canvas block 3. Read `CANVAS.md` (blocks 1–3, 10, 11), `DECISIONS.md` and the accepted entries in `experiments/LOG.md`. Load the `audience` skill. Use only accepted results; if a result has not been through `/review-results`, say so and stop.

## 1. Pick audience and format

Ask the user which audience and format, recommending one:

- **Decision memo** for the decision-maker: half a page, answer first.
- **README section** for the technical reader: how to reproduce, what was decided, what the results are.
- **Presentation storyline** for a talk: one line per slide.

## 2. Draft

**Decision memo**
1. Action title: the conclusion as a full sentence.
2. The answer to the question from block 2, in plain words.
3. At most three numbers, rounded, with units and a comparison (vs. baseline, vs. today).
4. How sure we are, in plain words.
5. Limits, including what the data cannot tell.
6. Recommendation and the conditions under which it holds.

**README section**
Question and decision; data and data decisions (link `DECISIONS.md`); split, baseline and checks; results per segment; how to reproduce with one command; limits.

**Presentation storyline**
Question → answer → evidence (one chart per claim, each with an action title) → limits → recommendation. Mark which team member presents which part, if known.

## 3. Sign-off

Show the draft. The recommendation is a proposal until the user confirms it; only then write it into canvas block 11 and record the sign-off in `DECISIONS.md`.

Done when the user has approved the text and, for memos, the recommendation.
