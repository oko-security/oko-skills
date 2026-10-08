---
name: ai-agents
description: Threats specific to LLM-backed features and autonomous agents (prompt injection, excessive agency, tool misuse).
triggers:
  imports: ["anthropic", "openai", "langchain", "llama_index", "@anthropic-ai", "ai", "mcp"]
applies_to: entry_points
---

# AI agents and LLM features

TODO(v0.2): align categories with the current OWASP Top 10 for LLM
Applications and the OWASP agentic threats taxonomy; cite versions.

| Category | Question |
|---|---|
| Indirect prompt injection | Does untrusted content (web pages, files, emails, tickets, tool output) reach the model's context? |
| Excessive agency | Can model output trigger tools with side effects (write, send, pay, deploy) without human confirmation? |
| Insecure output handling | Is model output passed to a sink (SQL, shell, HTML, file path, URL fetch) without validation? |
| Data exfiltration via tools | Can the model be steered to send context to an attacker-chosen URL or recipient? |
| Sensitive info in context | Do secrets, other users' data, or system prompts sit in context an attacker can elicit? |
| Tool / MCP supply chain | Are third-party tools or MCP servers trusted with credentials or broad scopes? |
| Cost / DoS | Can an attacker drive unbounded tokens, loops, or tool calls? |
