# Contributing

Feedback from real projects is the most valuable contribution. Useful issues describe:

- a situation where a skill led the agent astray, with what happened and what you expected,
- a mistake that a check, a canvas prompt or a skill rule would have caught,
- a canvas block that was unclear or missing in practice.

## Conventions for skills

- Follow the structure of [Matt Pocock’s skills](https://github.com/mattpocock/skills) and his `writing-for-agents` guide: short, steps with completion criteria, reference behind pointers.
- User-invoked skills set `disable-model-invocation: true` and have a one-line human-facing description. Reference skills keep a model-facing description with their triggers.
- Every human decision is an explicit **stop point**: the agent recommends, the user decides, the decision is logged.
- Skills read and write the project files named in the `## Agentic data science` section of `AGENTS.md`; they do not invent new locations.
- The canvas template has a single source: `skills/core/setup-ds-project/templates/CANVAS.md`.

## Releases

Add an entry under `## Unreleased` in `CHANGELOG.md` for every change that affects users of the skills or the canvas. Leave the version alone: maintainers cut releases with the `release-plugin` skill in `.claude/skills/`, which sets the version in `.claude-plugin/plugin.json`, tags `vX.Y.Z` and publishes a GitHub release.
