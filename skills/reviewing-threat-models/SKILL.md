---
name: reviewing-threat-models
description: Use when critiquing, auditing, or quality-checking a threat model (oko's or anyone's), or as the final "did we do a good job?" gate before handing a threat model back. Checks coverage, abstraction level, grounding, and ranking.
---

# Reviewing threat models

Run after `writing-threat-models` validates the file. Report findings as
**blocking** (fix before hand-back) or **advisory** (list in the hand-back).

## Blocking

- [ ] Any threat that fails the patch test (it names a line, a function, or a single bug).
- [ ] An entry point in section 3 with no threat and no section 5 entry.
- [ ] A `controls` value with no citation.
- [ ] No threat with empty evidence (gap-fill skipped).
- [ ] Top 5 ranking contradicts the scoring rules (e.g. `critical/likely` below `medium/possible`).
- [ ] Provenance missing target commit.

## Advisory

- [ ] Assets with `critical` sensitivity that no threat touches: missing threats or wrong sensitivity?
- [ ] Actors never used: are `insider` and `supply_chain` really out of scope? Say so in section 5.
- [ ] Every threat `unmitigated`: controls search probably shallow.
- [ ] Section 6 empty after a bootstrap: unlikely; the code never answers everything.
- [ ] More than ~25 threats: probably too granular; consider clustering.
- [ ] Fewer than ~5 threats on a networked service: probably too coarse.

For an external threat model (not written by oko), first map it onto the
schema, then run the same checklist, and report what could not be mapped.
