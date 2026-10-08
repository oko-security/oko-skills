---
name: my-lens
description: One line on what class of threats this lens surfaces.
triggers:
  files: ["**/*.example"]      # globs; lens runs if any match
  imports: ["some_sdk"]        # identifiers searched in source
  always: false                # true = run on every target
applies_to: entry_points       # entry_points | assets | system
---

# <Lens name>

Short paragraph: when this lens matters and what it catches that STRIDE misses.

| Category | For this <entry point/asset>, could an attacker... | Typical actor |
|---|---|---|
| ... | ... | ... |

## Ruled-out reasons (for section 5)

- <Category>: not applicable when <condition>.
