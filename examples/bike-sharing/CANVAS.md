# Agentic Data Science Canvas

**Project:** Bike availability for the morning peak
**Team:** (example)
**Version:** planning stage

> Owners: 👤 human decides · 🤖 agent drafts, human approves.

---

## Problem

### 1. Decision 👤
Every evening at 18:00 the operations lead decides how many bikes the night shift moves into the city centre for the next morning (07:00–10:00). Today she uses the same number every weekday and adjusts by feel for rain. Moving too few leaves stations empty; moving too many costs staff time and leaves bikes idle.

### 2. Questions 👤
1. How many rentals should we expect between 07:00 and 10:00 tomorrow?
2. How much do weekday, season, holidays and weather change the morning peak?
3. How much better is a forecast than the current fixed number?

Cannot be answered from this data: demand per station (the data is system-wide), demand that was lost because no bike was available (only completed rentals are recorded), and anything after 2012.

### 3. Audiences 👤
- Operations lead: a one-page memo with the forecast logic and when to trust it; later, one number per evening.
- Data team: repository with README, checks and a model card.

### 4. Success 👤
Metric: mean absolute error of the 07:00–10:00 total, in rentals. Baselines to beat: (a) the current fixed number, (b) the same weekday one week earlier. Underestimating is worse than overestimating (empty stations at peak), so errors are also reported separately by direction. Segments: working days vs. weekends/holidays; seasons.

---

## Data and method

### 5. Data 🤖
Hourly rental counts with date, hour, season, holiday and working-day flags, weather situation, temperature, humidity and wind speed, 2011–2012; split into casual and registered users. Some hours are missing (hours without data); see `docs/data-fact-sheet.md`. Weather values are normalised in the source; units documented in `GLOSSARY.md`.

### 6. Known in advance 👤
At 18:00 the day before: calendar (date, weekday, holiday, season), all rentals up to 18:00, and the **weather forecast** for the next morning. Observed weather of the next morning is *not* known; using it in modelling overstates accuracy. Decision: use observed weather as a stand-in for the forecast in this project and state this as a limit, or add noise to approximate forecast error (see `DECISIONS.md`).

### 7. Data decisions 👤
- Target: sum of rentals 07:00–10:00 per day (casual + registered).
- Missing hours: the source does not say whether a missing hour means no rentals or a missing record. Decision: treat them as missing, flag days with missing morning hours and exclude those days from evaluation.
- Weather situation encoded as categories; temperature kept numeric.
- Split by time: 2011 and the first half of 2012 for training, Q3 2012 for validation, Q4 2012 for test.

### 8. Checks 🤖
- Load: row count equals the source file; one row per date and hour.
- Target: one target value per date; every date of 2011–2012 present once.
- Features: no feature uses information after 18:00 of the previous day (except the documented weather stand-in).
- Split: latest training date before earliest validation date; validation before test.
- Metrics: both baselines reproduce their recorded values.

---

## Evidence and action

### 9. Experiments 🤖
Planned cards: (1) tracer bullet with both baselines; (2) linear model with calendar features; (3) add weather; (4) add yesterday’s rentals; (5) gradient-boosted trees. Each card’s decision rule: adopt if validation MAE improves by at least 5 % without a worse working-day segment.

### 10. Findings 🤖
(After experiments: answers to questions 1–3, error by segment and direction, the effect of using observed instead of forecast weather, limits.)

### 11. Recommendation 👤
(After review: what number to move each evening, how to adjust it, and when not to rely on it, e.g. special events the data has never seen.)

---

## Open questions
- Does the operations team have historical weather forecasts? (operations lead)
