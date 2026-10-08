---
name: generalizing-threats
description: Use when turning a list of vulnerabilities, bugs, CVEs, or pentest findings into threat-model threats, or when a threat statement reads like a single bug and needs zooming out. Groups findings by entry point, weakness class, and asset; applies the patch test; estimates how widespread a weakness is from look-alike code.
---

# Generalizing threats

**Patch test:** suppose every item in the evidence column were fixed tomorrow.
If the threat sentence would then be false, it describes a bug, not a threat.
Make it broader until it would still be true.

## 1. Group

Bucket the past issues by three keys: the entry point they came through, the
kind of weakness, and the asset they reached. Each bucket becomes **one**
candidate threat.

- Two path-traversal fixes in the upload handler and one in the avatar
  resizer, all writing outside the media directory → "Arbitrary file write
  on the app server through user-supplied file names".
- An IDOR on `/invoices/<id>` and another on `/reports/<id>` → "Users read
  other tenants' billing data through unscoped object lookups".

## 2. Look for relatives

For each bucket, search for code with the same shape that is not in the issue
list: other handlers that build paths from user input, other routes that
fetch by ID without a tenant filter. The goal is to see how far the pattern
spreads, not to confirm new bugs. The more relatives you find, the higher the
likelihood.

Record relatives in your working notes and in the report to the user. They
**never** go in `evidence`.

## 3. Write the row

Fill in `threat` (one active-voice sentence naming the result), `actor`,
`surface`, `asset`, and `evidence` (the bucket's IDs). Scoring is left to
`scoring-risk`.

## Common mistakes

| Draft | What's wrong | Better |
|---|---|---|
| "Integer overflow in `read_chunk()`" | One bug | "Worker takeover through crafted archive uploads" |
| "No rate limit on /login" | One missing control | "Account takeover through credential stuffing on the login endpoint" |
| "Hackers could break in" | No actor, surface, or result | Name all three |
