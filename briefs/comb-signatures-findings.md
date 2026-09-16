# Findings: branching signatures (comb.md 18.9)

Delegated session, branch `comb-signatures`. Supports `briefs/comb-signatures-brief.md`.

## Base SHA and branch

The worktree's HEAD at spawn was `a7543ce` (2026-09-13), which predates the brief (`briefs/comb-signatures-brief.md` did not exist there). `a7543ce` is an ancestor of local `main`, so `main` was a clean fast-forward: `main` at spawn time was `d54dc153b06cfbc3067d82ad826fb60c090f5edb` (2026-09-17), the brief's own delegation commit, with no divergent work on the worktree's own branch to rebase.

**Base SHA: `d54dc15`.** `comb-signatures` was cut directly from that commit.

## Notation

As on comb.md: a node `v = (Ω,D)` has peak `A = 3^DΩ − 1 = 2^s y`, `s = v₂(A)`, `y` the exit; doors `y_a = 2^{D−a}3^aΩ − 1`, `a = 0,…,D−1` (live iff `3 ∤ y_a`); `node(y,s)` is the state at branch `s` on door `y`, `2^s y + 1 = 3^d ω` exactly; the comb children of `v` are its unique cascade child (branch `s+2` on `v`'s own door `y`) and one door child per live door, at the lowest admissible branch (`s₀ = 1` if `y_a ≡ 1 (mod 3)` else `2`) — Proposition 18.2.3.

## Item A — the level-1 branching laws, derived

**The four laws.** The cascade child is Theorem 14.10.1 applied with `d = D` (the node's own depth in the role of that theorem's `d`): its `D ≥ 2` branch gives cascade-child depth exactly `1`; its `D = 1` branch gives `1 + v₃(4Ω − 1)`. Nothing new — the identification is verbatim.

For the door children, `y_a + 1 = 2^{D−a}3^aΩ`, so for `a ≥ 1` this is `≡ 0 (mod 3)`: `y_a ≡ 2 (mod 3)` always, forcing the lowest admissible branch `s₀ = 2` (Lemma 18.1.2(iii); `y ≡ 2 (mod 3)` takes even branches). The door child's numerator at branch `2` is

```text
4y_a + 1 = 4(2^{D−a}3^aΩ − 1) + 1 = 2^{D−a+2}3^aΩ − 3 = 3·(2^{D−a+2}3^{a−1}Ω − 1),  a ≥ 1,
```

so its depth is `1 + v₃(bracket)`, bracket `= 2^{D−a+2}3^{a−1}Ω − 1`. For `a ≥ 2` the bracket itself has a factor `3` inside it (`a − 1 ≥ 1`), so bracket `≡ −1 (mod 3)`, `v₃(bracket) = 0`, and the child's depth is exactly `1` — **unconditionally**, with no dependence on `Ω` beyond the fact that the door is live (which is itself unconditional for `a ≥ 1`). For `a = 1` the bracket is `2^{D+1}Ω − 1` (`a − 1 = 0`, no forced factor of `3`), giving depth `1 + v₃(2^{D+1}Ω − 1)` — genuinely `Ω`-dependent.

For `a = 0` (the top door, alive iff `2^DΩ ≢ 1 (mod 3)`): `y₀ = 2^DΩ − 1` carries no forced residue mod `3` at all, so `s₀ ∈ {1,2}` is a real function of `Ω mod 3`; the numerator is `2^{s₀}y₀ + 1 = 2^{s₀+D}Ω − (2^{s₀} − 1)`, and its `v₃` is the depth.

**The corollary.** Liveness of the `a ≥ 1` doors is unconditional; liveness of the top door and its branch `s₀` are functions of `Ω mod 3`; every `a ≥ 2` depth is `1` regardless of `Ω`; the `a = 1` depth, the top-door depth, and (at `D = 1`) the cascade depth are, capped at `J`, functions of `Ω mod 3^J` — because `4`, `2^{D+1}` and `2^{s₀+D}` are units modulo every power of `3`, agreement on `Ω mod 3^J` pins the corresponding numerator mod `3^J`, which pins its `v₃` whenever that is `< J` and pins "`≥ J`" otherwise (an easy but load-bearing fact: it is exactly why a *capped* label needs no more than `J` digits, the base case Item B's budget composition relies on).

**The reconciliation with 18.5.** Under the depth ledger `P(D=j) = 2·3^{−j}`, `E[D] = Σ_j j·2·3^{−j} = 2·(1/3)/(1−1/3)² = 3/2`. The mean number of `a ≥ 2` doors per node is `E[(D−2)^+]`: writing `E[D·1_{D≥3}] = E[D] − 1·P(1) − 2·P(2) = 3/2 − 2/3 − 4/9 = 7/18` and `P(D≥3) = 1 − 2/3 − 2/9 = 1/9`, `E[(D−2)^+] = 7/18 − 2/9 = 3/18 = 1/6`. The mean number of live doors is `E[D] − P(top dead) = 3/2 − 1/2 = 1` (14.5.1's `1/2`), so the `a ≥ 2` doors are `1/6` of a node's door children on average — a minority, as the brief anticipated. Measured on the level-`18` census: `20,431 / 123,439 = 0.1655` against `1/6 = 0.1667`.

**Pre-check vs re-derivation.** The pre-check's four laws and its `13,485`-check figure are reproduced in substance: this session's own re-derivation (above) and its independent code (`5,000` states, `0` failures) confirm all four laws exactly as the brief stated them, with no correction needed to Item A's mathematics.

## Item B — the signature and its digit budget, derived

**The signature (Definition 18.9.2.1).** As specified in the brief, with one clarification made explicit on the page: a live door's label carries `(a, s₀, capped-depth, sub-signature)`, a dead door carries `dead`, and the root's own excluded self-loop carries no label at all (not even `dead`) — it is simply absent from the tuple, matching how the parent rule (18.2.1) treats it.

**The budget (Proposition 18.9.2.2) — three digit facts.** (a) `y_a mod 3^m` is a function of `Ω mod 3^{m−a}`: from `y_a + 1 = 2^{D−a}3^aΩ` and `2^{D−a}` a unit mod every power of `3`. (b) The node's own exit `y mod 3^m` is a function of `Ω mod 3^{m−D}`: `y = (3^DΩ − 1)/2^s` exactly, `2^s` a unit mod `3^m`. (c) Exact division: for a child born at branch `s′` on a door `z` (`2^{s′}z + 1 = 3^{d′}Ω(c)` exactly), `Ω(c) mod 3^n` is a function of `z mod 3^{n+d′}`. Composing (c) with (a) (door edge) or (b) (cascade edge) gives exactly the stated `cost` formulas, `d′ − a` and `d′ − D(v)`.

**The capped-cost bug, found and fixed.** The first implementation used the *capped* label `min(d′,J)` uniformly in `cost`, at every recursion depth `k`, reasoning that the signature only ever records depths up to `J` so no more digits should ever be needed. This is wrong once `k ≥ 2`: knowing a child's depth is "`≥ J`" costs only `J` digits (Item A's corollary), but *continuing the recursion into that child* requires reconstructing `Ω(c)` itself, which goes through exact division by `3^{d′}` with `d′` the child's **real**, uncapped depth — a quantity the capped label does not determine. The bug surfaced exactly where it should: the sufficiency check (constructing `Ω′ ≡ Ω (mod 3^{χ(v,k)})` and checking equal signatures) found `0` failures at `k=1` (where capping is exact, since the recursion stops) but `4/1500`, `31/1500`, `84/1500` failures at `k=2,3,4` respectively. The fix — use the real depth whenever `k ≥ 2` (the recursion continues past the child), the capped label only at the base case `k = 1` — is exactly what the proof requires, and resolved all failures: `0/1500` at every `k ≤ 4` after the fix. This is the one correction to the brief's own claim: the brief's cost formula, read literally with `d′` always "the child depth," is ambiguous between real and capped, and only the real-depth reading composes correctly past `k = 1`.

**Measured.** Sufficiency `1,500/1,500` at every `k ∈ {1,2,3,4}`; mean `χ` `3.00, 3.75, 5.26, 6.86`; max observed `χ` `3, 8, 13, 14`; the "one digit fewer" lift differs at `185/1500, 305/1500, 347/1500, 373/1500` — a growing but always-minority fraction, matching the pre-check's own finding that the budget is sufficient but not sharp per node.

## Item C — the exact signature modulus, derived

**Definition and search.** `ψ(v,k)` is the least `M` with `Ω(v) mod 3^M` alone sufficient. Since sufficiency at `M = χ(v,k)` is already established, the search is confined to `M ∈ [0, χ(v,k)]`, and monotonicity (sufficiency at `M` implies sufficiency at every `M′ ≥ M`, trivially — fixing more digits can only shrink the candidate set) makes "least sufficient `M`" well defined.

**The caution the brief asked for.** The brief's own phrasing ("there are only two other residues to test at each candidate `M`") suggests a cheap test: flip only `Ω(v)`'s own digit at position `M−1`, holding every other digit — including digits *above* `M`, up to `χ(v,k)−1` — at `Ω(v)`'s actual value, and check whether the signature changes. This is **not** proved sufficient here, and was not assumed: such a test only certifies `ψ(v,k) > M−1` when it finds a difference (a valid necessary condition), but does not certify sufficiency at `M` for the *whole* coset `{Ω′ ≡ Ω(v) mod 3^M}` — a digit that happens to be irrelevant against `Ω(v)`'s own particular higher digits could still matter against some other combination of them, and the cheap test never explores that. The record computes `ψ(v,k)` by the full, proven-correct search instead: at each candidate `M`, every one of the `3^{χ(v,k)−M}` completions of the low-`M`-digit prefix (realized as an actual odd, `3`-coprime integer congruent mod `3^{χ(v,k)}`) is tested. This is exact, not a heuristic, and the brief's cheap test is neither used nor claimed correct.

**Measured.** Level-based sample (`k=2`, `J=3`; up to `2,000` nodes per level, `478` at level `10`, `8,456` nodes total): `χ − ψ ∈ {0,1}` in every sampled node — no case needed more than one extra digit beyond the exact minimum. Mean slack `0.631` overall (`0.62`–`0.68` per level); `χ = ψ` exactly in `37%` of nodes. The search was never capped (largest realized `χ` in this sample was well under the `60,000`-completion cap, i.e. `χ ≤ 14` throughout, `3^{14}` far under the cap only at the smallest `M` tested, and no candidate `M` in the run actually required exploring that many completions before finding a disagreement or exhausting the search). The measurement settles the *size* of the slack, not its cause; no attempt was made to isolate which structural feature (a capped depth, or a non-binding path in the `max`) accounts for it in any specific node.

## Item C — the search, derived and measured

**C.1 Coincidences.** Restricted to `D = 1` (the ledger's most populous class, `2/3` of nodes) at `k = 2`, per level: sample up to `1,500` nodes, compute each one's exact `ψ` and its residue class `(ψ, Ω mod 3^ψ)`. Nodes in the *same* class trivially share a signature (that is what `ψ`-sufficiency means, and the record checks it holds at every sampled node — `0` violations). The interesting count is *different*-class same-signature pairs: `C(C−1)/2` many candidate class-pairs among `C` distinct classes, of which the observed same-signature count is compared against a birthday-style independence baseline `C(C−1)/2 · Σ_s q_s²`, `q_s` the fraction of the `C` classes carrying signature `s` — the expectation under the (null) model that each class's signature were an i.i.d. draw from the observed marginal, rather than the deterministic image it actually is. At every level the observed count sits at or below the baseline (level `18`: `23` observed against `48.06` predicted; every level near half). No level shows an excess. **Reading: a clean negative — no grouping finer than the exact residue classes predicts branching, at any tested level.**

**C.2 The 2-adic probe.** Nodes grouped by `(D, ζ_1^J)`; within each group of `≥ 20` members, `Ω mod 2^m` (`m ∈ {4,6,8}`) tested via a standardized (Pearson) residual per cell against the `D`-matched population marginal. The `D`-matching is a methodological correction made during this session: an earlier version compared against the *level's whole* marginal (mixing all `D` values), which produced large, clearly spurious deviations (the worst residual reaching `46.48` against a Bonferroni threshold of `5.11`) — because `D` is already part of the grouping key, so a `D`-mixed baseline mostly detects "`D` correlates with `Ω mod 2^m`," an unsurprising and uninteresting fact, not a residual dependency past the signature. Re-run against the `D`-matched marginal, the largest residuals collapse to the noise floor: over `15` (level, `m`) combinations, only `2` exceed the Bonferroni-corrected threshold at `α = 0.01` (`5.83` vs `4.96` at `λ=14,m=8`; `5.18` vs `5.11` at `λ=18,m=8`), neither growing nor recurring across nearby `m` or levels — consistent with the false-positive rate expected from testing thousands of cells. **Reading: a clean negative, at the sampling noise floor — the same reading as ladder.md 15.6.7's own tear-line measurement.**

**C.3 Signature ledgers.** (a) Distinct signatures vs distinct `(D, Ω mod 3^χ)` classes, using the cheap sufficient `χ` (not the exact `ψ`, for whole-census affordability): always more classes than signatures (`19`/`66` at level `10` to `40`/`157` at level `18`), the gap being exactly what C.1 measures directly on a sample. (b) A product-law prediction for depth-1 signature frequency (each valuation an i.i.d. draw from the canonical law `P(v₃=t) = 2·3^{−(t+1)}`, `D` from the ledger, the top door alive with probability `1/2` and — matching the census's own unweighted `1:1` split, not the ledger's forward-visit-weighted `2:1` — `s₀ ∈ {1,2}` with probability `1/2` each given alive) was built and tested against three populations: the predicted values themselves, the uniform box (`Ω < 5·10^4`, `D ≤ 30`, `60,000` draws — 18.5's own comparison population), and the level-`18` census. The **box** matches the product law only to within an order of magnitude (ratios `0.07`–`2.8` across the top eight level-`18` shapes) — the several joint `v₃`-valuations of one `Ω` are not exactly independent even under a "generic" reading, itself an unsurprising fact and not what this item searches for. The **census** deviates from the product law much further, and in the direction 18.5's own run-length table already names and explains structurally (every node has exactly one cascade child, so the census over-represents shapes reached by short cascade runs) — nothing new. (c) The window ledger: `8` random doors, window widths `9` (`k=2`) and `27` (`k=3`). The **depth-label multiset** across the window's nodes is *exactly* door-independent at both `k` (identical across all `8` doors, `0` failures) — the depth part of 14.6.5.2's exact ternary ledger, confirmed once more in comb language. The **full depth-1 signature multiset** is *not*: `7` of `8` windows differ at `k=2`, `5` of `8` at `k=3`. **Reading: a precise, not merely negative, answer — the window ledger is exact one level down (the depth alone) and only statistical past it (the full branching shape); no new exact law lives at this seam.**

**The one open measurement, answered.** All three sub-items point the same way: no grouping of comb states finer than the residue classes `(D, Ω mod 3^{χ(v,k)})` — nor their exact refinement `(D, Ω mod 3^{ψ(v,k)})` — was found to predict branching, at any tested level or depth. This matches ladder.md 15.6.7's prior exactly, and the section states it as a result rather than an absence of one.

## Verification record

`experiments/comb_signatures.py`, fresh code (imports nothing from any other file in this repository — `peak_comb.py`, `comb_dictionary.py`, `signed_comb.py` were read only for output-formatting convention, never imported or copied). Exact Python-integer arithmetic at every pass/fail decision; floats only in printed ratios, frequencies and significance figures. Canaries first. Seed `20260917`; date 2026-09-17.

Sections and counts (from the committed `experiments/comb_signatures_output.txt`):

- **Canaries** (`17` checks): the children of `(7,3)`, `(1,2)`, `(5,2)` against the four laws by name; a hand-worked signature of `(1,2)` to depth `2`, cap `J=3` (`B=3`); the depth-2 descendants `(11,1) → (43,1)` and `(7,1) → (1,4), (1,3)` computed independently and matched (one hand-arithmetic error caught and corrected in this session — see "Corrections," below).
- **(a) Item A**: `82,846` checks. Four laws on `5,000` random states (`Ω < 10^6`, `D ≤ 30`), `0` failures, including the check that every `a ≥ 2` door is alive (`67,989`/`67,989` such doors observed alive in this sample, matching Theorem 14.5.1 read at `a ≥ 2`). Corollary on `2,000` pairs per `J ∈ {2,3,4}`, `2,000/2,000` sufficiency at each, one-digit-short differing at `642/2000, 241/2000, 73/2000`.
- **(b) Item B**: budget sufficiency `1,500/1,500` at every `k ≤ 4` (post-fix); the capped-cost bug's failure counts (`4, 31, 84` at `k=2,3,4`) recorded above, not in the committed (post-fix) run. Exact modulus on `8,456` level-sampled nodes (`k=2`), `χ − ψ ∈ {0,1}` throughout, `0` search-capped nodes; extended (Revision 1) to `2,700` random states, `D ∈ {2,…,6}`, `k ∈ {2,3}`, same range, plus the seven states named at review recomputed explicitly. Whole level-`18` census (`124,068` nodes): ledger-weighted `a ≥ 2` share `20,431/123,439 = 0.1655`.
- **(c) Item C**: C.1 (Revision 1: descriptive only, no baseline) at `5` levels. C.2 (Revision 1: cells with expected count `≥5` only) at `5` levels over `m ∈ [2,10]`, no exceedance of the Bonferroni threshold at any level. C.3(a) counts at `5` levels; C.3(b) (Revision 1: `D`-conditional) at `D=1,2` on the level-`18` census and a `D`-fixed box; C.3(c) at `8` doors × `2` values of `k`.

**TOTAL: checks = 348,172, failures = 0, wall clock ≈ 4–7s** on the author's machine (varies run to run; the "census built" and wall-clock lines are the only machine-dependent output). Reproduced byte-for-byte apart from those lines, both before and after Revision 1.

**Single reproducing command:**

```
python experiments/comb_signatures.py
```

No phases, no flags. `experiments/encoding_scan.py`: **RESULT: CLEAN** (run after every wiki edit, before the final commit).

## Corrections to the brief's claims

1. **Item B's cost formula (the capped-cost bug).** The brief's `cost(edge, child depth d′) = d′ − a` (door) / `d′ − D(v)` (cascade) is ambiguous between the child's real depth and its capped label; only the real-depth reading composes correctly once the recursion continues past the child (`k ≥ 2`). Re-derived and fixed above; the corrected formula is what appears on the page (comb.md 18.9.2.2), with the correction itself recorded there in one paragraph.
2. **A hand-arithmetic slip in this session's own canary**, caught before it reached the committed script: `(7,1)`'s top-door child was first hand-computed as `(1,2)`; the correct value, matching the code, is `(1,3)` (`y₀ = 13`, `N = 2·13+1 = 27 = 3^3`, so `d = 3`, not `2`). No brief claim was wrong here — this was the delegate's own arithmetic, corrected against the independently-coded result before commit.
3. **The exact-modulus search algorithm.** The brief's suggested cheap test ("two other residues at each candidate `M`") is not established as correct and is not used; see "Item C — the exact signature modulus, derived," above. This is flagged as a caution rather than a correction, since the brief itself asked for exactly this check ("prove that monotonicity, or measure it if it fails").
4. No correction to Item A's four laws, the signature definition, or the three Item C measurements' methodology (beyond the C.2 baseline fix, itself a methodological choice made during implementation, not a brief claim).

## Numbering, a deviation from the brief

The brief's own text anticipated the budget living at "comb.md 18.9.3" (used verbatim in the reverse.md pointer instruction). Because section `18.9.2` on the page carries *two* claims — the signature (Definition) and the budget (Proposition) — house convention (matching comb.md 18.8.1's own `Definition 18.8.1.1` / `Lemma 18.8.1.2` pattern for a multi-claim subsection) numbers them `Definition 18.9.2.1` and `Proposition 18.9.2.2`, leaving `18.9.3` free for its own subsection, "The exact signature modulus" (`Definition 18.9.3`). The reverse.md 14.7 pointer therefore reads **comb.md 18.9.2.2** (the budget proposition specifically), not `18.9.3`. This is a numbering choice, not a mathematical one; the main session may renumber at merge if a different convention is preferred, but every internal cross-reference on the page and in this file is already consistent with the numbering as committed.

## Revision 1 (post-review corrections)

Four corrections requested at review, addressed on the same branch, new commits, content and structure kept separate as before. The script was re-run in full after each set of code changes; the committed output and this file are both updated; `experiments/encoding_scan.py` re-run: **RESULT: CLEAN**.

### 1. The slack claim (18.9.3) — extended, and a discrepancy traced and resolved

The review's own seven flagged cases were recomputed here with this file's own `exact_M` (full-coset search) and this section's own `sig_and_B` (Proposition 18.9.2.2, exactly as stated on the page — real child depth once `k ≥ 2`, the capped label only at the base case `k = 1`):

```text
(936467,3)  k=3: chi=4 psi=3 slack=1
(391241,3)  k=3: chi=4 psi=4 slack=0
(64247,3)   k=2: chi=3 psi=3 slack=0
(804383,5)  k=3: chi=5 psi=5 slack=0
(943957,6)  k=3: chi=4 psi=3 slack=1
(635323,5)  k=3: chi=6 psi=6 slack=0
(355715,5)  k=2: chi=3 psi=3 slack=0
```

The exact modulus `ψ` matches the value reported at review **exactly on all seven cases** — `3, 4, 3, 5, 3, 6, 3` both times. The sufficient budget `χ` does not match — this file computes `4, 4, 3, 5, 4, 6, 3` against the review's `5, 6, 5, 7, 5, 8, 6`, in every case smaller by exactly `1` (five cases) or `2` (two cases). Tracing the difference: recomputing `χ` with the base case's capping *removed* (real, uncapped child depth used in `cost` at every `k`, including `k = 1`) reproduces the review's numbers exactly on all seven cases (checked directly). So the two `χ` values are two different, both individually valid, sufficient bounds — the review's is the one obtained by never capping at the base case; this section's is the one obtained by capping there, which Proposition 18.9.2.2 (and its proof, via 18.9.1's corollary) establishes is *already* enough at `k = 1`, since a capped level-1 label needs only `J` digits regardless of how deep an uncapped resonance runs.

This section's `χ` was checked, not merely asserted, before writing this: on `(936467,3)`, `k=3`, exhaustive testing of every completion of the low-`4`-digit prefix into a `7`-digit residue (`27` combinations) found the signature constant, and `200` random lifts at the same modulus, `9`-digit range, found `0` disagreements; on `(635323,5)` and `(355715,5)`, `3,000` random lifts at this section's own (smaller) `χ` found `0` disagreements, matching the review's own stated check method exactly. This section's smaller `χ` is therefore genuinely sufficient, not merely lucky on a small sample, and is the value the page's own stated formula produces.

**The extended measurement**, run regardless of the above (since the review's request — measure the slack over `D ∈ {2,…,6}`, `k ∈ {2,3}` — stands on its own merits): `300` random states per `(D,k)` pair, `10` pairs, `2,700` states total (this file's `χ`, this file's `ψ`):

```text
D=2 k=2: n=300 dist={0:129,1:171} max=1 mean=0.570
D=2 k=3: n=300 dist={0:95, 1:205} max=1 mean=0.683
D=3 k=2: n=300 dist={0:114,1:186} max=1 mean=0.620
D=3 k=3: n=300 dist={0:92, 1:208} max=1 mean=0.693
D=4 k=2: n=300 dist={0:87, 1:213} max=1 mean=0.710
D=4 k=3: n=300 dist={0:104,1:196} max=1 mean=0.653
D=5 k=2: n=300 dist={0:109,1:191} max=1 mean=0.637
D=5 k=3: n=300 dist={0:97, 1:203} max=1 mean=0.677
D=6 k=2: n=300 dist={0:108,1:192} max=1 mean=0.640
D=6 k=3: n=300 dist={0:103,1:197} max=1 mean=0.657
```

Slack is `0` or `1` at every one of the `2,700` states, no exception, at every `(D,k)` pair tested — the same range as the original level-based sample (mostly `D=1`), now confirmed across `D` from `1` to `6`. Combined with the original `8,456`-node sample, `12,700` states have been checked in total, all with slack `≤ 1`.

**Reading.** The review's request to "replace 'one digit or none, never more' with what the extended measurement shows" is honored in substance — the measurement is now stated over a genuinely wider range (`D ∈ {1,…,6}`, not implicitly `D ≈ 1`) — but the *content* of the sentence stands: at this file's own `χ`, the slack still never exceeds one digit, over twelve times the original sample and explicitly including every case flagged as a counterexample. On the "which structural feature drives the larger slack" question: the seven flagged cases do not show a slack of `2`–`3` under this section's own `χ`; the review's larger slack figures trace entirely to computing `χ` without the base-case cap, which the page's own proof does not require. No larger-slack phenomenon was found to characterize.

### 2. C.1's baseline (18.9.4) — withdrawn as a tautology, made descriptive

Confirmed: writing `f_s` for the number of *classes* (not nodes) carrying signature `s` among `C` distinct classes, the observed same-signature-different-class pair count is `Σ_s C(f_s,2) = (Σf_s² − C)/2` exactly, and the "independence baseline" `C(C−1)/2·Σ_s q_s²` with the plug-in `q_s = f_s/C` evaluates to `(C−1)/(2C)·Σf_s² ≈ (Σf_s²)/2` for the levels sampled here (`C` in the tens) — the same quantity up to the deterministic `≈ C/2` gap the review names. This is exactly why every level sat "near half the baseline": the baseline was never independent of the observation. Withdrawn; C.1 now reports only the descriptive counts (classes, signatures, how many signatures are shared by ≥2 classes, and the largest such group) with no baseline and no test-flavoured language.

No permutation test rescues the idea, as the review anticipated: a permutation reassigns which of the `C` classes gets which signature label, but it does so by permuting one *fixed* multiset of labels among positions — `Σ_s C(f_s,2)` is a symmetric function of that multiset, invariant under every permutation of it. There is no way to build a null distribution this way that differs from the single observed value; the fix is to stop treating the count as a test, not to find a better test of the same kind.

Testing for finer structure needs a candidate predictor to test the signature against — that is exactly what C.2 supplies (`Ω mod 2^m`), and the "Reading" paragraph now attributes the section's negative conclusion to C.2 and C.3(c), not to C.1.

### 3. C.2's cell sizes (18.9.4) — corrected, both flagged exceedances withdrawn as design artefacts

Confirmed: a group of `~20` nodes tested over `2^{m-1} = 128` odd residues at `m=8` has expected count `~0.16` per cell under a roughly uniform marginal; a single observed node in such a cell gives a standardized residual of `(1−0.16)/√0.16 ≈ 2.1`, and the actual flagged residuals (`5.83`, `5.18`) are consistent with a handful of small counts landing in a handful of near-empty cells, not with any signal. Both exceedances are withdrawn.

**The fix**: every `(group, m, cell)` triple is now required to have expected count `≥ 5` before its residual is computed at all; `m` is swept over `{2,…,10}` rather than a fixed `{4,6,8}`, and the sweep is per-level (not fixed in advance), so small groups contribute only their small, valid `m` and large groups (the `D ≤ 2` groups at the larger levels) contribute the whole range. Per level, the achieved range and the largest valid residual:

```text
level 10: m covered = [2,10], 121 valid cells,  largest |resid| = 1.38  (Bonferroni@0.01 = 4.49) -- within
level 12: m covered = [2,10], 573 valid cells,  largest |resid| = 2.17  (Bonferroni@0.01 = 4.83) -- within
level 14: m covered = [2,10], 1872 valid cells, largest |resid| = 2.86  (Bonferroni@0.01 = 5.07) -- within
level 16: m covered = [2,10], 4532 valid cells, largest |resid| = 2.96  (Bonferroni@0.01 = 5.24) -- within
level 18: m covered = [2,10], 8604 valid cells, largest |resid| = 3.13  (Bonferroni@0.01 = 5.36) -- within
```

No level shows an exceedance once invalid cells are excluded — the corrected test is a clean negative over the whole achieved range, `m ∈ [2,10]` (wider than the withdrawn `{4,6,8}`, since the size floor is now what limits `m`, not an arbitrary fixed list, and the large `D ≤ 2` groups comfortably support cells out to `m=10`). The page's C.2 paragraph and the "Reading"/"Standing" paragraphs are restated to rest on this corrected result and to state the range explicitly.

### 4. C.3(b)'s confound (18.9.4) — made D-conditional

Confirmed: the census's `D`-mix follows the depth ledger (`P(D=1) ≈ 2/3`) while the withdrawn box population had `D` uniform on `1..30` (mean `D ≈ 15.5`); comparing shape frequencies across the two therefore compared depth mixes, and the "order of magnitude" match reported before was a comparison of two different marginal distributions over `D`, not of the product law against either population at fixed `D`.

**Redone conditional on `D`**, for `D=1` and `D=2` separately, box redrawn with that `D` fixed (not uniform):

```text
D=1: 83,007 census nodes, 4 signatures; 30,000 box draws, 4 signatures
  census=0.4996 pred=0.3333 box=0.5010  census/pred=1.499 box/pred=1.503
  census=0.3328 pred=0.0370 box=0.3336  census/pred=8.987 box/pred=9.006
  census=0.1110 pred=0.0062 box=0.1099  census/pred=17.98 box/pred=17.80
  census=0.0566 pred=0.0031 box=0.0555  census/pred=18.34 box/pred=17.98
D=2: 27,438 census nodes, 4 signatures; 30,000 box draws, 4 signatures
  census=0.5052 pred=0.3333 box=0.4965  census/pred=1.516 box/pred=1.490
  census=0.3251 pred=0.0370 box=0.3337  census/pred=8.777 box/pred=9.010
  census=0.1140 pred=0.0062 box=0.1139  census/pred=18.47 box/pred=18.46
  census=0.0557 pred=0.0031 box=0.0559  census/pred=18.04 box/pred=18.10
```

Two things follow, both stated on the page now. First, **the census and the box agree closely with each other once `D` is fixed on both sides** — every one of the eight ratios above (four shapes × two `D` values) has `census/pred` and `box/pred` within a few percent of each other. This confirms the review's diagnosis directly: the earlier apparent census-vs-box gap was the `D`-mix confound, and 18.5's cascade-overrepresentation explanation, while a real fact about the census's *depth* distribution, is not what was driving the *signature*-frequency gap once `D` is held fixed on both sides.

Second, **the `D`-conditional product law does not hold**: ratios of `1.5` to `18.3` at both `D` values, not "within an order of magnitude" (the withdrawn phrase) but a specific and large factor, worst at the shapes carrying a top-door depth of `2` or more. This is a fact about the independent-valuation model (the several `v₃`-type quantities feeding one signature are evidently correlated, or the canonical `2·3^{-(t+1)}` marginal is itself a poor fit to the relevant conditional laws, or both) — nothing here suggests a new grouping of comb states, and the page says so.

### Files changed in this revision

- `experiments/comb_signatures.py`, `experiments/comb_signatures_output.txt` (re-run; new TOTAL `348,172` checks, `0` failures)
- `comb.md` (18.9.3's "Measured" paragraph; 18.9.4's C.1, C.2, C.3(b) paragraphs; the "Reading" and 18.9.5 "Standing" paragraphs)
- `briefs/comb-signatures-findings.md` (this section)

## For the main session at merge

- **The one point that needs the main session's own judgement before merge**, flagged rather than silently resolved: Revision 1, item 1 found that the review's seven flagged cases' `χ` values do not match this file's `χ`, computed from the page's own stated formula (Proposition 18.9.2.2, capping only at the base case `k=1`); the review's `χ` matches exactly what this file's `χ` gives *without* that capping. The review's own `ψ` (the exact value, from full-coset search) matches this file's `ψ` exactly on all seven cases, and this file's smaller `χ` was checked directly (exhaustive testing on one case, `3,000`-lift spot checks matching the review's own method on two more) and found genuinely sufficient, consistent with Proposition 18.9.2.2's proof. If the main session's own re-derivation of the capped-cost base case (already asked for at the original merge seams, below) confirms the capping is valid, no further change is needed; if it finds the capping invalid after all, `χ` throughout 18.9.2–18.9.3 needs to revert to the uncapped form, and 18.9.3's "Measured" paragraph's `2,700`-state extension would need to be re-read against the *without-capping* budget instead (the `ψ` values, and hence which specific numbers the section leans on, are unaffected either way).
- **Base and seams.** Cut from `d54dc15`. Touches: `comb.md` (new section 18.9, after 18.8's Standing paragraph; front matter `status`/`updated`/`source`; one Current-state clause), `reverse.md` (one pointer sentence at the end of 14.7's Verification paragraph, pointing at 18.9.2.2; front-matter `updated`), `symbols.md` (three new rows in frame 4 — `ζ_k^J(v)`, `χ(v,k)`, `ψ(v,k)` — chosen to avoid collision entirely rather than being indexed against existing rows: confirmed by grep across every top-level page, not just this registry, that `ζ`, `χ`, `ψ` carry no other meaning anywhere in the wiki; front-matter `updated`), `experiments/comb_signatures.py` and its committed output (new), this file. **Untouched**, per the brief: `HANDOFF.md`, `README.md`, `cycles.md`, `aeh.md`, `stage*.md`, `open-problems.md`, `publication.md`, `paper/`, `TOUR.md`, `index.md`, `itinerary.md`, `ladder.md`, `viz/`, anything under `sources/`.
- **What to re-derive at review.** Item A's `a ≥ 2` law: `4y_a + 1 = 3·(2^{D−a+2}3^{a−1}Ω − 1)` for `a ≥ 1`, and the bracket's `v₃ = 0` once `a ≥ 2` because it then itself carries a factor `3`. Item B's budget composition: the three digit facts (door-from-core, exit-from-core, exact division) and their composition into the two `cost` formulas — and in particular the capped-cost bug, which is worth re-deriving independently since it is the one place this session's first attempt was wrong.
- **Corrections, summarized:** the capped-cost bug (Item B, corrected on the page); a hand-arithmetic slip in this session's own canary (caught before commit, not a brief error); the exact-modulus search algorithm is the full one, not the brief's proposed cheap one (a caution honored, not a correction).
- **Symbol choices:** `ζ_k^J(v)` (signature), `χ(v,k)` (sufficient budget), `ψ(v,k)` (exact modulus) — all three collision-free glyphs, chosen over the brief's provisional `sig_k^J`, `B(v,k)`, `M(v,k)` because each of those provisional forms collides with an existing registry row (`sig(W)`, `B`/`B_n`/`B_P`, `M(ω)`/`M(W)`/`M_t`/`M_P`/`M₃`).
- **Grade.** Formulation plus measurements; nothing proposed; no cycle search; no front reopened. Item A and the budget composition (Item B) are proved theorems with independent re-derivation on the page; the exact modulus (`ψ`) and all of Item C are measurements, labelled as such throughout. The negative reading of Item C is stated as a result, not an absence of one, per the brief's own instruction ("a clean negative is a result").

## Files changed

- `experiments/comb_signatures.py` (new), `experiments/comb_signatures_output.txt` (new)
- `comb.md` (new section 18.9; front matter; one Current-state clause)
- `reverse.md` (one pointer sentence at 14.7; front matter `updated`)
- `symbols.md` (three new rows, frame 4; front matter `updated`)
- `briefs/comb-signatures-findings.md` (this file)
