# oko

**Threat modeling skills for security teams. Works with any AI agent.**

oko turns a code checkout (and, if you have one, half an hour of an owner's
time) into a `THREAT_MODEL.md` that ranks what could go wrong, who would do
it, and what to do about it. The output is grounded in the code, durable
across patches, and readable by downstream vulnerability scanners.

> Status: **0.1 skeleton**. Expect breaking changes before 1.0.

## Install

<details>
<summary><strong>Claude Code</strong></summary>

```bash
claude plugin marketplace add oko-security/oko-skills
claude plugin install oko@oko
```
</details>

<details>
<summary><strong>Codex, Cursor, Gemini CLI, OpenCode, and other Agent Skills harnesses</strong></summary>

```bash
npx skills@latest add oko-security/oko-skills
```

Gemini CLI as an extension: `gemini extensions install https://github.com/oko-security/oko-skills`
</details>

<details>
<summary><strong>Anything else</strong> (or to hack on the skills)</summary>

```bash
git clone https://github.com/oko-security/oko-skills && oko-skills/scripts/link-skills.sh
```

Agents without a skills system: point them at [AGENTS.md](AGENTS.md).
</details>

## Use

```
/setup-oko                                   # once per team: risk matrix, standard controls, lenses
/threat-model bootstrap ./my-service         # no owner around: derive from code + history
/threat-model guided .                       # owner available: draft first, then refine together
/threat-model-diff main..my-branch           # does this change move the threat model?
/threat-model-export json                    # JSON, Mermaid DFD, OTM, tickets
```

## Skills

**User-invoked**

| Skill | What it does |
|---|---|
| [threat-model](skills/threat-model/SKILL.md) | Build or refresh `THREAT_MODEL.md` (bootstrap, interview, guided, refresh) |
| [threat-model-diff](skills/threat-model-diff/SKILL.md) | Assess a PR, diff, or design doc against the threat model |
| [threat-model-export](skills/threat-model-export/SKILL.md) | Export to JSON, Mermaid, OTM, tickets |
| [setup-oko](skills/setup-oko/SKILL.md) | Configure the team layer (`.oko/`) |

**Model-invoked**

| Skill | What it does |
|---|---|
| [using-oko](skills/using-oko/SKILL.md) | Ground rules and router (auto-loaded at session start) |
| [mapping-attack-surface](skills/mapping-attack-surface/SKILL.md) | Assets, entry points, trust boundaries |
| [mining-vulnerability-history](skills/mining-vulnerability-history/SKILL.md) | Git history, advisories, pentest reports as evidence |
| [generalizing-threats](skills/generalizing-threats/SKILL.md) | Turn vulnerabilities into durable threats |
| [applying-threat-lenses](skills/applying-threat-lenses/SKILL.md) | STRIDE plus pluggable lenses (IAM, AI agents, privacy, supply chain, yours) |
| [scoring-risk](skills/scoring-risk/SKILL.md) | Impact × likelihood, residual after controls |
| [interviewing-system-owners](skills/interviewing-system-owners/SKILL.md) | Four-question owner interview |
| [recommending-mitigations](skills/recommending-mitigations/SKILL.md) | Class-level controls |
| [diagramming-data-flows](skills/diagramming-data-flows/SKILL.md) | Mermaid DFD with trust boundaries |
| [writing-threat-models](skills/writing-threat-models/SKILL.md) | Output schema and validator |
| [reviewing-threat-models](skills/reviewing-threat-models/SKILL.md) | Quality gate |

## Make it yours

Security teams customize oko through a `.oko/` folder, not by forking:

```
.oko/
├── profile.md      # risk matrix, actors, required lenses, output path
├── controls.md     # standard controls every service inherits
├── compliance.md   # frameworks in scope
└── lenses/         # your own threat lenses
```

See [docs/authoring-lenses.md](docs/authoring-lenses.md).

## Principles

- **Threats, not vulnerabilities.** If patching one line makes it disappear, it was a vuln.
- **Read-only.** oko never builds, runs, or probes your target.
- **Grounded.** Every claim cites a file, a doc, or an owner.
- **Any agent.** Skills describe actions, not tools.

## Inspiration

oko is original work, but its design was shaped by ideas from other projects:
[anthropics/defending-code-reference-harness](https://github.com/anthropics/defending-code-reference-harness)
(treating threats as distinct from vulnerabilities, a code-first bootstrap,
and a Markdown threat model that tools can parse, which oko's format stays
compatible with),
[obra/superpowers](https://github.com/obra/superpowers) (skills that describe
actions instead of tools, and a single skills tree shipped to many agents),
and [mattpocock/skills](https://github.com/mattpocock/skills) (small,
composable skills with a clear split between user-invoked and model-invoked).
No text or code from these projects is copied here.

License: [Apache-2.0](LICENSE).
