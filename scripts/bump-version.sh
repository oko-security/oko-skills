#!/usr/bin/env bash
# Set one version across every manifest.
set -euo pipefail
v="${1:?usage: bump-version.sh x.y.z}"
cd "$(dirname "$0")/.."
python3 - "$v" <<'PY'
import json, sys, pathlib
v = sys.argv[1]
files = [".claude-plugin/plugin.json", ".codex-plugin/plugin.json", ".cursor-plugin/plugin.json",
         "gemini-extension.json", "package.json"]
for f in files:
    p = pathlib.Path(f); d = json.loads(p.read_text()); d["version"] = v
    p.write_text(json.dumps(d, indent=2) + "\n"); print(f"{f} -> {v}")
m = pathlib.Path(".claude-plugin/marketplace.json"); d = json.loads(m.read_text())
for pl in d["plugins"]: pl["version"] = v
m.write_text(json.dumps(d, indent=2) + "\n"); print(f"{m} -> {v}")
PY
