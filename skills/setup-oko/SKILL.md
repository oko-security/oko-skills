---
name: setup-oko
description: Configure oko for your security team - risk matrix, standard controls, actors in scope, required lenses, compliance frameworks. Writes a .oko/ folder the other skills read.
disable-model-invocation: true
argument-hint: "[<dir to write .oko/ into, default ./>]"
---

# /setup-oko

Run once per org (central repo) or once per service repo. Writes `.oko/`.

## Steps

1. Ask where `.oko/` should live. Recommend a central security repo plus
   `OKO_PROFILE=<path>` for org-wide defaults, and per-repo `.oko/` only for
   overrides.
2. Interview the security engineer, **one question at a time**, recommending
   an answer each time. Questions, in order:
   1. Org or team name, and what kinds of systems you model most (web APIs,
      mobile, data pipelines, IaC, AI features, native code)?
   2. Which actors are in scope? Any to add (e.g. `partner_api`,
      `contractor`) or drop?
   3. Risk matrix: keep oko's 5×5 impact/likelihood, or map to your scale
      (P0-P4, CVSS bands, Critical/High/Medium/Low)?
   4. Standard controls every service inherits (SSO, WAF, service mesh mTLS,
      secrets manager, EDR, centralized logging)? These stop false "unmitigated".
   5. Compliance frameworks in scope (SOC 2, PCI DSS, HIPAA, ISO 27001, none)?
   6. Lenses that must always run (`privacy-linddun`, `ai-agents`, ...)?
   7. Where should `THREAT_MODEL.md` be written, and where do tickets go?
3. Write from the templates in `templates/` in this directory:
   `profile.md`, `controls.md`, and `compliance.md` if any framework is in scope.
   Create an empty `lenses/` with a README pointing to the lens template.
4. Print what was written and tell the user: "Run `/threat-model` on a repo
   to use it."
