---
name: threat-model-diff
description: Assess whether a PR, diff, branch, or design doc changes a system's threat model - new entry points, new assets, weakened controls, new threats.
disable-model-invocation: true
argument-hint: "<base>..<head> | <PR number> | <design-doc path> [--model <THREAT_MODEL.md>]"
---

# /threat-model-diff

Security design review at the speed of a PR. Read-only.

TODO(v0.4). Planned method:

1. Load the existing `THREAT_MODEL.md` (or say none exists and recommend
   `/threat-model bootstrap` first; continue with a surface-only review).
2. Get the change: `git diff <range>`, `gh pr diff <n>`, or read the design doc.
3. Call the Skill tool with `mapping-attack-surface` on the changed paths
   only. Classify each change: new entry point, changed trust boundary, new
   asset, removed or weakened control, none.
4. For each non-`none` change, call the Skill tool with
   `applying-threat-lenses` and `scoring-risk` on the affected surface.
5. Output a short report:
   - **Verdict**: no model change / model update needed / needs security review
   - New or changed threats (proposed rows, IDs continuing from the model)
   - Weakened controls with `file:line`
   - Questions for the author
6. Offer to apply the proposed rows to `THREAT_MODEL.md`.

Planned CI: a GitHub Action that runs this headless on PRs touching
security-relevant paths and posts the verdict as a comment.
