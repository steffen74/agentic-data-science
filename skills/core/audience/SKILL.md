---
name: audience
description: Rules for communicating data science results to decision-makers and technical readers - action titles, answer first, uncertainty and limits in plain words. Use when writing memos, chart titles, README sections, presentations or model documentation.
---

# Audience

Every result is written for a named reader from canvas block 3. Before writing, state who it is and what they already know.

## Decision-maker

- **Answer first.** The first sentence answers the question; details follow.
- **Action titles.** Every chart and section title states the conclusion as a sentence (“Weekends sell a quarter more, mostly rolls and croissants”), not the topic (“Sales by weekday”).
- **Few numbers.** At most three per message, rounded, with unit and comparison (vs. baseline, vs. last year, vs. today).
- **Uncertainty in plain words.** “In 8 of 10 weeks the forecast was within 15 %” instead of standard errors; say what the uncertainty means for the decision.
- **Association, not cause.** “Sales are higher on warm days” unless the analysis was designed to show cause.
- **Limits are part of the answer.** Say what the data cannot tell and under which conditions the recommendation does not hold.
- **Recommend, with conditions.** What to do, starting when, under which conditions; and where not to rely on the analysis.

## Technical reader

- How to reproduce everything with one command.
- What was decided and why (link `DECISIONS.md`), especially data decisions and the split.
- Results per segment, next to the baseline, with variance across runs where relevant.
- Known weaknesses and what you would try next.

## Charts

One message per chart. Label axes with units. Order categories meaningfully (weekdays Monday to Sunday, not alphabetically). Show uncertainty (confidence intervals, ranges) when comparisons are made. Prefer direct labels over legends.
