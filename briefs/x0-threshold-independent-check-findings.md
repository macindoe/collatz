# Findings: independent check of cycles.md 12.8.7 (the staircase at threshold X₀)

Brief: `briefs/x0-threshold-independent-check-brief.md`. Branch `x0-threshold-independent-check`, base `e7a3f5e`. Size-only: no cycle search, no divisibility test, nothing excluded. `cycles.md` is not edited; what is below is findings only.

**Verdict (L-A12): ripe to offer.** Every numbered claim of 12.8.7 holds on a fresh implementation, every shared number reproduces exactly, and the proof of Thm 12.8.7.2 holds as written. The five findings below are wording and rounding fixes to make before or alongside the offer. None of them touches a numbered statement's truth.

## 1. Implementation and reproduction

`experiments/x0_threshold_independent_check.py` was written from the text of `cycles.md` 12.1, 12.6.1, 12.8, 12.8.6.2 and 12.8.7 alone, and committed with its output (`541ebf8`) before the original script or its output was opened.

- **Command:** `python experiments/x0_threshold_independent_check.py`. It writes `experiments/x0_threshold_independent_check_output.txt`, is deterministic and seeded, and takes about 15 minutes.
- **Arithmetic:** exact integers and Fractions throughout. Every real quantity is a rigorous dyadic interval at 720 bits: `ln` by an atanh series with a tail bound, and `exp` by a Taylor series with a tail bound. An interval comparison that cannot be decided raises instead of guessing.
- **Enclosure of `L`:** width `2^-716`, cross-certified against exact `3^b` vs `2^a` at 16 convergents and 300 random fractions. `K = bitlength(3^n) = ⌈nL⌉` was checked for `n ≤ 3000` and for 40 random `n ≤ 4·10^6`.
- **Independent of the original in method:**
  - `R_r` is evaluated by a forward Horner scheme. At small sizes it is also checked against the literal sum. At large `n` the transport recurrence is used, closed exactly against a direct `R_(p-1)` and back to `R_0`.
  - The dictionary (i) is checked as an exact rational identity in which the arc terms are built from the arcs themselves.
- **Result:** 43 checks, 0 failures, and all negative controls bite.

## 2. Grid and totals

**Prop 12.8.7.1 and Cor 12.8.7.3 (necessity):**
- Exhaustive grid: `p ≤ 4`, `n ≤ 13`, `K ∈ {⌈nL⌉, ⌈nL⌉+1}`, all `(m, s)`. That is 57,396 configurations, 462 of them size-passers.
- Random: 30,000 configurations with `p ≤ 9`, mixing uniform and staircase-shaped draws (seed 20261019). 1,918 of them are size-passers.
- Totals: 87,396 configurations, of which 2,380 are (S)-passers and 1,903 have a unit block. There are 9,809 (S)+(X) pairs over `X₀ ∈ {1,2,3,5,10,30,100,1000}`, and 20,384 forced-(X) instances.
- (iv) was also checked on 3,000 random positive-rational sequences at every cyclic start.

**Thm 12.8.7.2:**
- 598 `(p, n)` points, `p = 2..24`, `n ∈ [3p+40, 40000]` (seed 8128).
- 308 points meet (H0)+(H1′): 52 deep crash and 256 unit crash. 206 of them also meet (H1).
- The proof's algebra was checked by 200 exact-rational substitutions.

**Thm 12.8.7.4:**
- `p₁` for every `X₀ = 2^j`, `j ≤ 200`, for every integer `X₀ ≤ 16`, and at the named values.
- Two-distance structure enumerated for `k = 1..13`, with `N` up to 301,739.
- Brute-force miss runs over `n ≤ 3·10^6` for four arcs.
- Top windows `[n*−N+1, n*]`: 101 windows over `X₀ ∈ {1,2,5,6,16,100,256,1000,4096}`, `p = p₁ … 24–27`, giving 233 Construction B instances (`n` up to about 1.1·10^6). 92 are deep crashes and 141 have some `m_t = 1`.
- 24 windows placed at random lower in the scale range (the "every scale" sentence).

**Remark 12.8.7.5:** the condition and the exact inequality, evaluated at `p = p₁(X₀)` at the weakest point of the window for 9 table rows.

## 3. Per-claim verdicts

| Claim | Verdict |
|---|---|
| 12.8.7.1 (i) identity, at every rotation, and `γ−1 ≤ log₂(x_min+1) < γ + log₂ p` (exact integer form), including the `r₀ = j*` all-terms-`< 2^γ` step | holds, 0 failures |
| (i) "`γ ≥ log₂(X₀+1)+1` forces `x_min ≥ X₀`" | holds (20,384). Negative control: with the `+1` dropped, (X) fails at 678 instances, so the `+1` is load-bearing |
| (ii) trim, (iii) unit block | hold on all 2,380 / 1,903 passers |
| (iv) Rozier minimax | holds at every start. Equality at the real extremal `m_j = L^j` (gap `10^-214`). Negative control: `L·ε_p` in place of `ε_p` fails there |
| Cor 12.8.7.3 necessity / the "Consequently" line | holds on 9,809 (S)+(X) pairs |
| Thm 12.8.7.2: entries ≥ 1, `Σm = n`, `c ≥ 1`, (S) at all `p` rotations, Rozier max `= m_0 ≤ γ − η`, (X) at the largest admissible `X₀` | holds at all 308 points and all 233 + 24 window instances |
| Thm 12.8.7.4: every top window and every random lower window contains `n` with `γ ∈ [g, g+1]`; (H0), (H1′), `η ≤ 2^-20`, (S), (X); `λ ≤ γ − ε_p n ≤ λ+1.5`; `ε_p n ≤ m_0 ≤ γ`; `γ−1 ≤ log₂(x_min+1) ≤ γ+1.874469`; the `X₀ ≥ 6` form; `Λ ≥ 2^{-γ}`; `Λ > 0.054·2^{-ε_p n}` (natural-log `Λ`) | holds, all exact or certified. Measured: `γ − ε_p n ∈ [2.7261, 3.8267]`, `log₂(x_min+1) − γ ∈ [0.0074, 0.5035]`, `γ − log₂(X₀+1) ∈ [1.0025, 1.9974]` |
| `2^{-(λ+1.5)} = 0.05405… > 0.054` | holds (`0.054051848`). The retired `0.0541` is false here, as already corrected |
| Sweep: max gap of `N = q_k+q_{k-1}` points is `θ_{k-1}` | holds, `k ≤ 13`. Brute-force longest miss runs are 28, 52, 2,300 and 15,600 against `N−1` = 52, 52, 16,265 and 16,265. The bound is attained at `X₀ = 16`. Negative control: the previous CF level's `N′` is too short for all four arcs |
| `p₁` table: 10 (`X₀ ≤ 16`, every integer), 22 (`2^8…2^12`), 36, 94, 98, 110, 309 | holds exactly |
| Remark 12.8.7.5: the condition holds from `2^20` (`p = 36`) through `2^200` and implies the exact negation of (iii); it fails at `2^8` and `2^12` | holds |
| Negative control: Construction B at trim-forbidden `n` | (S) fails at all 112 |

## 4. Findings (discrepancies and wording); none changes a numbered claim's truth

1. **"`p₁ − log_L X₀ ∈ [2.92, 10.42]` over the table" is true only of the original's sampled rows.**
   - The original tabulates `j ∈ {0..20, 30, 40, …, 200}`, and the extremes `2.920` (`j=16`) and `10.415` (`j=17`) reproduce exactly here.
   - Over every `j ≤ 200`, which is what the Verified line's "`p₁` for `X₀ = 2^j`, `j ≤ 200`" suggests, the range is **`[2.784, 10.629]`**, attained at `j = 143` (`p₁ = 218`) and `j = 74` (`p₁ = 122`).
   - Diagnosis: the original samples `j` in steps of 10 above 20. Every `p₁` value the two computations share agrees.
   - Fix: either quote `[2.78, 10.63]` over all `j ≤ 200`, or say "over the tabulated rows".
2. **"For `X₀ ≥ 5.541`" is a hair low.** The switch point is `2^λ − 1 = 5.54100467…` (certified `> 5.541`). On `[5.541, 5.5410047)`, `g = 1+λ`, so `γ ≤ log₂(X₀+1)+2` is not implied. Fix: write `X₀ ≥ 5.5411` (or `X₀+1 ≥ 2^λ`). This is the same genre as the 0.0541 correction.
3. **The 1.874469 constant is rounded down.**
   - The proof's bound is `log₂(1 + 2^{-3(L-1)}/(1 − 2^{-(2L-3)})) = 1.87446912…`, which I re-derived independently: `e_0 ≥ 3(L−1)−1`, growth `≥ 2L−3` per climb block, an infinite geometric sum, and `(1−2^{-s_c}), 2^{-δ} ≤ 1`. The original adds `2^-30` for the post-binding tail.
   - So the derivation supports `≤ γ + 1.8744692`, not `1.874469`. The difference is 1.2·10⁻⁷.
   - The true slack is large: the sup over the construction's own cap dynamics is 0.643, and the measured maximum is 0.5035. So the inequality as printed is true; only the printed constant is not what the derivation gives.
   - Fix: `1.87447`.
   - Also, "`p ≥ 10`" in that sentence is not used by the bound as re-derived. It at most controls the post-binding tail.
   - The original checks these brackets in floating point with `1e-9` tolerance (its line 858). Here they are certified intervals.
4. **The "deep crash" paragraph overstates.** "Where `γ < Γ(p, n)`, the budget never binds and `c` is large" is false as a universal statement. Of 102 points meeting (H0)+(H1′) with `γ < Γ`, the budget is reached at 50, all landing at `c = 1`. The original's own summary shows the same thing: (H1) fails at 83 of its 95 runs, but only 66 are deep crashes. Diagnosis: `Γ` is sufficient, not necessary, for crash depth 1, as 12.8.6.2's "conservative by 0.6–0.9 bits" already records. Thm 12.8.7.2 itself claims only `c ≥ 1`, and Remark 12.8.7.5's "forced" is a separate argument via (iii), so no numbered claim is affected. Fix: "where `γ < Γ`, crash depth 1 is no longer certified, and typically `c` is large".
5. **Remark 12.8.7.5's constant 2.09 needs `p ≥ 12`.**
   - The exact slack is `1.5 + (L−1)(1 + 1/(L^{p-1}−1))`: 2.0944 at `p = 10`, 2.0909 at `p = 11`, and `≤ 2.0887` from `p = 12`.
   - The remark is applied only at `p ≥ 36`, so the claim stands.
   - Fix: add "(valid for `p ≥ 12`)", or use 2.095.

**Reconciliation of shared numbers.**
- Matching:
  - the `L/(L−1)` and `λ` digits;
  - the convergent denominators;
  - two-distance `N` and `k ≤ 13`;
  - the miss runs at `X₀ = 1` (28) and at the `N = 16266` level (15,600);
  - every `p₁` that both computations evaluate.
- Nine of the original's Construction B instances were re-run here: `(1,10,164)`, `(1,23,68117)`, `(1,27,429906)`, `(10,13,1188)`, `(31,15,5614)`, `(100,24,534318)`, `(1000,22,345217)`, `(4096,22,427212)`, `(4096,25,1760971)`. Each one:
  - lies in its window, at the same offset counted from `n*`;
  - has the same `γ`, `ε_p n`, `γ − ε_p n` and crash depth `c` to all printed digits;
  - passes (S), (X) and (H1′).
- Measured ranges differ only by grid. The original's `γ − ε_p n` minimum is 2.7532 over 95 runs; mine is 2.7261 over 233. Both are `≥ λ`.
- No numerical discrepancy was found other than finding 1.

## 5. Hand re-derivation of Thm 12.8.7.2's proof

Notation as in 12.8.6.2. `η = −log₂(1 − 2^{-s_c})`, `s_c = S − p + 1`, and `log₂ q = K − γ`.

1. **The caps.**
   - `log₂ X_r = L·T_{r−1} + (n − T_{r−1} + p−1−r) + s_c − η`.
   - Subtracting `K − γ` and using `s_c = K − n − p + 1` gives `log₂(X_r/q) = γ − η + (L−1)T_{r−1} − r = f_r`, so `cap_r = ⌊f_r⌋`.
   - **Holds.**
2. **Climb rotations (`r ≤ p−2`).**
   - In rotation `r`, the crash block sits at position `t = p−1−r`, with `M_t = T_{r−1}` and `S_t = (p−1−r) + (n − T_r)`.
   - So that term is `X_r/2^{m_r}`, and `m_r ≤ cap_r ⇔ q ≤` that term `≤ R_r`, since all terms are positive.
   - Step (a) needs only `γ ≥ 2+η`, which gives `cap_0 ≥ 2` and `f_{r+1} − f_r = (L−1)cap_r − 1 ≥ 2L−3 > 0`, together with (H0) after binding. I checked the post-binding case: `T_{j−1} = n−p+j` gives `f_j ≥ γ + (L−1)(n−p) − j(2−L) − η ≥ 1` by (H0).
   - **Holds as written.**
3. **Crash rotation.**
   - The position-0 term is `3^{T_{p−2}}(2^{s_c}−1)`. Its `log₂` is `L·T_{p−2} + s_c − η`, and comparing with `K − γ` gives exactly `L·T_{p−2} ≥ n+p−1−γ+η`. This is in fact an iff for that term.
   - *Never binds:* `T_r > A_r` by induction from `T_{−1} = A_{−1} = 0`, using `⌊f⌋ > f−1` and `L > 0`, so the inequality is strict. The clearing identity `L·A_{p−2} − (n+p−1−γ+η) = [(L^p−1)/(L−1)]·(γ − Γ′)` holds: I expanded it by hand and checked it by 200 exact substitutions. So (H1′) suffices. A tie `budget = cap` is harmless, because it yields `T_{p−2} = n−1`, the binding case.
   - *Binds:* afterwards each `m_j = 1` (budget 1, `cap ≥ 1`), so `T_{p−2} = n−1`. The requirement `(L−1)n ≥ L+p−1−γ+η` follows from (H0) since `Lp ≥ L+p−1`.
   - **Holds.**
4. **Entries, `Σm = n`, `c ≥ 1`.** `m_{r−1} ≤ budget_{r−1}` gives `budget_r ≥ 1` and `T_{p−2} ≤ n−1`. `budget_0 = n−p+1 ≥ 1` because `S ≥ p` forces `n ≥ p`. **Holds.**
5. **Rozier quantity.**
   - Climb terms are `m_r − (L−1)T_{r−1} ≤ f_r − (L−1)T_{r−1} = γ − r − η`.
   - The crash term is `n − L·T_{p−2} ≤ γ+1−p−η` by step 3. It is `≤ 0` when the budget binds, since `n ≥ 3`.
   - **Holds, with one unstated case.** The text's comparison "`< ⌊γ−η⌋`" identifies `m_0` with `cap_0`, which is true unless the budget binds already at `r = 0`. In that case `m_0 = n−p+1` and every other term is `≤ 1 − (L−1)(n−p+1) < 1 ≤ m_0`, so `max = m_0` still holds. `m_0 ≤ cap_0 = ⌊γ−η⌋ ≤ γ−η` in all cases. This is an exposition gap only; it was checked at every instance.
6. **(X).** The empty-arc term of (i) is `2^γ(1−2^{-s}) ≥ 2^{γ−1}`, so `x_r + 1 ≥ 2^{γ−1} ≥ X₀+1`. **Holds.**

Every step holds as written. The only gap is the unstated binding-at-0 case in step 5, and the claim is true there too.

## 6. Ripeness for L-A12

**Ripe.** The statement, the proof of 12.8.7.2, the `p₁` table and the `0.054` constant are confirmed by a fresh implementation, and the original's instances reproduce digit for digit. Make the wording fixes 1–5 (`[2.78, 10.63]` or "tabulated rows"; `5.5411`; `1.87447`; the deep-crash sentence; `p ≥ 12` for 2.09) in `cycles.md` before or alongside the offer. None changes the claim being offered.
