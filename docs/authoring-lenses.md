# Authoring a threat lens

A lens is a question set that surfaces a class of threats STRIDE misses or
under-weights. Lenses are the main way a security team teaches oko what it
cares about, without editing skills.

1. Copy `skills/applying-threat-lenses/lenses/_template.md`.
2. Put it in your team layer: `.oko/lenses/<name>.md` (private), or open a PR
   adding it to `skills/applying-threat-lenses/lenses/` (shared).
3. Set `triggers` so it runs only where it matters (`files` globs, `imports`,
   or `always: true`). Add it to `required_lenses` in `.oko/profile.md` to
   force it.
4. Write each category as a question about one entry point or asset, phrased
   so "yes" maps directly to a threat row.
5. List common ruled-out reasons so section 5 stays informative.
6. Add or update an eval target that a good run of the lens must catch.

Good lens ideas for teams: payments/money movement, multi-tenancy isolation,
mobile client trust, OT/ICS, healthcare data flows, internal admin tooling.
