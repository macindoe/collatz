# Brief: KL–LP density refinement (for a delegated session)

**Context required before starting (in order):** `README.md` (esp. the strategy/stopping rules), `AGENTS.md` (binding house norms), `reverse.md` §14.4–14.6 (the density program, the mortality/renewal analysis, and the base density theorem 14.6.4), and §8 of `paper/collatz-mirror-v1.tex` (the canonical five-lemma proof of the base bound). Reference paper: Krasikov–Lagarias 2002, `arXiv:math/0205002`.

## The state you are starting from

The reduced formalism already proves a self-contained density lower bound (Theorem 14.6.4):

```text
π̃(X) ≥ 2^(−3.6) · X^0.3,   critical exponent c* ≈ 0.3304.
```

That bound is deliberately *weak*: it was derived from a single-type door tree that throws away three resources the formalism actually possesses (stated in the 14.6 "Remark on position and the refinement path"):

1. **Doors.** The core uses **one** door per state; a state `(Ω,D)` has `D` doors, all but the `a=0` door provably alive (Theorem 14.5.1).
2. **Residue types mod 3^k.** The core tracks door residues only mod 3 (the triple law 14.6.2, "two of three kept"). KL's strength comes from difference-inequality systems over residues mod `3^k` (they use `3^11`).
3. **Anchor phases.** The core places the anchor phases *adversarially* (worst-offset tiling). But the anchor law 14.2.4 gives the branching **exactly**, not as a bound — this is the one structural asset KL's difference inequalities do not have.

The heuristic full-tree renewal mass (14.5.3) has minimum ≈ 1.52 at `c ≈ 0.7` and predicts full density (exponent 1). So there is real, quantified headroom between the rigorous 0.30 and the heuristic ~1. This brief is the program to convert some of that headroom into a rigorous exponent.

## Task

Reinstate the three discarded resources into a *fully rigorous* density argument, structured as a linear program over the reduced formalism's exact branch inventory — mirroring Krasikov–Lagarias, but with the anchor law supplying exact local branching where KL used inequalities. Push the rigorous exponent up, one resource at a time, and either clear the success bar or record the obstruction precisely.

## Queue, in order (each stage stands alone; stop when the criterion is met)

1. **Multi-door renewal, rigorously.** Replace the single-door core with the full door inventory of each state (all `D` doors, `a=0` mortality per 14.5.1), keeping everything truncated and rigorous (no measured/stationary inputs — those are heuristic and belong to 14.5.3, not here). Recompute the rigorous critical `c`. Expected: a clean lift above 0.30. State it as a theorem extending 14.6.4; verify the renewal mass and the truncation bookkeeping with fresh code.

2. **Residue types mod 3^k, as an LP.** Refine the mod-3 triple law (14.6.2) to a difference-inequality / branch-count system over door residues mod `3^k` for small `k` (start `k=2`, then `k=3`). Set it up as a linear program in the KL sense — variables are the per-residue-type branch masses, constraints are the exact local branching relations. Solve the LP (an actual solver: `scipy.optimize.linprog` or equivalent) for the best rigorous `c` at each `k`. Report the exponent as a function of `k`.

3. **Exact anchor phases.** Replace the adversarial worst-offset phase placement with the *exact* phase distribution given by anchor law 14.2.4. This is the point of the whole program — determine whether exact branching (vs. KL's bounded branching) tightens the LP. Fold it into the stage-2 LP as equality constraints where the law pins a phase, inequalities where it does not.

## Explicit success / stop criterion (this is the point of writing a brief)

- **Primary success:** rigorously beat **c = 0.43** (Krasikov 1989) — i.e., prove `π̃(X) ≥ const · X^c` with `c > 0.43`, fully self-contained, verification recorded.
- **Stretch:** approach or beat **c = 0.84175** (Krasikov–Lagarias 2002). Reaching this answers, in the affirmative, the open question posed at the end of 14.6's remark ("whether exactness buys anything beyond 0.84").
- **Stop / obstruction (equally valid outcome):** if the LP saturates below the bar even with all doors, residues mod `3^k`, and exact anchor phases, **stop and record the obstruction precisely** — which constraint binds, which resource fails to help, and specifically whether the *exact* anchor law improves the LP optimum over the same LP with only KL-style inequalities. A clean negative ("exactness does not beat size-counting for tree density, and here is the binding constraint") is a publishable result and closes the front honestly. Do not grind `k` upward indefinitely chasing decimals — if the marginal gain per `k` flattens well short of the bar, that flattening *is* the finding; report the trend and stop.

## Rules (non-negotiable, from AGENTS.md)

- Every "proved" claim gets an **independent** numerical check — fresh code, not the code that suggested the result. Record what was checked, the range, seeds, and the date, in `reverse.md` and in the AGENTS.md verification record.
- Distinguish rigor levels explicitly: this front's output must be *rigorous* (truncated, worst-case). Any heuristic/measured input (like the stationary depth law) may guide exploration but may **not** enter a claimed bound — keep those in 14.5.3's register, not here.
- Failures and dead ends are recorded, not deleted (the 14.4 recorded failure — single-type equation ignoring door multiplicity — is the precedent; do not regress into it).
- **Numbering:** new results extend `reverse.md` as **14.6.5+** for incremental lemmas, or open a new section **14.13 "The KL–LP refinement"** if volume warrants. Never renumber existing anchors (14.6.1–14.6.4 are fixed citations).
- Work on branch **`kl-lp`**, commit per lemma/stage with the verification in the same commit, and **do not merge to main** — the main session reviews and re-runs all verification code before merging (the mirror-queue precedent: ~50k checks re-run in review).
- LP code goes in `experiments/` (suggested `experiments/density_lp.py`), states which result it supports, stays runnable, and pins the solver + seeds so the review session reproduces the optimum.
- No scope expansion. If something interesting-but-off-brief appears, log it in `briefs/kl-lp-findings.md` and continue.

## Definition of done

Either (a) a rigorous theorem `π̃(X) ≥ const · X^c` with `c` past the success bar, stated in `reverse.md`, proved, verified with recorded counts, on branch `kl-lp` with clean per-stage commits and the LP code committed; **or** (b) a precisely stated obstruction — the LP formulation, its rigorous optimum as a function of `k`, the binding constraint, and the exact-vs-inequality comparison — recorded the same way. Both outcomes end with an honest status paragraph and a one-line update to the 14.6 remark's open question.
