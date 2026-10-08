# Claude Code tool mapping

| oko action | Claude Code tool |
|---|---|
| Invoke a skill | `Skill` |
| Dispatch a subagent / run briefs in parallel | `Agent` (send all briefs in one message so they run concurrently) |
| Ask the user a question | `AskUserQuestion` (one question at a time; put the recommended option first) |
| Read a file | `Read` |
| Search file contents | `Grep` |
| Find files by pattern | `Glob` |
| Run git / advisory lookups | `Bash` (only `git`, `gh api`, `ls`, `find`, `cat`, and oko's own scripts) |
| Write the output file | `Write` |
| Track a multi-step checklist | `TodoWrite` |

Plugin scripts live under `${CLAUDE_PLUGIN_ROOT}/skills/<skill>/scripts/`.
