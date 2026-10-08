# Generic agent mapping

For any agent without a dedicated mapping (Aider, Cline, Copilot, Windsurf,
custom SDK agents):

- **Invoke a skill**: open `skills/<name>/SKILL.md` and follow it.
- **Dispatch a subagent**: if you cannot spawn agents, run each brief yourself
  in sequence. Write each brief's result to the checkpoint before starting the
  next, so a context reset loses at most one brief.
- **Ask the user**: ask one question, then stop and wait.
- **Shell**: use only read-only commands (`git log`, `git show`, `ls`, `find`,
  `cat`, `grep`/`rg`) plus oko's own `scripts/`.
