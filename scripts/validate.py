#!/usr/bin/env python3
"""Repo lint: skill frontmatter, invocation consistency, manifest versions, examples."""
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
errors: list[str] = []


def frontmatter(p: Path) -> dict[str, str]:
    m = re.match(r"^---\n(.*?)\n---\n", p.read_text(), re.S)
    if not m:
        return {}
    return dict(re.findall(r"^([\w-]+):\s*(.*)$", m.group(1), re.M))


for skill in sorted((ROOT / "skills").iterdir()):
    if not skill.is_dir():
        continue
    md = skill / "SKILL.md"
    if not md.exists():
        errors.append(f"{skill.name}: missing SKILL.md")
        continue
    fm = frontmatter(md)
    if fm.get("name") != skill.name:
        errors.append(f"{skill.name}: frontmatter name '{fm.get('name')}' != folder")
    if not fm.get("description"):
        errors.append(f"{skill.name}: missing description")
    yaml = skill / "agents" / "openai.yaml"
    if not yaml.exists():
        errors.append(f"{skill.name}: missing agents/openai.yaml")
        continue
    user_cc = fm.get("disable-model-invocation") == "true"
    user_codex = "allow_implicit_invocation: false" in yaml.read_text()
    if user_cc != user_codex:
        errors.append(f"{skill.name}: invocation differs between SKILL.md and openai.yaml")
    body = md.read_text()
    for ref in re.findall(r"\.\./([\w-]+)/", body):
        errors.append(f"{skill.name}: cross-skill path '../{ref}/'; use 'Call the Skill tool with'")

versions = {}
for f in [".claude-plugin/plugin.json", ".codex-plugin/plugin.json", ".cursor-plugin/plugin.json",
          "gemini-extension.json", "package.json"]:
    versions[f] = json.loads((ROOT / f).read_text())["version"]
if len(set(versions.values())) != 1:
    errors.append(f"manifest versions differ: {versions}")

tm = ROOT / "skills/writing-threat-models/scripts/tm.py"
for ex in (ROOT / "examples").glob("**/THREAT_MODEL.md"):
    r = subprocess.run([sys.executable, str(tm), "validate", str(ex)], capture_output=True, text=True)
    if r.returncode:
        errors.append(f"{ex.relative_to(ROOT)}:\n{r.stdout}")

for e in errors:
    print(f"ERROR {e}")
print("OK" if not errors else f"{len(errors)} error(s)")
sys.exit(1 if errors else 0)
