# Findings: staircase-allp-diophantine (2026-07-28)

Brief: `briefs/staircase-allp-diophantine-brief.md`. Target: the Diophantine
coverage gap named at `cycles.md` 12.8.6.1 as the **sole remaining gap** of the
floor-grade all-`p` staircase result, and the hedge it keeps alive in the
published `thm:staircase`.

**Base SHA.** The worktree was cut from `2225b68`, which does not contain the
brief. It was moved to the launch instruction's `main` SHA **`e0c34a9`**
("briefs: the all-`p` staircase reopened, in two independent halves") before any
work began; branch `staircase-allp-diophantine` starts there.

**Verification code.** `experiments/staircase_allp_diophantine.py`, written from
the statements alone. It imports nothing from `staircase_allp.py`,
`uniform_trim.py`, `p22_passer.py` or any other file here; the rotation-sum
evaluator is a second, structurally different implementation (Horner for `R_0`,
then the transport recurrence of 12.6.1.1 for every other rotation, with an
exact divisibility assertion at each transport step), and it reproduces the
published `p = 7` instance and the trivial-cycle identity `R = 4^p - 3^p`
independently. Committed output: `experiments/staircase_allp_diophantine.out`.

**Stopping-rule compliance.** PLACEHOLDER

---

## PLACEHOLDER — filled after the full run

