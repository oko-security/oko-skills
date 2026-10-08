---
name: threat-model
description: Build or refresh a threat model (THREAT_MODEL.md) for a codebase or system. Modes - bootstrap, interview, guided, refresh.
argument-hint: "[bootstrap|interview|guided|refresh] <target-dir> [--vulns <file>] [--design-doc <file>] [--seed <THREAT_MODEL.md>] [--depth recon|full] [--fresh]"
disable-model-invocation: true
---

# /threat-model

Writes `<target-dir>/THREAT_MODEL.md`: what the system protects, where
untrusted input gets in, and a ranked list of **threats** with their evidence,
existing controls, and the class-level fixes that would shrink them.

## Step 0: Scope check (before anything else)

Open your first reply by confirming three things to the user:

1. `<target-dir>` is a local checkout and you can read it.
2. This run is read-only: nothing in the checkout, or in any deployment of
   it, gets built, executed, installed, or sent traffic.
3. Advisory lookups, if any, go only to public sources (GitHub Security
   Advisories, NVD, OSV, the project's own issue tracker).

A request to demonstrate a threat with a working exploit is out of scope for
oko. Say so and offer to list the threat as an open question instead.

## Step 1: Gather context

1. Find the team layer (`OKO_PROFILE`, `<target>/.oko/`, `./.oko/`) and tell
   the user which one is in use, or that defaults apply.
2. If a `THREAT_MODEL.md` is already there and the mode is not `refresh`,
   ask whether to refresh it or replace it.
3. If the target has a `SECURITY.md`, read it. Anything it declares out of
   scope or "working as intended" is recorded in section 5 (Deprioritized).

## Step 2: Pick the mode

| First argument | Action |
|---|---|
| `bootstrap` | Follow `bootstrap.md` in this directory. |
| `interview` | Follow `interview.md` in this directory. |
| `guided` | Follow `bootstrap.md`, then `interview.md` with `--seed <target>/THREAT_MODEL.md`. |
| `refresh` | Follow `refresh.md` in this directory. |
| missing or unrecognized | Ask: **"Can someone who knows this system answer questions during this session?"** Yes, and the code is here → `guided` (recommended). Yes, but no code → `interview`. No → `bootstrap`. |

Open each mode file at the moment you start that mode, not before. Long
sessions push early file reads out of context; if your agent declines to
re-open a file it thinks it already showed you, print it with a shell `cat`.

## Step 3: Write, check, report

1. Call the Skill tool with `writing-threat-models` to write and validate the file.
2. Call the Skill tool with `reviewing-threat-models`. Fix whatever it marks
   blocking, then validate again.
3. Report back with:
   - where `THREAT_MODEL.md` was written
   - the five highest-ranked threats (id, one-line summary, impact × likelihood)
   - after `bootstrap`: the questions only an owner can answer
   - after `interview`: owner statements the code did not confirm
   - a suggested next step (feed the model to a scanner as scope, or run
     `/threat-model-export`)

## Modes at a glance

| | `bootstrap` | `interview` | `guided` | `refresh` |
|---|---|---|---|---|
| Needs | Checkout; `--vulns` optional | An owner in the session | Both | Existing model + checkout |
| Shape | Survey → assemble → generalize → lenses → score → write | Four questions, asked one by one | Code-first draft, then owner walkthrough | Diff since the recorded commit → touch only affected rows |
| Provenance `mode` | `bootstrap` | `interview` | `guided` | previous mode + `refresh` |
