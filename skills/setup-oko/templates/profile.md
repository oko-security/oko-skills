---
org: Example Security
output_path: THREAT_MODEL.md          # relative to target dir
actors:
  add: []                             # e.g. [partner_api, contractor]
  out_of_scope: []                    # e.g. [local_admin]
required_lenses: [stride]             # always-on lenses beyond triggers
risk_matrix: default                  # default | custom (see below)
ticket_tracker: none                  # none | github | jira | linear
---

# Team profile

Free-text context the agent should know about every system you model:
deployment platform, typical architecture, threat actors you actually see,
risk appetite.

## Custom risk matrix (only if risk_matrix: custom)

| impact \ likelihood | very_rare | rare | possible | likely | almost_certain |
|---|---|---|---|---|---|
| existential | P1 | P0 | P0 | P0 | P0 |
| critical | P2 | P1 | P1 | P0 | P0 |
| high | P3 | P2 | P2 | P1 | P1 |
| medium | P4 | P3 | P3 | P2 | P2 |
| low | P4 | P4 | P4 | P3 | P3 |
