# Gemini CLI tool mapping

TODO(v0.3): verify against current Gemini CLI tool names.

| oko action | Gemini CLI |
|---|---|
| Invoke a skill | `activate_skill` (or read the SKILL.md directly) |
| Dispatch a subagent | Not available: run briefs sequentially. |
| Ask the user a question | Ask in your reply and wait. |
| Read / search files | `read_file`, `search_file_content`, `glob` |
| Write the output file | `write_file` |
| Run git | `run_shell_command` (read-only commands only) |
