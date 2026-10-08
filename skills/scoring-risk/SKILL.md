---
name: scoring-risk
description: Use when assigning or reviewing impact, likelihood, status, and controls for threat-model threats, or when the user asks how risky a threat is. Applies the default (or team-overridden) risk matrix and scores residual risk after controls.
---

# Scoring risk

Fill in `actor`, `impact`, `likelihood`, `status`, and `controls` for each
threat row.

## Inputs

- The row itself: surface, asset, evidence, and how many look-alike code
  paths were found.
- The sensitivity of the asset in section 2.
- The team layer: risk-matrix overrides in `profile.md` and inherited
  controls in `controls.md`.

## How to score

1. **Actor.** Ask who can reach the surface. If the route needs a login
   first, the actor is `remote_auth`. If anyone on the internet can call it,
   the actor is `remote_unauth`. If the input is a file, the actor is
   whoever supplies the file.
2. **Impact.** Combine how sensitive the asset is with how bad the outcome
   is. Code execution in an internet-facing service is `critical`. Exposing
   data that is already public is `low`.
3. **Likelihood.** Start high if there is a track record, and lower it as
   the evidence gets thinner:

   | Signal | Floor |
   |---|---|
   | Exploited in the wild, or a public working exploit | `almost_certain` |
   | One or more confirmed past issues on this same surface | `likely` |
   | No past issues, but common technique and look-alike code found | `possible` |
   | Needs unusual configuration and real expertise | `rare` |

4. **Controls lower likelihood.** Search for protections relevant to the
   stack: input validation, size limits, sandboxing, prepared statements,
   auth middleware, output encoding, rate limits, compiler hardening. Also
   apply `.oko/controls.md`. Cite each control. The score is what remains
   **after** the controls.
5. **Status.** Use `mitigated` only when a cited control removes the whole
   class. Use `risk_accepted` only when an owner or the team profile says so.
   Anything in between is `partially_mitigated`. If there are no controls,
   use `unmitigated`.

The full definition of each value is in the format spec. Call the Skill tool
with `writing-threat-models` if you need it.

TODO(v0.2): support team-defined numeric matrices (for example 5×5 mapped to
P1-P4) via `risk_matrix:` in `profile.md`, and include the resulting priority
in the report.
