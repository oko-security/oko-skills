# Codex tool mapping

TODO(v0.3): verify against current Codex tool names.

| oko action | Codex |
|---|---|
| Invoke a skill | Skills load by description match; name the skill explicitly in your plan. |
| Dispatch a subagent | Not available: run each brief yourself, sequentially, and keep notes per brief. |
| Ask the user a question | Ask in your reply and stop; resume on their answer. |
| Read / search files | `shell` with `cat`, `rg`, `ls`, `find` (read-only). |
| Write the output file | `apply_patch` |
