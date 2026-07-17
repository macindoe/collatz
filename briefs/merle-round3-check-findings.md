# Findings: merle-round3-check (2026-07-18)

Answers `briefs/merle-round3-check-brief.md` items 1-6: Eric Merle's
transport recurrence (his candidate L-A1) verified and adjudicated for
antecedence against our record; the collapse-payoff accounting; his two
corrections; and our key turned on his L4 (the AEH cross-verification
and class spectrum).

Code: `experiments/merle_round3_check.py` (items 1-4; 29,211 exact
checks, 0 failures, ~3 s) and `experiments/merle_aeh_key_check.py`
(item 5; 6,013 checks, 0 failures, ~1 s). Both fresh per AGENTS.md —
no imports from any committed script; every pass/fail decision exact
integer/`Fraction`; floats only in labeled display and measurement
columns (log2 margins, frequencies, the transfer-matrix spectrum, drift).
Seed `20260718` throughout. Convention pins (the `ROUND_HALF_EVEN`
partial-sum rounding of Construction 12.8.6.2, `K = (3^n).bit_length()`,
crash block last) were read from the committed scripts' text to align
conventions, per the pincer session's precedent; no code imported or
copied. Dates: 2026-07-18.

## Summary for the reply (verdicts, liftable)

1. **The transport recurrence is exact and correctly stated.** Under our
   12.6.1 conventions, with `σ_r = s_r + m_{r+1 mod p}`, his identity
   `R_{r+1} = (3^{m_r} R_r + (2^{s_r} − 1)·q) / 2^{σ_r}` holds verbatim
   — no index correction needed — for **every** profile `(m_t, s_t)_{t<p}`
   with entries `≥ 1`, no closure assumption, `q = 2^K − 3^n` of either
   sign. Verified exactly on 600 random profiles (p ≤ 12, including 32
   with `q < 0`), the trivial-cycle profiles p = 1..7, and the recorded
   instances (p = 7 `n = 94`, p = 22 `n = 25217` and `n = 31202`). All
   corollaries confirmed: exact divisibility by `2^{σ_r}`; unit
   transport `2^{σ_r} R_{r+1} ≡ 3^{m_r} R_r (mod q)` with `gcd(q,6) = 1`
   (`q` odd as even − odd; `q ≡ (−1)^K (mod 3)`); `gcd(q, R_r)`
   rotation-invariant; `q | R_0` iff `q | R_r` for all `r`.

2. **Antecedence: not in the cycles frame; equivalent to Lemma
   14.15.9.2 under an explicit dictionary in the mirror frame.**
   His reading of `cycles.md` is correct — the record tests the `p`
   divisibility conditions severally and states neither the recurrence
   nor the collapse. In `reverse.md`, Lemma 14.15.9.2(1)-(2) (merged
   2026-07-17, one day before his letter of 2026-07-18) **is** the same
   mathematical content: the recurrence is the rotated-fixed-point
   affine orbit equation multiplied through by the common denominator,
   the gcd corollary is the shared-reduced-denominator clause, and his
   auditor's ghost identity is Corollary 14.15.9.4(1). The dictionary
   is a one-line telescoping identity, `N_r + q = 2^{m_r} R_r`, stated
   and proved below (item 2), verified exactly on the 14.15.9 grid
   (20 probe words + 3 integer words, all rotations) and 600 random
   profiles. One systematic difference: his modulus is the unreduced
   `q = 2^K − 3^n`; 14.15.9's `q` is the reduced denominator. The two
   statements are interderivable in one line but numerically different
   exactly on profiles where `gcd(R_r, 2^K − 3^n) > 1` — witnesses
   below, including the recorded p = 7 staircase seed itself
   (`gcd(q, R_r) = 7`). Independent simultaneous discovery; the dates
   are in item 2(c); credit language is the author's call.

3. **What the collapse buys: divisibility yes, size no, and the
   practical speedup is small.** Divisibility tests collapse `p`-to-1
   (and further under rotation dedup: the period-2 record's eleven
   quadruples are six rotation classes). The size tests `q ≤ R_r` do
   **not** collapse — exhibited: the p = 22 `n = 25217` pre-correction
   profile passes size at 13 rotations and fails at 9. In the recorded
   searches the binding per-rotation work is computing `R_r` (needed
   for size regardless); divisibility was only ever run on
   size-passers, so the collapse saves on the order of a few hundred
   bigint mod operations across the entire recorded history. His Lean
   point is his side's; noted without comment.

4. **His two corrections.** (a) Ghost alignment: confirmed as an
   algebraic identity for every profile (it is 14.15.9.4(1) under the
   dictionary), hence carries no cycle-selective information — his
   auditor's conclusion is exactly right. (b) KS dedup: on **our**
   construction, `cd = 1` and `cd = 2` do *not* give identical `u` —
   exact equality at no rotation — but the values are near-identical
   (differences below `2^{−1000}`) at the ~80% of rotations away from
   the crash block and materially different (O(0.1)) at the 3-5
   rotations at/near it. His deduplication rule describes his
   construction/statistic, not ours, though pooling both crash depths
   would still heavily duplicate a `u`-sample. His corrected values
   (`D = 0.1525`, ~34 independent instances) are recorded as the
   ledger-facing numbers on his key, at the weight he assigns.

5. **L4, our key turned: confirmed at measured grade, with one
   normalization flag.** Canaries reproduce; both exact skeleton values
   are theorems of our record and reproduce in our fresh run
   (`(1 mod 8, d odd) → d_next = 1` in 19,036/19,036 and 13,987/13,987
   at the two cuts; `(5 mod 8, d odd) → P(even) = 0.6663 ± 0.0034` and
   `0.6693 ± 0.0040` vs exact 2/3); `P(s = j)` tracks `2^{−j}` with all
   `|z| ≤ 2` and **no** `s = 1` excess at our start scale (2^55) —
   consistent with his attribution of his excess to small starting
   values. Class transfer matrix: `|λ₂| = 0.028` (cut 2^20) and
   `0.036` (cut 2^30) — both inside his `≤ 0.06`, spectral gap ≥ 0.96,
   his measurement confirmed (float measurement, labeled). Drift: his
   `−0.33/−0.36` artifact is reproduced *as a family* — cut-conditioned
   estimators land at `−0.35` to `−0.41` (survivor-averaged slope, per
   F-step) and `−0.387/−0.376` (censored, per odd step) — and his
   survivorship attribution is **confirmed**: under our fixed-horizon
   unweighted protocol the drift returns to theory at both
   normalizations (per odd step `−0.4166 ± 0.0037` vs `log₂3 − 2 =
   −0.4150`; per F-step `−0.8367 ± 0.0060` vs `2(log₂3 − 2) =
   −0.8301`, altitude-control population). The flag: his stated
   theoretical `−0.415` is the per-odd-step (classical T-step) value;
   the per-F-step (per-block) value under `π_k` is `2(log₂3 − 2) =
   −0.830`, since `E[m] = E[s] = 2`. Whichever unit his "per step" is,
   one member of his (measured, theoretical) pair needs renormalizing;
   the artifact and its cause are protocol-level either way. His scope
   sentence (generic face only) is exactly our own framing (aeh.md
   13.3.3, README stopping rules) — agreement recorded.

## Item 1: the transport recurrence, verified

**Convention alignment.** 12.6.1 reads, for rotation `r` (indices in
rotation order starting at `r`): `R_r = Σ_{t=0}^{p−1} 3^{M_t} 2^{S_t}
(2^{s_t} − 1)`, `M_t = Σ_{j>t} m_j`, `S_t = Σ_{j<t} σ_j`, with
`σ_t = s_t + m_{t+1}` (the step data of a cycle; for an arbitrary
profile this is the *definition* of `σ_t`), `n = Σ m_t`,
`K = Σ s_t + n = Σ σ_t`, `q = 2^K − 3^n`. Under these conventions his
recurrence aligns with **no index shift or rotation**:

```text
2^{σ_r} · R_{r+1} = 3^{m_r} · R_r + (2^{s_r} − 1) · q ,      σ_r = s_r + m_{r+1 mod p},
```

an exact integer identity (the division by `2^{σ_r}` is exact), for
every profile `(m_t, s_t)_{t<p}` with all entries `≥ 1` — closure never
used, `q` of either sign. Derivation (three lines, recorded for the
reply): shifting the rotation start from `r` to `r+1` sends term `t` of
`R_r` (for `t ≥ 1`) to term `t−1` of `R_{r+1}` with `M`-exponent larger
by `m_r` and `S`-exponent smaller by `σ_r`; so `3^{m_r} R_r −
2^{σ_r} R_{r+1}` telescopes to the two boundary terms, `3^{m_r} ·
3^{n−m_r}(2^{s_r}−1)` (the old `t = 0`) minus `2^{K−σ_r}·2^{σ_r}
(2^{s_r}−1)` (the new `t = p−1`), i.e. `−(2^K − 3^n)(2^{s_r}−1)`.

**Checked** (`experiments/merle_round3_check.py`, `check_profile`):
the recurrence, exact divisibility, unit transport mod `q`,
`gcd(q, 6) = 1` (with the two one-line reasons asserted separately:
`q` odd; `q ≡ (−1)^K (mod 3)`), `gcd(q, R_r)` rotation-invariance, and
the all-or-nothing divisibility pattern, on:

* 600 random profiles, `p ∈ 1..12`, entries uniform in `1..8` (500
  profiles) and `1..20` (100 profiles), seed `20260718`, **no closure
  assumption**; 32 of them have `q < 0` (the identity is sign-agnostic
  algebra);
* the trivial-cycle profiles `m_t = s_t = 1`, `p = 1..7` (exercising
  the full-divisibility branch: `R_r = q = 4^p − 3^p` per 12.6.1's
  sanity identity);
* the recorded 12.8.6.4 instances: p = 7 `n = 94` (`m = (4,7,9,15,23,
  35,1)`, `s = (1,1,1,1,1,1,49)`, `γ = 6.744`), p = 22 `n = 25217`
  (`γ = 11.186`) and `n = 31202` (`γ = 14.746`), the two p = 22
  configurations exactly as printed in
  `briefs/merle-pincer-check-findings.md`; all rotations pass size,
  none passes divisibility, `γ` values match the record.

29,211 exact checks total across items 1-4, 0 failures. His "verified
on 200 random ones, 0 failures" is independently reproduced at 3x his
scale plus the recorded instances.

## Item 2: antecedence adjudication

### (a) The cycles frame: not there

Confirmed by reading, with the record's own words. Proposition 12.6.1
concludes severally: "In particular `q > 0` divides all `p` numbers
`R_r`, and `q ≤ min_r R_r`" — `p` conditions, no relation among them
stated. Theorem 12.7.1: "none passed the triple divisibility
`q | R_0, R_1, R_2`" — exactly the p = 3 enumeration his letter quotes.
Remark 12.8.3: "All fail the divisibility conditions `q | R_r`";
Proposition 12.8.6.4: "checked against the full divisibility system
`q | R_r`: none passes". The searches (12.5.4, 12.7.1, 12.8.6.3-4)
evaluate and test every rotation. Nowhere in `cycles.md` is the
recurrence, the unit transport, or the collapse stated.

**What 12.6.1's proof contains implicitly.** For a *closed cycle* the
recurrence is one multiplication away from displayed material: the step
identity `2^{σ_r} 3^{a_r} ω_{r+1} = 3^{d_r} ω_r + (2^{s_r} − 1)`
(12.1.1, quoted in 12.6.1's proof) times `q`, using `R_r = ω_r
3^{a_{r−1}} q` (12.6.1's conclusion) and `d_r − a_{r−1} = m_r`, is
exactly the recurrence. The honest reading: the closed-cycle instance
is implicit; the *profile-level* identity (no closure), its mod-`q`
collapse, and any use of either are absent. His "if I am not missing a
place where you have already collapsed them" — he is not, in this
frame.

### (b) The mirror frame: equivalent to Lemma 14.15.9.2 under an explicit dictionary

**The dictionary.** Map the cycle profile `(m_t, s_t)_{t<p}` to the
periodic word with letters `(m_i, r_i) := (m_i, s_i)`, same cyclic
order. This is the forward-block reading of the mirror letters: a block
with entry `x` (`v₂(x+1) = m`, unit `u = (x+1)/2^m`) exits at
`x' = (3^m u − 1)/2^s`, which is verbatim `G`'s defining formula with
`r = s` — so block entry values propagate by the per-letter affine maps
`g_i(u) = α_i u + β_i`, `α_i = 3^{m_i}/2^{m_i+s_i}`, `β_i = (3^{m_i} −
2^{m_i})/2^{m_i+s_i}` (14.14.4.1). Under this map `S_P = Σ(m_i+r_i) =
K` and `M_P = Σ m_i = n`, so 14.15.9.1's denominator `D = 2^{S_P} −
3^{M_P}` **equals** 12.6.1's `q = 2^K − 3^n` (unreduced), and the
rotated composed fixed point is `y^*_r = N_r/q` with 14.15.9.1's
numerator `N_r` computed on the rotation starting at `r`.

**The seam identity** (the displayed dictionary, new to both frames as
a stated identity): for every profile and every rotation `r`,

```text
N_r + q = 2^{m_r} · R_r .
```

*Proof.* In rotated labels, `S_t := Σ_{j<t} σ_j = Σ_{j<t}(m_j+s_j) +
m_t − m_0`, so `2^{m_0} R_r = Σ_t 3^{M_t} 2^{S'_t} · 2^{m_t}(2^{s_t}−1)`
with `S'_t := Σ_{j<t}(m_j+s_j)`. Subtracting `N_r` term by term leaves
`Σ_t 3^{M_t} 2^{S'_t}(2^{m_t+s_t} − 3^{m_t}) = Σ_t (u_{t+1} − u_t)`
with `u_t := 3^{Σ_{j≥t} m_j} 2^{S'_t}`, which telescopes to
`u_p − u_0 = 2^{S_P} − 3^{M_P} = q`. ∎

**Consequences, each verified exactly** (grid: the 14.15.9 Setup's 7
single-letter non-integral + 13 multi-letter probe words + the 3
integer words `1`, `−5`, `−17` (word `((4,1),(3,3))`), all rotations,
plus the 600 random profiles):

1. `y^*_r + 1 = 2^{m_r} R_r / q`: 12.6.1's rotation numerator **is**
   the numerator of the rotated fixed point's 2-adic unit — 14.15.9.4's
   `q^*_r = (y^*_r+1)/2^{m_r} = R_r/q`. (For a closed integer cycle
   this is 12.6.1 itself: `y^*_r = 2^{m_r}·3^{a_{r−1}}ω_r − 1 =
   x_entry,r`.)
2. **The recurrence = 14.15.9.2(1).** Substituting `y^*_r = (2^{m_r}R_r
   − q)/q` into the affine orbit equation `y^*_{r+1} = α_r y^*_r + β_r`
   and clearing denominators gives exactly `2^{σ_r} R_{r+1} =
   3^{m_r} R_r + (2^{s_r}−1) q`; dividing the recurrence by `q`
   recovers the orbit equation. Equivalent, both directions, one line
   each.
3. **The gcd corollary = 14.15.9.2(2).** `gcd(N_r, q) = gcd(2^{m_r}R_r
   − q, q) = gcd(R_r, q)` (`q` odd), so the reduced denominator of
   `y^*_r` is `|q|/gcd(q, R_r)`: "one shared reduced denominator" and
   "`gcd(q, R_r)` rotation-invariant" are the same statement in two
   frames. Verified: the shared reduced denominators match the known
   fixed-point denominators on all 23 grid words (5, 13, 7, 23, 11, 5,
   37; 23, 5, 37, 5, 37, 101, 47, 7, 101, 47, 175, 229, 431; 1, 1, 1).
4. **The collapse corollary = integrality is rotation-invariant.**
   `q | R_r` for all `r` iff for one `r` iff the reduced denominator is
   1 iff `y^* ∈ Z` — and 14.15.9.4(3) identifies that case as exactly
   the integer-cycle case (the three integer words, including the
   classical negative cycle `−17` with `q = 2^{11} − 3^7 = −139` and
   `gcd(139, R_r) = 139` at every rotation, confirm the branch).

**The one systematic difference: unreduced vs reduced modulus.** His
`q = 2^K − 3^n` is 14.15.9.1's `D`; 14.15.9's `q` is the reduced
denominator `|D|/gcd(D, R_r)`. They differ exactly when the fraction
reduces. Witnesses: the profile `m = (1,1)`, `s = (2,2)` — under the
dictionary the word `((1,2),(1,2))`, the multi-letter probe's own
"constant pair" — has unreduced `q = 55`, `gcd(q, R_r) = 11`, reduced
denominator 5; the **recorded p = 7 staircase seed** (`n = 94`) itself
has `gcd(q, R_r) = 7` shared across all seven rotations (reduced
denominator `q/7`); 5 further witnesses among the 600 random profiles
are printed by the script. His statements survive the difference —
unit transport mod the unreduced `q` implies it mod every divisor —
but the two `q`'s are not the same number, and 14.15.9's height laws
are phrased in the reduced one.

**Verdict** (in the brief's first form): **equivalent to Lemma
14.15.9.2 under an explicit dictionary** — the transport recurrence is
14.15.9.2(1) multiplied through by the (unreduced) denominator, via the
seam identity `N_r + q = 2^{m_r} R_r`; the gcd/collapse corollaries are
14.15.9.2(2) (+ 14.15.9.4(3) for the integer-cycle identification) in
integer form. Neither statement strictly contains the other as
*stated*: his is native to 12.6.1's integer numerators (the
Lean-friendly form) and carries the unreduced modulus; 14.15.9.2 is
native to the rotated fixed points and carries the reduced one; the
seam identity that identifies them is stated in neither frame and is
supplied here. Scope is identical on both sides (all profiles/periods
with entries `≥ 1`, both signs, no closure).

### (c) His auditor's identity vs Corollary 14.15.9.4(1)

Reconstruction: in his p = 7 local-global context, `w` is the local
(2-adic) solution of rotation `r`'s equation, `w = R_r · q^{−1}` (`q`
odd, hence a 2-adic unit), and his identity `v₂(3^m w − 1) = s` reads
`v₂(3^{m_r} R_r − q) = s_r`. This holds for **every** profile: by the
recurrence, `3^{m_r} R_r − q = 2^{s_r}(2^{m_{r+1}} R_{r+1} − q)`, and
the bracket is odd (`m_{r+1} ≥ 1`, `q` odd). Verified on every profile
and rotation the script touches (600 random + grid + recorded
instances; part of the 29,211). Under the dictionary `w = q^*_r` and
the statement **is** Corollary 14.15.9.4(1), `v₂(3^{m_i} q^*_i − 1) =
r_i` — same statement, two frames, his auditor's proof algebraic, ours
adelic/cylinder-theoretic.

**Timing, stated flatly.** `reverse.md` 14.15.9 (Lemmas 14.15.9.1-2,
Theorem 14.15.9.3, Corollary 14.15.9.4) was committed 2026-07-17,
15:48-15:52 UTC, and merged 2026-07-17 15:55 UTC (commit `6b494b3`).
Merle's letter is dated 2026-07-18. His letter shows he read our
public record (he quotes `cycles.md`'s p = 3 enumeration, and he cites
`reverse.md` 14.15.3-6 by number); it nowhere mentions 14.15.9, and
his frame and proofs are different (integer recurrence on 12.6.1's
numerators, auditor-algebraic; ours fixed-point/adelic). Whether he
saw the 14.15.9 merge before writing is not knowable from here and is
not asserted either way. The mathematical relationship is as stated
above; the dates are as stated; credit language is the author's call.

## Item 3: what the collapse buys in our pipeline

**Divisibility (collapses).** The period-2 record (12.5.4): the fresh
re-search (`item3_period2_search`, full enumeration `n ≤ 200`,
`K = ⌈n log₂ 3⌉` per the ceiling lemma; the recorded survivors all have
`n ≤ 29`) reproduces exactly the **11** size-passing quadruples, and
the divisibility pattern `q | R_0 ⟺ q | R_1` holds at each (the
collapse, instance-level; only the degenerate `(1,1,1,1)` passes).
Severally that was 22 divisibility conditions; the collapse makes it
11; and the 11 quadruples comprise **6 rotation classes** — 1 symmetric
(`(1,1,1,1)`) and 5 rotation pairs (`(1,2,1,1)~(2,1,1,1)`;
`(1,4,1,2)~(4,1,2,1)`; `(1,4,2,1)~(4,1,1,2)`; `(2,3,1,2)~(3,2,2,1)`;
`(2,3,2,1)~(3,2,1,2)`) — so the fully deduplicated count is **6**
distinct divisibility conditions. Period 3 (12.7.1): 51 size-passers ×
3 conditions = 153 severally → 51 under the collapse. The 12.8.6.4
instance record: one condition per instance instead of `p` (Σp ≈ 300
over the range `p ∈ {2..23}` plus the second p = 22 row).

**Size (does not collapse).** `R_r` varies across rotations, and the
binding test of every survivor search is `q ≤ R_r`, which must be
evaluated per rotation regardless. Exhibit (recorded instance,
recomputed fresh): the p = 22 `n = 25217`, `cd = 1` **base**
construction (pre-correction) passes size at rotations 0-11 and 21
(13 of 22) and fails at rotations 12-20 (9 of 22), worst rotation 20 at
−7.86 bits — one instance, size passing at one rotation and failing at
another, ending the question. (The corrected passer's `R_r` span
39,957-54,699 bits across rotations: `q ≤ min_r R_r` is a genuinely
`p`-fold system.)

**Net practical effect, counted (no benchmark campaign).** In every
recorded search the per-rotation cost is dominated by computing the
`R_r` themselves (required for size); divisibility is one bigint `mod`
per rotation applied only to size-passers. Collapsed accounting across
the entire recorded history: ~11 mod-ops saved at p = 2, ~102 at p = 3,
~300 over the staircase instance record — order hundreds of bigint
operations total. The collapse's value in our pipeline is conceptual
(one condition, one Lean obligation, the "the `p` conditions are one
condition" statement) rather than computational. His Lean-obligation
point is his side's to develop; noted without comment. The stopping
rules stand: no divisibility-based exclusion attempt was made or is
proposed (README; brief's compliance paragraph).

## Item 4: his two corrections

**(a) The ghost alignment carries no information — confirmed.** The
identity `v₂(3^{m_r} R_r − q) = s_r` holds for every profile (item
2(c)), cycle-admissible or not; a statement true of every profile
cannot distinguish any subclass, so it is not a test. This is his
auditor's conclusion, reached here as 14.15.9.4(1) under the
dictionary; "the real content is the uniform-distance framing" matches
our own use (the pincer findings' distance profiles).

**(b) The KS dedup reason, checked on our instances.** His stated
reason for 62 → ~34: "`c = 1` and `c = 2` give the same `u`". On our
construction (12.8.6.2 fresh, both crash depths, at the four recorded
calibration instances — p = 21 `n = 15601`, p = 23 `n = 47468`, p = 22
`n = 25217` and `n = 31202`; the cd = 1 rows and the recorded
Merle-match margins reproduce exactly, and the cd = 2 rows match where
recorded):

* the `(m, s)` profiles are **not** identical across crash depths (the
  crash block is 1 vs 2 and one-two adjacent climb blocks shift by one
  unit);
* the exact `u_r = min(R_r mod q, q − R_r mod q)/q` values coincide at
  **no** rotation (`Fraction` comparison);
* but at the rotations away from the crash block (18/21, 20/23, 18/22,
  17/22) the difference is below `2^{−1000}` — the two constructions'
  `R_r` differ by ~`2^{19000}` against `q ~ 2^{24700}` at p = 21, so
  the residues shift by a relatively infinitesimal amount — while at
  the 3-5 rotations at/nearest the crash the difference is O(0.1).

So: exact coincidence no; statistical near-duplication at ~80% of
rotations yes. His deduplication rule describes his construction (or a
per-instance statistic insensitive to the crash-adjacent rotations),
not ours exactly; had we pooled both crash depths into a `u`-sample,
most pairs would indeed be effective duplicates. Recorded at his
stated weight: the ledger-facing numbers on his distance-statistic key
are his corrected `D = 0.1525` with ~34 independent instances (his
data, not reproducible from our side; not attempted, per the brief).

## Item 5: our key on L4 (AEH cross-verification)

`experiments/merle_aeh_key_check.py`; 3,000 orbits, odd uniform starts
in `[2^55, 2^56)`, seed `20260718`, whole descents recorded; cuts
`2^20` and `2^30`; 6,013 checks, 0 failures, ~1 s. All dynamics exact
integers; spectrum and drift are float **measurements**, labeled.

**(a) Canaries.** `F(1,1) = (1,1)` (A = 2, s = 1, exit 1) and the block
of 7 exits at 13 (`R(7) = (1,3)`; `(3³·1 − 1)/2 = 13`): both confirmed
by direct computation from spine.md 9.1.1. His two canaries are the
right ones.

**(b) The exact skeleton values are theorems of our record.** The
paper's `sec:aeh` sentence (collatz-reduced-v2.tex, the class-skeleton
sentence): "from class `(ω≡1 (8), d odd)` the next depth is exactly 1
(since `m_+ = 1`, `a_+ = 0` there), and from `(ω ≡ 5 (8), d odd)`,
`P(d_next even) = 2/3` exactly." Owning laws: Proposition 11.8.1.3.1
(stage1.md — the mod-8 classification giving `s` per class), spine.md
9.3 (odd `s` ⟹ `a_+ = 0`), aeh.md 13.2 (the exact product law `π_k`
and both class-chain entries). The `(1, odd)` fact is per-transition
exact (every transition, not an average); the `(5, odd)` 2/3 is a
`π_k` statement (Haar over the lifting shells). Cited, not re-proved.

**(c) His protocol at his scale.** Transitions counted while the source
exit exceeds the cut: 135,016 (cut 2^20) / 99,185 (cut 2^30) over the
3,000 orbits.

* `(1 mod 8, d odd) → d_next = 1`: **19,036 of 19,036** (2^20) and
  **13,987 of 13,987** (2^30). His 15,515 of 15,515: same law, his
  sample size between our two cuts' samples.
* `(5 mod 8, d odd) → P(d_next even)`: `0.6663 ± 0.0034` (2^20),
  `0.6693 ± 0.0040` (2^30), pooled binomial SEs (per-orbit-mean SEs
  0.0041/0.0048), vs exact 2/3. His `0.6626 ± 0.0074`: consistent.
* `P(s = j)` vs `2^{−j}`, `j = 1..8`: all `|z| ≤ 2.0` at both cuts. No
  `s = 1` excess at our start scale — consistent with his attribution
  of his small excess to small starting values (our starts are 2^55;
  the calibration record's bottom-regime account predicts exactly
  this).
* **Class transfer matrix** (8 classes = `ω mod 8 ∈ {1,3,5,7}` ×
  `d` parity), built from observed class-to-class transitions,
  spectrum by numpy (measurement): `|λ₂| = 0.0277` (cut 2^20, gap
  0.972) and `|λ₂| = 0.0355` (cut 2^30, gap 0.964). **His `|λ₂| ≤
  0.06` at both cuts is confirmed**; the class chain mixes in
  effectively one step. (Row counts 13,987-19,270 per class; the
  next moduli are ≤ 0.035, so the gap statement is robust to the
  estimator noise at this sample size.)

**(d) The drift artifact — his attribution tested.** Theoretical
identities under `π_k`, stated precisely (the owning laws: the ledger
`P(s = j) = 2^{−j}` and the entry-depth law, aeh.md 13.2/13.3.2, paper
`sec:aeh`): per odd (T-)step the drift is `log₂ 3 − 2 = −0.4150`
(`E[v₂(3x+1)] = 2`); per F-step (per block) it is `E[m]·log₂3 − E[m] −
E[s] = 2(log₂ 3 − 2) = −0.8301`, since `E[m] = E[s] = 2` under `π_k`
(both measured at `2.00 ± 0.01` in our run). The brief's shorthand
"`log₂ 3 − 2` per block" conflates these; the per-block value is
`2(log₂ 3 − 2)`. His letter compares a measured "drift-per-step" to
`−0.415`, i.e. the per-odd-step baseline.

Cut-protocol estimators (all biased by construction; this is the
artifact space, measured):

```text
                                          cut 2^20     cut 2^30
crossing-included   per F-step            -0.834       -0.834      (unbiased-looking)
crossing-included   per odd step          -0.419       -0.419      (unbiased-looking)
censored both ends  per F-step            -0.777       -0.755
censored both ends  per odd step          -0.387       -0.376
survivor-avg slope  per F-step            -0.407       -0.347
survivor-avg slope  per odd step          -0.204       -0.174
```

His `−0.33/−0.36` is bracketed by the censored per-odd-step
(`−0.387/−0.376`) and survivor-averaged-slope per-F-step (`−0.407/−0.347`)
families; his exact estimator is under-determined by the letter, but
every member of the cut-conditioned family with per-orbit survival or
endpoint censoring shows the same upward (less negative) bias, growing
with the cut — the direction and rough size of his artifact.

**The decisive test** (our calibration methodology, aeh.md 13.5's
standing rule: fixed horizon, unweighted, per-visit pooling, no
stopping rule, no cut, no per-orbit ratio estimators): same population,
T = 15 F-steps: per F-step `−0.8430 ± 0.0077` (z = −1.7 vs theory),
per odd step `−0.4246 ± 0.0048` (z = −2.0; one rare fast-faller dips
to 2^4.6 within the horizon — mild bottom contamination, measured, not
excluded). Altitude-control population (starts `[2^80, 2^81)`, T = 25,
same seed construction; minimum altitude visited 2^27.9): per F-step
`−0.8367 ± 0.0060` (z = −1.1), per odd step `−0.4166 ± 0.0037`
(z = −0.4). **Drift returns to theory at both normalizations when the
cut-conditioning is removed: his survivorship-bias attribution is
confirmed.** The one flag to send back: with the per-block reading of
"step" his theoretical comparison point should be `−0.830`, not
`−0.415`; with the per-odd-step reading his measured values need the
censoring/survivorship mechanism above. Either way the artifact is
protocol-level, exactly as he suspected — "flagged, not sold" was the
right label, and the flag now has a mechanism and a clean-protocol
resolution.

**(e) Scope.** His closing scope sentence — generic face only; a
spectral gap says nothing about exceptional orbits; the cycles live in
the distributional-to-pointwise gap — is exactly our own framing:
aeh.md 13.3.3 ("Even in full, AEH yields almost-everywhere statements
only... not excluded for any *individual* orbit") and the README
stopping rules. Agreement recorded; no new framing invented.

## Item 6: proposal lines (drafted, NOT applied — author's decision)

**For `cycles.md`, a remark under 12.6.1** (candidate text):

> **Remark 12.6.1.1 (transport recurrence; the divisibility conditions
> are one condition).** The rotation numerators satisfy the exact
> identity `2^{σ_r} R_{r+1} = 3^{m_r} R_r + (2^{s_r} − 1) q` for every
> profile `(m_t, s_t)` with entries `≥ 1` (no closure needed), whence,
> since `gcd(q, 6) = 1` (`q` odd; `q ≡ (−1)^K mod 3`), `R_{r+1} ≡
> (unit)·R_r (mod q)`: `gcd(q, R_r)` is rotation-invariant and
> `q | R_0` iff `q | R_r` for all `r` — the `p` divisibility conditions
> of this Proposition are one condition. The size conditions
> `q ≤ R_r` do not collapse (they genuinely vary by rotation; see the
> 12.8.6.4 instances). In the mirror frame this is Lemma 14.15.9.2
> exactly: via the seam identity `N_r + q = 2^{m_r} R_r`
> (`experiments/merle_round3_check.py`), the recurrence is the rotated
> fixed points' affine orbit equation cleared of denominators, and the
> gcd invariance is the shared-reduced-denominator clause — with
> 12.6.1's `q = 2^K − 3^n` the *unreduced* denominator (they differ,
> e.g., at the p = 7 seed of 12.8.3, where `gcd(q, R_r) = 7`).
> Independently found by Eric Merle (correspondence, 2026-07-18;
> proposed as ledger entry L-A1) and, in the fixed-point frame, by
> this repository (Lemma 14.15.9.2, merged 2026-07-17); [credit
> phrasing per the author]. Verified: 600 random profiles + recorded
> instances, 29,211 exact checks, 0 failures (2026-07-18,
> `experiments/merle_round3_check.py`).

**For `aeh.md`, a line in the calibration record §13.4** (candidate
text):

> * **External replication (measured grade, 2026-07-18):** an
>   independent implementation by Eric Merle (3,000 orbits, cuts 2^20
>   and 2^30) reproduces the class skeleton's two exact values and the
>   `2^{−j}` ledger, and measures the 8-class transfer-matrix spectrum
>   at `|λ₂| ≤ 0.06` (our re-run: `0.028/0.036` at the two cuts —
>   `experiments/merle_aeh_key_check.py`); his flagged drift artifact
>   (`−0.33/−0.36` vs `−0.415`) is confirmed to be survivorship bias
>   from the cut protocol: under this page's fixed-horizon standing
>   rule the drift is `−0.4166 ± 0.0037` per odd step (`log₂3 − 2 =
>   −0.4150`) and `−0.8367 ± 0.0060` per block (`2(log₂3 − 2) =
>   −0.8301`). Spectral numbers are measurements, not theorems; the
>   generic-face scope of 13.3.3 is unchanged.

**Ledger-facing (for the author's reply, not a wiki page):** L-A1
verdict: recurrence verified (our key turned), antecedence answer as in
item 2 — new in the cycles frame, equivalent under an explicit
dictionary to Lemma 14.15.9.2(1)-(2)/14.15.9.4(1) (merged one day
before his letter), independent simultaneous discovery; the seam
identity `N_r + q = 2^{m_r} R_r` is the object neither side had stated.
L4 verdict: both keys turned at measured grade, with the drift
artifact resolved (survivorship confirmed, one normalization flag) and
the spectrum confirmed under his bound. His corrections: ghost identity
confirmed-as-uninformative; KS dedup reason does not transfer exactly
to our construction (exact `u`-coincidence nowhere, near-duplication at
~80% of rotations); his corrected `D = 0.1525`/~34 recorded at his
weight.

## Compliance

Verification and adjudication only. No cycle search, no
divisibility-based exclusion attempt (the collapse's invitation
declined, per the brief), no transfer-operator theory (spectrum at his
scale only), no Lean work, no equidistribution proof effort. Off-brief
observations, logged and stopped: (i) the recorded p = 7 staircase seed
has `gcd(q, R_r) = 7` — a live reduction instance on our own books
(surfaced in item 2's witnesses; no development); (ii) the structural
near-coincidence of `u` across crash depths (mechanism in item 4(b); no
development). Both scripts run clean end-to-end from a fresh checkout
(`python experiments/merle_round3_check.py`, ~3 s;
`python experiments/merle_aeh_key_check.py`, ~1 s; numpy required for
the spectrum only).
