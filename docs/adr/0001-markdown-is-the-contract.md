# ADR 0001: THREAT_MODEL.md is a Markdown contract

**Status:** accepted (2026-10-07)

## Context

Threat models get read and edited by people during review, and they also get
parsed by other tools (scanners that take the model as scope, triage helpers,
CI drift checks). A JSON-first format would be easier to validate. It would
also be harder to review in a PR, and every downstream reader would need a
new parser.

## Decision

Markdown is the source of truth. Sections 1-8 have fixed headings, column
order, and enum values. oko only grows by adding optional sections (9 and up)
or new provenance keys. Existing columns and enum values never change.
`tm.py to-json` gives tools a machine-readable view.

## Consequences

- Before changing the schema, ask: "Would a parser written for v1 still read
  this file?"
- Teams may add their own actors or enum values, but the docs must say that
  this breaks strict parsers.
