# Working on oko

Rules for agents (and humans) changing this repo.

- **Skills name actions, not tools.** Write "dispatch a subagent", "ask the
  user", "search files". Tool names live only in
  `skills/using-oko/references/*-tools.md`.
- **Cross-skill calls** are written as "Call the Skill tool with `<name>`",
  never as `../other-skill/FILE.md` links. Shared material lives in the skill
  that owns it (e.g. the schema lives in `writing-threat-models`).
- **Invocation.** Gerund names are model-invoked. Short command names
  (`threat-model`, `setup-oko`, ...) are user-invoked: set
  `disable-model-invocation: true` in frontmatter **and**
  `policy.allow_implicit_invocation: false` in `agents/openai.yaml`. A
  user-invoked skill is never called from another skill.
- **Every skill** has `SKILL.md` (frontmatter `name` = folder name,
  `description`) and `agents/openai.yaml`.
- **Schema changes** are additive only. Sections 1-8 are a frozen contract
  (see `docs/adr/0001-markdown-is-the-contract.md`). Update `schema.md`,
  `tm.py`, `examples/`, and bump the schema version together.
- **Read-only** is non-negotiable: no skill may instruct building, running,
  or probing a target.
- **Versions** move together: `scripts/bump-version.sh <x.y.z>`.
- Before committing: `python3 scripts/validate.py`.
- **Original text only.** Other projects can inspire ideas, but never copy
  their prose, prompts, examples, or code into this repo. Don't name other
  projects in skills, docs, or code. Credits go only in the README.
