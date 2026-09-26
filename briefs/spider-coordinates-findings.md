# Findings: the coordinates of a spider (spiders.md 19.5)

## Base and branch

The worktree was cut from a stale HEAD (`946e0d8`), which did not contain `briefs/spider-coordinates-brief.md`. Per the brief's Rules it was brought onto local `main` first: `946e0d8` is an ancestor of `main`, so this was a fast-forward to `6a3b450` (the brief's own commit), with nothing of the worktree's to carry over. Branch `spider-coordinates` was cut there. **Base SHA: `6a3b450`.**

## What the pre-check got right, and where this session differs from the brief

The three pre-checked identities (Items A, B, C) re-derive and verify as stated; nothing in them was wrong. Points where the page departs from, sharpens or corrects the brief:

1. **Item A's statement, the `b = 0` case.** The brief lists the lower legs as `b = 1, …, D−1` and treats `(y_0(Ω, D+1)/3^t, 1)` at `t ≤ 1` as one further leg. The page splits that leg by `t`: at `t = 0` it is `y_0(Ω, D+1)` itself, a door of `(Ω, D+1)` like the others, and it takes the *lower* lens form with `b = 0`; only at `t = 1` is it the **top leg**, `y_0(Ω, D+1)/3`, with the `3x_0 + 1` form. The brief's own lens section already has this split (its "lower leg `b ≥ 1`" and "top leg (`t = 1`)"); the page makes the `t = 0` case explicit (lower leg, `b = 0`, a fork).
2. **Item C(c), the exponent.** The brief left the exponent open ("`Ω mod 3^{f+1+b}` or whatever the exact exponent is — derive it"). Derived: whether `w` starts the hair is a function of `x_0 mod 3^{f(w)+1}`, i.e. of `(D, Ω mod 3^e)` with `e = max(0, f(w) + 1 − b)` at a lower leg (the `b` digits are already fixed by `x_0 ≡ −1 mod 3^b`, so the lower leg's index *subtracts*, not adds) and `e = f(w) + 2` at the top leg; the end of the hair costs one digit more. Measured exact by full-coset search over `Ω mod 3^7` (`D = 2..6`, every leg type): the least modulus equals `3^e` in all `1,426` non-forced cases; the `39` forced cases are `35` with `e = 0` and `4` instances of `b = 2`, `w = 0101` (`e = 1`, forced because the only excluded digit value is `0`, which `3 ∤ Ω` rules out).
3. **Item E.2, the expected growth.** The brief expected the position's modulus to grow by ternary digits per fork step "by 19.3's accounting". It does not: the descent reads **two binary digits per step** and **one ternary digit in all**, because `(3x+1)/4 ≡ 1 (mod 3)` for every `x` and `(x+1)/4 ≡ x + 1 (mod 3)`. Proved sufficient: `x mod 2^{2j+3}·3`; measured exact for `j = 0..7` (`24, 96, …, 393,216`). The ternary budget of 19.3 and 19.5.3(c) belongs to the *ascent* from a leg (hair shape from the abdomen); the *descent* from a member is a fixed-parity segment of `T`, i.e. a Terras cylinder. This is recorded in the page as a correction of the expectation, with the derivation.
4. **Item E.2, the owner's `D` and `Ω mod 3`.** The brief asked whether either is determined by a bounded residue at fixed `j`. Answered *no* by proof, not only by measurement (Proposition 19.5.5.1): the member sees `D` only through `2^{D+1−b}` in its leg, which any fixed `2`-adic modulus loses; shifting `D` by one and `Ω` by `2^{−1}` mod a high power of `3` keeps the member's residue and flips `Ω mod 3`. The existence of long enough hairs at `b = 1` legs is part of the proof (choose `Ω ≡ 2^{−D−1} mod 3^{j−1}`, which puts `x_1 ≡ 1 mod 3^j`, and fork steps multiply `x − 1` by `4/3`). Verified by `336` explicit constructions.
5. **Item E.1, the skip rule.** The brief said to skip `(α, β)` pairs where `αx + β` can vanish. It vanishes only at core `1` with `β = −α`, and skipping those pairs would drop exactly the fork-step invariant `g_{1,−1}`. The script keeps every pair and gives the value `0` a sentinel instead; `25` pairs, `337` zero values, all at abdomens `(1, D)`.
6. **Item E.1, the window.** A first run showed every pair "constant" on `41,061` spiders with a matching shuffled baseline — the abdomens at level `18`, which have no leg inside the window and are pieces of size `1`. They are left out of every spider table (a check asserts they are alone in the window), and counts are given both over the `41,429` spiders with abdomen at level `≤ 17` and over the `5,129` complete ones (every hair ends inside the window). The window cut also produces `3,460` spiders with a constant exit — each an abdomen with only its cascade leg and that leg's link-step child in the window (a cascade chain cut at level `18`); on complete spiders the count is `0`.
7. **Glyphs.** `P` (the brief's provisional name) is the period in `symbols.md` §4; the descent map is `desc`. `b` and `w` collide with aeh.md's bit scale and cycles.md's arc weight; `ε` and `c` gain a meaning each. All registered with collision rows. "Lens" is an ordinary word in anchor-digit-search.md 17.7.4 ("operation lenses"), noted in the row.

## Derivations beyond the brief (proved and verified; in the page)

- **The lens as a door.** `lens_{b,w}(x) − 1` is the door `b` (top leg: door `0`) of `(Ω, D + 1 + 2k)`. So the lens carries a member at hair position `k` to a representative of the abdomen's core at depth `D + 1 + 2k` — the exact form of the analogy with `x + 1 = 2^m 3^a ω`.
- **The raw descent lands on the run.** 19.5.2's raw map read on `n mod 8` (not `mod 16`) takes every depth-`1` member down its hair and one step further, onto the run element `y_b(Ω, D)` of its owner — by the sibling move from a lower leg (`n_0 = 4y_b(Ω, D) + 1`), by a two-halving step from a top leg (`3n_0 + 1 = 4y_0(Ω, D)`) — whose state and door index are the owner and the leg index. In raw terms the owner is read by two valuations *at the end of* the walk.
- **The deep legs (Corollary 19.5.3.1).** A lower leg with `b ≥ 3` carries exactly the hair `0 1 0` (four nodes); `b = 2` begins `0 1 0 1`, the fifth node a link iff `2^{D−1}Ω ≡ 2 (mod 3)`; at `b = 1` the second node ends the hair iff `2^DΩ ≡ 1 (mod 3)`. Checked at every lower leg walked (`23,944` with `b ≥ 3`, `29,295` with `b = 2`, `84,490` with `b = 1`, census and random together).
- **The two step invariants.** A link step preserves `free(3x − 1)` (the exit `y`: `3x′ − 1 = 4(3x − 1)`); a fork step preserves `free(x − 1)` (`x′ − 1 = (4/3)(x − 1)`, the all-fork case of the member formula). No affine pair preserves both.

## A flag on 19.2's hair-length law (not edited; for the author and the main session)

By Corollary 19.5.3.1 the first steps of a hair at a leg with `b ≥ 1` are fixed by the leg's own digits. Measured over every leg of the `82,490` census abdomens, walked to the true end (`192,282` hairs; shares of lengths `1, 2, 3, 4` nodes):

```text
b = 0 (41,286)   0.332 0.114 0.146 0.086     chain from a fork: 0.333 0.111 0.148 0.086
b = 1 (82,490)   0     0.501 0.167 0.056     chain from a link: 0     0.333 0.111 0.148
b = 2 (27,432)   none below 5
b >= 3 (13,721)  all 4
top  (27,353)    0.170 0.220 0.129 0.115
all  (192,282)   0.0954 0.2705 0.1214 0.1299  19.2's predicted mixture: 0.0950 0.2700 0.1217 0.1306
```

So 19.2's two-state chain is not the law leg type by leg type (only the `b = 0` fork legs follow it closely), while the mixture over all legs agrees with 19.2's prediction to within `1%` at lengths `1–4`, as 19.2 itself measured. 19.2 calls the chain "forced by Items A.1–A.2" with the depth ledger as a measured input; what this adds is that the per-step `t` draws are not independent of the leg's position along a hair's first steps, and the agreement is a property of the mixture. The page states this in one flat paragraph after Corollary 19.5.3.1 and does not examine why the leg types average to the chain; §19.2 is not reworded (per the brief). Whether 19.2's wording ("forced by Items A.1–A.2") wants a pointer is the author's call.

## Reading of Item E

The searches close negative in the forms tried, and each positive-looking count has a derived cause:

- **E.1, affine lenses.** Nothing is constant on spiders beyond one small-core coincidence (the spider of `(1,2)`, where `Ω = 1`), at the shuffled baseline's level (`≤ 1`). On hairs, exactly two pairs are constant at scale — `g_{3,−1}` on the `22,934` window hairs whose steps are all link steps, `g_{1,−1}` on the `6,408` whose steps are all fork steps (plus one small-core coincidence, `5, 19, 25`) — and both are the derived step invariants, not discoveries. Every other count is `≤ 4`, against a baseline maximum of `3`.
- **E.1 (ii), lenses returning the owner's core.** The pairs that return `Ω` at a member are exactly the `k ≤ 2` lenses of Proposition 19.5.3(b) whose coefficients lie in the searched range — each at `100%` of its position class and nowhere else beyond `769` coincidences among `1,097,430` hits (`≤ 12` per pair). The search rediscovers the lens identity for short words and nothing else.
- **E.1, comb quantities.** Peak and top door are injective; the peak's odd part is the exit by definition; exit and `F` are constant only on window-cut cascade chains; `F²` also on two complete spiders next to the root (`(1,2)`, `(3641,2)`, all members within two `F`-steps of `(1,1)`).
- **E.2.** The position is a Terras-type cylinder: bounded residue at each fixed `j`, modulus `2^{2j+3}·3`, no single modulus for all `j`. The owner's `D` and `Ω mod 3` are decided by no bounded residue at any `j` (proved).

The answer the page gives the author: the coordinates `(Ω, D; b, w)` with the lens identity, exact in the direction abdomen → member; in the direction member → abdomen, the hair descent, which is the member's own Collatz orbit in two-halving steps and sibling moves, of unbounded length. The closure is stated as bounded (the coefficient ranges and residue forms searched) with no impossibility claimed beyond Proposition 19.5.5.1.

## Literature check (Item D)

What was checked, with no web access: `TOUR.md`'s dictionary rows and the works they cite; both published papers (`paper/collatz-reduced-v3.tex`, `paper/collatz-mirror-v1.tex`) and their bibliographies; the drafts under `sources/drafts/` (grep for `4n+1`, `4x+1`, `4y+1`, "sibling", "preimage tree", "inverse tree", "predecessor"). No name for the object was found. The relation `T(4n + 1) = T(n)` appears in the record only as the cascade step (reverse.md 14.10.1) and in comb.md 18.4.1. Paper 2's related work cites Wirsching 1998 for predecessor trees; the record does not hold Wirsching's text, so whether it names this object is not checked. Recorded flat in TOUR.md's spider row and in 19.5.4.

## Verification record

- `experiments/spider_coordinates.py` — fresh code, imports nothing from any other script in the repository (numpy only, for the E.1 tables, on `int64` arrays with the headroom asserted: largest core `45,812,984,491`, `27·max + 27 < 2^62`). Seed `20260926`. Single reproducing command `python experiments/spider_coordinates.py`, which writes `experiments/spider_coordinates_output.txt` itself (no shell redirection). **`15,380,113` checks, `0` failures, wall clock about `34–35` s** (`33.8`, `34.6`, `35.2` s across the final runs). Part 0 (canaries) `16` checks; Part A `1,046,447`; Part B `1,199,762`; Parts C–D `13,108,179` (the walk `12,779,358`, lifts `327,356`, the full-coset measurement the rest); the census check and Part E the remainder.
- Counts and ranges: census to level `18` built fresh, `247,932` nodes (per-level counts equal to spider_layer.py's); Item A on `3,000` random abdomens (`Ω < 10^6`, `2 ≤ D ≤ 14`) and all `82,490` census abdomens, plus `2,000` depth-`1` nodes for (a) at `D = 1`; Item B on `15,000` random depth-`1` nodes (`x < 10^9`) and all `165,441` census depth-`1` nodes; Items C–D at `978,238` members (`906,149` from every leg of every census abdomen, inside or past the window, `192,282` hairs; `72,089` from `2,000` random abdomens), longest hair `55` nodes, `770,195` raw moves; `163,678` random lifts for 19.5.3(c); the full-coset word measurement over `Ω mod 3^7`, `D = 2..6`; E.2's full-coset position search for `j = 0..7` with `300` lifts per `j`; `336` constructions for Proposition 19.5.5.1.
- Output lines carrying wall-clock times differ run to run; everything else is deterministic under the seed.
- Date: the work and the verification lines are dated 2026-09-26, the brief's date; the session's final re-runs of the script ran across midnight into 2026-09-27 with identical counts.
- `experiments/encoding_scan.py`: **RESULT: CLEAN** (run before the final commit; `553` tracked files with this file included).

## For the main session at merge

- Re-run `python experiments/spider_coordinates.py` (about `35` s, foreground); the committed output should match except the timing figures.
- Re-derive independently, as the brief plans: Lemma 19.5.1 (the four lines of (a)–(b) are one identity each, `4y_a + 1 = 3y_{a−1}(Ω, D+1)` and `4A + 1 = 3y_{D−1}(Ω, D+1)` and `2y_0 + 1 = y_0(Ω, D+1)`), and Proposition 19.5.3(a)–(b) (a two-line induction). The exponent in 19.5.3(c) is the one place the page chose a formula the brief did not supply; its proof is the digit fact 18.9.2.2(c) applied step by step, and the measurement found it exact wherever the prefix is not forced.
- Proposition 19.5.5 (position modulus) and 19.5.5.1 (owner not a bounded residue) are new proofs, short; the second's existence step (long hairs at `b = 1` legs from `Ω ≡ 2^{−D−1} mod 3^{j−1}`) is worth a hand check.
- The flag on 19.2 (above): per leg type the hair lengths are not 19.2's chain; the mixture agrees. The page records it in 19.5.3 without rewording 19.2; whether 19.2 wants a pointer is the author's decision.
- E.1's affine table uses a sentinel for the `25` pairs with `αx + β = 0` (at core `1` only) instead of skipping them as the brief said, because skipping would have removed the fork-step invariant `g_{1,−1}`; the page says so in one clause.
- E.2's result corrects the brief's expected accounting (descent: binary digits, two per step; the ternary budget belongs to the ascent). Stated in the page with the derivation, not as a dispute.
- No edits outside `spiders.md`, `symbols.md`, `TOUR.md`, `index.md`, the new script and output, and this file; `HANDOFF.md`, `README.md`, `viz/` untouched. No cycle searched, no front moved, nothing proposed, no anchor or family-frame vocabulary.
