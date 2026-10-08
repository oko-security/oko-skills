# Contributing

Read [CLAUDE.md](CLAUDE.md) first: it holds the rules for skill authoring.

| Contribution | Bar |
|---|---|
| New lens | Lens file + an eval target or `expected.yaml` entry it must catch |
| Skill change | Before/after eval run showing it helps (or does not regress) |
| New harness | Follow [docs/porting.md](docs/porting.md); include eval results |
| Schema change | Additive only; ADR + `tm.py` + `examples/` updated together |

Run `python3 scripts/validate.py` before opening a PR.
