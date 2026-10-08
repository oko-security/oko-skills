---
name: recommending-mitigations
description: Use when proposing mitigations, controls, or remediation strategy for threat-model threats (section 8), or when asked "what should we do about these threats?". Prefers class-level controls that survive the next bug over per-instance patches.
---

# Recommending mitigations

Each row is a **class-level control**: a change that removes or substantially
reduces an entire group of threats, including instances nobody has found
yet.

| Prefer | Over |
|---|---|
| Tenant ID applied in the repository layer for every query | Adding an owner check to `/invoices/<id>` |
| Uploads stored under random names in a dedicated bucket | Stripping `../` from one filename |
| Short-lived, audience-bound tokens issued by one service | Rotating one leaked key |
| Template engine with autoescaping turned on everywhere | Escaping one field |
| A person approves any agent tool call that has side effects | Blocking one malicious prompt |

## Steps

1. Group threats that share a mitigation; one row can cover several IDs.
2. Mark `closes_class: yes` only if the control removes the class, not just
   lowers likelihood.
3. Estimate `effort` S/M/L against the codebase as it is.
4. If `.oko/controls.md` lists a standard org control that would close the
   class, recommend adopting it by name before inventing a new one.
5. Order by (threats covered × impact) / effort.

TODO(v0.2): optional mapping to OWASP ASVS / CIS / NIST 800-53 control IDs.
