# AGENTS.md

Instructions for agents working on this repository (the skills themselves, not a data science project that uses them).

- Skill conventions: see [CONTRIBUTING.md](CONTRIBUTING.md).
- When a change affects users of the skills or the canvas (anything under `skills/`, `.claude-plugin/` or `canvas/`), add an entry under `## Unreleased` in `CHANGELOG.md`.
- Do not edit `version` in `.claude-plugin/plugin.json` by hand. Releases go through the `release-plugin` skill (`.claude/skills/release-plugin/`), which picks the version bump, tags and publishes.
- New skills under `skills/` must also be added to the `skills` list in `.claude-plugin/plugin.json`.
