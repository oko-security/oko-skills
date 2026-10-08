---
name: diagramming-data-flows
description: Use when drawing a data flow diagram (DFD), architecture-with-trust-boundaries diagram, or section 9 of a threat model. Produces a Mermaid flowchart whose nodes match the threat model's entry points and assets.
---

# Diagramming data flows

Output: one fenced `mermaid` block for section 9 (or a standalone `DFD.mmd`).

## Conventions

- `flowchart LR`.
- Each trust zone is a `subgraph` named for the zone ("Internet", "DMZ",
  "App VPC", "Data tier", "Third party").
- External actors: `([actor])`. Processes: `[process]`. Data stores: `[(store)]`.
- Edge labels name the protocol and data: `-->|HTTPS: login creds|`.
- Every edge that crosses a subgraph is a trust boundary and must match a
  section 3 row. Every data store must match a section 2 asset.
- Annotate top threats on edges: `-->|"gRPC: orders (T3, T7)"|`.

## Example

```mermaid
flowchart LR
  subgraph Internet
    U([remote user])
  end
  subgraph App["App VPC"]
    API[HTTP API]
    W[worker]
  end
  subgraph Data["Data tier"]
    DB[(orders DB)]
  end
  U -->|"HTTPS: requests (T1, T2)"| API
  API -->|SQL| DB
  API -->|queue: jobs| W
```
