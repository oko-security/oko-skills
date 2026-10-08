#!/usr/bin/env bash
# Symlink every oko skill into local agent skill dirs. `git pull` then updates them.
set -euo pipefail
REPO="$(cd "$(dirname "$0")/.." && pwd)"
if [ $# -gt 0 ]; then DESTS=("$@"); else DESTS=("$HOME/.claude/skills" "$HOME/.agents/skills"); fi
for DEST in "${DESTS[@]}"; do
  mkdir -p "$DEST"
  for src in "$REPO"/skills/*/; do
    name="$(basename "$src")"
    [ -f "$src/SKILL.md" ] || continue
    ln -sfn "${src%/}" "$DEST/$name"
    echo "linked $name -> $DEST"
  done
done
