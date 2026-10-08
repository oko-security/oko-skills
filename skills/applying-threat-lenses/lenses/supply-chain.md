---
name: supply-chain
description: Dependencies, build pipeline, and release integrity.
triggers:
  files: ["**/package-lock.json", "**/pnpm-lock.yaml", "**/poetry.lock", "**/Cargo.lock", "**/go.sum", "**/requirements*.txt", "**/vendor/**"]
applies_to: system
---

# Supply chain

| Category | Question |
|---|---|
| Dependency takeover | Are dependencies pinned by hash? Any typosquat-prone or unmaintained packages? |
| Build integrity | Can a PR or a compromised action alter release artifacts? Are builds reproducible or attested? |
| Install scripts | Do dependencies run code at install (`postinstall`, `setup.py`)? |
| Vendored code | Is vendored code tracked to an upstream version so fixes are pulled? |
| Release signing | Are artifacts signed, and do consumers verify? |
