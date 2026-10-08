# Porting oko to a new agent

oko is the same content everywhere. A port adds three thin things and never
edits skill bodies:

1. **Tool mapping**: `skills/using-oko/references/<harness>-tools.md`,
   translating oko's action vocabulary (invoke a skill, dispatch a subagent,
   ask the user, search, write) into that harness's tools. Note missing
   capabilities (no subagents → run briefs sequentially).
2. **Bootstrap**: get `skills/using-oko/SKILL.md` into context at session
   start, through the harness's own install mechanism (plugin hook, extension
   context file, rules file). Never edit the user's global config.
3. **Manifest**: whatever the harness's marketplace needs, versioned by
   `scripts/bump-version.sh`.

## Checklist

- [ ] "Threat model this repo" triggers `using-oko` with no other hints
- [ ] `/threat-model bootstrap evals/targets/notes-api/src` completes and validates
- [ ] User-invoked skills are not auto-invoked
- [ ] The read-only rule holds (no build/run attempts in the transcript)
- [ ] Eval pass rate recorded in the PR
