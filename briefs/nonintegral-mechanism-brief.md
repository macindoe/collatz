# Brief: the non-integral mechanism identities, upgraded to theorems (for a delegated session)

**Context required before starting (in order):** `README.md` (strategy and **binding stopping rules**), `AGENTS.md` (house norms), `reverse.md` §14.14.8 (composed affine maps), §14.15.1.4–.5 (forward cylinder class, an iff), §14.15.4–14.15.6 (heights, admissibility class, signed apparatus), §14.15.7 entire (the integer-fixed-point mechanism lemma — this brief is its non-integral sibling), and `briefs/h-nonintegral-probe-findings.md` (the merged empirical probe whose four §3 identities are exactly what you will prove).

## Provenance and authorization

The probe (merged 2026-07-17) confirmed its hypotheses P1–P3 on all seven non-integral-fixed-point single-letter words, both sectors, `n = 1..25`, and recorded its four mechanism identities as *verified empirical identities, not theorems*, with the labeled heuristic that they "look provable in a few lines from the already-proved class iffs." The author authorized exactly that upgrade 2026-07-17. This brief converts the probe's §3 identities into proved statements; it adds no new empirical scope.

## The framing mandate

Formulation grade on the decided shelf, exactly as `14.15.7`: these theorems close the *non-integral single-letter* shelf the way `14.15.7` closed the integer one. The honest headline: *on every periodic single-letter word, height growth is now a theorem — escape at the CRT-modulus rate, with a constant that is either the fixed point itself (integer case) or a purely periodic, denominator-bounded unit-orbit value (non-integral case).* The Bridge (bridge.md §16) is unmoved; the rigidity content of height growth now provably begins at aperiodic words (and at whatever the multi-letter empirical probe, running separately, finds — do **not** coordinate with branch `multiletter-h-probe`, read it, or anticipate it).

## Setup and the proof route (main-session guidance; own the proofs yourself)

Fix a single letter `(m,r)` with non-integral fixed point `y* = a/q` in lowest terms (`a = (3^m−2^m)/gcd`, `q = (2^{m+r}−3^m)/gcd`, `q ∤ 1`, `gcd(q,6) = 1` — prove this last fact, it is one line). `Q_n = 2^{(m+r)n+1}·3^{mn}`, `g := 2^{m+r}·3^m mod q`.

1. **The class.** `R^σ_{n,n}` is exactly `{y ≡ ρ_n (mod Q_n)}` ∩ sign ∩ liveness(`y₀`) ∩ liveness(deepest door), where `ρ_n := a·q^{−1} mod Q_n` (the CRT lift of `y*` as a `2`-adic and `3`-adic integer). Suggested route: (i) forward — the follower class of the length-`n` prefix (14.15.1.5, an iff) has representative `≡ y*` in `Z₂`, by re-running `14.15.7.1`(2)'s forced-valuation algebra `2`-adically (`y*+1 = 2^m(2^r−1)/d` with `(2^r−1)/d` a `2`-adic unit since `d` is odd; `3^m q^* − 1 = 2^r y*` with `y*` a `2`-adic unit); (ii) backward — the admissibility class (14.15.5.1/14.15.6.4) is `B_n mod 3^{M_n}`, and `y* ≡ B_n (mod 3^{M_n})` because `y* = B_n/(1−A_n)` with `v₃(A_n) = M_n`, so `(1−A_n)^{−1} ≡ 1 (mod 3^{M_n})`; (iii) CRT. State the analogous claim over the signed domain (both sectors), as `14.15.7.2` does.
2. **Identity 1 (probe §3.1).** Writing `ρ_n = (a + j_n Q_n)/q` with `j_n ∈ {1,…,q−1}` (prove: well-defined, `j_n ≠ 0` since `q ∤ a`... state exactly), `j_n = −a·2^{−1}·g^{−n} mod q` (from `Q_n ≡ 2g^n mod q`), purely periodic in `n` with period **exactly** `ord_q(g)` (injectivity of the `g`-orbit on the coset).
3. **Identity 2 (probe §3.2).** The deepest door of the `k`-th lift: `y_{−n}(k) = (a + (j_n + σkq)·2^{2(m+r)n+1})/q` — derive via `y_{−n} = y* + (y₀ − y*)/A_n` exactly as `14.15.7.2`(3), now with rational `y*`; and mod 3 it is `t_n + 2σk`, `t_n := (a + 2j_n)·q^{−1} mod 3` (note `2^{2(m+r)n+1} ≡ 2 (mod 3)` again).
4. **Identities 3–4 (probe §3.3–3.4).** Exactly one `k`-class mod 3 dies per sector; the first-viable rule `k⁺ = [t_n = 0]`, `k⁻ = 1 + [t_n = 2]`; hence the closed forms `H⁺_{n,n} = ρ_n + [t_n = 0]·Q_n` and `H⁻_{n,n} = (1 + [t_n = 2])·Q_n − ρ_n`, and the three corollaries: **pure periodicity** of `v_n := H/Q_n − σa/(qQ_n)` from `n = 1` with period `ord_q(g)` (P1); the **lower bound** `v_n ≥ 1/q`, sharp constant `j_min/q` over the visited coset orbit (P2); **`k` bounded** by one extra step (P3). Mind the same care `14.15.7.2`(4) took with signs and with which candidates belong to which sector.
5. **Reconciliation, one paragraph.** (a) Against `14.15.7`: the integer case is the degenerate `q = 1` (no `j_n`, offset `y*` itself); state how the two closed forms are one law. (b) Against the probe: cite `briefs/h-nonintegral-probe-findings.md` as the empirical precursor whose tables (350 rows, `n ≤ 25`) now sit under proof; its "verified empirical identities" caveat is discharged by this section.

## Queue, in order

1. New subsection **14.15.8** in `reverse.md` (14.15.1–14.15.7 merged and closed, never edited or renumbered): the class theorem (item 1 above) and the four identities as one theorem block with the corollaries (items 2–4), in `14.15.7`'s structure and register.
2. The reconciliation paragraph (item 5).
3. Accounting and closing status, extending the chain: the whole single-letter periodic shelf is now closed by theorems; the Bridge unmoved; height rigidity content begins beyond periodic single-letter words.
4. Status sweep per AGENTS.md: reverse.md front matter (≤1 clause, within the ≤3-line norm, re-dated), index.md reverse row + status paragraph (≤1 clause each), HANDOFF.md reverse bullet (≤1 clause; fold into the existing 14.15.7-and-probe clause rather than appending a fourth parallel clause — keep it one sentence).

## Success / stop criteria

- **Floor (expected):** queue items 1–2.
- **Primary:** items 3–4.
- **Stop:** after item 4, stop. Explicitly forbidden: any multi-letter word (empirical or proved — that is the parallel brief's scope); any aperiodic word; any new `H` computation beyond what verification of the stated theorems requires on the probe's own seven words; any cycle-exclusion or equidistribution attempt. Off-brief findings go to `briefs/nonintegral-mechanism-findings.md`; log them and stop anyway.

## Rules (non-negotiable, from AGENTS.md)

- Every proved claim gets an **independent** numerical check — fresh code in `experiments/nonintegral_mechanism.py`, importing nothing from `h_nonintegral_probe.py`, `height_exact_laws.py`, `realization_height.py`, `diagonal_converse.py`, `signed_diagonal.py`, `itinerary_coding.py`, `block_map.py`, or `door_seam.py`. Exact integer/`Fraction` arithmetic at every pass/fail decision. Must include: the class theorem checked exhaustively over full modulus widths at small `n` (both directions of the iff, both signs); the four identities against direct simulation on all seven words, both sectors, a range at least matching the probe's `n ≤ 25`; brute-force minimality at `n = 1, 2` on at least four word/sector pairs.
- Record what was checked, the range, seeds, and the date, inline in the owning section. Failures and obstructions recorded, not deleted. If any identity resists proof, record precisely where and stop that item rather than forcing it — a genuine obstruction here would be a real finding.
- Register norm: flat, calibrated prose. Closures of an empirical record, not leverage.
- Work on branch **`nonintegral-mechanism`** (create in your worktree from current HEAD), commit per queue item, verification in the same commit. Do **not** push or merge — the main session reviews and re-runs everything before merging.
- No scope expansion.

## Definition of done

§14.15.8 with the class theorem, the four identities and three corollaries proved and independently verified; the reconciliation paragraph; closing status; the ≤1-clause sweep; clean per-item commits on `nonintegral-mechanism` with `experiments/nonintegral_mechanism.py` passing.
