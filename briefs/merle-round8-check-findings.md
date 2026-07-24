# Findings: round-8 verify (merle-round8-check)

Delegated session, 2026-07-24. Brief: `briefs/merle-round8-check-brief.md`.
Branch `merle-round8-check`, base commit `7614815` (the brief commit). Launch note,
for the record: the worktree was cut at `d2b9960` (one commit behind); the branch was
created directly from `7614815`, which was present in the repository — no rebase needed.
Register: findings only; confirmations and flags separated; nothing here disputes the
letter's text — pasted digits are author-verbatim; where observation and claim differ,
both are recorded. Verification code: `experiments/merle_round8_check.py` (fresh code,
imports nothing from any Merle repository and nothing from prior Merle-check scripts;
exact integer arithmetic at every pass/fail decision; canaries hand-computed and printed
before sweeps); full run output committed alongside as
`experiments/merle_round8_check_output.txt`. **0 failures across all parts.**

## Item 1 — the shared repo at `b8842bb`

Unauthenticated read-only clone of `github.com/macindoe/one-obstruction-three-faces`
into the scratchpad succeeded (2026-07-24). **HEAD:
`b8842bb60bf828a12c7717730415442923966665` (`b8842bb`) — matching the letter's pin
digit-exact.** Author Eric MERLE, 2026-07-24 12:40:05 +0200, message: "L3 correction
(local obstruction at 7, no Hasse gap; REQ-017); L-A4 descent closes structured refuge
(REQ-016); accept cadeaux A+B with capacity margin ~0.27n (REQ-014); NOTE §4/§6
reframed to equidistribution."

### (i) L-A4 entry — CONFIRMED as described; one key (his), as expected

Exact current text (entire entry, verbatim):

> ## L-A4 — Descent: no new cycle in structured families (Merle, correspondence 2026-07-24)
>
> **DRAFT — one key (Merle); for co-editing.**
>
> In the tuned regime, every periodic profile `P` (period `d | gcd(n, S)`, a repeated
> word in reduced coordinates) is a cycle iff its base is: `q_P | R_0(P) ⟺ q_B | R_0(B)`
> (fixed-point invariance under repetition, extending L-A2). Hence no structured family
> contains a *new* cycle — one there would descend to a strictly smaller cycle — and any
> hypothetical nontrivial cycle must be **aperiodic/generic**. Verified 3,600/3,600 exact
> over periodic draws (`n ∈ {24, 36, 60}`, `d = 2..6`, base lengths `1..3`); canaries =
> trivial-cycle inheritance (`([1],[1])` cycle → `B²` cycle, `q = 7`, `R = 7`) and
> non-cycle base → non-cycle power. Companion measurements closing the naive routes: the
> odd-step ("no 3-absorption") stratum carries no congruence/gcd rigidity the general
> family lacks (REQ-MATH-013); the finite-scale near-integer mass is a **size artifact**
> (94–98% from the degenerate `R_0/q < 1` region, no cycle possible there; REQ-MATH-016).
> So the residual gap is genuinely the generic-family equidistribution, not a structured
> escape hatch.
>
> **Artifacts — Merle (2026-07-24), stack `017288f`:** [REQ-MATH-016] (descent +
> size-artifact), [013] (no congruence rigidity), [014] (capacity–demand), [015]
> (Weyl/structure). Canary-checked, exact big-integer arithmetic.

Against the letter: statement, check count 3,600/3,600, and the trivial-cycle-inheritance
canary all match; the entry carries one additional canary the letter compresses
(non-cycle base → non-cycle power) — consistent, not a mismatch. Keys: **one key
(Merle) only**, exactly as the letter's "seeded for your co-editing" implies. Two
observations, flat: the entry uses `d` (his repetition count) as the "period", i.e.
"period `d | gcd(n, S)`" means the profile is a base of length `ℓ` repeated `d` times
with `d | n` and `d | S` (his REQ-MATH-016 code makes this exact); and the letter's
phrase "the fixed-point inheritance of your L-A2, one level up" corresponds to the
entry's "(fixed-point invariance under repetition, extending L-A2)".

### (ii) L3 — correction CONFIRMED additive; recorded data untouched

The correction text (verbatim, the whole added block):

> **Correction / sharpening (Merle, 2026-07-24, REQ-MATH-017).** The "solvable at every
> local place, insoluble globally" reading is imprecise. For a *linear divisibility*
> `q | R` there is no Hasse gap (`q | R ⟺ v_p(R) ≥ v_p(q)` for all `p`, by CRT), so a
> global failure forces a local one; the earlier check tested only ℝ/ℤ₂/ℤ₃ (the
> structural primes, where `q` is a unit) and missed the obstructing prime. The `p = 7`
> instance has `7 | q`, `v_7(q) = 3 > v_7(R_r) = 1` at every rotation
> (`gcd(q, R_r) = 7`), so it fails already in **ℤ₇**. Accurate statement: every
> non-cycle is locally obstructed at some prime of the seam `q = 2^K − 3^n`; the
> surviving, substantive content is that *no single fixed* finite place handles all
> profiles (the structureless prime-local probe), the obstructing prime tracking the
> uncontrollable factorization of `2^K − 3^n` — so the missing mathematics is the
> **equidistribution** of `R_r mod q` along the family, not a Hasse-type global defect.
> Ben's independent distance profile (the two-key content) is unaffected: this corrects
> the Merle-side interpretation, kept with its data per protocol. Open for co-editing.
> Artifact: [`test_REQ-MATH-017`] (pinned at his commit `017288f`).

**Data-untouched check, by diff:** `git show b8842bb -- LEDGER.md` is pure addition —
three inserted blocks (this correction, the L-A3 additions, the L-A4 entry), **zero
deletions**; the L3 entry's original claim paragraph, its two-key status paragraph
(distance profile `[0.0538, 0.4784]`), and both artifact lines are byte-identical to
their state at `61d2cf3`. The correction adds interpretation without altering recorded
data, exactly as the letter claims. No flag.

### (iii) L-A3 — additions CONFIRMED; citation accurate; margin numbers match the letter

The added paragraph (verbatim):

> **Additions accepted (Merle, 2026-07-24).** (A) The signed characterization (Macindoe,
> wiki Thm 14.15.6.7, §14.15.6): the negative cycles become ordinary periodic diagonal
> points, `−1` the sole exception — adopted as the unifying frame for both shores.
> (B) The spent stock as the rational-anchor instance of the digit-match ceiling
> (logarithmic capacity vs linear demand, `cycles.md` 12.6.1.3) — Merle-side
> quantification (REQ-MATH-014): the capacity–demand margin is `≈ 0.27·n` (odd-step
> stratum) / `≈ 0.08·n` (general), positive and linearly growing, so the no-conspiracy
> cycle-count decays like `2^(−margin)`. The `positive odd integer` precision (Ben,
> 2026-07-24) is folded into §4.

Checked against the wiki: (A)'s citation is accurate — Theorem 14.15.6.7 (itinerary.md
14.15.6(c)) is the signed diagonal characterization, and "negative cycles as ordinary
periodic diagonal points, `−1` the sole exception" is exactly 14.15.6(d)(i)–(iii).
(B)'s citation is accurate — cycles.md 12.6.1.3's register sentence is precisely the
spent-stock/digit-match-ceiling identification, "logarithmic capacity against linear
demand". The margin numbers match the letter digit for digit. Keys: the entry's status
remains **two keys** (from the 2026-07-19 co-edit); the additions carry Merle's
acceptance, with (A) attributed to Macindoe (our side's content, already proved in the
wiki) and (B)'s *quantification* carrying **his key only** so far (REQ-MATH-014; our
replication is item 3(c) below — the shared-ledger key turn itself is not this
session's to make).

**Flag (definitional, resolved by artifact, recorded not disputed):** the entry states
the margin's *values* but no operational *definition*. The definition lives in his
artifact REQ-MATH-014 (item 2): `margin(n) = K − log₂(#profiles)`, `K = bitlength(3^n)
≈ log₂ q`, general count `Σ_p C(n−1,p−1)·C(S−1,p−1)`, stratum count
`Σ_p C(n−1,p−1)·oddcomp(S,p)` — the "no-conspiracy" expected-cycle-count exponent
(expected count ≈ #profiles/q = `2^(−margin)`). Observation on vocabulary: in
REQ-MATH-014 "capacité" is `log₂ q` (linear) and "demande" is `log₂ #profiles`, whereas
in cycles.md 12.6.1.3 "capacity" is the *logarithmic* 2-adic tracking capacity and
"demand" the *linear* digit-match demand — the ledger sentence joins the two vocabularies
under one name; the numbers are unambiguous once the artifact is read, but a co-edit
should pin the definition into the entry.

### (iv) NOTE.md sections 4 and 6 — CONFIRMED rewritten as the letter says

**§4 (Face III — the seam), exact current text:**

> The closure equation `ω·q = R_r` is a linear divisibility, so it has **no Hasse gap**:
> `q | R_r` iff `v_p(R_r) ≥ v_p(q)` at every prime — an integer solution exists exactly
> when a local one does at each place. The obstruction is therefore **local, at the
> uncontrollable primes of the seam `q = 2^K − 3^n`**: the `p = 7` instance already
> fails in `ℤ₇` (`7 | q`, `v_7(q) = 3 > v_7(R_r) = 1`, `gcd(q, R_r) = 7`), which our
> earlier `ℝ/ℤ₂/ℤ₃`-only reading missed [L3, corrected 2026-07-24]. What survives is
> that *no single fixed* finite place handles all profiles — the prime-local probe is
> structureless (no coset confinement, no coarse-invariant law), the obstructing prime
> tracking the wild factorization of `2^K − 3^n`; so the residual gap is quantitative:
> whether `R_r mod q` **equidistributes** along the forced family (an equidistribution
> statement, not a congruence). Structured (periodic) profiles are closed by descent —
> a cycle there forces a strictly smaller one — so any new cycle is aperiodic [L-A4].
> The realization-height theorem (Macindoe wiki, `itinerary.md` §14.15.5(b), Corollary
> 14.15.5.4 — the combined characterization; the wrong-sign clause at §14.15.5(c)): an
> itinerary is realized by an integer iff its 2-adic and 3-adic limits coincide at a
> positive odd integer; the classical negative cycles reappear as diagonal points of
> the wrong sign.

The realization-height reference cites itinerary.md §14.15.5(b) / Corollary 14.15.5.4 /
§14.15.5(c) accurately (the pin our `430c00c` pushed, verified against itinerary.md's
own text this session). The "positive **odd** integer" fold-in is present and correctly
placed — one precision, flat: the fold-in is our own commit `d2407b9` (2026-07-24,
pushed on the author's go-ahead), which the letter acknowledges as "your … precision …
folded into section 4"; his `b8842bb` rewrite of §4 **preserved** both the pin and the
odd-precision wording. Observation (co-edit candidate, the author's call): NOTE §4's
realization-height sentence still cites the unsigned characterization (14.15.5.4 with
the wrong-sign clause at 14.15.5(c)); the signed upgrade he accepted as frame (A) —
Thm 14.15.6.7, under which the negative cycles are *ordinary* diagonal points — appears
in the ledger (L-A3 additions) but not yet in NOTE §4's sentence.

**§6 (What remains, stated exactly), exact current text:**

> The residual hypothesis, now stated exactly: the **equidistribution of `R_r mod q`**
> along the aperiodic forced family (the structured refuge closed by descent [L-A4]);
> strictly weaker than `ProductBoundThreshold`; honestly placed on the ×2×3 gap. The
> capacity–demand margin is positive and grows linearly — `≈ 0.27·n` in the odd-step
> stratum, `≈ 0.08·n` in general [L-A3 cadeau B; REQ-MATH-014] — so the no-conspiracy
> cycle-count decays like `2^(−margin)`, making that one equidistribution the exact
> remaining gap. No promise past the calculations.

The equidistribution naming sentence is the first sentence above, recorded verbatim.
Register note per the brief: the `2^(−margin)` decay clause is heuristic language — his
own artifact labels it so ("LIMITE HONNETE: c'est l'heuristique 'sans conspiration'");
quoted here as heuristic.

### (v) Commits relied on and the diff range `61d2cf3..HEAD`

Full hashes: `b8842bb60bf828a12c7717730415442923966665` (HEAD),
`d2407b943f261e46731c12c728430084ffdf9a0b` (ours, odd precision),
`430c00c03bda8ab249bab9358f1942f8c1aeb7a2` (ours, pin),
`61d2cf30a6c53418913b8b93a345ae2fcacbfb5a` (range base, his, round-7 record),
`f496abe1faf63c2d54f5c878001199913c5d582e` (his, round-7 record, cited only).
Merle-side artifact commit: `017288fe237ce4b81e11322bd26cf2cd462ca90c` (item 2).

Diff range `61d2cf3..HEAD`, file by file:

- `430c00c` (macindoe, 2026-07-24 09:06:49 +1000) — `NOTE.md`: §4's realization-height
  reference pinned to itinerary.md §14.15.5(b) / Corollary 14.15.5.4 / §14.15.5(c),
  replacing the "renumbering in progress — pin on co-edit" placeholder. One paragraph.
- `d2407b9` (macindoe, 2026-07-24 09:07:04 +1000) — `NOTE.md`: one word in §4,
  "positive integer" → "positive odd integer".
- `b8842bb` (Eric MERLE, 2026-07-24 12:40:05 +0200) — `LEDGER.md`: three inserted
  blocks, zero deletions (L3 correction; L-A3 "Additions accepted"; new L-A4 entry).
  `NOTE.md`: §4 paragraph rewritten (no-Hasse-gap/local-obstruction framing, descent
  clause added; pin and odd-precision preserved), §6 paragraph rewritten
  (equidistribution named exactly; margin sentence added).

Whole range: 2 files, 16 insertions, 2 deletions (the 2 deletions are the two rewritten
NOTE paragraphs).

## Item 2 — the Merle-side scripts at `017288f`

**Found.** `017288f` = `017288fe237ce4b81e11322bd26cf2cd462ca90c`, the current HEAD of
`ericmerle3789/one-obstruction-three-faces-lean` (unauthenticated clone, 2026-07-24).
Author Eric MERLE, 2026-07-24 12:38:30 +0200 — two minutes before his shared-repo
commit `b8842bb`, consistent ordering. Message: "Add fissure scripts REQ-MATH-013..017:
stratum rigidity (neg), capacity-vs-demand (margin ~0.27n), equidistribution+descent,
mod-7 local obstruction (corrects L3 pure-global reading)". Contents: **five scripts**
(matching the letter's count) plus five output files, 797 insertions:

- `test_REQ-MATH-013_rigidite_strate_sans3.py` — defines the odd-step stratum
  exactly: **all `s_t` odd** ("sans souffle de trois": `3 | 2^s − 1` iff `s` even, so
  all-odd `s` means no factor of 3 enters via the `2^{s_t} − 1` terms). Claims to
  check: whether the normalized distance `u = dist(R_0 mod q, 0)/q` is rigid (bounded
  away from 0) in the stratum vs the general family; complete enumeration at small
  `n`, dense sampling otherwise; v2 after a self-red-team correcting an untuned
  `q < 0` artifact in v1. Result claimed (per ledger/letter): no congruence/gcd
  rigidity the general family lacks.
- `test_REQ-MATH-014_capacite_vs_demande.py` — the margin: `margin(n) = K − log₂ D`,
  `K = bitlength(3^n)`, `D` = #profiles (general: Vandermonde closed form
  `C(K−2, n−1)`; stratum: odd-composition sum); canaries = Vandermonde identity,
  odd-compositions-sum = Fibonacci, log-comb stability. His output: margin/n at
  `n = 1280`: **0.2730** (stratum), **109.3/1280 = 0.0854** (general).
- `test_REQ-MATH-015_equidistribution_et_structure.py` — Weyl sums `W_k` of `R_0/q`
  and near-zero over-density on the tuned family, plus tuned periodic families
  (`d | gcd(n, S)`); this is where his first "equidistribué" label broke (the header
  of 016 says so: "Mon label 'equidistribue' etait FAUX"), matching the letter's "the
  near-integer mass I first mistook for a signal".
- `test_REQ-MATH-016_artefact_taille_et_descente.py` — (A) the size-artifact
  adjudication: his output table's "dont R0/q<1" column reads **0.94, 0.95, 0.97,
  0.98** at `n = 24, 40, 63, 90` — the letter's "94 to 98 percent" digit-exact;
  (A bis) small-modulus equidistribution (`mod 7` biased, chi²/df 6.43/7.63; 11, 13
  uniform); (B) the descent check: **3,600/3,600** over `n ∈ {24,36,60}`,
  `d = 2..6` with `d | n`, `d | S`, base lengths `1..3`, 400 draws per cell —
  the L-A4 entry's numbers, digit-exact.
- `test_REQ-MATH-017_mod7_obstruction_locale.py` — the L3 correction instance:
  canaries `ord_7(2) = 3`, `v_7(2^149 − 3^94) = 7-exactly-3`; per-rotation table
  `v_7(R_r) = 1`, `gcd(q, R_r) = 7`, `ℤ₇`-insoluble at all 7 rotations; the
  local-vs-global exclusion fractions; the prime bias table — **5: chi²/df 1.91
  uniform; 7: 3.43 biased; 11, 13, 17, 23, 31, 127 all uniform** (the letter's list
  "5, 11, 13, 31, 127 all equidistribute; 7 … solitary" matches, with 17 and 23 also
  uniform in his table); and `ω = R_0/q` integer 0 times in 60,000 tuned draws.

Per the brief: his code was **read, not run** — it informs the definitions (margin,
stratum) and records his claims; nothing below substitutes it for verification.
Convention note, verified: his `R0` uses `sigma_t = s_t + m_{(t+1) mod p}`, which is
exactly cycles.md 12.6.1's convention (the round-3 seam-identity record spells this
out); our independent implementation matches on every recorded instance.

## Item 3 — independent computational verification

`experiments/merle_round8_check.py`, run 2026-07-24; full output in
`experiments/merle_round8_check_output.txt`. Canaries hand-computed and printed before
sweeps: the trivial word and its square (`q, R = (1,1)` and `(7,7)`), the `(−5)`-shore
word `([2],[1])` and its square (`q = −1, R = 1` → `q = −17, R = 17 = 1·17`), a
non-cycle base `([2,1],[3,1])` and its square (`q = 101, R = 37` → `q = 15655 =
101·155, R = 5735 = 37·155`), the transport recurrence on 200 random profiles, and the
recorded p = 7 staircase seed reproducing its published record (γ = 6.7438, size 7/7,
divisibility 0/7). All passed before any sweep ran. **0 failures overall.**

### (a) L-A4 clean-room — the derivation goes through, stronger than stated

**Derivation (the co-edit substance).** Conventions as in cycles.md 12.6.1 /
12.6.1.1: profile `(m_t, s_t)_{t<p}`, `n = Σm`, `K = Σs + n`, `q = 2^K − 3^n`,
`σ_t = s_t + m_{(t+1) mod p}`, `M_t = Σ_{j>t} m_j`, `S_t = Σ_{j<t} σ_j`,
`R_0 = Σ_t 3^{M_t} 2^{S_t} (2^{s_t} − 1)`.

Let `B` have length `p` and `P = B^k` (`k ≥ 2`). Then `n_P = k·n_B`, `K_P = k·K_B`,
so `q_P = 2^{k K_B} − 3^{k n_B}`. Index `P`'s blocks as `cp + t` (`c < k` the copy,
`t < p` the position). Two bookkeeping identities:

1. `M_{cp+t}(P) = (k−1−c)·n_B + M_t(B)` — the m-mass after position `cp+t` is the
   `k−1−c` whole copies to the right plus `B`'s own tail.
2. `S_{cp+t}(P) = c·K_B + S_t(B)` — since `S_t = Σ_{j<t} s_j + Σ_{j=1}^{t} m_j`
   (unrolling `σ`), and any `cp` consecutive indices of a `p`-periodic sequence sum
   to `c` full periods: `Σ s`-part contributes `c·S_B^{tot}`, `Σ m`-part `c·n_B`,
   and `S_B^{tot} + n_B = K_B`.

Therefore each term of `R_0(P)` factors: term`(c,t) = 3^{(k−1−c)n_B} 2^{cK_B} ·
3^{M_t(B)} 2^{S_t(B)} (2^{s_t} − 1)`, and summing over `t` first,

```text
R_0(P) = R_0(B) · G_k,   G_k := Σ_{c=0}^{k−1} 3^{(k−1−c) n_B} 2^{c K_B}.
```

`G_k` is exactly the geometric factor in `q_P = (2^{K_B} − 3^{n_B}) · G_k = q_B · G_k`
(the factorization `x^k − y^k = (x − y)(Σ x^c y^{k−1−c})` at `x = 2^{K_B}`,
`y = 3^{n_B}`). `G_k` is a positive integer for every base and every `k`. Hence

```text
q_P | R_0(P)  ⟺  q_B G_k | R_0(B) G_k  ⟺  q_B | R_0(B),
```

cancelling the common nonzero factor `G_k`. ∎

Three observations, flat: (1) **no tuning hypothesis is needed** — the identity and the
biconditional hold for every profile with entries ≥ 1, both signs of `q`, exactly like
L-A1/L-A2; his entry's "in the tuned regime" restricts the *claim's scope*, not the
mechanism (a co-edit can widen it). (2) The multiplicative identity
`R_0(P) = R_0(B)·(q_P/q_B)` is *stronger* than the biconditional and immediately
re-derives L-A2's gcd law (`gcd(q_P, R_0(P)) = G_k·gcd(q_B, R_0(B))` up to the
`gcd(G_k, ·)` bookkeeping L-A2 already closed) — "the fixed-point inheritance of L-A2,
one level up" is accurate. (3) The descent consequence as drawn (a cycle in a
structured family forces a cycle on its strictly smaller base; contrapositive: no new
cycle hides in any repeated-word family) follows from the biconditional plus L-A2's
divisible-iff-base "never a new one" clause — consistent with the wiki's record.

**Verification grid** (stated explicitly; identity + factorization + biconditional
checked exactly at every draw):

- Grid 1, exhaustive: all bases of length 1..3 with `m_i, s_i ∈ {1,2,3}`
  (9 + 81 + 729 = 819 bases), repetitions `k ∈ {2,3,4,5}` — 3,276 (base, k) pairs,
  24 of them with a divisible base (all inherited upward).
- Grid 2, random: 300 draws, lengths 4..6, entries 1..8, `k ∈ {2,3,4}`.
- Grid 3, tuned regime mirroring his: `n ∈ {24, 36, 60}`, `d = 2..6` with `d | n` and
  `d | S`, base lengths 1..3, 40 draws per cell — 720 draws.

Total 4,296 (base, k) pairs × 3 exact checks = **12,888 checks, 0 failures** (same
order as his 3,600, exceeded). Canaries: trivial-cycle inheritance exactly as he names
it (C1), plus our own hand-computed pair — the `(−5)`-shore square (C2, negative-`q`
inheritance) and a non-cycle square (C3).

### (b) L3 correction instance — CONFIRMED exactly

**The no-Hasse-gap principle, stated (no computation needed).** For a fixed nonzero
integer `q`, the equation `ω·q = R` has an integer solution iff `q | R` iff
`v_p(R) ≥ v_p(q)` at every prime `p` (unique factorization). Solvability over ℝ is
automatic (`q ≠ 0`); over `ℤ_p` with `p ∤ q` automatic (`q` a `p`-adic unit); over
`ℤ_p` with `p | q` it is exactly `v_p(R) ≥ v_p(q)`. So an integer solution exists iff
a local solution exists at every place: a linear divisibility has no local–global gap,
and any global failure is witnessed locally at some `p | q`. A check that tests only
ℝ, ℤ₂, ℤ₃ — where `q = 2^K − 3^n` is a unit — can never see the failing place; that
is the session-2 reading's precise error, and the correction is right.

**The `p = 7` instance, re-verified from our own records** (the recorded staircase
seed, `m = (4,7,9,15,23,35,1)`, `s = (1,1,1,1,1,1,49)`, `n = 94`, `K = 149`,
`q = 2^149 − 3^94`; round-3 record and cycles.md 12.6.1.1's `gcd = 7` note):

- `v_7(q) = 3` exactly (`7³ | q`, `7⁴ ∤ q`) — matches his claim.
- `v_7(R_r) = 1` at **every** rotation `r = 0..6` — matches.
- `gcd(q, R_r) = 7` at every rotation — matches the round-3 record.
- Hence `v_7(R_r) < v_7(q)` at every rotation: the closure equation is **insoluble in
  ℤ₇** at every rotation — the local obstruction is real.
- Calibration: the entry's recorded two-key distance profile recomputed —
  min 0.0538, max 0.4784, matching `[0.0538, 0.4784]` digit-exact.

### (c) Margin measurement — replicated digit-exact at his grid; definitional flag

Definition used (from artifact REQ-MATH-014, since the ledger entry states none —
flag recorded in item 1(iii)): `margin(n) = K − log₂(#profiles)`,
`K = bitlength(3^n)`, `S = K − n`; general = compositions `(m, s)` of `(n, S)` into
`p ≥ 1` parts each (counted by the direct sum `Σ_p C(n−1,p−1)·C(S−1,p−1)` — our
implementation sums directly rather than using his Vandermonde closed form); stratum =
same with all `s_t` odd (odd-composition count derived independently via
`s_i = 2a_i + 1` and cross-checked against a DP for `S ≤ 24`). Exact integer
combinatorics, deterministic — no sampling; grid = his `n ∈ {10, …, 1280}` plus our
extension `n = 2560`.

| n | margin/n stratum (ours) | his | margin/n general (ours) | his |
|---|---|---|---|---|
| 320 | 0.2884 | 0.2884 | 0.0997 | 31.9/320 = 0.0997 |
| 640 | 0.2784 | 0.2784 | 0.0904 | 57.9/640 = 0.0905 |
| 1280 | **0.2730** | 0.2730 | **0.0854** | 0.0854 |
| 2560 | 0.2701 | — | 0.0825 | — |

**Agreement: digit-exact at every n of his grid.** The margin is positive and grows
linearly on both families, as claimed. One flat observation from our extension: the
per-`n` slope is still declining slowly at `n = 2560` (0.2701 / 0.0825), so "≈ 0.27·n"
and "≈ 0.08·n" are the values at `n ~ 10³`, not proven limits — consistent with the
letter's own "about". No exclusion claim is made or implied here (per the brief: this
is measurement replication only; the decay sentence remains heuristic).

### (d) Door-closure spot checks — consistent with the letter at reduced scale

Explicitly labeled spot checks, not key turns. Our sampler is uniform over
compositions (positive parts via random cuts; odd parts via random bar placement) —
note his odd-part sampler is multinomial-weighted, a different ensemble; the results
agree anyway at this scale.

- **Degenerate-mass fraction** (stratum, `n ∈ {40, 63}`, N = 12,000 each; his 30,000
  at four n): of the near-integer mass `u < 0.01`, the fraction with `R_0/q < 1`
  (degenerate — no cycle can live below the minimal-element bound) came out **0.94**
  (n = 40) and **0.97** (n = 63) — inside his 94–98% range. Consistent.
- **Prime contrast 5 vs 7** (stratum, `n = 63`, N = 12,000): `R_0 mod 5` chi²/df =
  0.61 (uniform), `R_0 mod 7` chi²/df = 2.96 (biased) — the letter's contrast
  (5 equidistributes; 7 = 2³ − 1 special, `ord_7(2) = 3`) reproduced. The rest of his
  list (11, 13, 31, 127 uniform) is read from his OUT_REQ-MATH-017, not re-run.

## Adjudication summary (one line per letter claim)

| Letter claim | Status |
|---|---|
| 1. L-A4 seeded (statement, 3,600/3,600, canary, descent consequence) | **Confirmed** — entry verbatim, one key (his); clean-room derivation goes through, in fact with no tuning hypothesis; our 12,888 checks, 0 failures |
| 2. Congruence door dead; near-integer mass a size artifact; gap = equidistribution | **Consistent-at-reduced-scale** — degenerate fractions 0.94/0.97 (his 94–98%); renaming verbatim in NOTE §6; REQ-MATH-013's no-rigidity negative read and recorded, not independently re-run |
| 3. L3 correction (no Hasse gap; p = 7 fails in ℤ₇; data untouched) | **Confirmed** — principle correct as stated; `v_7(q) = 3 > v_7(R_r) = 1` all rotations, gcd = 7; LEDGER diff pure-additive, distance profile intact digit-exact |
| 4. Gifts A + B accepted; margin ≈ 0.27n / 0.08n; odd precision folded into §4 | **Confirmed** — ledger + NOTE texts verbatim, citations accurate; margin replicated digit-exact at his grid; flag: entry lacks the margin's operational definition (artifact supplies it); the §4 fold-in is our own `d2407b9`, preserved by his rewrite |
| 5. Prime-7 isolated (5, 11, 13, 31, 127 equidistribute) | **Consistent-at-reduced-scale** — 5-vs-7 contrast reproduced (0.61 vs 2.96); the full list read from his output, not re-run |
| 6. State pins (`b8842bb`, `017288f`, five scripts, NOTE §4/§6 rewritten) | **Confirmed** — both hashes resolve digit-exact; five scripts + outputs present; §4/§6 rewritten as described |

**Flags, collected:** (i) the margin definition is absent from the L-A3 entry (values
only; definition recovered from REQ-MATH-014) — co-edit should pin it; note also the
capacity/demand vocabulary inversion relative to cycles.md 12.6.1.3. (ii) Observation,
not a defect: NOTE §4 still carries the unsigned characterization (14.15.5.4); the
signed frame (A) he accepted lives in the ledger only — natural co-edit candidate,
the author's call. (iii) L-A4's "in the tuned regime" is narrower than the mechanism
needs (holds untuned, both signs) — co-edit can widen or keep scope as he prefers.
No discrepancies of digits, hashes, or texts anywhere this round. **Handbacks: none**
— no push or external write was needed; all clones unauthenticated and read-only.
