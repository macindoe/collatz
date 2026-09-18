# Findings: the 3-adic Baker cap on the mirror side (Rubin correspondence, 2026-09-05)

Brief: `briefs/rubin-3adic-baker-brief.md`. Branch **`rubin-3adic-baker`**.

**Base SHA.** The worktree was cut from `7232912` (pre-brief HEAD) and lacked
`briefs/rubin-3adic-baker-brief.md`. `git merge main` fast-forwarded to
**`36a8cf1`** ("briefs/rubin-3adic-baker-brief.md: delegation brief..."),
local `main`'s tip at session start, which does carry the brief. Branch
`rubin-3adic-baker` was cut from `36a8cf1`.

Register: flat, calibrated prose. Every number below either comes from
`experiments/mirror_baker_cap.py`'s committed output or is a hand computation
reproduced in this file; nothing is labeled proved without that script's
independent check.

---

## 1. Provenance (paraphrased; no verbatim letter, no address)

Per the brief: on 2026-09-05 Brett Rubin, an independent worker on the
problem since 2022, wrote to the author after reading paper 1 at v3. Point 3
of his letter, paraphrased: for fixed `e`, a small `k` can carry a deep
valuation whenever his reparametrized anchor `diagonalCenter` opens with a run
of zero digits, so the 3-adic analogue of the unconditional clause has to cap
the size of the constant rather than slow the rate of growth — he named this
a real gap and said he does not hold the Yu / Bugeaud–Laurent references. The
main session's 2026-09-05 pre-check already identified his law as Theorem
14.2.4 exactly (under `s = (e mod 3) + 2k`, `diagonalCenter` an affine
reparametrization of `M₃`) and his
`e = 1` degeneration as Lemma 14.2.1 / Proposition 14.2.3. This session's job
is Point 3's gap: a cap on `d` as a function of `s`, transplanting
stage1-synthesis.md 11.8.3.11.

Credit clause used throughout: "flagged by Brett Rubin (correspondence
2026-09-05)". No email address appears in any tracked file.

**Correction (2026-09-16).** This section originally also claimed no verbatim
quotation of his letter appeared in any tracked file. That claim was wrong:
the sentence rendered here and in reverse.md 14.2.5 was within a word of his
own wording ("so the analogue of your Theorem 3.3's unconditional clause has
to bound the constant rather than the growth"), and his reply of 2026-09-16
caught it — the delegate that wrote it was working only from the main
session's paraphrase and had nothing to compare against. Both occurrences are
now reworded to a genuine paraphrase (above, and reverse.md 14.2.5); see §8.

---

## 2. The derivation, written out (Queue 1)

Start from Theorem 14.2.4: for a door `y` (odd, `3∤y`) and `s` of the
admissible parity (14.1.1: `s` odd if `y ≡ 1 (mod 3)`, `s` even if
`y ≡ 2 (mod 3)`),

```text
d = v₃(2^s y + 1) = 1 + v₃(s − M₃(y)).
```

**Step 1 (squaring reduction).** By 14.2.4's own proof, `v₃(2^s y + 1) ≥ 1`
whenever `s` has the admissible parity, and since `(2^s y + 1) − (2^s y − 1)
= 2` is a 3-adic unit, `v₃(2^s y − 1) = 0` always. Hence

```text
d = v₃(2^s y + 1) = v₃(2^s y + 1) + v₃(2^s y − 1) = v₃((2^s y + 1)(2^s y − 1))
  = v₃(4^s y² − 1).
```

Multiplying by the unit `y²` (`3∤y`) does not change the valuation, so with
`α₁ = 4, b₁ = s, α₂ = y^(−2), b₂ = 1`:

```text
d = v₃(4^s y² − 1) = v₃(y² (α₁^b₁ − α₂^b₂)) = v₃(α₁^b₁ − α₂^b₂) = v₃(Λ).
```

This is the step the 2-adic pin did not need in this form: on the forward
side, the anchor `N(ω)` is *defined* by `9^n ≡ ω^(−1)`, so `9` and `ω^(−1)`
already sit as two independent bases with `ω^(−1)` raised to the fixed
exponent `1` — no squaring is needed to produce that shape. On the backward
side the raw quantity `2^s y + 1` has `y` appearing linearly, not
exponentiated, so there is no second base-to-a-power term to read off
directly; squaring converts `y` (linear) into `y²` (a fixed base to the fixed
exponent `1`), at the cost of also converting `2^s y + 1` into `4^s y² − 1`,
which is why the valuation identity above needs the intermediate unit fact
`v₃(2^s y − 1) = 0` to go through. This is exactly the step the brief
anticipated.

**Step 2 (principal units, `D = 1`, `g = 1`).** `α₁ = 4 ≡ 1 (mod 3)` and
`α₂ = y^(−2) ≡ 1 (mod 3)` (`y² ≡ 1 (mod 3)` by Fermat, since `3∤y`): both are
already principal units mod `3`, so the least `g` with `α₁^g ≡ α₂^g ≡ 1
(mod 3)` is `g = 1` — automatic, exactly mirroring 11.8.3.11's "`9 ≡ 1
(mod 8)`, `g = 1`" at `p = 2`. Both `α₁, α₂` are rational, so
`D = [Q(α₁,α₂):Q] = 1`, matching 11.8.3.11's `D = 1`.

**Step 3 (multiplicative independence, and the excluded case).** `α₁ = 2²`
carries only the prime `2` in its factorization; `α₂ = y^(−2)`, for
`|y| ≥ 5` (odd, coprime to `6`), carries none of it. So `α₁^a = α₂^b` (for
integers `a, b`) forces `4^a` and `y^(−2b)` to agree prime-by-prime, hence
`a = 0` and (since `|y| ≥ 5`) `b = 0`. `α₁, α₂` are multiplicatively
independent **exactly when `|y| ≠ 1`**: at `y = ±1`, `α₂ = 1`, and `1` is
multiplicatively dependent with everything (`α₁^0 = α₂^b` for every `b`).

This is the second step the brief anticipated, and it is a genuine, not a
cosmetic, difference from the forward side. On the forward side,
11.8.3.11's own sentence — "multiplicatively independent whenever `3∤ω`,
which holds for every valid odd core by definition" — does not explicitly
exclude `ω = 1`, even though `α₂ = ω^(−1) = 1` at `ω = 1` is exactly as
degenerate as `y = ±1` here (see §6, "for the author's reply", for why this
is worth a quiet look but is not something this session edited). On the
backward side there are *two* excluded points, not one, because the relevant
algebraic quantity is `y²` (invariant under `y ↦ −y`), and because reverse.md
extends the underlying arithmetic identity beyond the literal (always
positive) doors of 14.1.1 to match Rubin's own sign-unrestricted `e`. In the
literal tree of 14.1.1, doors are always positive (`y_a = 2^(D−a)3^aΩ − 1 ≥
1`), so only `y = 1` is ever realized as an actual door; `y = −1` completes
the arithmetic identity's degenerate locus and matters for Rubin's own
`e`-indexed law and, later, for itinerary.md's signed extension (14.15.6.1
already excludes `y = −1` there, for the unrelated dynamical reason that `−1`
is `T`'s fixed point).

**Step 4 (the excluded case itself).** At `y = ±1`, Lemma 14.2.1 (`v₃(2^t−1)
= 1+v₃(t)` for even `t`) settles the law exactly, without any Baker input:

- `y = 1`, `s` odd: `2^s + 1 = 2^s + 1^s`; LTE for `p = 3` odd exponent gives
  `v₃(2^s + 1^s) = v₃(2+1) + v₃(s) = 1 + v₃(s)`.
- `y = −1`, `s` even: `2^s·(−1) + 1 = 1 − 2^s = −(2^s − 1)`, and Lemma 14.2.1
  gives `v₃(2^s−1) = 1+v₃(s)` directly.

So `d = 1 + v₃(s)` at both `y = 1` and `y = −1` — matching `M₃(1)`, `M₃(−1)`
being the two elements of `E₃` with vanishing `Z₃`-component (`M₃(−1) = 0`
exactly, since `2^0 = 1 = −1/(−1)`; `M₃(1)`'s `Z₃`-part is `0` too, by
Proposition 14.2.3's own computation, mod `2·3^(k−1)` the value `3^(k−1)`,
which is `0` in the `Z₃`-component and `1` (odd) in the `Z/2`-component).
This is Rubin's `e = 1` degeneration, his `diagonalCenter = −1/2`. It is *sharper* than
the general cap, not just an exception to it: `d = 1+v₃(s) ≤ 1 + log₃ s`,
linear in `log s`, the same phenomenon as cycles.md 12.6.1.3(b)'s rational
anchor point (`ω = 1` there, elementary and logarithmic against the general
`(log n)²` Baker ceiling).

---

## 3. The source statement, verbatim, and the specialization (Queue 2)

**What was obtainable.** ScienceDirect's copy of the primary source (Y.
Bugeaud, M. Laurent, *Minoration effective de la distance p-adique entre
puissances de nombres algébriques*, J. Number Theory 61 (1996), 311–342) is
behind a Cloudflare challenge that blocks both `WebFetch` and a direct
`curl` with a browser user-agent (HTTP 403, "Cf-Mitigated: challenge") — it
was not the open archive the brief expected. An arXiv note improving the
same paper (T. Yamada, *A note on the paper by Bugeaud and Laurent...*,
arXiv:math/0607072) was obtained in full but restates only the authors'
Lemme 10/11 and Théorème 1, not Corollaire 2, so it does not supply the
needed statement.

**What was used instead.** M. A. Bennett, Y. Bugeaud, *Effective results
for restricted rational approximation to quadratic irrationals* (2011),
obtained in full (`personal.math.ubc.ca/~bennett/BeBu.pdf`). Yann Bugeaud —
one of the two 1996 authors — restates the needed bound there as their own
Theorem 2.1, introduced as "a slightly simplified proof of Théorème 3 of
[Bugeaud–Laurent 1996]" (their reference [10], the exact J. Number Theory 61
(1996), 311–342 paper). Quoted verbatim (their notation; `Q̄_p` an algebraic
closure of `Q_p`, `ν_p` its valuation normalized `ν_p(p)=1`):

> Let `p` be a prime number and denote by `Q̄_p` an algebraic closure of the
> `p`-adic field `Q_p`. We equip the field `Q̄_p` with the ultrametric
> absolute value `|x|_p = p^(−ν_p(x))`... Let `α₁` and `α₂` be algebraic over
> `Q` and regard them as elements of the field `Q̄_p`. Write
> `D = [Q(α₁,α₂):Q]`. Our goal is to deduce a lower bound for the
> ultrametric absolute value of `Λ = α₁^b₁ − α₂^b₂`, where `b₁` and `b₂` are
> arbitrary positive rational integers.
>
> We assume that `ν_p(α₁) = ν_p(α₂) = 0` and denote by `g` the smallest
> positive integer such that `ν_p(α₁^g − 1) > 0` and `ν_p(α₂^g − 1) > 0`. It
> is easily seen that `g ≤ p^D − 1`. Let `A₁ > 1, A₂ > 1` be real numbers
> such that `log A_i ≥ max{h(α_i), (log p)/D}` for `i = 1` and `2`, where `h`
> denotes the logarithmic Weil height. Set `b' = b₁/(D log A₂) + b₂/(D log
> A₁)`.
>
> **Theorem 2.1.** With the above notation, if the algebraic numbers `α₁`
> and `α₂` are multiplicatively independent, then `ν_p(Λ)` is bounded above
> by
>
> `[24pg / ((p−1)(log p)^4)] D^4 (max{log b' + log log p + 0.4, (10 log
> p)/D, 10})^2 log A₁ log A₂.`

**Naming caveat (for the author).** Bennett–Bugeaud cite this as their
"slightly simplified proof of Théorème 3" of the 1996 paper, not as "their
Corollaire 2" — the name stage1-synthesis.md 11.8.3.11 uses. This session
did not obtain the 1996 French text itself to confirm the numbering matches
name-for-name; the identification rests entirely on the content and the
numerical control below, not on the label. See §6.

*Closed at review (2026-09-13).* The author supplied Corollaire 2 from the
1996 text: "Avec les hypothèses et notations du Théorème 3, supposons de
plus que α₁ et α₂ appartiennent à U_v^1. Alors v(Λ) ≤ 24p/((p−1)(log p)^4)
D^4 (max{log b' + log log p + 0.4, 10 log p / D, 10})^2 log A₁ log A₂ ≤
208 D^4 (max{…})^2 log A₁ log A₂." So Corollaire 2 is exactly the `g = 1`
case of Théorème 3 that both pins use; 11.8.3.11's label was right, the
Bennett–Bugeaud restatement is Théorème 3 in general `g`, and the two
agree at `g = 1`. The second inequality is the source of 11.8.3.11's
`208`: the paper's own uniform constant, `24p/((p−1)(log p)^4) ≤ 208` for
every prime `p`, attained at `p = 2` (`207.94…`). No label changes anywhere.

**The `p = 2` control (required before trusting the `p = 3` reading).**
Specializing Theorem 2.1 at `p = 2, D = 1, g = 1` (`9 ≡ 1 (mod 8)`),
`A₁ = 9, A₂ = ω, b₁ = n, b₂ = 1` — 11.8.3.11's own setup — gives:

```text
prefactor: 24·2·1 / ((2−1)·log(2)^4) · 1^4 = 207.940648...   (11.8.3.11 quotes "208")
```

and, at `ω = 5`:

| `n` | this formula | 11.8.3.11's published value | rel. error |
|---|---|---|---|
| `34,000` | `73,534.0` | `~73,555` | `0.029%` |
| `10^6` | `131,508.3` | `~131,500` | `0.006%` |
| `10^9` | `302,455.3` | `~302,500` | `0.015%` |

The residual `~0.03%` is fully explained by 11.8.3.11's own rounding of
`207.94...` to the displayed `208` (`208/207.9406 = 1.000285`, matching the
`34,000`-row error to three figures). **The control reproduces
11.8.3.11's constant.** Verified: `experiments/mirror_baker_cap.py` PART G.

**The `p = 3` specialization.** `D = 1, g = 1` (Step 2 above), `A₁ = 4`
(`log A₁ = log 4 ≥ max{log 4, log 3}`, the height requirement met with
equality), `A₂ = y²` (`log A₂ = 2 log|y| ≥ max{2log|y|, log 3}`, true for
every admissible `|y| ≥ 5`), `b₁ = s, b₂ = 1`, `b' = s/(2 log|y|) + 1/log 4`:

```text
d = v₃(4^s y² − 1)
   <= [36/(log 3)^4] · log 4 · log(y²) · (max{log b' + log(log 3) + 0.4, 10 log 3, 10})^2.
```

Collecting the `y`-dependence into a single coefficient of `(log s)²` (as
11.8.3.11 collects `208 log9 logω` into `C(ω)`):

```text
C₃(y) := 144 · log 2 · log|y| / (log 3)^4  ≈  68.5189 · log|y|.
```

`d ≤ C₃(y)·(log s)²` for `s ≥ 1` of the admissible parity, `|y| ≠ 1` — up to
the floor, exactly as 11.8.3.11's own `C(ω)` statement is qualified (see
§6). This is Corollary 14.2.5.1; Corollary 14.2.5.2 is the digit-match
reading via `d = 1+v₃(s−M₃(y))`.

---

## 4. Rubin's point about the constant, verified (Queue 3)

His two named instances, checked by direct integer computation
(`experiments/mirror_baker_cap.py` PART D):

- `e = 5, k = 1`: `s = (5 mod 3) + 2·1 = 4`; `2^4·5+1 = 81 = 3^4`, so `d = 4`.
- `e = 41, k = 13`: `s = (41 mod 3) + 26 = 28`; `2^28·41+1 = 11,005,853,697
  = 3^6 · 15,097,193` (the cofactor `≡ 2 (mod 3)`, confirming `v₃ = 6`
  exactly).

Both reproduce exactly. His `diagonalCenter`'s two named runs of zero digits
(his own symbol; not entered into the wiki's registry — see §5) are the
mechanism: `diagonalCenter` opens with two zero base-`3` digits at `e = 5`
before the digit that delivers `d = 4` at `k = 1`, and with a longer such run at `e = 41` before
the digit delivering `d = 6` at `k = 13`.

**Texture, against the cap** (PART F, `S = 4,000`, fresh integer scan):

| `y` | max `d(y,s)` for `s ≤ 4000` | at `s` | cap at `S = 4000` |
|---|---|---|---|
| `5` | `7` | `1192` | `13,309.9` |
| `7` | `8` | `335` | `16,092.4` |
| `11` | `10` | `2876` | `19,830.3` |
| `13` | `8` | `3799` | `21,211.8` |
| `41` | `8` | `2458` | `30,710.8` |
| `−5` | `8` | `1921` | `13,309.9` |
| `−7` | `8` | `2522` | `16,092.4` |

Rubin's own two instances against the cap **at their own `s`** (not `S =
4000`): `e=5,k=1` (`s=4`): observed `d=4`, cap `13,309.9`; `e=41,k=13`
(`s=28`): observed `d=6`, cap `30,710.8`. The cap is nowhere near binding at
either — stated flatly, per the brief: it excludes nothing, and bounds how
long a run of vanishing digits can last, not how often one occurs.

**Sanity-check narrative for `y = 5`** (PART F, mirroring 11.8.3.11's own
numeric paragraph): the bound is `~13,310` for `s` up to `~116,000`
(dominated by the floor `10 log 3 ≈ 10.986` inside the `max`), then grows as
`(log s)²` beyond that — `~19,042` at `s = 10^6`, `~44,324` at `s = 10^9` —
large but finite and slow-growing, the same qualitative picture as
11.8.3.11's.

---

## 5. Registry check (Queue 5, `symbols.md`)

`symbols.md`'s existing `D` collision index (frame 4, "Door / itinerary
frame") already carries three meanings: state depth in `state(y)=(Ω,D)`
(14.14.1), the unreduced fixed-point denominator (itinerary.md 14.15.9.1),
and the AEH window cap `W_{k,D}` (aeh.md 13.2). Rubin's own `diagonalCenter`
(his affine reparametrization of `M₃`, `e·2^((e mod 3)+2·diagonalCenter) =
−1`) is a **fourth** possible meaning — checked, and **not added** to the
registry, per the brief: it is his name for an object the wiki already has a
name for
(`M₃`, via the affine identity `s − M₃(e) = 2(k − diagonalCenter)` the main
session's pre-check already established). `C₃` was checked for collisions across the
whole tree (`grep`) and found unused before this session — no collision-index
entry was needed for it, only the new row alongside `C(ω)`.

---

## 6. For the author's reply

The drafted sentence "It transplants directly" needs three corrections, all
recorded above and all in reverse.md 14.2.5 itself, not silently smoothed
over:

1. **The squaring step is not free.** The 2-adic anchor's defining
   congruence (`9^n ≡ ω^(−1)`) hands Baker's theorem its two-logarithm shape
   for free; the backward law's `2^s y + 1` does not, because `y` appears
   linearly, not as a base-to-a-power. Converting it costs one extra
   valuation fact (`v₃(2^s y − 1) = 0`, itself a one-line consequence of
   14.2.4) and one squaring, which is why the mirror's statement reads
   `4^s y² − 1` rather than a direct analogue of `9^n ω − 1`.

2. **The excluded case is two points, not the forward side's (unstated)
   one.** `y = ±1` both degenerate (`y² = 1` either way), against the
   forward side's single `ω = 1`. Worth a quiet look on the forward page at
   some point: 11.8.3.11's own sentence "multiplicatively independent
   whenever `3∤ω`, which holds for every valid odd core by definition" does
   not itself flag `ω = 1` as an exception, even though `α₂ = ω^(−1) = 1`
   there is exactly as degenerate as `y = ±1` is here (`1` is
   multiplicatively dependent with everything). This session did **not**
   edit stage1-synthesis.md's math to add that caveat — out of scope for
   this brief, and the numbers there are unaffected (`ω = 1`'s law is
   already handled elsewhere and correctly, via the elementary reading at
   cycles.md 12.6.1.3(b)) — but the author may want it named explicitly
   there too, for the same reason Rubin's letter asked for the mirror's own
   version of this cap.

3. **The constant is pinned, but the source citation carries a naming
   gap.** The general-`p` statement used here (§3) is quoted verbatim from
   Bennett & Bugeaud (2011) Theorem 2.1, which they present as derived from
   "Théorème 3" of the 1996 Bugeaud–Laurent paper — not literally "their
   Corollaire 2", the name stage1-synthesis.md 11.8.3.11 uses. This session
   could not reach the 1996 French text itself (ScienceDirect's copy is
   behind a Cloudflare challenge; the brief's assumption of an "open
   archive" did not hold in practice). The identification of Theorem 2.1
   with 11.8.3.11's cited "Corollaire 2" rests on content and on the `p = 2`
   control reproducing 11.8.3.11's own pinned `208` constant and its three
   worked numeric values to `< 0.03%` (§3) — strong evidence they are the
   same result under two different exposition's numbering, but not a
   confirmed name-for-name match against the original. If the author (or a
   future session) obtains the 1996 paper directly, this is the one thing
   worth a two-minute check.

---

## 7. Compliance

`python experiments/encoding_scan.py` — see the top-level session report for
the exact `RESULT:` line (run once, immediately before the final commit, per
the brief).

---

## 8. Follow-up: the author's reply of 2026-09-16 (paraphrased; no verbatim letter, no address; main session, not a delegate)

Brett Rubin replied to the 2026-09-12 letter. Paraphrased throughout, per the
standing convention for every correspondent (HANDOFF.md):

1. **Authorship disclosed.** He works this material with Claude sessions of
   his own, the same division of labour this project's own README and the
   mirror paper's appendix state. He said the substantive content of his
   2026-09-05 letter — the identification of `M(ω)` with his `columnCenter`,
   the 3-adic law, the judgment calls about what did and didn't overlap our
   work, and the sentence quoted (now paraphrased) in reverse.md 14.2.5 — came
   from that session work; what was his was the decision to flag the gap and
   insist it be filled properly rather than filed as a hand-wave. He raised,
   without instructing us either way, that a named credit line for drafted
   prose should be accurate rather than flattering. **This is recorded here
   as a fact of provenance; the wiki's credit line at reverse.md 14.2.5 is
   unchanged pending the author's decision — see "Open" below.**

2. **One claim withdrawn.** His 2026-09-05 statement that the mirror
   construction "didn't overlap anything" we had was an overreach — he had
   read only Remark 7.2 of paper 1, not the mirror preprint our 2026-09-08
   reply named. He now acknowledges the correction; no wiki change follows
   (the credit line already reflected only the constant, never the
   construction).

3. **Both original arithmetic results confirmed, independently rerun on his
   side.** No change to our record; this is corroboration, not new content.

4. **The `diagonalCenter`-to-`M₃` relation confirmed exactly**, on his own
   terms: with `σ = (e mod 3)` and `s = σ + 2k`, he gives
   `M₃(e) = σ + 2·diagonalCenter(e)`, matching `s − M₃(e) = 2(k −
   diagonalCenter(e))` derived here. He confirms the `e = 1` case exactly
   (`diagonalCenter(1) = −1/2`, `M₃(1) = 0`) and attributes the sign-degenerate
   half of our excluded locus (`y = −1`) to Definition 14.2.2's `E₃ = Z/2 ×
   Z₃` structure, which his own working definition had collapsed to the `Z₃`
   part alone — an error on his side, in his own glossary's prose only, not
   in his defining equation; no correction needed here since this session
   worked from the equation throughout. He asked that the object be named
   `diagonalCenter` rather than `D` in any surviving credit line, since `D`
   already names a different object (a diagonal index) in his own library.
   **Applied throughout this file and reverse.md 14.2.5 (this session).**

5. **The phrasing question answered.** He confirms the cap's own sentence in
   14.2.5 ("it bounds how long a run of vanishing digits can persist, not how
   often one occurs") is ours, not a rendering of anything he wrote — no
   compliance issue there. He adds a further observation, in his own
   framework's terms: depth and frequency are governed separately, since deep
   runs recur at every scale (`siblingIndex ≡ diagonalCenter mod 3^N` forces
   `d ≥ N + 1`, infinitely often) while the cap bounds only how deep any *one*
   instance reaches. On our side this is the frequency half of Lemma 14.6.5.2
   (`P(d = j) = 2·3^{-j}` per branch, and the exact ternary ledger of
   14.6.5.2 mirror-side) read together with the depth cap of 14.2.5 — the two
   statements were already both in the record, stated separately, and his
   remark is that they answer complementary questions about the same object.
   **No wiki edit made**: this is a cross-reading, not a new claim, and adding
   it as a page cross-reference is left to the author (see "Open").

6. **A compliance defect he caught, corrected.** The sentence rendered in
   quotes in reverse.md 14.2.5 and in §1 above was, in his words, "within a
   word" of his actual sentence — a near-verbatim rendering, not the paraphrase
   this file's own header claimed. **Fixed this session**: both occurrences
   reworded to a genuine paraphrase (reverse.md 14.2.5; §1 above), and §1's
   false compliance claim corrected in place with a dated note. He raised no
   objection to being quoted verbatim (he calls it "your rule, not mine"), so
   the choice to paraphrase rather than now quote him explicitly is this
   session's continuation of the standing house convention ("letters
   paraphrased, never quoted", applied uniformly to every correspondent), not
   a reading of his preference — flagged for the author in case a different
   choice is wanted.

7. **An independent confirmation of two existing results, offered as a
   negative.** He had drafted an observation that our backward theory "lives
   at door resolution" and cannot be restated at the state level; a script he
   wrote to check it before sending refuted his own draft — a door value
   determines its state and index uniquely, so a door carries nothing a state
   lacks. He connects this to Theorem 6.1 (state-resolution criterion),
   Theorem 7.1, Remark 8.9, and Lemma 14.6.5.1 (the state-recovery formula) —
   all already in the record. **No wiki change**: this confirms existing
   claims from an independent implementation; it adds no new one. Recorded
   here as an external verification, in the sense the record already grants
   Merle's independent checks.

8. **A question left open, addressed to the author.** He asks for a sharper
   statement of what backward controllability of the anchor walk (Remark 7.4
   / reverse.md 14.12.3) would have to yield to say something about the
   forward, unsolved direction — even the shape of an implication, not a
   route to one. **Not answered here**: this calls for the author's own
   judgment on a genuinely open question, not a verification task.

9. **Scripts attached, not yet run.** Three self-contained Python 3 scripts
   (`verify_anchor_identity.py`, `verify_3adic_mirror.py`,
   `verify_door_vs_state_resolution.py`), cited to paper 1 v3, each stating
   its checked propositions in its own docstring. The Gmail tools available
   to this session expose attachment names and MIME types only, not content
   bytes — there is no tool call that retrieves the script text. **They have
   not been read or run.** Per the standing convention (HANDOFF.md: "his
   scripts, if sent, run as reproduction, not verification"), running them
   once obtained confirms nothing beyond what this file's own independent
   code (`experiments/mirror_baker_cap.py`) already establishes; they are
   evidence of his own reproduction, not new verification.

**Open, all the author's:**

- Whether the credit line at reverse.md 14.2.5 / HANDOFF.md should reflect
  the authorship disclosure of item 1, and how — the record already credits
  external correspondents by name (Merle throughout the shared ledger)
  without a parallel disclosure of their own tooling, so there is precedent
  either way; his own letter states explicitly that the choice is ours.
- Whether to add the depth-vs-frequency cross-reference of item 5 to
  reverse.md 14.2.5 / 14.6.5.2 — a small, low-risk addition if wanted, but not
  made unilaterally given the front's current low-priority standing and the
  author's recent redirection of effort toward the peak comb (comb.md §18).
- The three scripts (item 9) — need to be obtained as files or pasted text
  before they can be read or run.
- The Remark 7.4 question (item 8) — the author's to answer or decline.
