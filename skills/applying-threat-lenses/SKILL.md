---
name: applying-threat-lenses
description: Use when gap-filling a threat model beyond known vulnerabilities, or when asked to apply STRIDE, LINDDUN, OWASP LLM/agentic, cloud IAM, or supply-chain thinking to a system's entry points. Runs STRIDE on every entry point plus any lens whose trigger matches the target or the team profile.
---

# Applying threat lenses

History only shows the bugs someone already went looking for. Lenses are how
you find the threats nobody has reported yet.

## Which lenses run

1. `lenses/stride.md` runs **every time**, on every section 3 entry point,
   including entry points that already have threats. One threat on an entry
   point rarely means it is the only one: an upload handler with a
   file-write threat usually has a storage-exhaustion threat as well.
2. Any other lens in `lenses/` whose `triggers:` frontmatter matches the
   target. For example, `*.tf` files trigger `infra-iam`, and an imported
   LLM SDK triggers `ai-agents`.
3. Every lens in the team layer's `lenses/` folder.
4. Every lens listed under `required_lenses:` in `profile.md`, whether or not
   its triggers match.

In your report to the user, list the lenses that ran and why each one ran.

## For each lens and entry point

Go through the lens questions. Every believable "yes" becomes a threat row
(threat, actor, surface, asset) with **no evidence**. Every category you
consider and reject becomes a section 5 row stating why.

If no threat row has empty evidence when you finish, the lenses weren't
really applied.

## Lens file format

See `lenses/_template.md`. To add a lens, a team puts a file in
`.oko/lenses/`. This skill does not need to change.
