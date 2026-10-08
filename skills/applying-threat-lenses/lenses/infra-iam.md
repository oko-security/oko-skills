---
name: infra-iam
description: Cloud identity, access grants, and drift in infrastructure-as-code.
triggers:
  files: ["**/*.tf", "**/k8s/**/*.yaml", "**/deploy/**/*.yaml", "**/Dockerfile*", ".github/workflows/*.yml"]
applies_to: entry_points
---

# Infra and IAM

STRIDE was designed for request-handling code and doesn't map well onto
identities and permission grants. Use these questions for infrastructure
entry points.

| Category | Question |
|---|---|
| Excess permission | Does a role reach resources the workload never uses, such as a whole project instead of one bucket, or every table instead of one? |
| Shared identity | Do other workloads on the same node, namespace, or service account get this identity too? |
| Unmanaged grants | Are any permissions created by hand or in another repo, so this code's reviews never see them? |
| Leftover access | When something is renamed, migrated, or deleted, do its keys, tokens, or role bindings remain? |
| Over-broad reads | Does a query or export pull sensitive fields the workload doesn't need? |
| Automation limits | If a bot can approve, merge, deploy, or write, what restricts which paths, labels, or environments it can affect? |
| CI exposure | Can a fork or outside PR run code in a job that has secrets or a write-scoped token? |
