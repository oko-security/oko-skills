---
name: stride
description: Spoofing, Tampering, Repudiation, Information disclosure, Denial of service, Elevation of privilege.
triggers:
  always: true
applies_to: entry_points
---

# STRIDE

Work through each row for every entry point.

| Category | Question for this entry point |
|---|---|
| Spoofing | Can a caller claim an identity, origin, or signature it does not own? |
| Tampering | Can stored or in-flight data be changed by someone who shouldn't change it? |
| Repudiation | Could someone act here and later deny it, because nothing reliable records who did what? |
| Information disclosure | Can a caller see data, metadata, or errors meant for someone else? |
| Denial of service | Can one caller starve others of CPU, memory, storage, connections, or paid quota? |
| Elevation of privilege | Can a caller end up with rights they were never granted? |

## Typical reasons to rule a category out

- Repudiation: one user per deployment, or nothing needs an audit trail.
- Spoofing: the entry point has no concept of identity (for example, a pure
  computation library).
