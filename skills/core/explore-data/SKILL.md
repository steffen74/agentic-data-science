---
name: explore-data
description: Profile the project's datasets, write the data inventory into the canvas and surface every data decision the team has to make. No modelling.
disable-model-invocation: true
---

# Explore the data

Build a factual picture of the data and hand every judgement call to the user. Read `CANVAS.md` (especially blocks 2 and 6) and `GLOSSARY.md` first. Raw data is read-only.

## 1. Profile every dataset

For each source, establish and record:

- **Shape and grain**: rows, columns, what one row is (one day? one product per day?).
- **Keys**: candidate keys and whether they are unique. Duplicated keys are a finding.
- **Time coverage**: first and last date, missing dates, incomplete periods at the edges.
- **Types and ranges**: per column; values outside plausible bounds.
- **Missing values**: count per column, and whether missingness relates to other columns or to time (compare rows with and without the value). Missingness that depends on something is a finding.
- **Joins**: for every planned join, the share of keys that match on each side and whether the join would change the row count.
- **Origin and license**, if known.

Run the code; quote numbers, not impressions. Put long outputs in `docs/data-fact-sheet.md`.

## 2. Write the inventory

Summarise block 5 of `CANVAS.md` in a few lines and link the fact sheet. Add new variables, codes and units to `GLOSSARY.md`.

## 3. Surface data decisions

List every point that needs a judgement call: how to join, how to treat each kind of missing value, which encoding, what to exclude, which incomplete periods to drop. For each, give the options, the evidence from step 1, and your recommendation. Ask them in one numbered round, like `/grill-question`.

Also flag any question in block 2 that the data cannot answer, and any column that may violate block 6 (known in advance).

## 4. Propose checks

Every fact that must stay true later (one row per date and product, every date of the period present exactly once, no future dates in training) is a candidate check. List them for block 8; the user confirms which ones to keep.

Done when every dataset is profiled, every open data decision is answered by the user and logged in `DECISIONS.md` and block 7, and the confirmed checks are listed in block 8.
