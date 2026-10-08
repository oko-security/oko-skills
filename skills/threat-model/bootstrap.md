# /threat-model bootstrap

Draft a threat model from the **code and its security history** alone, with
no owner available. Works for any language. Read-only throughout.

## Inputs

- `<target-dir>` (required): a local checkout.
- `--vulns <path>` (optional): known issues as a plain list of CVE IDs, a CSV
  (`id,title,component,description`), a Markdown pentest report, or a JSON
  array of objects with `id` and `description`.
- `--design-doc <path>` (optional): an architecture or design document.
- `--depth recon|full` (default `full`): `recon` ends after Phase 2, writes
  sections 1-3, and adds "re-run with --depth full" to section 6.
- `--fresh`: discard any saved progress.

## Saving progress

Long runs save after each phase so a crash or context reset can pick up where
it left off. State goes in `./.oko-state/` under the current working
directory (never inside the target), and every read or write of it goes
through `scripts/checkpoint.py` in this skill's directory:

```
python3 <skill-dir>/scripts/checkpoint.py load  ./.oko-state
python3 <skill-dir>/scripts/checkpoint.py reset ./.oko-state
python3 <skill-dir>/scripts/checkpoint.py save  ./.oko-state <N> <name> --from ./.oko-state/_chunk.tmp
python3 <skill-dir>/scripts/checkpoint.py done  ./.oko-state <N>
```

To save phase N, first write its JSON to `./.oko-state/_chunk.tmp` with your
file-write action, then run `save`. Text that came from the target must never
travel through shell arguments, heredocs, or stdin.

**On start**, run `load`:

- `absent` or `complete`, or the user passed `--fresh`: run `reset` and begin
  at Phase 1.
- `running` with `stage_done: N`: read `stage1.json` through `stageN.json` in
  order, tell the user you are resuming after Phase N, and continue from N+1.

## Phase 1: Survey

Run the briefs below. Use parallel subagents when you can; run them one after
another yourself when the target is small (roughly 50 source files or fewer)
or your agent cannot dispatch subagents. Every brief receives the target's
absolute path and the read-only rule, copied exactly.

| Brief | Source skill | Produces |
|---|---|---|
| Docs | `mapping-attack-surface` → docs | What the system is and who uses it; security fixes it documents |
| Surface | `mapping-attack-surface` → surface | Draft section 3 rows |
| Infra | `mapping-attack-surface` → infra | Infra entry points, plus threats where the config itself is the problem |
| Assets | `mapping-attack-surface` → assets | Draft section 2 rows |
| Commits | `mining-vulnerability-history` → git | Past-issue rows from history |
| Advisories | `mining-vulnerability-history` → advisories | Past-issue rows from public advisories |
| Supplied list | `mining-vulnerability-history` → file (only with `--vulns`) | Normalized past-issue rows |

Load the brief text by calling the Skill tool with `mapping-attack-surface`
and then `mining-vulnerability-history`, and paste each brief into its
subagent's prompt.

Save as phase 1: `{"stage":1,"survey":{"<brief>": <its output>, ...}}`.

## Phase 2: Assemble sections 1-3

Merge what the briefs returned. Collapse duplicate entry points, record which
assets each one can reach, and write the section 1 narrative. Keep a working
list of past issues as `{id, title, component, class, vector}` and tie each
one to the entry point it came through (add the entry point if the survey
missed it). Fold in `.oko/controls.md` now so scoring sees inherited
controls.

Save as phase 2. With `--depth recon`, write the file and stop here.

## Phase 3: Generalize

Call the Skill tool with `generalizing-threats`, giving it the past-issue list
and sections 2-3. It returns draft section 4 rows with evidence, plus notes on
similar code elsewhere. Save as phase 3.

## Phase 4: Fill the gaps

Call the Skill tool with `applying-threat-lenses`. STRIDE covers every entry
point; other lenses join when their triggers match or the team profile
requires them. Rows found this way start with no evidence. If the finished
section 4 has no evidence-free row, this phase was skipped: go back and run
it. Categories considered and dismissed go to section 5. Save as phase 4.

## Phase 5: Score and write

1. Call the Skill tool with `scoring-risk` for every section 4 row.
2. Call the Skill tool with `recommending-mitigations` for section 8.
3. If useful, call the Skill tool with `diagramming-data-flows` for section 9.
4. Continue at Step 3 of `SKILL.md`.
5. Run `checkpoint.py done ./.oko-state 5`.

Provenance: `mode: bootstrap`, today's date,
`target: <path> @ <git rev-parse HEAD>`, the inputs used, `owner: unset`.
