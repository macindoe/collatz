# Findings: round-12 §4 drift hand-backs, §9 rotation facts, the §10 silence, and the two small corrections

**Brief:** `briefs/merle-r12-drift-check-brief.md`. **Branch:** `merle-r12-drift-check`.
**Base SHA: `9d9d1ec`** ("round 12 received: …") — the worktree was cut at the stale
`3eab8f1` and was fast-forwarded to `9d9d1ec` by `git merge main` before anything was
read, per the brief's first rule.

**Script:** `experiments/merle_r12_drift_check.py` + committed output
(`experiments/merle_r12_drift_check_output.txt`): **152 checks (76 distinct × 2 working
precisions, dps 120 and 240), 0 failures**, verdict lists asserted identical at both
precisions before the summary prints; canaries and negative controls printed first, in
the regime-column spirit — every asserted equality tested in a regime chosen against it
(small `x` for the series, spread configurations for the sums, both a rescaled and a
real cycle for §4(b), and the failing `J = 11, 12` and the wrapping `J = 14` for the
sweep). Fresh code; imports nothing from any earlier check.

**Interaction record.** Three fresh read-only clones in the session scratchpad, nothing
else: the shared repo `macindoe/one-obstruction-three-faces` at HEAD **`7c05458`** (the
expected round-12 pin), his Lean repo `ericmerle3789/one-obstruction-three-faces-lean`
at HEAD **`d48ba9e`** (expected pin), and `ericmerle3789/collatz-cycles-lean` at HEAD
**`b38758d`** (three commits past the recon's pinned `1d77168`, all three his round-12
retraction-marker commits; the §10.2 verification below was performed **at the pinned
`1d77168`**). No pushes, no forks, issues, comments, stars, watches, follows; no key
turned, no ledger text pushed, no reply paragraph. Nothing in `HANDOFF.md`, `cycles.md`
or any existing findings file was edited; every correction below is **drafted here** for
the main session to apply at merge.

Verdicts in one line each: **§4(d) CONFIRMED — the display is a truncation, the
correction is ours to own; §4(b) CONFIRMED — the shared 44-decimals diagnosis is
refuted, the ratio is scale-invariant; §4(e)/(f) all small numbers CONFIRMED, credit
lines recorded as he fixed them; §9 every claim CONFIRMED, proposed `12.8.6.1` block
drafted below; §10 the silence is REAL, recommendation = retain with a scope clause in
the `+0.22/−0.29/−0.57` shape, established not assumed; 3,100/3,175 CONFIRMED with the
mechanism (blob 3,100 bytes + 75 LF lines → 3,175 under CRLF, both copies); §10.2
CONFIRMED — fifteen printed quotients, Jackson–Matthews 2002 cited for the 10,000.**

---

## 1. §4(d) — the display is a truncation, and the correction is ours to own

### 1.1 The series, derived here and confirmed

With `u = 1/(3x)`: `D(x) = log₂(3 + 1/x) − log₂(3 − 1/x) = (2/ln2)·artanh(u)`, and
`δ_x = 2/(3x·ln2) = 2u/ln2`, so

> `D(x)/δ_x = artanh(u)/u = 1 + u²/3 + u⁴/5 + u⁶/7 + …`
> `         = 1 + 1/(27x²) + 1/(405x⁴) + 1/(5103x⁶) + …`

The denominators are `(2k+1)·9^k`: `3·9 = 27`, `5·81 = 405`, `7·729 = 5103` — **his
coefficients are exact** (script 1.1), and the residual after three terms is
`1/(59049x⁸)·(1 + o(1))`, confirmed numerically at `x = 10` (script 1.2). Every term is
strictly positive, which is the whole verdict in one line: **the display
`D(x_min) = δ·(1 + 1/(27x_min²))` is the truncation of a positive series after its
first correction term, not an identity.** What is exact is the strict chain

> `D(x) > δ_x·(1 + 1/(27x²)) > δ_x`   for every `x > 1/3`,

verified with positive margins at `x ∈ {1, 7/3, 3, 17, 100, 2⁷¹}` (script 1.5). A
display of it as an equality under a "what is exact" heading is wrong, at every `x`.

### 1.2 His figures, all reproduced

| quantity | his figure | ours (script) | verdict |
|---|---|---|---|
| relative error of the truncation at `x = 1` | `2.58e-3` | `2.58121e-3` | MATCH |
| at `x = 3` | `3.06e-5` | `3.06276e-5` | MATCH |
| at `x = 17` | `2.96e-8` | `2.95674e-8` | MATCH (rounds to 2.96e-8) |
| at `x = 2⁷¹` | `7.94e-89` | `7.94376e-89` | MATCH |
| leading gap `D/δ − 1` at `2⁷¹` | `6.6432e-45` | `6.6431927e-45` | MATCH (and the record's `6.643193·10⁻⁴⁵` is the same number at 7 digits) |

Two of his sentences checked as sentences: the error is indeed **largest at `x = 1`**
and nothing in his (f) turns on it there (`D(1) = 1` against `s = 0.415`, factor 2.4);
and the second-order structure is as the series says (`gap·27x² − 1 = 1/(15x²) + O(x⁻⁴)`,
script 1.4). The canary pair C0.1/C0.2 exhibits the regime trap he names: the same
falsehood is a `2.58·10⁻³` relative error at `x = 1` and `7.94·10⁻⁸⁹` at `2⁷¹` —
invisible to any check run in the regime the work lives in.

### 1.3 Every site our record carries the display, verbatim

The display and its "what is exact" framing are **ours** — they entered at the round-11
hygiene check and were propagated by us into the sent reply and the shared LEDGER. His
letter hands the correction back; the acceptance is ours to state, flat, with the
mechanism named (an asymptotic taken for an identity, undetectable in the working
regime — structurally the same error as his §4(a), as he says himself).

**(a) The shared LEDGER, round-11 co-edit theorem-hand-back block** — read from the
fresh clone at HEAD `7c05458` (the block is inside the L-A8 entry; it entered at our
co-edit push `1d7907c` and is byte-identical in `briefs/merle-round11-coedit-findings.md`
§3.5 and in `briefs/merle-round11-coedit-patches/0001-*.patch` lines 101–109). The two
defective sentences, verbatim from the clone:

> At `x_min = 2⁷¹` the two sides agree to 44 decimal places, which is presumably why it
> reads as exact. Second, what **is** exact is the constant identification:
>
> > `D(x_min) = δ·(1 + 1/(27·x_min²))`, where `δ = 2/(3·x_min·ln2)` is T1's own constant.

(the second defect, the 44-decimals sentence, is §2's subject; both sit in the same
block). The surrounding block — the seam identity, its three-line derivation, the
sharp-bound correction of "exactly `n·δ`", the two-shore reading, the `x = 1`
corollary — is **unaffected**: nothing else in it asserts the truncation as exact, and
the identity `Σᵢ log₂(1 ± 1/(3xᵢ)) = K − n·log₂3` is exact and stands.

**(b) `briefs/merle-r11-hygiene-check-findings.md`** — four sites, plus the one that
had it right:

- line 604 (§8.2): `Σ_i D(x_i) ≤ n·D(X) = n·δ·(1 + 1/(27X²))`, `δ := 2/(3X·ln2)` —
  the equality embedded in the display;
- line 615 (§8.2): `D(x_min) / δ = 1 + 6.64·10⁻⁴⁵` at `x_min = 2⁷¹` — the truncation
  written as an equality at a fixed scale (here harmless numerically, wrong as "the
  constant identification is exact");
- line 702 (§8.4, the hand-back draft): `D(X) = δ·(1 + 1/(27X²))`;
- line 774 (§10, recommendation 6): `D(x_min) = δ·(1 + 1/(27x_min²))`;
- **line 567 (§8.1) is the correct form and needs nothing**:
  `D(x) = 2/(3x·ln2) · (1 + 1/(27x²) + O(x⁻⁴))`, and `D(x) > 2/(3x·ln2)` strictly —
  Merle's own observation that "your next sentence names the omitted terms and states
  the strict inequality; the two sentences are not consistent and the second is the
  correct one" is exactly right about this pair.

**(c) `briefs/merle-round11-coedit-findings.md`** — the §3.5 block (lines 180–184,
byte-identical to the LEDGER block above), and judgment call 6 (lines 252–262), which
verified the *direction* of the display character by character while carrying the
display itself as an equality ("The formula is `D(x_min) = δ·(1 + 1/(27·x_min²))`").
The direction stands; the equals sign does not.

**(d) `briefs/merle-round11-reply-draft.md`** (the sent round-11 reply) — line 521:

> `D(x_min) = δ · (1 + 1/(27·x_min²))`,  `δ = 2/(3·x_min·ln2)`

under the header sentence "**What is exact is the constant identification, and it is
the real content:**" (line 519), with line 524's "by a relative
`1/(27x_min²) = 6.643·10⁻⁴⁵` at `2⁷¹`" — and, one line further (524–525), the same
paragraph *also* states the correct strict form ("`D`'s series in `u = 1/(3x)` has all
positive higher terms, so `D(x) > 2/(3x·ln2)` strictly") — the exact inconsistency his
§4(d) points at, in the sent letter.

**(e) `briefs/merle-round11-coedit-patches/0001-*.patch`** — the commit-message summary
(line 44: `D(x_min) = delta*(1 + 1/(27*x_min^2))`) and the block itself (lines
105–109). The patch is the archived form of (a); it is a frozen artifact and needs no
edit, recorded here so the census is complete.

**(f) `HANDOFF.md`** — four lines carry the display as an equality, all inside item 1's
round-11 paragraphs: line 65 (the review-correction sentence,
"`D(x_min) = δ·(1 + 1/(27x_min²))`, not the reverse"), line 67 (the reply-draft
paragraph, "**Drift direction verified character by character:**
`D(x_min) = δ·(1 + 1/(27·x_min²))` … relative excess `6.643193·10⁻⁴⁵` at `2⁷¹` agreeing
digit for digit with `1/(27x_min²)`"), line 70 (the co-edit paragraph), line 78 (the
hygiene paragraph, "what is real is `D(x_min) = δ·(1 + 1/(27x_min²))`"). Per the brief,
`HANDOFF.md` is not edited here; these are the lines the main session's merge pass
should sweep (the minimal repair is `=` → `>` … or the explicit truncation clause, per
the corrected form below).

**(g) `experiments/merle_r11_hygiene_check.py` + its committed output** — script lines
972–974 print the display as an equality inside the adjudication prose
(`sum_i D(x_i) <= n * D(X) = n * delta * (1 + 1/(27 X^2))`) and carry the transferred
44-decimals sentence ("So the sum is n*delta in the EXTREMAL limit and to 44 decimal
places at X = 2^71"); output line ~325 mirrors it. Recorded flat, not edited: repairing
a committed script's prose means regenerating its committed output, which is a main
session decision (the round's precedent: the record-consistency sweep left exactly this
class of site stale by design).

Not counted as record sites: `briefs/merle-round11-coedit-brief.md` line 49 and
`briefs/merle-round11-reply-brief.md` line 47 (frozen instructions, not record);
`briefs/merle-r12-drift-check-brief.md` (this window's own brief, which quotes the
display in order to correct it).

### 1.4 The drafted correction block — co-edit material, NOT pushed

For the shared LEDGER's L-A8 entry, to sit directly under the theorem-hand-back block,
in the round's co-edit style (dated, ours, appended — his prose untouched). Drafted
here; whether and when it goes is the main session's and the author's call, and the
round-12 response is expected to travel as a PR per the author's §13 acceptance.

> **Correction to the block above — ours, accepted from Merle's round-12 §4(d), with
> the mechanism named (2026-07-30).** The display "`D(x_min) = δ·(1 + 1/(27·x_min²))`"
> under "what **is** exact" is wrong as written, and it is our error, not his: the
> factor is the truncation of a positive series after its first correction term. With
> `u = 1/(3x)`, `D(x) = (2/ln2)·artanh(u)`, so
> `D(x)/δ_x = 1 + 1/(27x²) + 1/(405x⁴) + 1/(5103x⁶) + …` with every term positive.
> What is exact is the strict chain
> **`D(x) > δ_x·(1 + 1/(27x²)) > δ_x` for every `x > 1/3`** — `δ` remains strictly
> below the true per-step drift at the minimum element, and the direction of every
> sentence in the block above survives; only the equals sign was wrong. The truncation's
> relative error is the next term, `1/(405x⁴) + O(x⁻⁶)`: `2.58·10⁻³` at `x = 1`,
> `7.94·10⁻⁸⁹` at `2⁷¹` — invisible in the regime this correspondence works in, which
> is the regime column's case in one line. The same commit corrects the sentence two
> lines earlier ("the two sides agree to 44 decimal places, which is presumably why it
> reads as exact"): that diagnosis is refuted by scale invariance — see the §4(b)
> correction below. Mechanism, named: an asymptotic taken for an identity, undetectable
> at the scale the work lives in; found by Merle (round 12, §4(d)), verified here with
> fresh code in an adversarial regime (Macindoe artifact:
> `experiments/merle_r12_drift_check.py`, 152 checks, 0 failures, commit `[PIN: main
> merge SHA at push time]`).

*(A paired one-sentence §4(b) correction is drafted at §2.4 below; the two would travel
in the same commit.)*

---

## 2. §4(b) — the diagnosis we both reached is refuted; his scale-invariance claim is exact

### 2.1 The claim, verified at his four scales

The `−17` cycle is derived in-script from its seed (elements
`{17, 25, 37, 55, 41, 61, 91}`, `n = 7`, `K = 11`; script 2.1). Rescaling the shape to
`x_min = 17·2^k` and computing `R(k) = Σᵢ D(xᵢ·2^k) / (7·D(17·2^k))`:

| scale | `R(k)`, 22 digits | `|R − shape|` |
|---|---|---|
| `17·2^20` | `0.4755266037564546434541` | `2.98·10⁻¹⁷` |
| `17·2^71` | `0.4755266037564546732308` | `5.87·10⁻⁴⁸` |
| `17·2^200` | `0.4755266037564546732308` | below dps-240 resolution |
| `17·2^1000` | `0.4755266037564546732308` | below dps-240 resolution |

**His `0.4755266037564546…` is confirmed at every scale, as printed** — all four values
begin with exactly those 16 digits (script 2.3). One flat precision note, recorded
because this window's job is digits: his figure is a *truncation* (the 17th significant
digit of the limit is a 7, so a 16-digit rounding would print `…4547`), and at
`k = 20` the value differs from the limit in the 17th digit (`…46434…` against
`…46732…`) — a relative deviation of `6.3·10⁻¹⁷`, consistent with the `O(x_min⁻²)`
correction (`1/(27·(17·2^20)²) = 1.16·10⁻¹⁶`) and invisible at his printed precision.
Nothing he printed is wrong; the invariance is exact *to leading order* and his own
sentence says so.

### 2.2 The leading-order identity, verified

His mechanism sentence — "to leading order the ratio is `(1/n)·Σᵢ(x_min/xᵢ)`, a pure
function of shape" — is confirmed twice over:

- the exact rational `(1/7)·Σ(17/xᵢ) = 0.4755266037564546 7323…` (script 2.2) is the
  value all four scales converge to;
- the deviation `R(k) − shape` falls by a factor `4.0000` per doubling of scale
  (script 2.4) — the `O(x_min⁻²)` signature, i.e. exactly the truncation term of §1.

The real cycles with two or more elements both show the same structure (script 2.5):
`−17` native ratio `0.4754938591` (within `O(1/(27·17²))` of the shape constant), `−5`
native ratio `0.8568830442` against its shape constant `6/7 = 0.8571428571…`, and the
rescaled `−5` shape is scale-invariant at `6/7` to 15 digits at `k ∈ {20, 71, 200}`. On
`−17` at native scale his §4(a) numbers reproduce: `Σ D = 0.188336` against
`n·D(x_min) = 0.396085`, factor `2.103` (script 2.5).

### 2.3 What actually agrees to 44 decimals, and what the error was

The pairing that converges is the **per-step** one: `D(X)/δ = 1 + 6.64·10⁻⁴⁵` at
`X = 2⁷¹` — 44 zero decimals in the ratio (script 2.6). The summed pairing does not
converge at any scale: `Σᵢ D(xᵢ)/(n·δ(x_min)) = 0.4755…` on the `−17` shape at
`17·2^67` (script 2.6), and canary C0.4 shows the ratio motionless between `k = 20` and
`k = 1000` (`|R(1000) − R(20)| = 3·10⁻¹⁷`) where the 44-decimals diagnosis predicts
drift toward 1. Canary C0.3 exhibits the degenerate/spread pair: all elements at
`x_min` gives ratio exactly 1 (the equality case that fooled the regime), any spread
gives the shape constant. **His account of the mechanism — the per-step convergence was
transferred to the sum — is exactly what the numbers show, and his rule ("a claim about
a sum over a configuration must be tested on a configuration with spread") is the right
lesson; it is the regime column again, phrased for sums.**

### 2.4 Where our record carries the 44-decimals explanation, and the drafted correction

The sentence is ours (hygiene check, round 11), was co-drafted independently by him
(his §4(b) says so), and sits at:

- `briefs/merle-r11-hygiene-check-findings.md` line 609–610 (§8.2): "At `X = 2⁷¹` the
  two sides agree to 44 decimal places, which is presumably why it reads as exact.";
- `briefs/merle-round11-reply-draft.md` lines 516–517 (**sent**): "At `X = 2⁷¹` the two
  sides agree to 44 decimal places, which is presumably why it reads as exact.";
- the shared LEDGER block (§1.3(a) above, same sentence inside the L-A8 hand-back;
  mirrored in `briefs/merle-round11-coedit-findings.md` line 180 and the archived patch
  line 105);
- `experiments/merle_r11_hygiene_check.py` line 974 + its committed output line ~325
  (the "EXTREMAL limit … 44 decimal places" prose; §1.3(g)).

Drafted one-sentence LEDGER correction (travels with §1.4's block, NOT pushed):

> **And the diagnosis in the same block — "the two sides agree to 44 decimal places,
> which is presumably why it reads as exact" — is refuted, jointly (2026-07-30).** Both
> of us drafted it; Merle refuted it (round 12, §4(b)): the ratio
> `Σᵢ D(xᵢ)/(n·D(x_min))` is scale-invariant — `0.4755266037564546…` for the `−17`
> shape at `x_min = 17·2^20`, `17·2⁷¹`, `17·2^200` and `17·2^1000` alike, because to
> leading order it is `(1/n)·Σᵢ(x_min/xᵢ)`, a pure function of shape — so no scale
> makes the summed pair agree. What agrees to 44 decimals at `2⁷¹` is the per-step pair
> `D(X)` against `δ`; that convergence was transferred to the sum, by both of us. The
> equality case of the bound is the degenerate configuration only. Verified both sides
> (his four rescalings; Macindoe artifact as above, spread-vs-degenerate canaries
> included).

For our own wiki-side record the same refutation applies verbatim to the hygiene
findings' §8.2 sentence and the sent reply's line 516 — the reply is sent and stands as
history (no edit possible), so the correction rides in the round-12 response; the
hygiene findings file is the main session's to annotate at merge, not this window's to
edit.

---

## 3. §4(e)/(f) — flat confirms, small numbers, and the credit record

### 3.1 Every number, reproduced

| claim | ours (script) | verdict |
|---|---|---|
| `log₂(1+u) − log₂(1−u) = 2u/ln2 + O(u³)`, cubic coefficient `2/(3ln2)` | coefficient `0.96179670` vs `2/(3ln2) = 0.96179669` | MATCH (script 3.1) |
| `x* = 7/3` unique: `3(3x+1) = 4(3x−1) ⟺ x = 7/3` | single root in exact rationals; `(3x*+1)/(3x*−1) = 4/3` exactly | MATCH (script 3.2) |
| `log₂(4/3) = 2 − log₂3` identically | to working precision at both dps | MATCH (script 3.2) |
| `D` strictly decreasing on `(1/3, ∞)` | `u = 1/(3x)` decreasing, `artanh` increasing; grid confirms | MATCH (script 3.3) |
| `D(1) = 1` exact | `(3+1)/(3−1) = 2` in rationals; `log₂2 = 1` | MATCH, exact (script 3.4) |
| `D(3) = log₂(5/4) = 0.321928 < s = 2 − log₂3 = 0.415037` | `10/8 = 5/4` exact; digits match | MATCH (script 3.5) |
| `D(2⁷¹)/s = 9.8145e-22` | `9.814456·10⁻²²` | MATCH (script 3.6; his round-11 `9.8·10⁻²²` and our `9.8145·10⁻²²` were already on record) |

His restated corollary reads correctly with its referents: `D` strictly decreasing and
`D(7/3) = s`, so `D(x) > s` exactly for `x < 7/3`; the only odd positive integer below
`7/3` is `1`, where `D(1) = 1` exactly and already `D(3)` falls below `s`. Nothing to
correct anywhere in (e) or (f).

### 3.2 The credit record, as he fixed it — no action, just the record

- **The factor 2 (two-shore reading): "jointly arrived at."** His §4(e): the
  identification is ours ("the identification is yours and I had not made it"), the
  frame it lands on (the drift reading) is his item 4, and "the note should carry it as
  jointly arrived at." Recorded as he states it. Our own round-11 blocks credit it the
  same way in substance (our observation on his frame); no record text changes hands.
- **The corollary: his; the proof: ours.** His §4(f): he keeps the corollary at the
  grade we assigned it ("returning a credit you have already weighed is not modesty, it
  is a second error in your ledger"), and states flatly that the carrying argument —
  uniqueness via `3(3x+1) = 4(3x−1)`, one linear equation, one root, `D` strictly
  decreasing — is ours. So: **corollary Merle, proof Macindoe**, and the referent he
  adds ("that integer is the trivial cycle") matches our own §8.3 wording. This matches
  the shared LEDGER block as pushed ("the corollary with integer teeth is ours and he
  can have it"), which now reads consistently with his acceptance; nothing to repair.
- His self-corrections inside §4 (the `9.8145e-22` referent added; "grey terrain" his,
  as we noted) are recorded as his.

---

## 4. §9 — the rotation reformulation, every claim checked

Nothing passed on his word; every claim below was recomputed from scratch (script
part 4, with the exact `K(n) = bitlength(3ⁿ)` supplying `δ(n) = ⌈nL⌉ − nL` and the
maxgap computed directly from the sorted circle points at both precisions).

### 4.1 Claim-by-claim verdicts

| # | his claim | verdict | our figures (script) |
|---|---|---|---|
| 1 | `5L = 8 − θ`, `θ = 8 − 5·log₂3 = 0.0751874964…` | **CONFIRMED** (with one digit note: the true digits are `0.07518749639…`, so his ellipsis-suffixed figure is a 9-digit rounding, not a truncation — same convention `cycles.md 12.8.6.1` already uses) | script 4.1 |
| 2 | `δ(n)` advances by `θ` **mod 1** under `n → n+5`; second case iff `δ(n) ≥ 1 − θ` | **CONFIRMED** — the step is `θ` or `θ − 1` and nothing else over `n = 1..2000`, and the wrap condition is exactly `δ(n) ≥ 1 − θ` (his "when `δ(n) < 1 − θ`" is the complementary clause, same content) | script 4.3 |
| 3 | wrap count over `n = 1..2000` is 150, fraction `0.075 ≈ θ` | **CONFIRMED** — exactly 150 | script 4.3 |
| 4 | `K(n+1) − K(n) ∈ {1,2}`, identity `= 1 + (⌈(n+1)(L−1)⌉ − ⌈n(L−1)⌉)` | **CONFIRMED** over `n = 1..2000`; the identity is immediate from `⌈nL⌉ − n = ⌈n(L−1)⌉` | script 4.4 |
| 5 | Sturmian of slope `L − 1 = log₂(3/2) = 0.584963`, **not** `L` | **CONFIRMED** — mechanical words need slope in `[0,1]`, and the step-2 indicator is the slope-`(L−1)` mechanical word; letter-2 frequency over 2000 steps is exactly `1170/2000 = 0.585` | script 4.4 |
| 6 | factor complexity `p(m) = m + 1` for `m = 1..12` | **CONFIRMED** on a 20,000-letter word: `p(1..12) = 2,3,…,13` | script 4.4 |
| 7 | aperiodicity ⟺ irrationality of `log₂3` | statement-grade (standard Sturmian fact), consistent; not a computation | — |
| 8 | `1/θ = 13.3000838`; for `J ≤ 13` the points `{jθ}` are already sorted, so `maxgap(J) = max(θ, 1 − Jθ)` **exactly**, no three-distance machinery | **CONFIRMED** — `13θ = 0.97744 < 1`, the closed form matches the directly computed maxgap for every `J = 1..13` at both precisions | script 4.1, 4.5 |
| 9 | reproduces `maxgap(12) = 0.0977500433`, `maxgap(13) = θ` "to every digit you printed" | **CONFIRMED** — `0.0977500432694`, rounding to our printed `0.0977500433` (`cycles.md 12.8.6.1`; `briefs/staircase-gamma-upper-findings.md` §3 prints `0.097750043269`, same number) | script 4.5 |
| 10 | criterion `J ≥ (1 − ℓ)/θ = 12.2967` with `ℓ = 0.1169390665 − 0.0415 = 0.0754390665` | **CONFIRMED** — `12.296738`, ceil 13; identical to Lemma G's `J = ⌈(1 − ℓ)/θ⌉` for `ℓ > θ` | script 4.6 |
| 11 | **new result:** maxgap stays exactly `θ` for `J = 13..25`, first falls at `J = 26` to `14θ − 1 = 0.0526249495` | **CONFIRMED**, and structurally: at each `J` in `13..25` exactly `26 − J` unsplit `θ`-gaps remain; the points `j = 14..26` land in the 13 original `θ`-intervals one each, every one at offset `14θ − 1` into its interval | script 4.7 |
| 12 | identity `13(14θ − 1) + 14(1 − 13θ) = 1` | **CONFIRMED identically** — the `θ`-coefficient is `13·14 − 14·13 = 0` and the constant is `−13 + 14 = 1`; the gap multiset at `J = 26` is exactly thirteen `(14θ−1)`s and fourteen `(1−13θ)`s, 27 gaps for 27 points | script 4.7 |
| 13 | margin `ℓ − θ = 2.5157e-4`, `0.3335 %` of arc | **CONFIRMED** — `2.5157011·10⁻⁴`, `0.333475 %` (rounds to his `0.3335 %`) | script 4.8 |
| 14 | cost-not-failure: losing `θ ≤ ℓ` moves the sweep from 66 to 131 consecutive integers (via `J = 26`) and the unconditional range from `p ≥ 16` to `p ≥ 18`; window sizes `0.05L^p` are `125.7` at `p = 17`, `199.2` at `p = 18` | **CONFIRMED** — `5·13+1 = 66`, `5·26+1 = 131`; window sizes `125.688`/`199.210`; exact integer counts `{p=15: 50, 16: 79, 17: 126, 18: 199}`, so 66 first fits at `p = 16` and 131 first fits at `p = 18`, two periods added to the finite check exactly as he says | script 4.9 |

Negative controls (canaries C0.5a–c): `maxgap(11) = 0.1729375397 > ` both arcs; `J = 12`
genuinely fails the two-sided arc (89 failing starts in `N ≤ 4000`, first at `N = 22` —
the same first counterexample the gamma-upper record found); and the sortedness device
is genuinely `J ≤ 13`-only (`14θ = 1.0526 > 1`). His result is not vacuous and not an
artifact of the sorted regime.

**Relation to the merged record, stated flat.** Claims 1–3, 8–10 are re-derivations of
what `cycles.md 12.8.6.1` (and `briefs/staircase-gamma-upper-findings.md` §3) already
prove — his contribution there is the *packaging* (the closed form
`maxgap = max(θ, 1 − Jθ)` for the unwrapped range, replacing the gap-multiset
argument's generality where it is not needed). Claims 4–6 (the Sturmian step sequence
at slope `L − 1`, with the ceiling identity and the complexity check) and 11–14 (the
`J = 13..25` plateau, the `J = 26` fall with its partition identity, and the quantified
cost of losing `θ ≤ ℓ`) are **new content, his**, verified here. Claim 5's "not `L`"
corrects nothing of ours — no record text states a slope; it corrects his own first
formulation, as his letter says.

### 4.2 The proposed `12.8.6.1` block — proposed here, `cycles.md` NOT edited

He asked for exactly this: the reformulation in the marked section of `12.8.6.1`, under
both names. The natural place is a fourth italic-marker paragraph inside Theorem
`12.8.6.1`, between *What is consumed.* and *Superseded formulation…* (matching the
page's existing marker style), with one sentence added to the *Verified* paragraph.
Proposed text, consistent with the merged wording (same `θ`, `ℓ`, `J`, window-count
conventions; nothing in the theorem statement or proof changes):

> *The rotation reformulation (Eric Merle with Ben Macindoe, round 12, 2026-07-30).*
> The proof above is a statement about the irrational rotation by `θ` on `ℝ/ℤ`, and two
> of its objects have names there. The step sequence `K(n+1) − K(n) ∈ {1, 2}` is the
> Sturmian word of slope `L − 1 = log_2(3/2) = 0.584963` (not `L`: mechanical words
> take slopes in `[0, 1]`, and `K(n+1) − K(n) = 1 + (⌈(n+1)(L−1)⌉ − ⌈n(L−1)⌉)`);
> letter-2 frequency `0.585` over the first `2000` steps, factor complexity
> `p(m) = m + 1` for `m = 1..12`, aperiodicity exactly the irrationality of `log_2 3`.
> And since `1/θ = 13.3000838`, for every `J <= 13` the points `{jθ : 0 <= j <= J}`
> have not wrapped and are already sorted, so `maxgap(J) = max(θ, 1 − Jθ)` **exactly**
> — giving `maxgap(12) = 0.0977500433` and `maxgap(13) = θ` with no three-distance
> machinery, and the sweep condition as `J >= (1 − ℓ)/θ = 12.2967`, i.e. `J = 13`.
> Beyond the sorted range the plateau is rigid (Merle): `maxgap(J) = θ` **exactly** for
> every `J = 13..25`, and it first falls at `J = 26`, to `14θ − 1 = 0.0526249495` — the
> points `j = 14..26` split the thirteen `θ`-intervals one at a time, each at offset
> `14θ − 1`, with `13(14θ − 1) + 14(1 − 13θ) = 1` identically. This prices the margin
> `ℓ − θ = 2.5157·10⁻⁴` (`0.33 %` of the arc): **losing `θ <= ℓ` is a cost, not a
> failure** — the sweep lengthens from `66` to `131` consecutive integers (`J = 26`),
> which the window `[L^p, 1.05·L^p]` first supplies at `p = 18` (`126` integers at
> `p = 17`, `199` at `p = 18`), moving the unconditional range from `p >= 16` to
> `p >= 18` and widening the finite check by two periods. Nothing in the theorem or its
> constants moves; this names the mechanism and prices its slack.

with the *Verified* paragraph gaining:

> `; the rotation facts and the `J = 26` plateau: `experiments/merle_r12_drift_check.py`
> (2026-07-30, 152 checks, 0 failures, two working precisions)`

Two notes for the main session. (i) The credit line above follows his request ("under
both our names") with the plateau result explicitly tagged his, which matches the
verification asymmetry: the reformulation and the `J = 26` result are his, the theorem
and the check are ours. If the page convention prefers the `12.8.6.4` credit style, an
equivalent form is a trailing "credit: the rotation naming and the `J = 13..25`
plateau are Eric Merle's (round-12 correspondence), verified here." (ii) The block is
also the natural home Merle's §9 asks for if the marked section is instead read as the
joint note's apparatus section — the text above is written to survive either placement
unchanged.

---

## 5. §10 — the silence: established, not assumed

### 5.1 What his round-11 item 2 actually claimed

Our record of his round-11 letter's four negatives is
`briefs/merle-r11-hygiene-check-brief.md` (the letter itself is not on file verbatim;
the brief's Half-2 list is the transcription the whole round worked from). Item 2,
verbatim from that record (line 21):

> **The rhythm of the peaks.** No memory, no clustering (variance/mean² **0.831**
> against controls 0.745–0.949), no spectral line (top peak **5.62×** variance against
> a control maximum of **6.64×**). Includes his own withdrawn false alarm: a lag-1
> autocorrelation of **−0.077** raised against an i.i.d. Gauss–Kuzmin null, which is
> the wrong null (the Gauss map makes consecutive partial quotients weakly dependent by
> construction). Recomputed against real continued fractions on a common footing, 1500
> terms each: `log₂3` −0.070, π −0.063, `log₂5` −0.104, `log₂7` −0.103.

So the item has **three sub-claims** (no memory; no clustering; no spectral line) plus
the withdrawn false alarm. One numbering note, flat: his round-12 §10 says "your
confirmation of my item-1 retraction covers the same detector" — in his own numbering
the autocorrelation retraction evidently sits with item 1 (the golden ratio); our brief
transcribed it inside item 2. Same retraction, same detector, no substance in the
difference; recorded so the two numberings cannot later be read as two events.

### 5.2 What our side did with it — the silence is real, and it is total on two of three parts

- **The memory sub-claim was verified**, on the corrected footing:
  `briefs/merle-r11-hygiene-check-findings.md` §6.1 rebuilt the four lag-1
  autocorrelations from scratch (all four reproduce to three decimals on `log aᵢ`;
  `log₂3`'s `−0.070` inside the control range, second smallest of four), and the sent
  reply carries that paragraph ("Your retraction is confirmed, on a common footing",
  `briefs/merle-round11-reply-draft.md` lines 436–450).
- **The clustering and spectral sub-claims were never touched.** The numbers `0.831`,
  `0.745–0.949`, `5.62×`, `6.64×` occur in exactly one file in this repository — the
  hygiene brief's transcription — and in no findings file, no script, no committed
  output, and no reply paragraph (swept by grep this session). The hygiene findings'
  §8.4 sentence "item 2 (the rhythm of the peaks) reproduce here" is, read strictly,
  **an overstatement of its own §6**: what reproduced was the retraction's
  autocorrelations and item 1's Gauss–Kuzmin fit; the two structural detector results
  of item 2 were not reproduced anywhere. Recorded as ours, flat.
- **The sent round-11 reply contains no sentence on item 2's conclusion** — no
  "rhythm", no clustering, no spectral, none of the four numbers (grep of the sent
  draft, this session). His §10 statement "appears nowhere in your letter — I checked
  the full text" is **CONFIRMED from our side**.

### 5.3 The three options, against what our record supports

His question is narrow: does the structural half ("no memory, no clustering, no
spectral line") survive the detector being wrong — retain, retain with a scope clause,
or strike?

1. **Retain as-is: not supported.** The conclusion was drawn with an instrument its
   author has disowned (the i.i.d. Gauss–Kuzmin null), two of its three clauses are
   unreplicated on our side, and the detector's spec (what counts as a "peak", the
   threshold, the normalisation behind `variance/mean²`, the spectral estimator) is
   not recoverable from our record — the same non-recoverability the `0.00103`
   had before his round-12 §5 resolved it. Retaining flat would put a disowned
   detector's conclusion at record grade.
2. **Retain with a scope clause: supported, with a split.** The **"no memory"** clause
   survives the detector's death *independently*: it was re-established on the
   corrected instrument (real continued fractions on a common footing) and replicated
   our side — that clause is not merely retainable, it is at two-keys-in-substance
   grade. The **"no clustering"** and **"no spectral line"** clauses are his
   measurements, unreplicated, and their printed control ranges (`0.745–0.949`,
   `6.64×`) cannot be re-read from our record because we cannot establish which null
   produced the controls — if the controls are real-constant CFs (as the ranges'
   plural suggests), the disowned-null critique may not even apply to them, but that
   is exactly what our record cannot say.
3. **Strike: not supported either.** Striking discards a replicated negative (the
   memory clause) and two descriptive measurements nobody disputes; the null-model
   failure he reported was in the *significance calibration*, and his own retraction
   plus our common-footing recomputation repaired that half rather than voiding it.

### 5.4 Recommendation

**Option 2, in exactly the `+0.22/−0.29/−0.57` shape** (the precedent:
`briefs/merle-r11-hygiene-check-findings.md` §7.2–7.3 and the sent reply's "recorded as
yours and unreplicated … those three numbers stand entirely on your side of the two-key
protocol and we will describe them that way wherever they are used"):

- the **memory clause** recorded as replicated on the corrected footing, both sides —
  citing the §6.1 table, not the disowned detector;
- the **clustering and spectral clauses** recorded as his, unreplicated, on his side of
  the ledger, with the detector spec named as the one thing that would change that: one
  clause each (peak definition + threshold; the null behind the control ranges;
  series length) and replication our side becomes a cheap statistics computation on the
  continued fraction of `log₂3`. Unlike round-11's item 3, **the stopping rules do not
  place this out of reach** — no cycle search is involved, and the README's
  equidistribution rule explicitly allows experiments to feed the ledger — so the
  honest answer to his "if your stopping rules place it out of reach, that is an
  answer" is: they do not; what places it out of reach today is the unrecoverable
  spec, which is his to supply if he wants the second key;
- the conclusion sentence itself ("no memory, no clustering, no spectral line")
  retained **with the scope clause**, not struck: one clause replicated, two his-side
  pending spec.

This is established from the record above, not assumed: the split between the three
clauses is forced by which numbers exist where, and the stopping-rule half was checked
against README's rules rather than presumed. Drafting the reply paragraph is the
response window's job, not this one's.

---

## 6. The two small corrections, verified and recorded

### 6.1 The 3,175 — his 3,100 is right, and the mechanism is ours to name

Re-verified independently in the fresh clones (read-only, scratchpad):

| fact | value | where |
|---|---|---|
| `git cat-file -s b55095a` (T1-chain `LegendreApprox.lean`) | **3,100 bytes** | his Lean repo at `d48ba9e` |
| newlines in blob `b55095a` | **75 LF, 0 CR**, file ends with LF | same |
| `git cat-file -s a4fae1f` (Junction-family copy) | **3,100 bytes**, 75 LF, 0 CR | `collatz-cycles-lean` clone |
| `3,100 + 75` | **3,175** | script 5.1 |

**Mechanism, named:** our figure came from a Windows working-copy measurement — with
CRLF conversion active at checkout, each of the 75 LF-terminated lines gains one `\r`
byte, and a 3,100-byte blob measures exactly 3,175 bytes on disk. Both copies were
measured that way, which is why `briefs/junction-public-recon-findings.md` prints
"(3,175 bytes each)": the *each* is faithful — the two blobs are the same size — and
the number is the inflated one for both. His "the one number of yours I could not
reproduce this round" is therefore correct and the correction is ours; nothing else in
that findings item moves (the blob identities, the two-line `open Real` diff, the
immateriality verdict, and the SHA-256 values are all statements about blob content and
are unaffected — indeed the recorded SHA-256 hashes are hashes of the *blobs*, which is
consistent, so the file mixed one working-copy measurement into an otherwise
blob-grade table; that is the whole defect).

**Drafted addendum for `briefs/junction-public-recon-findings.md` Item 3** (dated note,
original untouched, the main session applies at merge):

> *(Addendum 2026-07-30, ours: the byte figure two paragraphs up is a working-copy
> measurement, not a blob size. Both blobs are `git cat-file -s` = **3,100 bytes**
> (75 LF-terminated lines, no CR); under this machine's CRLF checkout each copy
> measures 3,100 + 75 = 3,175 bytes on disk, which is the figure printed. "Same size
> each" stands; the honest byte count is 3,100. Flagged by Merle, round 12; mechanism
> verified in fresh clones, `briefs/merle-r12-drift-check-findings.md` §6.1.)*

### 6.2 The §10.2 sentence — fifteen printed quotients, Jackson–Matthews cited for the 10,000

Verified at the **pinned** recon commit `collatz-cycles-lean` `1d77168`
(`docs/PROOF_ASSEMBLY.md`, section `### 10.2. Continued Fractions of $\log_2 3$`,
line 247), verbatim:

> The continued fraction expansion $\alpha = [1; 1, 1, 2, 2, 3, 1, 5, 2, 23, 2, 2, 1,
> 1, 55, ...]$ (OEIS A028507) has been computed to 10,000 terms (Jackson–Matthews
> 2002).

That display contains exactly **fifteen** partial quotients (`a₀ = 1` through
`a₁₄ = 55`, then an ellipsis), and they are the correct first fifteen of `log₂3`; the
10,000 is a *reported computation*, cited to Jackson–Matthews 2002 (the reference
resolves in the same file, line 407: T. H. Jackson, K. R. Matthews, *J. Integer Seq.*
**5** (2002), Article 02.2.7). **His correction is confirmed in every particular.**

**Which sentence of ours overstated it:** `briefs/junction-public-recon-findings.md`
§5.2(iv), line 762 —

> with §10.2 giving the CF of `log₂3` to 10,000 terms (citing Jackson–Matthews 2002,
> OEIS A028507),

which reads as the file *supplying* 10,000 terms. It prints fifteen and attributes the
10,000-term computation. Our sentence had the citation present but attached to the
wrong role. His own clause stands with it: our point about §10.5 (the
convergent-confinement antecedent) is unaffected either way.

**Drafted correction** (same treatment — dated addendum for the main session, original
untouched):

> *(Addendum 2026-07-30, ours: "giving the CF of `log₂3` to 10,000 terms" overstates
> the file — §10.2 prints **fifteen** partial quotients, `[1; 1, 1, 2, 2, 3, 1, 5, 2,
> 23, 2, 2, 1, 1, 55, ...]`, and cites Jackson–Matthews 2002 for the 10,000-term
> computation. Verified at the pinned `1d77168`. Flagged by Merle, round 12; the §10.5
> point this section makes is unaffected.
> `briefs/merle-r12-drift-check-findings.md` §6.2.)*

(For completeness: `collatz-cycles-lean` HEAD has moved to `b38758d` — his three
round-12 retraction-marker commits over the pin; the §10.2 sentence is byte-identical
at HEAD, checked incidentally. The junction-followup window owns those commits; nothing
further is claimed here.)

---

## 7. Compliance and counts

- **Checks: 152 (76 distinct × 2 precisions), 0 failures**; verdict lists identical at
  dps 120 and 240; committed output regenerated via raw redirection — no BOM, pure
  ASCII (verified byte-level before commit).
- Read-only outside this repo: three scratchpad clones (SHAs in the header), zero
  interaction of any kind with either of his repositories or the shared repo beyond
  `git clone`/`cat-file`/`show`.
- `HANDOFF.md`, `cycles.md`, and every existing findings file untouched; all
  corrections drafted here only. No key turned, no ledger text pushed, no reply
  paragraph drafted beyond the two marked correction blocks and the proposed
  `12.8.6.1` block.
- Stopping rules: verification and record repair throughout; the one place a new
  computation was considered (§5.4's replication of the clustering/spectral detector)
  is recorded as *permitted but blocked on his spec*, and was not run.
- `experiments/encoding_scan.py`: **RESULT: CLEAN** (run before the final commit).
- One number in this file that could not be verified at a named place: none.
