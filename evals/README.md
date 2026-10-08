# Evals

Skills change how an agent behaves, so they need tests like any other code.
Before trusting a skill change, run the eval without it and confirm the
agent gets it wrong. Then run it with the change and confirm the agent gets
it right.

## Layout

```
evals/
├── rubric.md                 # judge-model grading rubric
└── targets/<name>/
    ├── src/                  # small, deliberately shaped target (TODO)
    └── expected.yaml         # must-find threats, must-not-find rows, coverage
```

## Planned targets

| target | shape | exercises |
|---|---|---|
| notes-api | Flask API + export worker + LLM summarizer | BOLA, SSRF, prompt injection, ai-agents lens |
| iam-terraform | Terraform for a data pipeline | infra-iam lens, drift, over-grant |
| media-parser | C single-header decoder with git history of CVE fixes | history mining, generalizing, evidence |
| agent-tools | MCP server exposing file + HTTP tools | excessive agency, exfil via tools |

## Running (TODO v0.1)

`scripts/run-evals.sh <harness> <target>` will run `/threat-model bootstrap`
headless (e.g. `claude -p`, `codex exec`, `gemini -p`), validate with
`tm.py`, then grade against `expected.yaml` with `rubric.md`. Track pass rate
per harness and skill version.
