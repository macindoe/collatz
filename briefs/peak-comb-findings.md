# Findings: the peak comb (comb.md §18)

Delegated session, branch `peak-comb`. Supports `briefs/peak-comb-brief.md`.

## Base SHA and branch

The worktree's HEAD at spawn was `a7543ce` (2026-09-13), which predates the brief: `briefs/peak-comb-brief.md` did not exist there. `git rebase main` fast-forwarded the worktree branch cleanly onto local `main` at `8eeba63` (2026-09-15, the brief's own delegation commit), and `peak-comb` was cut from there.

**Base SHA: `8eeba63`.**

## Claims (i)–(xi): derivations, and what the pre-check got wrong

Notation as on the page: `A = 3^d ω − 1 = 2^s y`, `s = v₂(A)`, `y` the exit; `state(y)` is door recovery (reverse.md 14.6.5.1); `node(y, s)` is the state at branch `s` on door `y`, `2^s y + 1 = 3^d ω`.

**(i) `A` determines the state.** `A + 1 = 3^d ω` with `3 ∤ ω`, so `d = v₃(A+1)`, `ω = (A+1)/3^d`. Holds as stated.

**(ii) An even `A` is a peak iff `3 | A + 1`.** Forward: `A + 1 = 3^d ω`, `d ≥ 1`. Backward: `A + 1` odd and divisible by `3` gives `d := v₃(A+1) ≥ 1` and an odd cofactor prime to `3`; `A ≥ 2` follows. Equivalently `A ≡ 2 (mod 6)`. Holds as stated.

**(iii) Alternation along a door.** `3 | 2^j y + 1 ⟺ 2^j y ≡ 2 ⟺ (−1)^j y ≡ −1 (mod 3)`: `j` odd for `y ≡ 1`, `j` even for `y ≡ 2`, never for `3 | y` — 14.1.1's admissibility verbatim, and `2^s y` is then the peak of the branch-`s` predecessor (its numerator is `2^s y`, so its exit valuation is `s` and its exit `y`). Holds as stated; the one boundary is `j = 0`, where `y + 1 ≡ 0 (mod 3)` for a side door but `y` is odd, hence not a peak — the page's "even numbers `2^j y`, `j ≥ 1`" excludes it.

**(iv) The raw maximum is `2A`.** Along `x_a, 2x_{a+1}, x_{a+1}, …, x_{d−1}, 2A, A, …, y` the terms `3x_b + 1 = 2x_{b+1}` increase with `b` and the cascade decreases, so the maximum is `3x_{d−1} + 1 = 2A` (spine.md §6.3). `2A + 1 = 2·3^d ω − 1 ≡ −1 (mod 3)`, so `2A` is never a peak. Stated as a remark, per the brief.

**Worked instance.** Door `5`: `4·5+1 = 21 = 3·7 → (7,1)`; `16·5+1 = 81 = 3^4 → (1,4)`; `64·5+1 = 321 = 3·107 → (107,1)`; peaks `20, 80, 320`; entry of `(107,1)` is `2·107 − 1 = 213`; `Col`-orbit `213 → 640 → 320 → 160 → 80 → 40 → 20 → 10 → 5`. Representatives of `(1,4)`: `2^{4−a} 3^a − 1 = 15, 23, 35, 53`; of `(7,1)`: `13`. None on the orbit. Confirmed by hand and by the script's canaries.

**(v) The parent rule is well defined; tree; node set.** Cascade parent at `s ≥ 3`: `2^{s−2} y ≡ 2^s y (mod 3)` since `4 ≡ 1`, so `3 | 2^{s−2} y + 1`; the parent's numerator is `2^{s−2} y`, valuation `s − 2 ≥ 1`, exit `y`. Door parent at `s ≤ 2`: `state(y) = F(ω,d)` (spine.md §3.7, `F = R ∘ x_exit`, and `R = state` by Proposition 14.14.1.1). Local chain lemma: `⌊(s−1)/2⌋` cascade edges reach the lowest sibling at branch `s₀ ∈ {1,2}`; from it a door edge goes to `F(v)` unless it is the root, which forces `y = 1` and `F(v) = (1,1)`. Induction gives: the chain visits `F(v), F²(v), …` in order and stops only at the root; it reaches the root iff the `F`-orbit reaches `(1,1)` (if `F^t(v) = (1,1)` the chain gets there; conversely the root is the lowest sibling of door `1`, so reaching it means some `F^i(v)` is on door `1`, whence `F^{i+1}(v) = (1,1)`, or is the root). One parent per non-root node plus termination at the root gives a tree. Holds as stated, with the root's `s = 1` self-loop excluded as the brief says.

**(vi) The root has exactly one child, `(1,2)`.** The root's single door is `y_0 = 1`, live, lowest branch `s = 1`, giving `2 + 1 = 3 → (1,1)` itself — the excluded loop. Its cascade child is branch `3` on door `1`: `8 + 1 = 9 → (1,2)`. Door `1`'s chain at branches `1, 3, 5, 7, 9`: `3, 9, 33 = 3·11, 129 = 3·43, 513 = 27·19` → `(1,1), (1,2), (11,1), (43,1), (19,3)`. Holds as stated.

**(vii) Finite degree.** Children = one cascade child + one door child per live door, and by Theorem 14.5.1 the live doors number `D` or `D − 1` (top door dead iff `2^D Ω ≡ 1 (mod 3)`). The inverse of the parent rule is exact: a node with `s ≥ 3` is the cascade child of the branch-`(s−2)` node; a node with `s ≤ 2` is at the lowest branch of its door, which is a live door of `state(y)`. Holds as stated. **Addition, not in the brief:** every node has a cascade child, so the comb has no leaves; a Garden of Eden (14.5.2) has exactly one child. Recorded as Remark 18.2.4.

**(viii) Peaks along a chain are `A, 4A, 16A, …`.** `2^{s+2} y = 4·2^s y`; equivalently 14.10.1's `N(y,s+2) = 4N(y,s) − 3` with the `−3` moved. Holds as stated.

**(ix) — CORRECTED.** The brief states: "`r` equals the number of door edges on the comb path to the root, and `ℓ − r` the number of cascade edges." This is false at every non-root node, by one. Counter-instance: `(1,2)` has `r = 1` (`F(1,2) = state(1) = (1,1)`) and its comb path is the single cascade edge `(1,2) → (1,1)`: zero door edges. Likewise `(11,1)`: `r = 1`, path `(11,1) → (1,2) → (1,1)`, two cascade edges, zero door edges.

*Re-derivation.* The path from `v` visits `F(v), F²(v), …, F^t(v) = (1,1)`, `t = r`, in order (claim (v)'s chain lemma). Each `F^{i+1}(v) ≠ (1,1)` is entered by the door edge from the lowest sibling on the door of `F^i(v)`'s exit. The root is entered differently: the root's only child is `(1,2)` (claim (vi)), so every path enters `(1,1)` by the cascade edge `(1,2) → (1,1)` — the door edge that would represent the last `F`-step, from the branch-`1` node of door `1` to `state(1)`, is the root's own self-loop, excluded by definition. Hence

```text
door edges on the path  = r − 1,
cascade edges           = ℓ − (r − 1) = ℓ − r + 1 ≥ 1   (the terminal edge is always one of them).
```

*What was wrong in the pre-check.* The root boundary: the self-loop's exclusion removes exactly one door edge from every path, and the pre-check counted the last `F`-step as a door edge. The corrected statement is Proposition 18.3.2(b); the script tests both forms — the stated one held on `0` of `3,000` random chains and `0` of `17,245` census nodes, the corrected one on all.

**(x) Siblings share `r` and are separated by `ℓ`.** All siblings share the exit `y`, hence `F`, hence `r = 1 + r(state(y))`; the branch-`s` sibling is `(s − s₀)/2` cascade edges above the lowest. Holds as stated.

**(xi) — CORRECTED in its equality clause.** `ℓ ≥ r` holds for every node (`ℓ − r = (cascade edges) − 1 ≥ 0`, from the corrected (ix)). The brief's "equality iff the path uses no cascade edge" is impossible for a non-root node — every path uses at least the terminal cascade edge. Corrected: `ℓ = r` iff the path carries exactly one cascade edge (the terminal one), i.e. iff `s(F^i(v)) ≤ 2` for every orbit state before `(1,2)` and the orbit enters `(1,1)` from `(1,2)`. Examples: `(1,2)` (`ℓ = r = 1`), `(7,1)` (`ℓ = r = 2`).

**Completeness against the raw map.** The brief's account is right and is re-derived as Proposition 18.4.1, with one refinement it left implicit: the even number `2A` is the `j = s + 1` instance of the cascade rule (its predecessor is the block's own last odd point), and `2y` for a side door `y = y_{a'}` has as predecessor the previous door `y_{a'−1}` of `state(y)` — the next block's rising run, not the current one's. The dictionary `2^j y ≡ 1 (mod 3) ⟺ j − 1` admissible (or `j = 1`, `y ≡ 2`) is Lemma 18.1.2(iii) applied at `j − 1`, and `w + 1 = 2(2^{j−1} y + 1)/3` places the predecessor as the last representative of the branch-`(j−1)` sibling.

**15.6.2 in comb language.** With `κ = 1 + 2^j k`, `k` odd, `j ≥ 3`: `A(κ,1) = 2 + 3·2^j k` has `s = 1`, so the comb edge is a door edge; the exit `e = 1 + 3·2^{j−1} k ≡ 1 (mod 3)` is the parent's top door with `m₊ = v₂(e+1) = 1` (`3·2^{j−1} k ≡ 0 mod 4`), `a₊ = 0`, so the parent is `(u₊, 1)` with `u₊ = 1 + 3·2^{j−2} k` and `v₂(u₊ − 1) = j − 2` exactly. Repeating while the current `j ≥ 3` gives `⌊(j−1)/2⌋` forced door edges at `s = 1`, `m₊ = 1`, then a depth-`1` core with `j ∈ {1,2}`. Not re-proved on the page (pointer to 15.6.2); verified on `14,099,479` census nodes. The brief's "repeating until `j < 3`" and the count `⌊(j−1)/2⌋` agree when `j` is the exact valuation; for a non-exact `j` the count is a lower bound. No change to ladder.md was needed.

**Largest peak at a level (addition).** A door child's peak is `2^{s₀} y_a ≤ 4 y_{D−1} < 4·(2A/3)`, a cascade child's is `4A`; so the level maximum quadruples, from `2` at the root: `2^{2λ+1}`, on door `1` only. Lemma 18.5.1; the census column confirms it at every level.

## The census comparison with reverse.md 14.4 — a seam

14.4's counts (`833` at `ω ≤ 2^10`, `6,261` at `2^13`) are produced by `experiments/reverse_tree.py`'s `tree_counts`, which expands states in increasing core, keeps predecessors with `ω ≤ X`, and **stops scanning a door's branches once the predecessor's core exceeds `X` and `s > s₀ + 6`** (an early break the page does not mention). That file was read for its counting convention only; the enumerator in `peak_comb.py` is written from 14.1.1 and reproduces both conventions:

- with the early break: `833` and `6,261` — the page's numbers;
- without it (full scan to `s ≤ 420`): `834` and `6,280`. The missed states are `(59,5)` at `2^10` and `19` states at `2^13` (`(203,9)`, `(293,5)`, `(293,6)`, …), each verified to be a 14.1.1 predecessor of a box-tree state, on a live door, at a branch past the break, with core `≤ X`.

Two further facts the comparison turned up, both recorded flat on the page: (1) 14.4's tree is the **box-connected** tree — states reachable backward through states with `ω ≤ X` — not the set of tree states with `ω ≤ X`; the comb's levels contain `2,088` nodes with `ω ≤ 2^10` (`1,322` outside the box tree, each with an `F`-iterate of core `> 2^10`) and `12,211` with `ω ≤ 2^13` (`7,214` outside). The brief's "the counts must agree" holds on the object 14.4 enumerates (every box-tree state has finite `λ`; every one with `λ ≤ 27` — `766` and `4,997` — is a census node at that level) and cannot hold on the naive comparison. (2) The largest `λ` over the box trees is `35` and `43`, so a census to level `27` does not contain the box trees whole.

**Whether to correct 14.4's printed counts is the main session's call**; this branch adds only the pointer sentence there.

## Verification record

`experiments/peak_comb.py`, fresh code (imports nothing from any other script; `reverse_tree.py` was read for its counting convention and not imported or copied). Exact integers at every pass/fail decision; floats only in printed ratios. Canaries first. Seed `20260915`; date 2026-09-15.

Sections and counts:

- Canaries: `(1,1)` and its single child `(1,2)`; door `1`'s chain; door `5`'s three states, peaks, and the raw orbit of `213`; `(7,3)`'s doors `55, 83, 125` and lowest children `(37,1)@1`, `(37,2)@2`, `(167,1)@2`; its cascade child `(251,1)` with peak `752 = 4·188`. `28` checks.
- (a): `2,002` random states (`ω < 10^6`, `d ≤ 40`), `3,000` random even integers `< 10^12`, `2,000` random odd `y` × `j = 1..40` (`80,000` pairs, `3 | y` included).
- (b): the box `ω < 10^5`, `3 ∤ ω`, `d ≤ 30` — `999,990` states, every one: parent valid and of the right type, at branch `s − 2` on the same door or equal to `F`; regenerated exactly once by the parent's child rule; the local chain lemma; the self-child exclusion fired nowhere but the root. Reachability exhaustive on `ω < 2·10^4`, `d ≤ 30` (`200,010` states, memoized; `1,937,973` distinct states visited; largest `r = 148`). `3,000` random full chains against full `F`-orbits (largest level `161`). Degree formula on `2,000` random `(Ω < 10^4, D ≤ 12)`: `361,890` 14.1.1 predecessors at `s ≤ 60` placed on cascade chains; forward scan of `(ω ≤ 3000, d ≤ 12)` at eight targets.
- (c): `3,000` random states, all representatives, `20,759` block trajectories.
- (d): `17,245` census nodes with `r` by direct `F`-iteration (every node while a level has `≤ 2,000`; a deterministic hash sample of about `2,000` per level above), plus the `3,000` chains of (b).
- (e): every odd `x < 2·10^5`, `699,994` trajectory points.
- (f): level-by-level pass to level `20` (`991,425` nodes, `0.9 s`) and depth-first pass to level `27` (`126,917,355` nodes, `63,457,557` at level `27`, **`215.6 s` wall clock** on the author's machine; whole script `257.4 s`); rows identical on levels `0..20`. Level `27` was chosen so that a review re-run stays under five minutes; one more level doubles both counts and the time.
- (g): `14,099,479` depth-`1` census nodes with core `≡ 1 (mod 8)`, the forced chain with exact valuations at every step.
- (h): the two run-length tables and the `s = 1 : s = 2` split, census and uniform box side by side.
- 14.4 comparison: both enumerator conventions at `2^10` and `2^13`; `λ` of every box-tree state by parent chaining; membership of every box-tree state with `λ ≤ 27` in the census at that level; every census node with `ω ≤ X` outside the box tree shown to leave the box.

**TOTAL: checks = 64,383,062, failures = 0.** Output committed verbatim at `experiments/peak_comb_output.txt` (the wall-clock lines are the only machine-dependent ones).

**Single reproducing command:**

```
python experiments/peak_comb.py
```

No phases, no flags. Runs in about four and a half minutes.

`experiments/encoding_scan.py`: **RESULT: CLEAN** (run after every wiki edit and again before the final commit).

## The exploratory table, read once

The uniform box (`ω < 10^5`, `d ≤ 30`) matches the `2^{−j}` ledger at every printed entry: own cascade run `P(k) = (3/4)4^{−k}` to four decimals, door runs geometric with mean `3.992` against `4`, door edges `2 : 1` at `s = 1 : 2`. The census population deviates in a fixed way: `P(k) ≈ 2^{−(k+1)}`, door runs halved (mean `2.000`), the split `1 : 1`. All three are the same structural fact — every node has exactly one cascade child, so half of each level sits above its lowest sibling, and the comb counts every door once where the forward ledger weights doors by visits (the door multiplicity `D` of 14.5.3's renewal). A calibration line; nothing proposed, per the brief.

## For the main session at merge

- **Base and seams.** Cut from `8eeba63`; touches `comb.md` (new), `reverse.md` (one sentence at the end of 14.4 and the front-matter date), `symbols.md` (the `A` row's cross-reference, five new rows at the end of §4, the `A` entry of the collision index, the date), `TOUR.md` (one dictionary row after the top-door row), `index.md` (one page-table row after `ladder.md`, one resolver entry `§18 → comb.md`, the date), `experiments/peak_comb.py` and its output, and this file. Nothing else. `ladder.md` untouched (the restatement of 15.6.2 needed no clause there: the mechanism as written already gives the exact valuation `j − 2` at each step). `HANDOFF.md`, `README.md`, `cycles.md`, `aeh.md`, `stage*.md`, `open-problems.md`, `publication.md`, `paper/`, `sources/` untouched.
- **Symbol choices.** The brief's `r` and `ℓ` both collide with registry rows (`r`: stratum component, frame 4, and rotation index, frame 3; `ℓ_n`: the letter at block `n`, frame 6). Adopted: **`η`** for the reduced distance and **`λ`** for the peak distance (the level). Neither carries a registry row; both appear as bound variables (aeh.md 13.2.4–13.2.5; cycles.md 12.7's `λ`-form), noted in the rows' "Elsewhere" column rather than the collision index, which lists glyphs with two or more rows. If the main session prefers other glyphs, the page uses each in a handful of places.
- **Two corrections to the brief's claims**, both re-derived above and tested in both forms by the script: (ix) `r = door edges + 1`, not `r = door edges`; (xi) equality `ℓ = r` iff exactly one cascade edge (the terminal one), not iff none. The cause is one fact — the root's self-loop is the only door edge into the root, and it is excluded, so every path enters the root by `(1,2) → (1,1)`. Worth an independent re-derivation at review (the brief already lists (v)–(vii) and (ix) for that).
- **14.4's counts.** `833`/`6,261` are the early-break variant of the enumeration; the full scan gives `834`/`6,280`. The page (18.5) records both flat and attributes the difference; whether reverse.md 14.4 should be corrected — and whether its "enumerated *completely*" wording should say "box-connected" — is the main session's decision; this branch adds only the pointer.
- **What the author should see first in the exploratory table:** nothing beyond the paragraph above — the census/ledger deviation is a population artifact of the comb's one-cascade-child-per-node structure, and the uniform box matches the ledger. The one small proved addition is Lemma 18.5.1 (largest peak at level `λ` is `2^{2λ+1}`, on door `1`), which the census column displays exactly.
- **Grade.** Formulation; no front moves; the family frame not reintroduced (the page uses "siblings on a door", never columns or cores as a grouping); the conjecture stated as "the comb spans every state", Theorem 9.8.3 unchanged.

## Files changed

- `experiments/peak_comb.py` (new), `experiments/peak_comb_output.txt` (new)
- `comb.md` (new, §18)
- `reverse.md` (one pointer sentence at 14.4; front matter `updated`)
- `symbols.md` (`A` row cross-reference; five rows in §4; collision-index `A` entry; front matter `updated`)
- `TOUR.md` (one dictionary row)
- `index.md` (page-table row; resolver entry; front matter `updated`)
- `briefs/peak-comb-findings.md` (this file)
