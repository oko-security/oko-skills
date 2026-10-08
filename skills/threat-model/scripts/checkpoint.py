#!/usr/bin/env python3
"""Checkpoint state for long /threat-model runs. Zero dependencies.

All paths are confined to the current working directory so a prompt-injected
path cannot write elsewhere. Payloads are read from a file (--from), never
from argv, so target-derived bytes never touch the shell.

  checkpoint.py load  <state-dir>
  checkpoint.py reset <state-dir>
  checkpoint.py save  <state-dir> <stage> <name> --from <file>
  checkpoint.py done  <state-dir> <stage>
"""
import argparse
import json
import os
import sys
import tempfile
from pathlib import Path


def confined(p: str) -> Path:
    cwd = Path.cwd().resolve()
    path = (cwd / p).resolve()
    if path != cwd and cwd not in path.parents:
        sys.exit(f"error: {p} escapes the working directory")
    return path


def atomic_write(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=path.parent, suffix=".tmp")
    with os.fdopen(fd, "w") as f:
        json.dump(data, f, indent=2)
    os.replace(tmp, path)


def main() -> None:
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    for c in ("load", "reset"):
        sub.add_parser(c).add_argument("state_dir")
    s = sub.add_parser("save")
    s.add_argument("state_dir")
    s.add_argument("stage", type=int)
    s.add_argument("name")
    s.add_argument("--from", dest="src", required=True)
    d = sub.add_parser("done")
    d.add_argument("state_dir")
    d.add_argument("stage", type=int)
    a = ap.parse_args()

    state = confined(a.state_dir)
    progress = state / "progress.json"

    if a.cmd == "load":
        if not progress.exists():
            print(json.dumps({"status": "absent"}))
        else:
            print(progress.read_text())
    elif a.cmd == "reset":
        if state.exists():
            for f in state.glob("*.json"):
                f.unlink()
        atomic_write(progress, {"status": "running", "stage_done": 0})
        print("reset")
    elif a.cmd == "save":
        src = confined(a.src)
        try:
            payload = json.loads(src.read_text())
        except json.JSONDecodeError as e:
            sys.exit(f"error: {src} is not valid JSON: {e}")
        atomic_write(state / f"stage{a.stage}.json", payload)
        atomic_write(progress, {"status": "running", "stage_done": a.stage, "last": a.name})
        print(f"saved stage {a.stage} ({a.name})")
    elif a.cmd == "done":
        atomic_write(progress, {"status": "complete", "stage_done": a.stage})
        print("complete")


if __name__ == "__main__":
    main()
