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
