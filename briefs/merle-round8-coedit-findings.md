# Findings: round-8 co-edit (merle-round8-coedit)

Delegated session, 2026-07-24. Brief: `briefs/merle-round8-coedit-brief.md`.
Branch `merle-round8-coedit`, base commit `83a71fb` (the brief commit). Launch note,
for the record: the worktree was cut at `eb30427` (one commit behind the expected
HEAD); `83a71fb` was present in the repository, so the branch was created directly
from it — no rebase needed. Register: flat; heuristics labeled; every downstream
claim below cites this session's own code output (`experiments/margin_asymptote.py`,
49 checks, 0 failures), not the brief's stated targets.

**The one line that gates everything external: the shared repo was NOT pushed.
The three key-turn commits exist only in the scratchpad clone (branch
`coedit-round8`) and as format-patch files committed into this repository;
the push happens later, from the main session, on the author's explicit word.**

## Part A — `experiments/margin_asymptote.py` (commit `52e8c5c`)

Fresh code (imports nothing from `merle_round8_check.py` or any Merle repository);
exact integer combinatorics for every count; floats only in logarithms and the
variational search, with the role stated in the header; canaries (brute-force
profile enumeration `n ≤ 12` against both closed forms, exact Vandermonde,
odd-composition closed form vs DP, a hand-computed entropy-bound instance) all
run and printed before any sweep. Full output committed as
`experiments/margin_asymptote_output.txt`.

**Derived constants vs the brief's targets: all matched.** `c_gen = 0.0793186128`
(target ≈ 0.07932), `c_strat = 0.2667875013` at `α* = 0.3747343562` (targets
≈ 0.26679, ≈ 0.37473); the two `c_gen` forms (closed and `β(1 − H(1/β))`) agree
to `1e-12`; the stratum maximum is interior (bracketed at `α* ± 10⁻⁴`; endpoint
`g(β−1) = H(β−1) = 0.979` well below `g(α*) = 1.3182`). One derivation-level
nuance, not a disagreement: the brief writes the variational domain as
`α ∈ (0,1)`; the odd-composition constraint `S ≥ p` makes the effective domain
`(0, β−1]` (`g = −∞` beyond) — same problem, same interior maximizer.

**The derivation (wiki-grade; backs Remark 12.6.1.5).** Definitions from
REQ-MATH-014, conventions of cycles.md 12.6.1: tuned family
`K = bitlength(3^n) = ⌊nβ⌋ + 1` (`β = log₂3`), `S = K − n`,
`margin(n) = K − log₂(#profiles)`.

*General family.* The count is `Σ_p C(n−1,p−1)·C(S−1,p−1) = C(K−2, n−1)` —
Vandermonde: put `j = p−1` and use `C(S−1,j) = C(S−1, S−1−j)`, so the sum is the
coefficient extraction `Σ_j C(n−1,j)·C(S−1,S−1−j) = C(n+S−2, S−1) = C(K−2, n−1)`.
The standard entropy bounds for binomials (via the binary type class;
Cover–Thomas Lemma 17.5.1), `2^{aH(b/a)}/(a+1) ≤ C(a,b) ≤ 2^{aH(b/a)}`, give
`log₂ C(K−2, n−1) = (K−2)·H((n−1)/(K−2)) + O(log n)`; since `(n−1)/(K−2) → 1/β`
and `H` is continuous, `(1/n)·log₂(#profiles) → β·H(1/β)`. Hence
`margin/n → c_gen = β − β·H(1/β) = β(1 − H(1/β))`; expanding
`H(1/β) = (1/β)log₂β + ((β−1)/β)(log₂β − log₂(β−1))` gives the closed form
`c_gen = β − β·log₂β + (β−1)·log₂(β−1)`. A genuine limit, elementary.

*Odd-step stratum.* Substituting `s_i = 2a_i + 1` turns compositions of `S` into
`p` odd parts into compositions of `(S−p)/2` into `p` nonnegative parts:
`oddcomp(S,p) = C((S+p)/2 − 1, p−1)` for `S ≥ p`, `S ≡ p (mod 2)`, else `0`
(cross-checked against a 2-D DP for `S ≤ 30`, every `p`). The count is
`Σ_p T(p)`, `T(p) = C(n−1,p−1)·C((S+p)/2 − 1, p−1)`. With `α = p/n` the entropy
bounds give termwise `(1/n)·log₂ T(αn) → g(α) := H(α) + ((β−1+α)/2)·H(2α/(β−1+α))`
with `O(log n)/n` error, uniformly on compact subsets of the domain `(0, β−1]`
(the constraint `S ≥ p` caps `α` at `S/n → β−1`). The sandwich
`max_p T(p) ≤ Σ_p T(p) ≤ n·max_p T(p)` costs another `log₂(n)/n`, the discrete
grid `p/n` is `(2/n)`-dense in its parity class, and `g` is continuous, so
`(1/n)·log₂(#profiles) → max_α g(α)` and `margin/n → c_strat = β − g(α*)`.
Positivity of both constants is printed to 10 digits; "positive and growing
linearly" cashes out to positivity of the limits plus the observed
monotone-from-above convergence of the exact counts.

**Exact counts.** Digit-exact reproduction of the round-8 findings at Merle's
grid (`0.2730` stratum / `0.0854` general at `n = 1280`; `0.2701`/`0.0825` at
`n = 2560`), extended via lgamma/log-sum-exp (precision argument in the header;
cross-checked against exact counts at every `n ≤ 2560`, max deviation `1.4e-15`)
to `n = 163,840`: `0.2669`/`0.0794`, gaps to the limits `0.00007` both. Strictly
decreasing at every doubling, strictly above the limits at every grid point.

**Mod-7 mechanism table — the verdict.** What the table supports, exactly:

- *Provable rows:* the `2^s − 1` factor mod `p` ranges over an orbit of exactly
  `ord_p(2)` values; `ord_p(2) ∈ {1, 2}` is impossible for `p ≥ 5`, and
  `ord_p(2) = 3 ⟹ p | 7` — so `7` is the unique prime with the minimum possible
  3-element orbit (`{0, 1, 3}`), the maximal collapse; next-coarsest `5`
  (4 values) and `31` (5 values); large-order `11` (10), `13` (12), `127`
  (7 among 127 residues). On the odd-`s` stratum the orbit halves iff `ord` is
  even: mod `5` → `{1, 2}`, the **zero excluded**; mod `7` (ord odd) the full
  orbit persists **including the zero atom at density 1/3**. The brief's
  parenthetical "(a 2-value orbit on odd s if that is what the table shows)"
  is answered: no — mod 7 the odd-`s` orbit stays 3-valued; it is mod 5 that
  collapses to 2 values.
- *Measured rows (exhaustive at `n = 12, 15`; sampled depth scan at `n = 63`,
  labeled):* every small-orbit prime is biased at small block count, magnitude
  ordered by orbit coarseness with `7` the extreme at every well-posed
  comparison (`TV 0.34` at depth 2, `n = 15`, exhaustive; `0.26` at depth 2,
  `n = 63`, the largest of all six); the bias decays with block count for every
  prime (TV at depths 6–7 under a fifth of depth-2, all primes); at depths
  `≥ 10` all six primes sit at the sampling noise floor.
- *The letter's claim, adjudicated:* "`7` solitary, `5, 11, 13, 31, 127`
  equidistribute" is **reproduced at his ensemble and his resolution** (stratum
  window, block count 5, `n = 63`: mod 7 chi²/df `7.73`, the largest, above his
  bar) — **and refined at higher resolution**: at `N = 30,000` mod `5` also
  crosses the chi²/df > 2 bar (`5.40`; TV `0.0128` vs 7's `0.0151`), where his
  REQ-MATH-017 values (5: 1.91, 7: 3.43) and our round-8 `N = 12,000`
  replication (0.61 / 2.96) sit below that resolution. So "solitary" is a
  statement about detectability at his sample size; what is structural and
  unique to `7` is the maximal orbit collapse, hence the largest and most
  robustly detectable bias — not an exclusive one. Recorded, not forced, and
  carried into the wiki remark and (nowhere else): the shared-ledger co-edits
  do not touch his REQ-MATH-017 wording (NOTE.md stays his; anything
  NOTE-shaped is reply material).
- *Two whole-family observations, recorded flat:* (i) exhaustive family
  aggregates at `n = 12, 15` show the **reverse** headline — mod 5 deviation
  larger than mod 7 (TV `0.012–0.023` vs `0.001–0.008`, general) — because the
  aggregate is dominated by its modal (deeper) depths where 7's small-depth
  bias has already mixed away; chi²/df is not comparable across family sizes
  (with exhaustive counts any deviation is "significant"), TV is the comparable
  number. (ii) Single-term distributions are far from uniform at every prime
  (TV `0.09–0.31`), so what separates primes is mixing speed under summation,
  which the orbit coarseness controls.

## Part B — wiki records (per-item commits)

- **Item 2, `d38b889` — cycles.md Remark 12.6.1.4** (descent; L-A4's wiki
  home, modeled on 12.6.1.3's housing of L-A3): the multiplicative identity
  `R_0(B^k) = R_0(B)·G_k` with `G_k = q_P/q_B` the geometric factor; proof by
  the two bookkeeping identities re-derived into wiki prose (the `3`-exponent
  gains `(k−1−c)·n_B`, the `2`-exponent gains `c·K_B` per copy, via unrolling
  `σ` and periodicity); scope untuned, both signs, entries ≥ 1; corollaries
  flat — (a) the descent biconditional with the shared-ledger status stated
  honestly as of this writing (his key + our verification 12,888/12,888; our
  key turn prepared, pending the author's review), (b) L-A2's gcd law one
  level up (`gcd(q_P, R_0(P)) = G_k·gcd(q_B, R_0(B))`), (c) primitivity —
  minimal/new cycles have primitive profiles, with "genuinely aperiodic"
  identified as this statement without correcting him in prose; calibration
  sentence per the 12.6.1.3 model; Verified paragraph cites
  `merle_round8_check.py`'s grids.
- **Item 3, `02eac83` — cycles.md Remark 12.6.1.5** (the asymptote).
  **Judgment call: a separate 12.6.1.5, not an addendum inside 12.6.1.3** —
  12.6.1.3 is a closed record (register sentence declared as "the whole
  claim", own Calibration and Verified blocks tied to
  `spentstock_digitcap.py`); splicing a second dated verification record
  inside it would reopen a closed remark and mix two scripts' records. The
  new remark pins the margin definition (and the capacity/demand vocabulary
  join flagged in the round-8 findings), states both limits with closed/
  variational forms and numerics, cites the convergence table's endpoints
  including his `n = 1280` digit-exact, keeps attribution flat
  (quantification seeded Merle-side at `n ~ 10³`; asymptote closed our side),
  and carries the calibration sentence (extends the exclusion by nothing;
  `2^(−margin)` stays the labeled heuristic; nothing about `q | R_0` moves).
- **Item 4, `c722e0f` — cycles.md Remark 12.6.1.6** (the mod-7 remark).
  **Judgment call on placement:** a new remark following 12.6.1.5 rather than
  text physically inserted after 12.6.1.1 — section numbers are permanent
  anchors and the file reads in numeric order; the remark's first sentence
  anchors it to 12.6.1.1's `gcd = 7` instance and the shared L3 correction,
  so no edit to the settled 12.6.1.1 text was needed. Content held to the
  part-A table: the provable uniqueness of 7's collapse, the odd-`s`
  zero-atom contrast with 5, the measured small-depth/decay/ordering facts,
  the resolution-dependence refinement stated flat, "structural, not a
  lever" kept as his letter's own conclusion, and the explicit
  closed-door/open-wall sentence.
- **Item 5, `8c6ef8a` — aeh.md Remark 13.6.7** (two equidistributions, not
  one): AEH's genericity form as an orbit-statistics statement vs the
  seam-residue family target as a family statement; sample spaces and limits
  named; neither implies the other as stated; both honestly on the ×2×3 gap;
  conflation named as the failure mode the note exists to prevent; 13.3.3's
  scope discipline explicitly unchanged; plus the one-line pointer from
  cycles.md 12.6.1.5's calibration paragraph.
- **Item 6, `3cf6b8a` — itinerary.md Corollary 14.15.10.3** (new cycles ⇔
  primitive door-words). **Judgment call: the dictionary's per-cycle table
  has instance grammar** (`word ↔ anchor ↔ cycle`; the `{−1}` line is an
  exception annotation, not a precedent for a quantified claim), so a table
  line would have needed surgery; instead a three-sentence corollary was
  appended after 14.15.10.2, touching zero existing text, with a one-line
  fixed-point-frame proof (`y*(P^k) = y*(P)`: `G_{P^k} = (G_P)^k` and an
  affine map of slope `≠ 1` has a unique fixed point) and the cross-pointer
  to 12.6.1.4(c). Not skipped, because the section's corollary grammar fits
  exactly; recorded here as the deviation from the literal "one line in the
  table".

## Part C — shared repo (prepared LOCAL-ONLY; **NOT pushed**)

Clone: scratchpad, `github.com/macindoe/one-obstruction-three-faces`; HEAD
re-verified **`b8842bb`** after `git fetch` (origin/main unmoved) — part C
proceeded. Local branch `coedit-round8` from `b8842bb`; author identity set
clone-locally to `macindoe <begemite0.o@gmail.com>`, matching the
`430c00c`/`d2407b9` practice. `LEDGER.md` only; NOTE.md untouched. Prepared
commits (local hashes, valid in the scratchpad clone; the patch files are the
durable record):

| local hash | entry | patch file (committed at `7bd0c39`) |
|---|---|---|
| `e18aed8` | L-A4 key turn + two offers | `briefs/merle-round8-coedit-patches/0001-L-A4-...patch` |
| `a7ac7b7` | L3 correction key turn | `briefs/merle-round8-coedit-patches/0002-L3-...patch` |
| `f9ad836` | L-A3 addition (B) | `briefs/merle-round8-coedit-patches/0003-L-A3-...patch` |

**Flag for the main session:** all three prepared blocks cite our artifacts at
branch commits (`d9ef06b` for `merle_round8_check.py`, `52e8c5c` for
`margin_asymptote.py`) with the clause "final wiki-main hash to be pinned at
review" — the main session should pin the post-merge hashes before the push.

The appended text, verbatim (the rest of each entry is byte-unchanged from
`b8842bb`; the patch files carry the same text with context):

### L-A4 — appended after the Merle artifacts line

> **Macindoe key turned (2026-07-24) — clean-room, with a strengthening.**
> Independent re-derivation from `cycles.md` 12.6.1's conventions only (no code
> or text reused from either Merle repository): the biconditional follows from
> a *multiplicative identity* — `R_0(B^k) = R_0(B) · (q_P/q_B)`, where
> `q_P/q_B = G_k = Σ_{c<k} 3^{(k−1−c)·n_B} · 2^{c·K_B}` is the geometric factor
> of `x^k − y^k` at `x = 2^{K_B}`, `y = 3^{n_B}` — proved by two bookkeeping
> identities (per copy `c`, the `3`-exponent of each term gains `(k−1−c)·n_B`
> and the `2`-exponent gains `c·K_B`), so numerator and seam gap scale by the
> *same* positive integer and `G_k` cancels from the divisibility. Verified
> exact at every draw over three grids — exhaustive bases of length `1..3`,
> entries `{1,2,3}`, `k = 2..5` (3,276 pairs; the 24 divisible bases all
> inherit upward); 300 random bases, lengths `4..6`, entries `1..8`,
> `k = 2..4`; and the tuned mirror of the REQ-MATH-016 grid
> (`n ∈ {24,36,60}`, 720 draws): **12,888/12,888 exact checks, 0 failures**.
> Canaries: trivial-cycle inheritance (`([1],[1]) → B²`, `q = R = 7`), a
> negative-`q` square (the `(−5)`-shore word), a non-cycle square. Wiki home:
> `cycles.md` Remark 12.6.1.4 (identity + proof + primitivity corollary).
> Artifact: `macindoe/collatz` `experiments/merle_round8_check.py` with
> committed output (branch commit `d9ef06b`; the final wiki-main hash to be
> pinned at review). Status: **two keys**.
>
> Two offers, inside the entry per the co-edit style — acceptance is Merle's
> call:
>
> - *(offer a — scope.)* The identity and the biconditional hold with **no
>   tuning hypothesis**: every profile with entries `≥ 1`, both signs of `q`,
>   exactly like L-A1/L-A2. "In the tuned regime" can drop, or stay as the
>   application's stated scope, as preferred.
> - *(offer b — vocabulary.)* "aperiodic/generic" → "**primitive** (not a
>   proper power of a shorter word)/generic" — the finite-word-correct term
>   for the descent's conclusion, mirroring the "positive odd integer"
>   precision.

### L3 — appended after the correction block

> **Macindoe key turned on the correction (2026-07-24).** Verified
> independently our side: the no-Hasse-gap principle is confirmed as stated
> (for fixed `q ≠ 0`, `q | R ⟺ v_p(R) ≥ v_p(q)` at every prime; solvability
> over ℝ, and over ℤ_p wherever `p ∤ q`, is automatic — so a check confined to
> ℝ/ℤ₂/ℤ₃, where `q` is a unit, cannot see the failing place); on the `p = 7`
> instance, independent exact code from our own records gives `v_7(q) = 3`
> exactly and `v_7(R_r) = 1`, `gcd(q, R_r) = 7` at **all 7 rotations** —
> insoluble in ℤ₇ everywhere, as claimed; the recorded two-key data is
> confirmed byte-untouched (diff of this entry against `61d2cf3`: pure
> addition, zero deletions), and the distance profile recomputes digit-exact
> (`[0.0538, 0.4784]`). Correction **accepted into the two-key record**.
> Artifact: `macindoe/collatz` `experiments/merle_round8_check.py` part (b)
> (branch commit `d9ef06b`; final wiki-main hash to be pinned at review).

### L-A3 — appended after the "Additions accepted" paragraph

> **On (B): definition pinned, replication, and the asymptote (Macindoe,
> 2026-07-24).** Operational definition, from REQ-MATH-014 (the entry stated
> the values without it): on the tuned family
> `K = bitlength(3^n) = log₂ q + o(1)`, `S = K − n`, and
> `margin(n) = K − log₂(#profiles)` — general family: entries `≥ 1`, count
> `Σ_p C(n−1,p−1)·C(S−1,p−1) = C(K−2, n−1)`; odd-step stratum: all `s_t` odd,
> count `Σ_p C(n−1,p−1)·C((S+p)/2−1, p−1)`. (One vocabulary clause: this
> margin is the counting shadow of `cycles.md` 12.6.1.3's capacity/demand
> pair — REQ-MATH-014's "capacité" is `log₂ q`, its "demande" is
> `log₂ #profiles` — both vocabularies now joined under one pinned name.)
> Replicated digit-exact at the REQ-MATH-014 grid (`0.2730` stratum /
> `0.0854` general at `n = 1280`). Asymptote, closed this round and
> **offered**: with `β = log₂ 3` and `H` the binary entropy,
>
> `margin/n → c_gen = β − β·log₂ β + (β−1)·log₂(β−1) = 0.0793186…` (general;
> equivalently `β·(1 − H(1/β))`), and
> `margin/n → c_strat = β − max_{α ∈ (0, β−1]} [H(α) +
> ((β−1+α)/2)·H(2α/(β−1+α))] = 0.2667875…` (stratum; interior maximum at
> `α* = 0.3747344…`)
>
> — genuine elementary limits (entropy bounds on the binomials, plus the
> largest-term sandwich for the stratum sum), with the exact counts
> approaching both constants monotonically from above (computed through
> `n = 163,840`: `0.0794`/`0.2669`). So "positive and linearly growing" is
> now anchored: positivity of the limit constants plus monotone-from-above
> convergence. The `2^(−margin)` decay clause remains the no-conspiracy
> **heuristic** (the artifact's own label, kept). Attribution, flat:
> quantification seeded Merle-side (REQ-MATH-014, `n ~ 10³`); asymptotic
> constants closed Macindoe-side. Artifact: `macindoe/collatz`
> `experiments/margin_asymptote.py` with committed output (49 checks,
> 0 failures; branch commit `52e8c5c`; final wiki-main hash to be pinned at
> review); wiki home `cycles.md` Remark 12.6.1.5. Status of (B): our key is
> turned on the `n ~ 10³` replication, and the asymptote is offered — (B)'s
> quantification carries **two keys** once Merle's acceptance of the
> asymptote lands.

## Flags and judgment calls, collected

1. **Base commit:** worktree cut at `eb30427`; branch recreated from
   `83a71fb` (the brief commit, present in the repo). No rebase needed.
2. **12.6.1.5 as a separate remark** (not a 12.6.1.3 addendum) and
   **12.6.1.6 numbering** (not physical insertion at 12.6.1.1) — reasons in
   Part B above.
3. **14.15.10 dictionary line delivered as Corollary 14.15.10.3** (the
   per-cycle table's instance grammar did not fit a quantified line; zero
   existing text touched).
4. **Variational domain nuance:** effective domain `(0, β−1]`, not `(0,1)`;
   same maximizer, recorded in code comments and above.
5. **Solitary-7 is resolution-dependent** (mod 5 also crosses his
   significance bar at `N = 30,000`, TV `0.0128` vs 7's `0.0151` in his
   window; whole-family aggregates at small `n` even reverse the headline).
   Recorded in the wiki remark; NOT written into his ledger/NOTE texts — it
   is reply material if the author wants it raised.
6. **Artifact-hash pinning owed at review:** the three prepared ledger blocks
   cite branch commits `d9ef06b`/`52e8c5c` with an explicit
   pin-at-review clause (see Part C flag).
7. **Nothing skipped**; no push was needed or attempted anywhere
   (**handbacks: none**). Our repo: branch commits only, unmerged, per the
   brief's stopping rule. Stopping-rule compliance: no cycle search, no
   exclusion attempt, no equidistribution proof effort; every touched section
   keeps its parked/calibration language.
