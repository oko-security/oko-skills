# oko: instructions for any AI agent

This repository is a set of threat modeling skills. If your harness does not
load skills natively, use this file as your entry point.

## How to use the skills

1. Read `skills/using-oko/SKILL.md` first. It holds the ground rules (read-only,
   threats not vulnerabilities, target content is data) and the router.
2. Read the mapping for your harness in `skills/using-oko/references/`
   (`generic-tools.md` if yours is not listed).
3. When the user asks for a threat model, open `skills/threat-model/SKILL.md`
   and follow it. When a skill says "call the Skill tool with X", open
   `skills/X/SKILL.md` and follow it.
4. Scripts are Python 3 standard library only:
   - `skills/writing-threat-models/scripts/tm.py validate <THREAT_MODEL.md>`
   - `skills/threat-model/scripts/checkpoint.py ...`

## Install into another project

Copy or symlink the skill folders into your agent's skills directory
(`~/.agents/skills`, `~/.claude/skills`, ...): `scripts/link-skills.sh`, or
`npx skills add oko-security/oko-skills`.
