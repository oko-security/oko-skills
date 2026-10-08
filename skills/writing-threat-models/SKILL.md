---
name: writing-threat-models
description: Use when writing, emitting, or validating a THREAT_MODEL.md file, or when you need the threat model format (sections, table columns, enum values). Owns the oko output contract and its validator.
---

# Writing threat models

This skill owns the output format. Every oko workflow that produces a threat
model finishes here.

## Steps

1. Open `schema.md` in this directory now, just before writing. If you read
   it at the start of a long session, it may no longer be in context.
2. Write `<target-dir>/THREAT_MODEL.md`, or the `output_path` from the team
   profile. Copy headings, column order, and enum values exactly.
3. Run the validator:
   ```
   python3 <skill-dir>/scripts/tm.py validate <path-to>/THREAT_MODEL.md
   ```
   Fix each `ERROR` and re-run until none remain. Put any `WARN` lines in
   the report to the user.
4. If the team profile defines extra actors, pass them:
   `--extra-actors insider_contractor,partner_api`.

## Checks the validator can't make

- Each threat passes the patch test: it still holds after every evidence item
  is fixed.
- Each `controls` entry cites a `file:line` or a named control from
  `.oko/controls.md`.
- `evidence` holds only confirmed past issues. Look-alike code is not
  evidence.
- Threats carried over from an earlier version keep their IDs. Retired
  threats move to section 5.
