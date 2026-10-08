# /threat-model refresh

Update an existing `THREAT_MODEL.md` after the code has moved, without
renumbering threats or losing owner-supplied context.

TODO(v0.4). Planned method:

1. Read section 7 (Provenance) for the commit the model was built at.
2. `git diff --stat <that-commit>..HEAD` in the target. If nothing
   security-relevant changed (docs, tests only), say so and stop.
3. Call the Skill tool with `mapping-attack-surface`, limited to changed
   paths. Add, change, or retire section 3 rows.
4. For each changed entry point, re-run `applying-threat-lenses` and
   `scoring-risk` on the affected threats only.
5. Retired threats move to section 5 with reason "surface removed in <sha>".
   IDs are never reused.
6. Append a provenance line: `refreshed: YYYY-MM-DD @ <sha>`.
