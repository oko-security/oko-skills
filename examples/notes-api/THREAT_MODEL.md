# Threat Model: notes-api

## 1. System context

notes-api is a small multi-tenant HTTP service (Python/Flask) that lets
signed-in users create, share, and export notes. It runs as a container
behind the org edge WAF, stores notes in Postgres, and renders exports to PDF
through a worker that fetches embedded images by URL. An LLM summarizer
endpoint summarizes a note on request.

## 2. Assets

| asset | description | sensitivity |
|---|---|---|
| notes DB | All tenants' notes and share links | high |
| session tokens | Signed cookies identifying users | critical |
| worker network position | Worker can reach the internal VPC and cloud metadata | high |
| LLM API key | Key for the summarization provider | medium |

## 3. Entry points & trust boundaries

| entry_point | description | trust_boundary | reachable_assets |
|---|---|---|---|
| HTTP API /notes/* | CRUD on notes (app/routes.py:12) | unauth network → authenticated session | notes DB, session tokens |
| HTTP /share/<token> | Public read of shared notes (app/routes.py:88) | unauth network → notes DB | notes DB |
| export worker | Fetches image URLs found in notes (worker/export.py:30) | user-controlled URL → internal network | worker network position |
| /notes/<id>/summarize | Sends note text to an LLM (app/llm.py:15) | user content → model context | notes DB, LLM API key |

## 4. Threats

| id | threat | actor | surface | asset | impact | likelihood | status | controls | evidence |
|---|---|---|---|---|---|---|---|---|---|
| T1 | Cross-tenant note access via broken object-level authorization | remote_auth | HTTP API /notes/* | notes DB | high | likely | partially_mitigated | owner check in app/routes.py:20 on read only | a1b2c3d |
| T2 | Internal network and metadata access via server-side request forgery in exports | remote_auth | export worker | worker network position | critical | possible | unmitigated | none | |
| T3 | Data exfiltration via indirect prompt injection in summarized notes | remote_auth | /notes/<id>/summarize | notes DB | medium | possible | unmitigated | none | |
| T4 | Enumeration of shared notes via guessable share tokens | remote_unauth | HTTP /share/<token> | notes DB | medium | rare | mitigated | 128-bit tokens app/share.py:9 | |

## 5. Deprioritized

| threat | reason |
|---|---|
| Repudiation on note edits | No audit requirement; single-owner notes |
| Generic web attacks on public HTTP | Covered by edge-waf (.oko/controls.md) as defense in depth; T1-T4 still scored without it |

## 6. Open questions

- Does the worker run with an instance identity that can read cloud metadata?
- Is the share-token endpoint rate limited at the edge?

## 7. Provenance

- mode: bootstrap
- date: 2026-10-07
- target: examples/notes-api @ (illustrative)
- inputs: none
- owner: unset
- profile: defaults
- generator: oko 0.1.0

## 8. Recommended mitigations

| mitigation | threat_ids | closes_class | effort |
|---|---|---|---|
| Enforce tenant scoping in the data-access layer, not per route | T1 | yes | M |
| Egress allowlist and metadata block for the export worker | T2 | yes | S |
| Treat summaries as untrusted output; no tools or links in summarizer | T3 | partial | S |
