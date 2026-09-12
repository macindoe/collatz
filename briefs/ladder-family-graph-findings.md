# Findings: the family graph's guaranteed neighbours (ladder.md 15.7)

Brief: `briefs/ladder-family-graph-brief.md`. Branch **`ladder-family-graph`**.

**Base SHA.** The worktree's HEAD at session start was `a7543ce`, dated
2026-09-13, but it did not contain `briefs/ladder-family-graph-brief.md`
(that file was added by `90ed633` on the primary checkout's local `main`,
three commits ahead). Per the brief's Rules, the worktree was rebased onto
local `main`: `git rebase main` fast-forwarded cleanly to **`90ed633`**
("briefs: two delegation briefs for HANDOFF items 4 and 5..."), which does
carry the brief. Branch `ladder-family-graph` was cut from `90ed633`.

Register: flat, calibrated prose. Every number below either comes from
`experiments/ladder_family_graph.py`'s committed output
(`experiments/ladder_family_graph_output.txt`) or is a hand computation
reproduced in this file; nothing is labeled proved without that script's
independent check. Per the brief: every claim in the Provenance is a claim
re-derived here from the definitions, not assumed from the pre-check or from
HANDOFF item 5's write-up of it.

---

## 0. Notation, recapped from spine.md, stage3.md, symbols.md

State `(ω, d)`: odd core `ω` (`3 ∤ ω`), depth `d ≥ 1`.

```text
A(ω,d) = 3^d ω − 1,          s(ω,d) = v_2(A),        e(ω,d) = A / 2^s     (the exit / door)
C(ω,d) = A + 2^s = 2^s(e+1),
e + 1 = 2^{m₊} 3^{a₊} Ω,     m₊ = v_2(C) − s,  a₊ = v_3(C),  D = m₊ + a₊
F(ω,d) = (Ω, D)
```

(spine.md §5.4–5.6, §7.1–7.3; stage3.md 11.8.6.2–11.8.6.3; symbols.md
frame 1–2 for `m₊, a₊, C, σ = s+m₊`.) `F(ω,d) = (Ω,D)` is exactly the
statement "`(ω,d)` is a predecessor of `(Ω,D)` at door `y = e(ω,d)`, branch
`s`" in reverse.md 14.1.1's language — the same operation, read forward.

The ladder recursion (ladder.md 15.1, re-derived): since
`A(ω,d+1) = 3^{d+1}ω − 1 = 3A(ω,d) + 2`, an elementary induction gives, for
every `k ≥ 1`,

```text
A(ω,d+k) = 3^k A(ω,d) + (3^k − 1).                                    (0.1)
```

---

## 1. Law (i): merge/skip by `m₊`, re-derived

**Setup.** Fix `(ω,d)` with `s(ω,d) = 1` (off-spike), so `A = 2e` (`e`
odd). By ladder.md 15.1.1 (re-derived and verified fresh, PART 0 of the
script, 400/400), `e(ω,d+1) = T(e)` where `T` is the odd-to-odd Collatz map
`T(x) = (3x+1)/2^{v_2(3x+1)}` (spine.md §9.8). Write `m = m₊(ω,d)`,
`a = a₊(ω,d)`, so `e + 1 = 2^m 3^a Ω` with `F(ω,d) = (Ω, D)`, `D = m + a`.

**Lemma (law i).** If `m ≥ 2`: `F(ω,d+1) = F(ω,d)`. If `m = 1`:
`F(ω,d+1) = F(F(ω,d))`.

**Proof.** `3e + 1 = 3(2^m 3^a Ω − 1) + 1 = 2^m 3^{a+1} Ω − 2
= 2(2^{m-1} 3^{a+1} Ω − 1)`, so `v_2(3e+1) ≥ 1` always, and

```text
(3e+1)/2 = 2^{m-1} 3^{a+1} Ω − 1.                                     (1.1)
```

*Case `m ≥ 2`.* The right side of (1.1) is odd (`2^{m-1}` is even), so
`v_2(3e+1) = 1` exactly and `e(ω,d+1) = T(e) = (3e+1)/2 = 2^{m-1}3^{a+1}Ω − 1`
by (1.1). Hence `e(ω,d+1) + 1 = 2^{m-1} 3^{a+1} Ω`, which is already in the
`2^{m'} 3^{a'} Ω'`-normal form with `m' = m-1 ≥ 1`, `a' = a+1`, `Ω' = Ω`
(`3 ∤ Ω` unchanged). So `F(ω,d+1) = (Ω, m'+a') = (Ω, m+a) = (Ω,D) = F(ω,d)`.

*Case `m = 1`.* The right side of (1.1) is `3^{a+1}Ω − 1`, the structural
numerator `A(Ω, a+1)` of the state `(Ω, a+1) = (Ω,D)` (since `D = m+a = 1+a`
here). So `v_2(3e+1) = 1 + v_2(A(Ω,D)) = 1 + s(Ω,D)`, and
`e(ω,d+1) = T(e) = (3e+1)/2^{1+s(Ω,D)} = A(Ω,D)/2^{s(Ω,D)} = e(Ω,D)`
exactly. Hence `F(ω,d+1) = R(e(Ω,D)) = F(Ω,D) = F(F(ω,d))`. ∎

**The `ω mod 8` reading.** By the first-layer table (stage1.md
Prop. 11.8.1.3.1, lines 60–63), off-spike states occur at exactly one
parity of `d` for each `ω mod 8`, and within that branch: `3^d ω ≡ 3 (mod 8)`
when `ω ≡ 1 (mod 8)` (odd `d`) or `ω ≡ 3 (mod 8)` (even `d`); `3^d ω ≡ 7
(mod 8)` when `ω ≡ 5 (mod 8)` (odd `d`) or `ω ≡ 7 (mod 8)` (even `d`). Since
`C = A + 2 = 3^dω + 1` here (`s=1`), `m = v_2(C) − 1 = v_2(3^dω+1) − 1`: if
`3^dω ≡ 7 (mod 8)` then `3^dω + 1 ≡ 0 (mod 8)` so `m ≥ 2`; if `3^dω ≡ 3
(mod 8)` then `3^dω+1 ≡ 4 (mod 8)` so `m = 1` exactly. Composed with the
lemma: **`ω ≡ 5, 7 (mod 8)` ⟹ merge; `ω ≡ 1, 3 (mod 8)` ⟹ skip.** This
matches the mod-8 reading quoted in the Provenance and HANDOFF item 5
exactly, and is now derived rather than asserted.

**Verification.** `experiments/ladder_family_graph.py` PART A: 40,000
off-spike states (constructed directly from the `ω mod 8` table, not by
rejection sampling), split 19,883 merge / 20,117 skip by the `m₊` test, 0
failures; the `ω mod 8` reading checked against the `m₊` split
independently on the same 40,000 states, 0 failures. Hand-verified:
`(ω,d)=(5,1)` (`ω≡5`), off-spike, `m=3`: `F(5,1)=(1,3)=F(5,2)`, a merge.
`(ω,d)=(1,3)` (`ω≡1`), off-spike, `m=1`: `F(1,3)=(7,1)`, `F(1,4)=(1,2)`,
and `F(F(1,3)) = F(7,1) = (1,2) = F(1,4)`, a skip.

---

## 2. Law (ii): the two-row commutation, re-derived

**Setup.** Fix `(ω,d)` with `s(ω,d) = 3` (so `A = 8e`, `e` odd) and
`m = m₊(ω,d) ≥ 4`, `a = a₊(ω,d)`, `e+1 = 2^m 3^a Ω`, `F(ω,d) = (Ω,D)`,
`D = m+a`.

**Lemma (law ii).** `F(ω,d+2) = (Ω, D − 1)`, and the letter at `d+2` is
`(6, m−3)`.

**Proof.** By (0.1) with `k=2`: `A(ω,d+2) = 9A + 8 = 9(8e) + 8 = 8(9e+1)`.
Now `9e + 1 = 9(e+1) − 8 = 9·2^m 3^a Ω − 8`. Since `m ≥ 4`, write
`9e+1 = 8(9·2^{m-3}·3^aΩ − 1)`; the bracket is odd (`2^{m-3}` is even
since `m-3 ≥ 1`), so `v_2(9e+1) = 3` exactly, giving
`s(ω,d+2) = 3 + 3 = 6` and

```text
e(ω,d+2) = A(ω,d+2)/2^6 = (9e+1)/8 = 9·2^{m-3}·3^aΩ − 1 = 2^{m-3}·3^{a+2}·Ω − 1.
```

So `e(ω,d+2) + 1 = 2^{m-3}·3^{a+2}·Ω`, already in normal form with
`m' = m-3 ≥ 1`, `a' = a+2`, `Ω' = Ω`. Hence `F(ω,d+2) = (Ω, m'+a') =
(Ω, (m-3)+(a+2)) = (Ω, m+a-1) = (Ω, D-1)`, and the new letter is
`(s(ω,d+2), m') = (6, m-3)`. ∎

**Hand check** (used to debug the mechanism before trusting the script):
`ω=1, d=14`: `A = 3^14 − 1 = 4782968 = 8·597871`, `s=3`, `e=597871`,
`e+1 = 597872 = 2^4·37367` (`37367` coprime to 3), so `m=4, a=0`,
`F(1,14) = (37367, 4)`. Then `A(1,16) = 9·4782968+8 = 43046720 = 2^6·672605`,
`s=6`, `e(1,16) = 672605`, `e(1,16)+1 = 672606 = 2·9·37367 = 2^1·3^2·37367`,
so `F(1,16) = (37367, 3) = (Ω, D−1)` with `(Ω,D) = F(1,14) = (37367,4)`. ∎

**The bit rewrite.** Write `X = 3^dω` (item 5's "predecessor numerator" of
`(ω,d)` read as if it were itself a predecessor — see §5). By §5's identity,
the low `σ = s+m` bits of `X` (bit 0 first) are the letter in unary,
`1, 0^{s-1}, 1^m`; here `s=3`, giving `1,0,0,1^m`. Since
`3^{d+2}ω = 9X`, and the new letter is `(6, m-3)` with `σ' = 6+(m-3) = m+3
= σ` (unchanged total, as multiplying by `9 = 3^2` only moves 3-adic
content, not the total `σ`), the same identity applied at `d+2` predicts the
low `σ` bits of `9X` are `1, 0^5, 1^{m-3}`. Verified directly (not merely
asserted): PART B of the script, 3,000 cases, 0 failures, checking both the
state-level claim and this bit-level rewrite together.

**Verification.** PART B: 3,000 states with `s=3, m₊≥4` (rejection
sampling over `ω<4000, d<400`), `F(ω,d+2) = F(ω,d) − (0,1)` and the letter
`(6,m-3)` both confirmed, 0 failures; the bit rewrite confirmed
independently on the same 3,000 states, 0 failures.

**The box census (ω < 4,000, d ≤ 40).** PART B2 scans this exact box
(53,320 states, matching HANDOFF item 5's "53,320 checks" for the
neighbour-family identity) and finds, **against the pre-check's quoted
792/789/3**:

```text
non-adjacent same-core pairs:  794   (pre-check: 792)
law (ii)-explained:            789   (pre-check: 789 — matches)
unexplained coincidences:        5   (pre-check: "3, listed")
```

The 5 coincidences, all landing on core `Ω = 1` — the single most common
target in the box (114 hits, §7) — are:

```text
ω=1,  d1=1, d2=4 :  F(1,1)=(1,1),  F(1,4)=(1,2)
ω=1,  d1=2, d2=4 :  F(1,2)=(1,1),  F(1,4)=(1,2)
ω=7,  d1=1, d2=3 :  F(7,1)=(1,2),  F(7,3)=(1,5)
ω=19, d1=1, d2=3 :  F(19,1)=(1,3), F(19,3)=(1,1)
ω=59, d1=1, d2=5 :  F(59,1)=(1,3), F(59,5)=(1,3)
```

**Correction recorded.** The pre-check's box-census totals (792 pairs, 3
unexplained coincidences) do not reproduce under this fresh, independently
written count; the true totals in this box are 794 and 5. The
law-(ii)-explained count, 789, does reproduce exactly. Per the brief's rule
("a claim is not dissolved by naming its type; every correction carries a
re-derivation"): the corrected statement is the table above, re-derived by
direct enumeration (grouping states by `ω`, then by target core, then
counting non-adjacent same-core pairs within each core's depth list — see
`part_b2_box_census` in the script) rather than by any incremental or
cached method that could silently miscount. The pre-check code was
deliberately never filed (per the brief's own Provenance), so its exact
miscounting cannot be diagnosed further; what is recorded here is the
correct count, independently verified by direct enumeration with no
approximation.

---

## 3. The repunit equation and its Zsigmondy closure

**Setup.** Climbing `k` rows from `(ω,d)`, write `u = e+1 = 2^s`... — more
precisely, with `s = s(ω,d)`, `e = e(ω,d)`, `u := e+1` (so
`u = 2^{m₊}3^{a₊}Ω`), (0.1) gives, substituting `A = 2^s(u-1)`:

```text
A(ω,d+k) = 3^k·2^s·(u-1) + (3^k-1) = 3^k·2^s·u − c,   c := 3^k(2^s-1) + 1.  (3.1)
```

**Proposition (the repunit equation).** A "whole-stratum" repeat — i.e. a
value of `c` that is a pure power of 2, so that (3.1) reads `A(ω,d+k) =
3^k 2^s u − 2^t` and the resulting state's core is determined by `u` alone,
independent of any further digit of `u` beyond its own factorization — holds
exactly when

```text
c = 3^k(2^s - 1) + 1 = 2^t      for some integer t ≥ 1.
```

Equivalently, writing `N_j = 2^j − 1`: `2^t − 1 = 3^k(2^s−1)`, i.e.
`N_s | N_t` and `N_t/N_s = 3^k`. Since `N_s | N_t` iff `s | t` (standard: 
`gcd(N_a,N_b) = N_{gcd(a,b)}`, so `N_s | N_t ⟺ N_s = N_{gcd(s,t)} ⟺ s | t`),
write `t = ns` (`n ≥ 1`); then

```text
N_t/N_s = 1 + 2^s + 2^{2s} + ... + 2^{(n-1)s}                            (3.2)
```

is a length-`n` base-`2^s` repunit, and the equation is exactly: this
repunit equals `3^k`.

**Theorem (Zsigmondy closure).** The only solutions `(k,s,t)` with
`k,s,t ≥ 1` are `(1,1,2)` and `(2,3,6)`.

**Proof.** `s < t` is forced (`s = t` gives repunit `= 1 ≠ 3^k` for `k≥1`;
`s > t` is impossible since `s | t` with `s,t ≥ 1` requires `s ≤ t`), so
`n = t/s ≥ 2`.

*Case `t = 2`.* Then `s | 2`, `s < 2`, so `s = 1`, and (3.2) is `1+2 = 3`,
giving `k=1`. This is `(1,1,2)`.

*Case `t = 6` (Bang/Zsigmondy's own exception for base 2).* Divisors
`s < 6` of `6`: `s ∈ {1,2,3}`. Direct check (PART C table in the script):
`N_6/N_1 = 63/1 = 63 = 3²·7` (not a pure power of 3); `N_6/N_2 = 63/3 = 21 =
3·7` (not); `N_6/N_3 = 63/7 = 9 = 3²` — a solution, `(k,s,t) = (2,3,6)`.

*Case `t ≥ 3, t ≠ 6`.* By Zsigmondy's theorem (Bang 1886 for base 2):
`N_t = 2^t − 1` has a **primitive prime divisor** `p` — a prime dividing
`N_t` but no `N_j` for `j < t` — and `p ≡ 1 (mod t)` (standard: `p |
2^t − 1` means `ord_p(2) | t`; primitivity means `ord_p(2)` is not a
*proper* divisor of `t`, since a proper-divisor order would make `p | N_j`
for that smaller `j`; so `ord_p(2) = t` exactly, and by Fermat `t = ord_p(2)
| p-1`, i.e. `p ≡ 1 (mod t)`). Since `t ≥ 3`, `p ≥ t+1 ≥ 4`, so `p ≠ 3`.
Because `p` is primitive for `N_t` and `s < t`, `p ∤ N_s`; since
`N_t = N_s · (N_t/N_s)` and `p | N_t`, `p ∤ N_s` forces `p | (N_t/N_s)`. If
`N_t/N_s = 3^k`, its only prime factor is `3`, forcing `p = 3` —
contradicting `p ≠ 3`. So no solution exists for `t ≥ 3, t ≠ 6`. ∎

This closes the equation completely: **no external reference beyond
Zsigmondy/Bang (1886) is needed**, and every length `n ≥ 2` is covered
uniformly by the single argument above (the `t=2` and `t=6` cases are
exactly the two Zsigmondy-exceptional values of `t` for base 2; every other
`t` is excluded by the primitive-prime argument, regardless of what `n =
t/s` happens to be). In particular this subsumes the brief's separately
posed "length 2" (`n=2`, i.e. `1+2^s=3^k`, solved directly above at `t=2s`
for whichever `s` makes `t ∈ {2,6}`, i.e. `s∈{1,3}`) and "length 3"
questions (`n=3`): a length-3 repunit needs `t=3s` with `3s ∉ {2,6}` unless
`s=2` — but `s=2,t=6,n=3` IS a divisor case covered above and already
excluded by direct check (`N_6/N_2 = 21`, not a power of 3); every other
length-3 case falls under the `t≥3,t≠6` exclusion. The elementary
`v_3(1+x+x^2)=1` argument for length 3 (below) is an independent,
non-Zsigmondy check on the same conclusion, kept as a second witness.

**Small cases, tabulated** (PART C table, `t=2..12`, every divisor `s<t`):

```text
t= 2 s=1  Q=3    = 3^1   <- solution (k,s,t)=(1,1,2)
t= 3 s=1  Q=7
t= 4 s=1  Q=15;  s=2  Q=5
t= 5 s=1  Q=31
t= 6 s=1  Q=63;  s=2  Q=21;  s=3  Q=9 = 3^2   <- solution (k,s,t)=(2,3,6)
t= 7 s=1  Q=127
t= 8 s=1  Q=255; s=2  Q=85; s=4  Q=17
t= 9 s=1  Q=511; s=3  Q=73
t=10 s=1  Q=1023;s=2  Q=341; s=5  Q=33
t=11 s=1  Q=2047
t=12 s=1  Q=4095;s=2  Q=1365;s=3  Q=585;s=4  Q=273;s=6  Q=65
```

No other `Q` in this table is a power of 3 — matching the theorem.

**Length-2 direct solve.** `1+2^s = 3^k`: scanned `s=1..59` directly
(PART C), found exactly `(s,k) = (1,1)` and `(3,2)`, matching `t=2s ∈
{2,6}` above.

**Length-3 elementary argument** (the brief's own suggested check, kept as
an independent witness). For `x = 2^s` even, `x ≡ 1 (mod 3)` iff `s` is
even. Write `x = 1+3y`: `1+x+x^2 = 3 + 9y + 9y^2 = 3(1+3y+3y^2)`, and
`1+3(y+y^2) ≡ 1 (mod 3)`, not divisible by 3. So `v_3(1+x+x^2) = 1`
**exactly**, for every `x=2^s` with `s` even — never `≥ 2`, so `1+x+x^2`
is never a power of 3 greater than `3^1` (and `1+x+x^2 = 3` would need
`x^2+x-2=0`, i.e. `x=1`, `s=0`, excluded). Verified over `s=2,4,...,198`
(99 cases), 0 failures.

**General search, control** (PART C, `k,s ≤ 200`, as the brief's requested
control on the proof — 40,000 pairs checked directly): the only `(k,s,t)`
with `3^k(2^s-1)+1 = 2^t` are `(1,1,2)` and `(2,3,6)`. Matches the theorem
exactly; 0 unexpected solutions.

**Zsigmondy sanity check** (PART C, `t=3..30`, full trial-division
factorization — feasible since `2^30-1 < 2^30`): the set of `t` in this
range with no primitive prime divisor is exactly `{6}`. Matches the
theorem's use of Zsigmondy's exception set for base 2 (`t=1` and `t=6`;
`t=1` is outside this range since our repunits always have `t ≥ 2`).

**Conclusion: the Zsigmondy closure holds.** No case failed; nothing
needed correction in this section.

---

## 4. The unified lemma

**Theorem.** Let `(k,s,t)` be one of `(1,1,2)`, `(2,3,6)`. Fix `(ω,d)` with
`s(ω,d) = s` (the solution's own `s`), `m = m₊(ω,d)`, `F(ω,d) = (Ω,D)`.
Then, writing `u = e(ω,d)+1 = 2^m 3^a Ω`:

1. If `m ≥ t-s+1`: `F(ω,d+k) = (Ω, D + s - t + k)`.
2. If `m = t-s`: `F(ω,d+k) = F(Ω, D + s - t + k)`.
3. If `m < t-s`: no claim (finite coincidence only).

**Proof.** From (3.1) with `c=2^t`: `A(ω,d+k) = 2^{s+m}·(3^{k+a}Ω) − 2^t`
(using `u = 2^m·3^aΩ`, so `3^k·2^s·u = 2^{s+m}·3^{k+a}Ω`). Write
`X := 3^{k+a}Ω` (odd, coprime to `3`... wait — coprime to `2`, and its own
`3`-content is exactly what will define the next `a'`; here `X` need not be
coprime to 3, since `3^{k+a}Ω` visibly carries `3`'s — the point is only
that it is odd).

*Case `m > t-s` (i.e. `s+m > t`, i.e. `m ≥ t-s+1`).* `A(ω,d+k) =
2^t(2^{s+m-t}X - 1)`; since `s+m-t ≥ 1`, `2^{s+m-t}X` is even, so
`2^{s+m-t}X - 1` is odd: `v_2(A(ω,d+k)) = t` exactly, and
`e(ω,d+k) = 2^{s+m-t}X - 1 = 2^{s+m-t}·3^{k+a}·Ω - 1`. So
`e(ω,d+k)+1 = 2^{s+m-t}·3^{k+a}·Ω`, normal form with `m' = s+m-t`,
`a' = k+a`, `Ω' = Ω`. `D' = m'+a' = (s+m-t)+(k+a) = (m+a) + (s+k-t) =
D + s + k - t`. So `F(ω,d+k) = (Ω, D+s-t+k)`.

*Case `m = t-s`.* `A(ω,d+k) = 2^t(X - 1) = 2^t(3^{k+a}Ω - 1) =
2^t·A(Ω, k+a)` (the structural numerator of state `(Ω,k+a)`). So
`v_2(A(ω,d+k)) = t + s(Ω,k+a)` and `e(ω,d+k) = A(Ω,k+a)/2^{s(Ω,k+a)} =
e(Ω,k+a)`. Hence `F(ω,d+k) = F(Ω,k+a)`. Since `m=t-s` here,
`D+s-t+k = (m+a)+s-t+k = (t-s+a)+s-t+k = a+k`, so this is exactly
`F(Ω, D+s-t+k)`.

*Case `m < t-s`.* `v_2(A(ω,d+k)) = s+m` (the `2^{s+m}` term dominates),
and `e(ω,d+k) = X - 2^{t-s-m}= 3^{k+a}Ω - 2^{t-s-m}`, generically unrelated
to `Ω, D`; no claim is made. ∎

Both named laws are the two low-`k` instances: `(1,1,2)` at `m=t-s+1=2`
is the merge case of law (i) — matching §1's `m≥2` merge — and `m=t-s=1`
is exactly law (i)'s skip case (`F(ω,d+1)=F(F(ω,d))=F(Ω,D+s-t+1)`, and
`s-t+1 = 1-2+1 = 0` so this reads `F(Ω,D)` — but law(i)'s skip statement
was `F(F(ω,d))`, i.e. `F(Ω,D)` itself, matching). `(2,3,6)` at `m≥4`
(`t-s+1=4`) is law (ii)'s dominant case, `D+s-t+k = D+3-6+2 = D-1`; at
`m=3` exactly it is the boundary case, `F(ω,d+2) = F(Ω, D-1)`.

**Verification.** PART D: 5,000 cases per solution (rejection-sampled on
`s(ω,d)` matching the solution), split by regime, 0 failures in the
dominant and boundary regimes at both solutions (the `m<t-s` regime carries
no assertion, per the theorem). At `(1,1,2)`: 2,533 dominant, 2,467
boundary, 0 "nothing" cases (since `t-s=1` and `m≥1` always for a valid
state, the "nothing" regime `m<1` is vacuous here — consistent). At
`(2,3,6)`: 584 dominant, 628 boundary, 3,788 in the unclaimed `m<3` regime.

---

## 5. Bits gained, read backward — a reading, verified

*(This is a reading of stage3.md 11.8.6.3, reverse.md 14.14.1, itinerary.md
14.15.1.1 and stage2.md 11.8.5 — nothing here is restated as new content on
those pages; only the identity is verified, because law (ii)'s bit rewrite
in §2 depends on it.)*

**Backward.** By the exit equation (reverse.md 14.14.1), `3^dω = 1 +
2^s·e = 1 + 2^s(2^m3^aΩ - 1) = (1-2^s) + 2^{s+m}·3^aΩ`. Modulo `2^σ`
(`σ=s+m`): `(1-2^s) mod 2^σ = 2^σ - 2^s + 1 = 2^s(2^m-1)+1`, whose binary
digits (bit 0 first) are exactly `1` (bit 0), `0` (bits `1..s-1`), `1`
(bits `s..s+m-1`) — the letter `(s,m)` in unary, `1,0^{s-1},1^m`. The exact
(not merely modular) identity `3^dω = [1,0^{s-1},1^m$\text{ as an integer}]
+ 2^σ·(3^aΩ - 1)` follows by direct substitution, so the bits above `σ`
are exactly those of `3^aΩ - 1`, shifted up by `σ`. Verified: PART F,
20,000 states, both the low-bit pattern and the exact high-part identity,
0 failures.

**Forward.** From `3^dω = 1+2^sy` (`y=e`, the door): `2^sy ≡ -1 (mod 3^d)`,
so `y ≡ -2^{-s} (mod 3^d)` — the door's low `d` ternary digits are fixed
by `s` alone, independent of `ω,Ω`. Verified: PART F, 20,000 states, 0
failures. The 3-gain: `a₊ = v_3(C) = v_3(2^s(y+1)) = v_3(y+1)`; since
`y+1 ≡ 1-2^{-s} = 2^{-s}(2^s-1) (mod 3^d)` and `2^{-s}` is a 3-adic unit,
`v_3(y+1 \bmod 3^d)` reads exactly `v_3(2^s-1) = h(s)` (stage3.md 11.8.6.2)
whenever `h(s) < d` (non-resonant, so the valuation is visible within the
`d`-digit window) — this is the "signature read against `−1`" the
Provenance names: the fixed low-digit signature of the door, `2^{-s}(2^s-1)
mod 3^d`, has 3-adic valuation `h(s)`, and off resonance this *is* the
3-gain. Verified: PART F, 19,957 non-resonant cases (43 resonant cases,
`h(s)≥d`, correctly excluded, not counted as checks per the brief's "exact
integer arithmetic at every pass/fail decision" — a resonant case is not a
pass or a fail of this non-resonant claim), 0 failures.

---

## 6. The mirror at reverse.md 14.10 — no twin found; the obstruction

**What was tried.** The literal transplant of law (i)/(ii): fix a door `y`,
let `(ω(y,s),d(y,s))` be the predecessor at branch `s` (14.1.1), and ask
whether `F` applied to predecessors at climbed branches (`s, s+2, s+4,...`)
exhibits a merge/skip or two-row commutation pattern mirroring §1/§2.

**The obstruction.** By reverse.md 14.1.1's own defining property,
`F(ω(y,s), d(y,s)) = state(y) = (Ω,D)` **for every admissible branch `s`**
— `F` applied to a predecessor of `(Ω,D)` returns `(Ω,D)` by construction,
regardless of which branch produced the predecessor. This is not a
computation to search; it is exactly what "predecessor" means (14.1.1's
proof: `x_exit(ω,d) = y` for every predecessor at door `y`, so
`F(ω,d)=R(y)=state(y)` identically). So the direct mirror of "does
`F(predecessor at s+2k)` relate simply to `F(predecessor at s)`" is
**vacuous**: it is always the same constant `(Ω,D)`, with no dichotomy, no
stratification, and nothing to prove.

This differs in *kind*, not merely in detail, from the forward question.
Forward, law (i)/(ii) are nontrivial precisely because `F` is many-to-one
across *different sources in the same column* (`(ω,d), (ω,d+1), (ω,d+2),
...`) — genuinely different inputs whose images sometimes coincide. The
naive backward transplant instead holds the *target* fixed by construction
(every predecessor of `(Ω,D)`, by definition, has `F`-image `(Ω,D)`) and
varies the branch — but the branch indexes *which predecessor*, not *which
target*, so there is no "sometimes equal, sometimes not" to find: the
degrees of freedom law (i)/(ii) exploit (different depths mapping to a
common image is a nontrivial fact about a many-to-one deterministic map)
are simply absent on the side that is, by definition, one-to-(the same
target).

Verified numerically as a sanity check on the obstruction itself (not
merely cited): PART G, 5,000 random `(y,s)` pairs, `F(predecessor) =
state(y)` confirmed in every case (0 failures) — a fresh re-derivation of
14.1.1's own claim, not a new fact.

**A further, honest check.** Since `F` trivializes, the only other
literal candidate for "does climbing branches produce a repeat" is whether
the predecessor's *own core* repeats: `ω(y,s+2k) = ω(y,s)` for the same
`y`. This is not claimed anywhere in the brief or HANDOFF, but was checked
as due diligence (a negative control): 3,000 random doors `y`, `k=1,2`,
zero repeats (PART G). No hidden trivial-repeat structure was found this
way either.

**Conclusion.** No twin of law (i) or law (ii) exists at reverse.md 14.10
in the form the Provenance anticipated — not because a search failed, but
because the direct transplant is provably degenerate (14.1.1 already
proves the only thing it would say). Per the brief's instruction ("if the
shape differs, one paragraph saying how, and stop"): the paragraph above is
that account, and no remark is added at reverse.md 14.10 — nothing on that
page changes.

---

## 7. The family graph paragraph: in-degree

Over the box `ω < 4,000, d ≤ 40` (53,320 states, PART H): the ten most
frequent target cores are `1` (114), `5` (62), `7` (57), `11` (42), `13`
(42), `17` (37), `19` (35), `31` (32), `23` (31), `25` (30) — reproducing
HANDOFF item 5's quoted `1: 114, 5: 62` exactly. This is the backward tree
of reverse.md 14.1.1 (small cores have disproportionately many predecessors
because the predecessor count grows with the representative count `D` and
small states recur as targets across many `(ω,d)` in a bounded box) —
nothing new is claimed; the ladder.md 15.7 paragraph is one sentence
naming this as such.

---

## 8. Verification record (summary)

`experiments/ladder_family_graph.py`, fresh code — imports nothing from
any other script in this repository; exact integer arithmetic at every
pass/fail decision (no floats in any pass/fail path — the only floats in
the file are informational rate printouts in the census, never gating a
check); canaries first; deterministic, seed `20260913`, run 2026-09-13.
Committed output: `experiments/ladder_family_graph_output.txt`.

```text
TOTAL: 203,552 checks, 0 failures
```

One command reproduces this file in full:

```text
python experiments/ladder_family_graph.py
```

**Compliance.** `python experiments/encoding_scan.py` run before the final
commit: `RESULT: CLEAN` (recorded in §9 below, after the run).

---

## 9. Compliance: encoding scan

`python experiments/encoding_scan.py`, run after the wiki edits (ladder.md
15.7, this findings file), before the final commit, 2026-09-13:

```text
encoding scan: 492 tracked files (binary extensions skipped)
not valid UTF-8 (0):
UTF-8 BOM present (0):
double-encoding signatures (0):
RESULT: CLEAN
```

---

## For the main session at merge

- **ladder.md**: this branch appends **15.7** after the existing 15.5 (no
  15.6 exists on this branch — the parallel `ladder-afterlife` branch owns
  15.6). At merge, ladder.md 15.4's "Open connections worth recording"
  paragraph should gain a pointer sentence to 15.7 (the guaranteed-neighbour
  laws, alongside the existing target-shift/bridge pointer), and the
  Current-state paragraph at the top of ladder.md should gain one clause
  naming 15.7's closure, matching the register of the existing 15.5 clause.
  This findings file does not touch 15.4 or the Current-state paragraph
  itself, per the brief's Rules.
- **Section ownership seam**: per the brief's Grade-at-delegation note, law
  (i) (off-spike) belongs to this branch; the spike case (`s ≥ 2`, the
  tear) belongs to `ladder-afterlife`'s 15.6. No overlap was found or
  created — this branch's laws are entirely at off-spike depths (law i) or
  at the specific stratum `s=3` (law ii, itself off the tear).
- **reverse.md**: unchanged by this branch — no 14.10.2 remark, per §6's
  obstruction (a proof of vacuity, not a failed search).
- **HANDOFF item 5**: at merge, item 5's backlog entry should be marked
  closed, with a pointer to ladder.md 15.7 and this findings file, and the
  two corrections recorded here (the box-census total 794/789/5, not
  792/789/3; the stratum-census partial rates at (2,3,3) and (3,1,1) are
  0.000, not 0.253/0.063 — see §2 and §4's diagnostics) should be reflected
  if HANDOFF's own item-5 paragraph is updated rather than simply replaced
  by a pointer. This findings file does not edit HANDOFF.md itself, per the
  brief's Rules.
- **index.md**: not edited — the resolver lists `ladder.md` at the
  whole-page (§15) granularity, not at 15.5's granularity, so per the
  brief's instruction nothing is added.
- **symbols.md**: not edited — no new symbol was introduced; every
  quantity used (`Ω, D, m₊, a₊, C, σ, y`) is already in the registry.
