# Grading rubric

Score each criterion 0-2. Pass = total ≥ 14 / 18 and no zero on criteria 1-3.

1. **Validity**: `tm.py validate` exits 0.
2. **Must-find recall**: every `must_find` threat in `expected.yaml` matched by
   a row with the same outcome, actor class, and surface (wording may differ).
3. **Abstraction**: no row matches a `must_not_find` pattern (vuln-level rows).
4. **Coverage**: every expected entry point has a threat or a section 5 reason.
5. **Grounding**: sampled controls and entry points cite real `file:line`.
6. **Evidence discipline**: evidence holds only confirmed past vulns.
7. **Ranking**: top 3 by I×L include the expected top threat.
8. **Mitigations**: at least one class-level mitigation per critical threat.
9. **Open questions**: the expected unanswerable questions appear in section 6.
