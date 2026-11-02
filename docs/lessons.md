# Learn it in seven lessons

Prompts are used once; a process can be repeated. These seven lessons walk through one process in the order you would run it on a real project. Each lesson is **one skill and one small exercise**, and ends with a self-check question and a one-line takeaway.

Plan about one to two hours per lesson. Do them in order: each lesson’s output is the next lesson’s input.

| Lesson | Skill | The failure it prevents |
|---|---|---|
| 1. Start with the canvas | `/setup-ds-project` | An analysis that serves no decision |
| 2. Sharpen the question | `/grill-question` | A precise answer to a fuzzy question |
| 3. Let the agent find the facts | `/explore-data` | Judgement calls hidden in code |
| 4. Agree on checks before code | `/to-analysis-plan` | Results nobody can verify |
| 5. Build the end-to-end baseline | `/to-experiments`, `/implement-experiment` | A model with nothing to beat |
| 6. Distrust your best result | `/review-results`, `diagnose-surprise` | A leak that looks like progress |
| 7. Close the loop | `/to-memo`, `/ds-retro` | A result nobody acts on |

---

## Lesson 1: Start with the canvas

**The failure it prevents.** “We have sales data, let’s predict sales.” The agent will happily do it, and the result will be a number that nobody needed in that form. Most analyses fail before the first line of code: nobody wrote down which decision they are meant to support.

**Skill:** `/setup-ds-project`

**Install the skills first.** In Claude Code: `claude plugin marketplace add steffen74/agentic-data-science`, then `claude plugin install agentic-data-science@agentic-data-science`. With any other agent (Copilot, Cursor, Codex and others; Node.js 22.20 or newer): `npx skills@latest add steffen74/agentic-data-science`. Everything after this assumes the skills are installed.

**Choose your path.** Work on a project of your own, or use the [bike-sharing example](../examples/bike-sharing/): public data and a canvas filled up to the planning stage. Its README says how to set up a repository and download the data. The example canvas is a reference answer for lessons 1–4; from lesson 5 on, you continue on the same data without one.

**When to skip.** Never entirely. Even a one-off question deserves block 1 (Decision) and block 2 (Questions), filled in by hand in five minutes.

**Exercise**
1. Run `/setup-ds-project` in your project repository and accept or adjust its recommendations.
2. Print the [canvas](../canvas/agentic-data-science-canvas.pdf). In ten minutes, by hand, fill in block 1 and as much else as you can.
3. Mark every block you could not fill.

**Self-check.** You have a dataset and a deadline. Which canvas block do you fill in first?
- A. Block 5, Data: you already know what you have.
- B. Block 1, Decision: who will act on the result, and how.
- C. Block 9, Experiments: time is short, so start modelling.

<details><summary>Answer</summary>

**B.** The decision determines which questions matter, which errors are costly and which data is legitimate. Starting from the data or the model gives you answers looking for a question.
</details>

**Takeaway:** a blank block is a decision nobody has made yet.

---

## Lesson 2: Sharpen the question

**The failure it prevents.** Hand an agent a vague question and it will answer it precisely: a clean chart, a significant test, a confident sentence. The precision hides that the question was never pinned down: sales in units or revenue, per branch or total, compared with what?

**Skill:** `/grill-question`

**When to skip.** When blocks 1–4 are already sharp and agreed, for example because someone else ran the interview. Never skip it because the question “seems obvious”; those are the ones that wobble.

**Exercise**
1. Run `/grill-question` with your question typed after the command, for example `/grill-question Should we open on Sundays?`. Answer one round at a time.
2. Disagree with at least one of the agent’s recommended answers, and say why.
3. For every question in block 2, write down one thing your data **cannot** answer.

**Self-check.** During `/grill-question`, which of these should the agent do itself rather than ask you?
- A. Look up the date range covered by the data.
- B. Choose the success metric.
- C. Decide which question matters most.

<details><summary>Answer</summary>

**A.** Facts that can be looked up are the agent’s job. Choosing a metric and prioritising questions are trade-offs, and trade-offs belong to the people who answer for the result.
</details>

**Takeaway:** facts are the agent’s job; decisions are yours.

---

## Lesson 3: Let the agent find the facts

**The failure it prevents.** Every analysis contains judgement calls: how to join, what to do with missing values, which periods to drop. When an agent makes them silently inside the code, nobody knows they were made, and nobody can question them.

**Skill:** `/explore-data`

**When talking is not enough.** Sometimes the interview reaches a question no one can answer by discussion: is the pattern even visible? Is there enough data in that segment? Answer it with a quick look: one throwaway plot or table, no checks, deleted afterwards. Write the answer into the canvas, not the code.

**When to skip.** When the data has not changed since the last profile. Re-run it whenever a source is added.

**Exercise**
1. Before running the skill, write down three guesses: how many rows, which column has the most missing values, which period is covered.
2. Run `/explore-data` and compare its numbers with your guesses.
3. Decide every open data decision it lists, and confirm which proposed checks to keep.

**Self-check.** `/explore-data` reports that a weather code is missing on a quarter of all days, mostly on sunny ones. What happens next?
- A. The agent fills the gaps with the most frequent code and moves on.
- B. You drop the column; missing data is unreliable.
- C. You decide how to treat it, based on the evidence, and log the decision.

<details><summary>Answer</summary>

**C.** Missingness that depends on the weather is information, not noise. Whether it becomes its own category, gets imputed or is dropped is a judgement call with consequences, so a person makes it and it goes into `DECISIONS.md`.
</details>

**Takeaway:** every judgement call about the data gets an owner and a log entry.

---

## Lesson 4: Agree on checks before code

**The failure it prevents.** Analysis code rarely fails loudly. A join that duplicates rows or a split that leaks the future runs without errors and produces plausible numbers. Reading every line of generated code does not scale, and looking only at the final metric is not enough.

**Skill:** `/to-analysis-plan` (with the reference skills `data-checks` and `leakage`)

**When to skip.** For a one-off descriptive question (one table, one test), a written plan is overkill: write the two or three checks that matter directly and run them. Write the plan as soon as there is more than one experiment.

**Exercise**
1. Run `/to-analysis-plan` and stop at the checkpoint confirmation.
2. For each check, name its source of truth: something the pipeline does not compute itself.
3. Find one check that would pass by construction and replace it.

**Self-check.** When should the checkpoints be agreed?
- A. After the first results, when you know what to look for.
- B. Only when something breaks.
- C. Before any code is written.

<details><summary>Answer</summary>

**C.** Checks written after seeing results tend to confirm them. Agreed in advance, they describe what correct means independently of what the code happened to produce.
</details>

**Takeaway:** decide how you will know it is right before anything is built.

---

## Lesson 5: Build the end-to-end baseline

**The failure it prevents.** Weeks go into a sophisticated model, and only at the end does anyone compare it with “same as last week”, or discover that the prediction file has the wrong IDs. Without a working pipeline and a baseline, there is nothing to measure progress against.

**Skills:** `/to-experiments`, then `/implement-experiment`

**When to skip.** Never skip the end-to-end baseline. You may skip `/to-experiments` when only one or two experiments are planned; write those cards by hand.

**On the bike-sharing example,** the reference canvas ends here: block 9 lists the planned cards, and the results are yours.

**Exercise**
1. Run `/to-experiments`. Check that card 1 is the end-to-end baseline: raw data → checks → baseline → evaluation → final output.
2. Run `/implement-experiment` on card 1. Watch the new checks go red before they go green.
3. Read the log entry it writes. Could someone else reproduce the result from it?

**Self-check.** What is experiment card 1?
- A. A complete pipeline from raw data to an evaluated simple baseline.
- B. The most promising model, so you get a good result early.
- C. Data cleaning, so the later models start from clean data.

<details><summary>Answer</summary>

**A.** Narrow but complete. Every later card changes one thing in a pipeline that already works end to end, and every later model has a number to beat.
</details>

**Takeaway:** start narrow, but go end to end.

---

## Lesson 6: Distrust your best result

**The failure it prevents.** The validation error drops sharply after a small change. It feels like progress and gets submitted. Often it is leakage: a feature that is only known afterwards, a shuffled time series, a scaler fitted on all the data. Fixing the number without fixing the process means the next run trips over the same thing.

**Skills:** `/review-results`, `diagnose-surprise`

**When to skip.** Never skip the review before a result is reported. `diagnose-surprise` is only needed when something looks too good, too bad or inconsistent.

**Exercise**
1. On a copy of your branch, plant a leak: shuffle a time series before splitting, or add a feature that is only known afterwards. Run the next experiment.
2. Run `/review-results`. Did it catch the leak? If the result looked too good, did `diagnose-surprise` find the cause?
3. Turn whatever caught it, or would have caught it, into a permanent check. Back on your real branch, implement and review the next card.

**Self-check.** After adding one feature, the validation error drops from 22 % to 6 %. What do you do?
- A. Submit it; this is the improvement you were looking for.
- B. Tune the model further to see how low it can go.
- C. Treat it as a bug until proven otherwise and test for leakage first.

<details><summary>Answer</summary>

**C.** Improvements that large from a small change are rare; leaks are common. Build a check that goes red on the surprise, test the leakage hypotheses one by one, and keep the check afterwards.
</details>

**Takeaway:** a surprising result is a bug until proven otherwise, and every surprise becomes a check.

---

## Lesson 7: Close the loop

**The failure it prevents.** The analysis is correct, the repository is tidy, and nothing changes, because the result never reached the person who decides in a form they can act on. And the next project repeats the same mistakes, because nobody wrote down what went wrong.

**Skills:** `/to-memo`, then `/ds-retro`

**When to skip.** Never skip the memo for results someone has to act on. The retro can be short, but run it after every milestone.

**Exercise**
1. Run `/to-memo` and write a decision memo for the decision-maker in block 3.
2. Give it to someone who has not seen the project. Ask what they would do. Does it match your recommendation?
3. Run `/ds-retro` and adopt the one or two changes that would have saved you the most time.

**Self-check.** Your memo is accurate, but the reader does not know what to do. What is missing?
- A. A recommendation, with the conditions under which it holds and its limits.
- B. More numbers and a more detailed chart.
- C. A more sophisticated model.

<details><summary>Answer</summary>

**A.** A decision-maker needs the answer first, a recommendation, and an honest sense of where it does not hold. More detail adds reading time, not clarity.
</details>

**Takeaway:** a result counts when someone can act on it.

---

## The full loop

You now have the pieces. Run the whole loop once on a real but small question, small enough that you can inspect every result:

1. `/setup-ds-project` once per project; the canvas before anything else.
2. `/grill-question` while the question is fuzzy.
3. `/explore-data` for the facts, and a quick look when talking is not enough.
4. `/to-analysis-plan` to agree on checks before code.
5. `/to-experiments` and `/implement-experiment`, end-to-end baseline first.
6. `/review-results` for every result; `diagnose-surprise` when one surprises you.
7. `/to-memo` for the decision-maker, `/ds-retro` for the next run.

When you are done you should have more than an answer: a canvas that explains it, checks that protect it, and a process that runs better next time.

## Bonus: neural networks

Training a neural network? Before trusting the first result, work through `debug-training` step by step, and agree a compute budget and tuning protocol with `training-protocol`. Document the final model with `/model-card`. See [deep-learning.md](deep-learning.md).
