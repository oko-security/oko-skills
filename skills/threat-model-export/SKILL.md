---
name: threat-model-export
description: Export a THREAT_MODEL.md to JSON, a Mermaid data flow diagram, Open Threat Model (OTM), or tickets in your tracker.
disable-model-invocation: true
argument-hint: "<json|mermaid|otm|tickets> [<THREAT_MODEL.md>]"
---

# /threat-model-export

| Format | How | Status |
|---|---|---|
| `json` | Run the `tm.py to-json` script owned by `writing-threat-models` | works |
| `mermaid` | Call the Skill tool with `diagramming-data-flows`; write `DFD.mmd` | v0.2 |
| `otm` | Map JSON to the Open Threat Model format (IriusRisk/OWASP) | TODO v0.4 |
| `tickets` | One ticket per section 8 mitigation (not per threat), linking threat IDs; tracker from `.oko/profile.md` | TODO v0.4 |

Always validate the source file first (call the Skill tool with
`writing-threat-models`). Creating tickets is an outward action: show the
list and ask before creating anything.
