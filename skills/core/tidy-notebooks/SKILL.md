---
name: tidy-notebooks
description: Turn exploratory notebooks into a reproducible pipeline without changing results, before handing in or publishing a project.
disable-model-invocation: true
---

# Tidy notebooks

Make the project reproducible from raw data to final results with one command or one run of one notebook, without changing any result.

## 1. Inventory

List every notebook and script, what it reads, what it writes, and whether the final results depend on it. Identify the **result path**: the cells and files that actually produce the reported numbers, charts and prediction files. Everything else is exploration.

## 2. Capture the golden output

Run the current result path from a clean state and save its outputs (metrics, prediction files, key tables) as the **golden output**. If the current path does not run from a clean state, stop and fix that first with the user.

## 3. Propose a structure

Propose a layout, for example: `src/` modules for loading, preparation, features, model and evaluation; one `run` script or notebook that calls them; exploration notebooks moved to `notebooks/exploration/` with a one-line header each. Keep the structure as flat as the project allows. Confirm with the user.

## 4. Refactor

Move code in small steps. After each step, re-run and compare with the golden output; any difference is a bug, not a cleanup. Keep all checks green.

## 5. Document

Update the README: how to set up the environment, the one command that reproduces everything, where results land.

Done when the result path runs from a clean state with one command, reproduces the golden output exactly (or within a documented numerical tolerance), and the user has approved the structure.
