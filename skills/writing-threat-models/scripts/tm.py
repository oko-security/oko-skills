#!/usr/bin/env python3
"""Validate and convert oko THREAT_MODEL.md files. Zero dependencies.

  tm.py validate <THREAT_MODEL.md> [--extra-actors a,b]   exit 1 on any ERROR
  tm.py to-json  <THREAT_MODEL.md>                        JSON on stdout
"""
import argparse
import json
import re
import sys
from pathlib import Path

REQUIRED = [
    "1. System context",
    "2. Assets",
    "3. Entry points & trust boundaries",
    "4. Threats",
    "5. Deprioritized",
    "6. Open questions",
    "7. Provenance",
]
OPTIONAL = ["8. Recommended mitigations", "9. Data flow diagram", "10. Compliance mapping"]

COLUMNS = {
    "2. Assets": ["asset", "description", "sensitivity"],
    "3. Entry points & trust boundaries": ["entry_point", "description", "trust_boundary", "reachable_assets"],
    "4. Threats": ["id", "threat", "actor", "surface", "asset", "impact", "likelihood", "status", "controls", "evidence"],
    "5. Deprioritized": ["threat", "reason"],
    "8. Recommended mitigations": ["mitigation", "threat_ids", "closes_class", "effort"],
    "10. Compliance mapping": ["threat_id", "framework", "control_id", "note"],
}

ENUMS = {
    "sensitivity": ["low", "medium", "high", "critical"],
    "actor": ["remote_unauth", "remote_auth", "adjacent_network", "local_user", "local_admin", "supply_chain", "insider"],
    "impact": ["low", "medium", "high", "critical", "existential"],
    "likelihood": ["very_rare", "rare", "possible", "likely", "almost_certain"],
    "status": ["unmitigated", "partially_mitigated", "mitigated", "risk_accepted"],
    "closes_class": ["yes", "partial"],
    "effort": ["S", "M", "L"],
}


def split_sections(text: str) -> tuple[str | None, dict[str, str], list[str]]:
    title = None
    m = re.search(r"^# Threat Model: (.+)$", text, re.M)
    if m:
        title = m.group(1).strip()
    sections: dict[str, str] = {}
    order: list[str] = []
    parts = re.split(r"^## (.+?)\s*$", text, flags=re.M)
    for i in range(1, len(parts), 2):
        name = parts[i].strip()
        sections[name] = parts[i + 1]
        order.append(name)
    return title, sections, order


def parse_table(body: str) -> tuple[list[str], list[dict[str, str]]]:
    lines = [l.strip() for l in body.splitlines() if l.strip().startswith("|")]
    if len(lines) < 2:
        return [], []

    def cells(line: str) -> list[str]:
        return [c.strip() for c in line.strip().strip("|").split("|")]

    header = cells(lines[0])
    rows = []
    for line in lines[2:]:
        vals = cells(line)
        rows.append(dict(zip(header, vals + [""] * (len(header) - len(vals)))))
    return header, rows


def to_dict(text: str) -> dict:
    title, sections, _ = split_sections(text)
    out: dict = {"title": title, "sections": {}}
    for name, body in sections.items():
        if name in COLUMNS:
            _, rows = parse_table(body)
            out["sections"][name] = rows
        else:
            out["sections"][name] = body.strip()
    return out


def validate(text: str, extra_actors: list[str]) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warns: list[str] = []
    enums = {k: list(v) for k, v in ENUMS.items()}
    enums["actor"] += extra_actors

    title, sections, order = split_sections(text)
    if not title:
        errors.append("missing '# Threat Model: <system name>' title")

    expected = REQUIRED + [s for s in OPTIONAL if s in sections]
    present = [s for s in order if s in expected]
    for s in REQUIRED:
        if s not in sections:
            errors.append(f"missing required section '## {s}'")
    if present != [s for s in expected if s in sections]:
        errors.append(f"sections out of order: {present}")

    for name, cols in COLUMNS.items():
        if name not in sections:
            continue
        header, rows = parse_table(sections[name])
        if header and header != cols:
            errors.append(f"{name}: columns {header} != {cols}")
            continue
        for i, row in enumerate(rows, 1):
            for col, allowed in enums.items():
                if col in row and row[col] and row[col] not in allowed:
                    errors.append(f"{name} row {i}: {col}='{row[col]}' not in {allowed}")

    _, threats = parse_table(sections.get("4. Threats", ""))
    ids = [t.get("id", "") for t in threats]
    for tid in ids:
        if not re.fullmatch(r"T\d+", tid):
            errors.append(f"threat id '{tid}' must match T<n>")
    if len(ids) != len(set(ids)):
        errors.append("duplicate threat ids")
    if threats and all(t.get("evidence") for t in threats):
        warns.append("every threat has evidence: the lens gap-fill stage probably did not run")
    for t in threats:
        if re.search(r"\w+\.\w+:\d+", t.get("evidence", "")):
            warns.append(f"{t.get('id')}: evidence looks like a file:line (siblings are not evidence)")
        if re.search(r"\w+\.(c|h|py|js|ts|go|rs|java):\d+", t.get("threat", "")):
            warns.append(f"{t.get('id')}: threat names a file:line, probably a vulnerability not a threat")

    _, assets = parse_table(sections.get("2. Assets", ""))
    asset_names = {a.get("asset", "") for a in assets}
    _, eps = parse_table(sections.get("3. Entry points & trust boundaries", ""))
    for ep in eps:
        for a in [x.strip() for x in ep.get("reachable_assets", "").split(",") if x.strip()]:
            if a not in asset_names:
                warns.append(f"entry point '{ep.get('entry_point')}' reaches unknown asset '{a}'")

    if "8. Recommended mitigations" in sections:
        _, mits = parse_table(sections["8. Recommended mitigations"])
        for m in mits:
            for tid in [x.strip() for x in m.get("threat_ids", "").split(",") if x.strip()]:
                if tid not in ids:
                    errors.append(f"mitigation '{m.get('mitigation')}' references unknown threat {tid}")

    prov = sections.get("7. Provenance", "")
    for key in ("mode", "date", "target"):
        if not re.search(rf"^- {key}:", prov, re.M):
            errors.append(f"provenance missing '- {key}:'")

    return errors, warns


def main() -> None:
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    v = sub.add_parser("validate")
    v.add_argument("path")
    v.add_argument("--extra-actors", default="")
    j = sub.add_parser("to-json")
    j.add_argument("path")
    a = ap.parse_args()

    text = Path(a.path).read_text()
    if a.cmd == "to-json":
        print(json.dumps(to_dict(text), indent=2))
        return
    extra = [x.strip() for x in a.extra_actors.split(",") if x.strip()]
    errors, warns = validate(text, extra)
    for e in errors:
        print(f"ERROR {e}")
    for w in warns:
        print(f"WARN  {w}")
    if not errors:
        print(f"OK    {a.path}")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
