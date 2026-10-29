---
name: ds-retro
description: Look back on a data science milestone and suggest improvements to checks, glossary, canvas and agent instructions.
disable-model-invocation: true
---

# DS retro

Suggest improvements to the project’s environment so the next milestone goes better. Read the session(s) or period the user names (default: the current session), `experiments/LOG.md`, `DECISIONS.md` and `CANVAS.md`.

Look for candidates in these categories, each with evidence from what happened:

- **Missing checks**: any mistake that a check would have caught (a duplicated join, a leak, a wrong row count). Propose the exact check and its checkpoint. A mistake caught by hand is a check waiting to be written.
- **Glossary**: terms that were misunderstood or used inconsistently.
- **Canvas**: blocks that turned out wrong or vague; open questions that are now answered; a success criterion that should be revisited.
- **Agent instructions**: recurring corrections the team had to give the agent. Prefer a check over a rule; reserve `AGENTS.md` rules for judgement calls no check can enforce.
- **Process**: steps that were skipped and cost time later.

Present the candidates as a numbered list with a recommendation each. Apply only what the user picks. Done when every picked item is written to the right file.
