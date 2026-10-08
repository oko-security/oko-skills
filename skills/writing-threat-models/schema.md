# THREAT_MODEL.md format (oko v1)

The file is Markdown so people can review and edit it in a normal PR. Tools
also read it, using simple regexes, so three things are fixed: heading text,
table column order, and the allowed enum values. Change any of them and
parsers break. Sections 1-7 must appear. Sections 8-10 are optional, and
anything that reads the file must cope with them being missing.

## Headings, in this order

```markdown
# Threat Model: <system name>

## 1. System context
## 2. Assets
## 3. Entry points & trust boundaries
## 4. Threats
## 5. Deprioritized
## 6. Open questions
## 7. Provenance
## 8. Recommended mitigations        (optional)
## 9. Data flow diagram              (optional)
## 10. Compliance mapping            (optional; only with .oko/compliance.md)
```

A reader that needs one section can match `^## <n>\. ` and stop at the next
`^## `.

## 1. System context

Plain prose, one to three paragraphs, no table. Cover purpose, users,
deployment, and the data it handles.

## 2. Assets

What an attacker would want, or what the business cannot afford to lose.

| asset | description | sensitivity |
|---|---|---|

`sensitivity`: `low`, `medium`, `high`, or `critical`.

## 3. Entry points & trust boundaries

Every place where outside input arrives or privilege changes hands. Build and
deploy paths count even when no request crosses them at runtime.

| entry_point | description | trust_boundary | reachable_assets |
|---|---|---|---|

- `trust_boundary`: describe the crossing in words, such as
  "public internet → logged-in user" or "uploaded file → worker memory".
- `reachable_assets`: section 2 asset names, comma-separated.

## 4. Threats

The core of the document. Each row pairs an attacker with a goal, written at a
level that stays true after individual bugs are fixed.

| id | threat | actor | surface | asset | impact | likelihood | status | controls | evidence |
|---|---|---|---|---|---|---|---|---|---|

- `id`: `T1`, `T2`, and so on. An ID is permanent. Deleting a row leaves a
  gap, and IDs are never recycled.
- `threat`: a single active-voice sentence naming the result. Write
  "Account takeover through forged password-reset links", not "token
  comparison in reset.py is not constant-time".
- `actor`: `remote_unauth`, `remote_auth`, `adjacent_network`, `local_user`,
  `local_admin`, `supply_chain`, or `insider`. A team profile may add more.
- `surface`: entry point name(s) from section 3, spelled the same way.
- `asset`: asset name(s) from section 2.
- `impact`: `low`, `medium`, `high`, `critical`, or `existential`.
- `likelihood`: `very_rare`, `rare`, `possible`, `likely`, or `almost_certain`.
- `status`: `unmitigated`, `partially_mitigated`, `mitigated`, or `risk_accepted`.
- `controls`: protections already in place, each with a `file:line` or a
  control name from `.oko/controls.md`. Write `none` if there are none.
- `evidence`: past issues that are concrete cases of this threat: CVE or GHSA
  IDs, issue or pentest IDs, fix commits. Leave it blank if there are none.
  Similar-looking code that has not been confirmed as a bug goes elsewhere.

Order rows by impact, highest first, then by likelihood.

## 5. Deprioritized

Threats that were considered and set aside, and why.

| threat | reason |
|---|---|

## 6. Open questions

A bullet list. After a bootstrap these are questions for an owner. After an
interview these are owner statements the code did not confirm.

## 7. Provenance

```markdown
- mode: bootstrap | interview | guided   (append "+ refresh" after a refresh)
- date: YYYY-MM-DD
- target: <path or repo url> @ <commit>
- inputs: <design doc | --vulns path | none>
- owner: <name> | unset
- profile: <path to the .oko/ used> | defaults
- generator: oko <version>
```

## 8. Recommended mitigations

Each row is a single control that addresses a whole class of threat, not a
fix for one bug.

| mitigation | threat_ids | closes_class | effort |
|---|---|---|---|

- `threat_ids`: comma-separated section 4 IDs.
- `closes_class`: `yes` or `partial`.
- `effort`: `S`, `M`, or `L`.

## 9. Data flow diagram

A single fenced `mermaid` block. Draw each trust boundary as a `subgraph`, and
label nodes with section 3 and section 2 names.

## 10. Compliance mapping

| threat_id | framework | control_id | note |
|---|---|---|---|

## Default risk scale

The `scoring-risk` skill applies these. A team profile can replace them.

| impact | what it looks like |
|---|---|
| low | Annoying, but no data is lost and the service stays up. |
| medium | Some data exposed, or some users see degraded service. |
| high | Serious data exposure, corrupted data, or a full outage. |
| critical | An attacker fully controls a primary asset: code execution, auth bypass, bulk data theft. |
| existential | The organization might not survive it. |

| likelihood | what it looks like |
|---|---|
| very_rare | Needs state-level resources or a long chain of unlikely conditions. |
| rare | Needs real expertise and a non-default setup. |
| possible | A determined attacker with off-the-shelf tools could do it. |
| likely | The surface is reachable, the technique is common, and there is a track record here or in similar systems. |
| almost_certain | Already exploited in the wild, or scriptable against a default install. |

Score likelihood **after** existing controls.
