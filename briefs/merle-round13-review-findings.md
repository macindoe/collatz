# Findings: round-13 review window — PR #3 verification, peak replication, section-96 reconstruction, paperwork drafts

Brief: `briefs/merle-round13-review-brief.md`. Branch **`merle-round13-review`**.

**Base SHA: `7d6d00fda4bba3d3cf80650765ab3e6111ddeced`** ("briefs: round-13 review
brief ..."). The worktree was cut at the stale `cbf8dae`, missing this brief,
and was fast-forwarded to `7d6d00f` by `git merge main --ff-only` before
anything was read, per the brief's own setup step. `7d6d00f` is local
`main`'s tip at session start and is the expected tip named in the launch
instruction.

Register: flat, calibrated prose. Every number carries its named source or
this session's own derivation; where a source disagrees with the brief, the
source wins and the disagreement is recorded (one instance below, §2). Every
defect found in Merle's material is a finding delivered kindly, in the
register of his own two round-12 reviews (quoted in full, §1).

---

## 1. State check (Queue 1)

**Fresh scratchpad clones, read-only** (`git clone`, no fork/issue/star/
watch/comment/push, no interaction with any repository beyond the clone and
`gh` reads):

| repo | expected HEAD | actual HEAD | status |
|---|---|---|---|
| `macindoe/one-obstruction-three-faces` | `308d6bb` | `308d6bb2ccae18fabcf87ca0b91164a47d9340a2` | **MATCH** |
| `ericmerle3789/one-obstruction-three-faces-lean` | `d48ba9e` | `d48ba9e4f941559b1adb42c57b140ad7e846471d` | **MATCH, unmoved** |
| `ericmerle3789/Collatz-Junction-Theorem` | new to record | `a57d29e7c062e6c614ebca4dc0875f70065561a9` (`main`) | recorded (see §4 — the retraction commit is NOT on this branch) |

Branches on the shared repo, confirmed: `round-13` at `ef1742d` (exact match
to the brief's PR #3 pin), `note-v1-draft` at `96ccadf` (merged, now part of
`main`'s history), `round-12` at `accda4b` (merged). All as expected; nothing
has moved beyond the brief's own Provenance.

### 1.1 PR #3 body, verbatim (`gh pr view 3`, read-only)

> Round-13 reply to round-12. Accepts the L-A9 grade-line correction
> (verified independently: c\*=0.9617 is the linear-form exponent, floor 1,
> μ=c+1, margin ~0.038 — the razor, not ~1.04). Applies h1–h4 to the claim
> block, accepts h5. Closes the Rhin warning on my side (BILAN_R201 R201-I3
> retracted in place). Supplies the item-2 peak-detector spec with the i.i.d.
> null flagged. Offers §96 (finiteness of quotient) for the 2-adic face.
> Second key = approving review, per PROTOCOL §13.

`baseRefOid: 308d6bb`, `headRefOid: ef1742d28928a0850325686a4c5693fe3ed41d28`,
state OPEN — all confirmed via `gh pr view 3 --json`.

### 1.2 His PR #1 review, verbatim (the round-12 second key, `gh pr view 1 --json reviews`)

> Second key — approving review (round-12, per PROTOCOL §13).
>
> Verified independently on my side, fresh computation:
>
> - §2 (L-A9 attack): CONFIRMED. c\* = 0.961722 cannot be a measure (a
>   measure is always ≥ 2; 0.96 is meaningless), so it is the linear-form
>   exponent, floor 1; the identity μ = c + 1 holds exactly, and in either
>   single convention the margin is 0.0383 — the razor you name, not the
>   ~1.04 my pairing read as. My grade line was wrong; the conclusion holds
>   and strengthens. I accept offer h1 (applied in round-13). The 'dream
>   c=2' deficit of 7159 is at k^3 (μ=3); at the true Dirichlet dream (μ=2,
>   k^2) it is a small factor, as you say.
>
> - §3 (Rhin): CONFIRMED and I withdraw my round-11 warning. Simons–de
>   Weger's Λ > e^{−13.3(0.46057+ln K)} is exactly const·K^{−13.3} (checked
>   to 20 digits) — a height-exponent linear-form bound, not a (log)² shape.
>   The Lean rule stands; BILAN_R201's 'PROUVÉ' is the artifact to retire,
>   which I am doing on my side.
>
> - §4, §5, §7, §8: accepted as recorded. The regime column (§4(d) →
>   PROTOCOL.md) is approved.
>
> Diff is exactly three files, additions only, nothing deleted from L-A9.
> Approving.

State: APPROVED, `2026-08-17T15:06:36Z`, commit `accda4b47c407ea1b2dfdfc5c01b6ad79784ce9b`.

### 1.3 His PR #2 review, verbatim (the note's second key)

> Second key — the two-page note, first version. Facts re-verified on my
> side: Hercher 704 < 1536 = 3·2⁶⁹ < 2048 = 2⁷¹; the staircase γ band
> 3.683012–5.140212; the ccchallenge entries; and the L-A9 δ8 paragraph,
> which carries the corrected razor (μ\* = c\*+1 ≈ 1.96 against the
> Dirichlet floor 2) and now matches the LEDGER.md headline fixed in PR #3
> (round-13). Attribution correct throughout; no over-claim (excludes
> nothing beyond cited ranges). Approving.

State: APPROVED, `2026-08-17T15:14:39Z`, commit `96ccadf889e5466eba81dddab953fbf45de994d3`.

Note (flat, for the record): his PR #2 review already forward-references PR
#3's fix ("matches the LEDGER.md headline fixed in PR #3") — the two rounds
were reviewed within eight minutes of each other on his side.

### 1.4 The round-13 diff, exact shape

`git diff 308d6bb..round-13 --stat` (in the shared clone):

```
LEDGER.md                           |  12 +-
briefs/merle-breach-campaign-map.md |  85 ++++
rounds/R13-merle.md                 | 142 ++++
3 files changed, 235 insertions(+), 4 deletions(-)
```

Matches the Provenance's `+8/−4` characterization of the LEDGER hunk closely
enough to confirm no drift (the Provenance's own count was approximate;
`git diff --stat`'s `12 +-` is the authoritative figure and is recorded here
rather than disputed against the rounder Provenance number).

---

## 2. The LEDGER co-edit, number by number (Queue 2)

Fresh code: `experiments/merle_r13_check.py` (Parts 0–4), 25 checks in this
section, 0 failures. Full output: `experiments/merle_r13_check_output.txt`.

**c\*, μ\*, the single-convention margin.** Re-derived from the clean-room
chain (`c* = ln(3·X₀ − K_H)/ln(K_H) − 1`, X₀ = 2⁷¹, K_H = 1.375·10¹¹):
`c* = 0.961722`, `μ* = c* + 1 = 1.961722`. Margin in the linear-form
convention (floor `c ≥ 1`): `0.0383`. Margin in the measure convention
(floor `μ ≥ 2`): `0.0383` — **identical**, verified as a structural fact
(not a numeric coincidence): shifting the exponent and its floor by the
same `+1` leaves the gap between them unchanged. Both LEDGER text and
Merle's PR #1 review state `0.0383`; both confirmed to six decimal places.

**The at-the-floor factor: 2.9 vs 2.93, reconciled.** The LEDGER's h1-applied
claim block says "the window would still stay open today by a factor `2.9`
on `k`"; the same LEDGER paragraph's h2-applied deficit sentence and
`merle-la9-check-findings.md` §4.2 say `2.93`. Recomputed at `μ=2,
κ=1/√5` (the Hurwitz constant): `k_max = 4.6859·10¹⁰`, ratio to `K_H` =
**2.9343**. `round(2.9343, 1) = 2.9`; `round(2.9343, 2) = 2.93`. **Not a
discrepancy** — one decimal place of rounding on the identical figure.

**The true-dream deficits at `μ=2`.** At `κ=1`: `k_max = 7.0071·10¹⁰`,
ratio `1.9623` (LEDGER/la9-findings: `≈2`, `1.96`), missing computation
`2^1.9451` (LEDGER: "`2^1.95`... `~2^2`" — both consistent, the LEDGER's own
`~2^2` is itself a stated rounding). At the Hurwitz constant: missing
`2^3.1060` (LEDGER/la9-findings: `2^3.11`). All confirmed to four
significant figures.

**Salikhov's `c=5.125`.** Standing record (`briefs/merle-la7-mu-check-
findings.md` §2.1, read this session, not re-fetched from the web since the
literature adjudication there is already primary-sourced): Salikhov 2007
(*Dokl. Akad. Nauk* **417**, no. 6) proves `μ(ln 3) ≤ 5.125 = 41/8` exactly —
an irrationality measure of the single number `ln 3`, not of `log₂3`, and
not a linear-form statement at all. `41/8 = 5.125` confirmed exactly as a
`Fraction`; `ln(3) ≈ 1.0986` and `log₂3 ≈ 1.5850` confirmed numerically
distinct. The LEDGER's parenthetical citation is unchanged by round 13 and
needed no correction; this session's check simply reconfirms the standing
adjudication rather than re-opening it.

### 2.1 The h4 numbers: re-measured, and a Provenance correction

The brief's Queue 2 describes the h4-applied numbers — the extended chord
`0.5001` to `2^2000`, the 30-bit local-slope floor `0.32`, and the `μ >
~2.05` widening threshold — as **"NEW numbers with no prior record on our
side"** and asks for independent re-measurement rather than transcription.

Re-measured with fresh CF/Crandall-jaw code (exact-integer Euclid on
`log₂3` at `dps=5000`, a stability canary against `dps=7000` agreeing on all
1600 probed terms — well past the 1171 terms needed to reach `2^2000` — and
a fast log-domain `k_min` evaluator cross-checked against an exact
`Fraction` evaluator to `1e-9`): **all three reproduce exactly** — chord
`0.500066` (rounds to `0.5001`), 30-bit floor `0.3229` (rounds to `0.32`),
400-bit floor `0.4867` ⟹ `μ > 2.0548` (rounds to `2.05`).

**Correction, recorded per the Rules' disagreement clause: the Provenance's
characterization is not accurate.** These three numbers are not new; they
are the exact figures `experiments/merle_la9_check.py`'s own PART 3 already
printed in the la9-check session (`full chord alpha ... = 0.5001`, `width
30 bits: min 0.3229`, `width 400 bits: min 0.4867`), and offer h4
(`merle-la9-check-findings.md` §6.4) drafted its wording directly from that
output. Merle's round-13 LEDGER text applies offer h4 near-verbatim — this
is our own prior computation being returned to us through his co-edit, not
independent verification of a fresh claim. This is not a defect in Merle's
material (he applied the offer exactly as given, in good faith); it is a
precision correction to the brief's own Provenance section, and the
re-measurement above stands as an honest independent re-derivation
regardless of the correction — it would have been worth doing even had the
Provenance been accurate.

---

## 3. The h5 gap (Queue 3)

**Confirmed: h5 is accepted in words but not applied.** The round-13 diff
touches only the L-A9 section (`LEDGER.md` lines ~432–456 in the shared
repo); no hunk touches the L-A8 `(d-bis)` block. Read directly: the L-A8
block's offer-g discharge paragraph still ends "... the 200-draw control
added — median 2, maximum 53, and **0 of 200 reaching 306**" — the exact
sentence offer h5 was drafted to replace. The L-A9 acceptance sentence
("**h5** (the seed-free census line) is accepted for the L-A8 (d-bis)
block") is real and present, but it is an acceptance-in-place-of-nowhere: it
lives in the L-A9 section and points at a change that was never made.

**Verified independently:** offer h5's text (`briefs/merle-la9-check-
findings.md` §6.4) — "among all 199,999 `n < 200000`, 897 (0.45%) have
smallest Ostrowski denominator ≥ 306; all ten eps-small `n` do (median 15601
against a population median of 2)" — reproduces exactly against
`merle_la9_check.py`'s own committed run (this session re-read that script's
committed output rather than re-running it, since Queue 3 does not ask for
recomputation and the figure is already independently keyed on our side).

**Disposition recommended.** This is a one-line, already-agreed, low-stakes
fix — not a case where the review should silently apply someone else's
accepted text mid-PR (that would blur who wrote what), nor one that should
block approval (nothing substantive is wrong; the census sentence is
strictly *stronger* evidence than the sentence it would replace, and the
weaker sentence currently in place is not itself false). **Recommended:
raise it plainly in the review as an open item for him to apply before
merge — his own text, already agreed, a one-line change** — with the
fallback, if that is inconvenient this round, of carrying it explicitly to
the next round rather than letting the acceptance sentence stand as if
already discharged. The review draft (§7 below) raises it this way.

---

## 4. The Rhin retraction, at its address (Queue 4)

**Fresh clone, read-only, of `ericmerle3789/Collatz-Junction-Theorem`.**

**Commit `77e3f07` exists.** It is the tip of branch `origin/proof-assembly-
v1` — **not** of `main` (main's tip is `a57d29e`, "Archive notice:
consolidation to collatz-nocycle-lean4", dated 2026-04-22, which predates
`77e3f07` by four months and does not contain it; `git merge-base 77e3f07
a57d29e` returns `6d30395`, the original BILAN_R201 commit both branches
share). This is recorded flat, not disputed: the retraction is real,
correctly committed, and exactly where Merle's letter says it is
("`Collatz-Junction-Theorem` at `77e3f07`") — but a reader following that
repository's own README (which points to `collatz-nocycle-lean4` as "the
active repo" and says "no further commits to this repo are planned") would
not discover it without knowing to check the `proof-assembly-v1` branch by
name. Not a defect in the retraction's substance; a locatability note, worth
one sentence in the review.

**The three claims, checked against the commit's own diff** (`f5ba6ce`,
"Retract R201-I3", is the substantive retraction; `77e3f07` is a follow-up
pass stamping two remaining unmarked restatements):

1. **R201-I3's "PROUVÉ" verdict retracted in place: CONFIRMED.** The formal-
   results table row now reads `**~~PROUVÉ~~ [RÉTRACTÉ 2026-08-17 — faux ;
   voir tête de fichier]**`; a new header block (`## ⚠️ RÉTRACTATION
   PARTIELLE`) states plainly "Il est faux, et sa prémisse est fausse" and
   gives the corrected mechanism in the file's own words (quoted in full
   below).
2. **Nothing deleted: CONFIRMED by inspecting the diff directly, not by
   trusting the commit message.** `f5ba6ce` is `+40/−6`; every one of the
   six removed lines is matched, in the same hunk, by an added line carrying
   the *same original text* plus a `~~strikethrough~~`/bracketed retraction
   marker — annotative, not destructive, checked line by line. `77e3f07`
   (`+2/−2`) is the same pattern on the two remaining unmarked instances.
3. **L-A7 named as the cross-adjudication: CONFIRMED**, in both the commit
   message ("Cross-adjudicated in the shared repository's LEDGER
   (macindoe/one-obstruction-three-faces, L-A7, round-12 Rhin re-source
   record), verified on both sides.") and the file's own new header block
   ("Adjudication croisée : `LEDGER.md` du dépôt partagé
   `macindoe/one-obstruction-three-faces`, entrée L-A7, « Macindoe
   adjudication record (round-12 Rhin 13.3 re-source warning) », vérifiée
   des deux côtés.").

**The retraction text, verbatim** (`research_log/BILAN_R201.md` at
`77e3f07`, the header block):

> **Le verdict R201-I3 (« C' ~ 13.3 MAL ATTRIBUÉ à Rhin 1987 », marqué
> PROUVÉ) est RÉTRACTÉ.** Il est faux, et sa prémisse est fausse.
>
> - **Ce qui a été affirmé.** Que Rhin 1987 ne traite que des mesures
>   d'irrationalité, pas des formes linéaires en deux logarithmes ; donc que
>   13.3 lui est mal attribué, la vraie constante étant 18.5–23.55 (Laurent
>   2008 / LMN 1995).
> - **Pourquoi c'est faux.** Rhin 1987 (*Progress in Math.* 71, Proposition
>   p. 160) prouve **les deux** : des mesures d'irrationalité **et** une
>   mesure d'indépendance linéaire effective de `1, log 2, log 3`, donnant
>   `|u₀ + u₁·log 2 + u₂·log 3| > H^(−13.3)` avec `H = max(|u₁|,|u₂|)` — une
>   borne de forme linéaire couvrant `(log 2, log 3)` directement. [...]
> - **Ce qui, dans le déclencheur, était réel.** R200 avait écrit la
>   constante de Rhin dans la forme `(log)²` de LMN
>   (`exp(−13.3·(log S)²)`) — *cette transcription-là* n'est pas de Rhin.
>   L'auditeur a rejeté l'**attribution** là où le vrai défaut était la
>   **transcription**.
> - **Statut.** Le 13.3 tient pour ce que la chaîne L-A7 consomme. Aucun
>   nombre engagé ne bouge.

This matches, sentence for sentence, the mechanism `merle-la7-rhin-check-
findings.md` established independently in this project's own round-12
adjudication (§3 there: "the audit caught a genuine misuse and filed it
under the wrong statute... drop the square [from R200's transcription] and
the statement is Rhin's, verbatim"). **This closes the last open item of
the round-11 warning** — the round-11 Rhin warning is now withdrawn on both
sides, with matching mechanisms independently arrived at; the `HANDOFF.md`
L-A7 line should carry this (done, §9 below).

---

## 5. The peak-detector spec and the corrected null (Queue 5)

Fresh code: `experiments/merle_r13_peak_replication.py`, 17 checks, 0
failures. Full output: `experiments/merle_r13_peak_replication_output.txt`.

### 5.1 Replication (Queue 5a)

Own CF code, `dps=5000` vs `dps=7000` stability canary (agreeing on 1900
probed terms for every constant used, comfortably past the `N=1800` cap),
`S=10`:

| statistic | his figure | this session | match |
|---|---|---|---|
| peak count | 250 | 250 | **exact** |
| mean gap | 7.19 | 7.1888 | **exact** |
| clustering (P4) | 0.831 | 0.8314 | **exact** |
| spectral (P3) | 5.62× @ f=124 | 8.48× @ f=254 | **not pinned** |

The three-way exact match on peak count, mean gap and clustering is strong
evidence the underlying partial-quotient sequence and the peak/gap
bookkeeping are identical to his. The spectral mismatch is therefore read as
an **estimator-convention gap, not a data gap**: "highest Fourier
coefficient of the centred peak-indicator, in units of its variance" admits
more than one reasonable periodogram normalisation and search-range
convention, and this session's own (a standard Fisher-g-style periodogram,
full range `f=1..900`, documented in the script) does not reproduce his
exact number. This matches a prior finding on the same detector
(`merle-r12-drift-check-findings.md` §5.2: "the spectral estimator... is not
recoverable from our record") — true again even with the fuller R13 §5
prose spec. The qualitative claim ("a spectral line clearly above noise")
replicates; the exact figure does not, and this session's own definition is
used consistently throughout, which is what the corrected-null comparison
actually needs.

**The i.i.d. control band, at n=300 rather than 5:** clustering `[0.6198,
1.2576]`, spectral max `10.85×` (his 5-draw, unseeded figures: `[0.745,
0.949]`, `6.64×` — both consistent with, well inside, this session's
much larger ensemble; not chased exactly, per the brief).

### 5.2 The corrected null (Queue 5b)

Precedent located (`briefs/merle-r12-drift-check-findings.md` §5.1, grepped
for "corrected footing"): the memory-clause recomputation replaced the wrong
i.i.d. null with real continued fractions — `log₂3, π, log₂5, log₂7` — "on a
common footing", same term count, same statistic, no seed to chase. Mirrored
here with the same discipline: same `S=10`, each constant's own two-
precision stability canary (Part 0 of the script), capped at the same
`N=1800`.

**Widened beyond the brief's named three** (`log₂5, log₂7, π`) **to six**,
per the brief's own invitation ("any further constants you judge useful;
state the choice"): three points make too thin a band to call anything
"inside" or "outside" with any confidence. Added: `ln2, γ (Euler–
Mascheroni), ζ(3)` (Apéry's constant) — all with no known non-generic
continued-fraction structure. **Deliberately excluded, and the reason
recorded rather than silently dropped:** `e = [2;1,2,1,1,4,1,1,6,...]` has
an explicit, fully regular, unbounded partial-quotient pattern — not
Gauss-Kuzmin-typical at all. Tried first as a sanity check: it gave
clustering `0.0000` and spectral `891×` — a real periodicity, useful as a
**positive control** confirming the estimator correctly flags genuine
structure when it is present, but the wrong kind of number for a "generic
irrational" comparison band. `√2, √3` were also tried and rejected: as
quadratic irrationals they are eventually periodic with bounded partial
quotients (Lagrange's theorem) — `√2`'s continued fraction is literally all
`2`s after the first term — guaranteeing **zero peaks** at `S=10` by
construction, the opposite of generic.

**Results, all six real constants plus `log₂3`:**

| constant | peaks | mean gap | clustering | spectral |
|---|---|---|---|---|
| log₂3 | 250 | 7.189 | 0.8314 | 8.479× @ f=254 |
| log₂5 | 230 | 7.751 | 0.6456 | 7.436× @ f=832 |
| log₂7 | 235 | 7.641 | 0.8698 | 8.117× @ f=415 |
| π | 253 | 7.127 | 0.9020 | 6.809× @ f=537 |
| ln2 | 227 | 7.801 | 0.7159 | 7.042× @ f=862 |
| γ | 259 | 6.903 | 0.7233 | 6.843× @ f=394 |
| ζ(3) | 222 | 8.023 | 1.2214 | 6.449× @ f=573 |

**Verdict, stated flat, both statistics, using rank tests rather than a
blunt min-max containment check** (with only 6–7 points, a single extreme
value is trivially "outside" a band that excludes it by construction — the
calibrated question is whether its rank is surprising):

- **Clustering: a clean non-finding.** `log₂3` (`0.8314`) sits inside the
  6-constant min-max band (`[0.6456, 1.2214]`) and is rank 4 of 7 — squarely
  unremarkable. The "no clustering" clause **survives** the corrected
  footing, matching the memory clause's own earlier disposition.
- **Spectral: genuinely marginal, reported flat rather than forced either
  way.** `log₂3` is the single *highest* of the 7 exchangeable values (rank
  1; one-sided `p = 1/7 ≈ 0.143` under a pure-chance/exchangeability null —
  unremarkable at any conventional significance threshold, but not a clean
  "comfortably mid-band" result the way clustering is). Two facts anchor the
  reading: it is not remotely close to the positive control (`e`'s `891×`,
  two orders of magnitude clear — this is not a real spectral line by that
  yardstick), and it is only `4–5%` above the next-highest real constant
  (`log₂7` at `8.117×`), a gap fully consistent with ordinary sampling
  variation at this series length. **Net reading: no evidence of a genuine
  spectral line, and the "no spectral line" clause is not falsified — but
  it is a softer non-finding than clustering's, and the review states both
  the "survives" and the "not as clean" readings rather than picking one.**

**Draft ledger wording** (offered for the item-2 entry, his side, "yours to
key once replicated" per the R13 letter — the key recommendation is the
main session's and the author's, not this session's):

> Replicated independently (fresh continued-fraction code, dps=5000/7000
> stability canary, N=1800, S=10): peak count 250, mean gap 7.19, clustering
> 0.831 — all reproduce to the reported figures. The i.i.d. Gauss-Kuzmin
> null is confirmed wrong (as you flagged) and replaced with real continued
> fractions on a common footing (6 constants: log₂5, log₂7, π, ln2, γ,
> ζ(3), same protocol). Clustering: log₂3 (0.831) sits cleanly inside the
> resulting band ([0.646, 1.221]), rank 4 of 7 — the non-finding survives
> the corrected footing. Spectral: MARGINAL, reported flat — log₂3 (8.48×)
> is the single highest of 7 values (rank 1, one-sided p=0.14, unremarkable
> at this sample size but not a clean mid-band result either); a positive
> control (e's regular partial-quotient pattern) gives 891× on the same
> estimator, two orders of magnitude clear, so log₂3's value is nowhere near
> a genuine spectral line by that yardstick. One estimator note: our
> spectral statistic's exact normalisation does not reproduce your reported
> frequency=124/5.62× pair even though it reproduces P4 exactly — the
> spectral windowing convention is under-specified in the prose spec and
> independent replications may land on different numbers; the qualitative
> reading (log₂3 unexceptional, not a genuine spectral line) is robust to
> this, the exact figure is not.

---

## 6. The map and section 96 (Queue 6)

### 6.1 Section 96, reconstructed (not reproduced)

Fresh code, `experiments/merle_r13_check.py` Part 7. His artifacts
(`run_048.py`, `run_049.py`) are local and unpublished and were not seen.

**The telescoping step, written out** (per the brief's instruction): for
`V(x) = x·f(x mod 2^k)` to be strictly decreasing under one accelerated
step `x → (px+1)/2^v`, and writing `g = log f`, the large-`x` approximation
gives `(log p − v·log 2) + g(r') − g(r) < 0` at every edge `(r, v, r')` of
the residue graph (`r = x mod 2^k`). Summed around a directed cycle
`r₁ → ... → r_L → r₁`, the `g`-terms telescope to exactly `0`, leaving the
necessary, `f`-independent condition `Σ(log p − v·log 2) < 0`, i.e.
`p^L < 2^K` (`K = Σv_i`, checked as an exact integer comparison — no
floating point anywhere in the faulty/not-faulty classification). A cycle
failing this ("faulty") obstructs *every* choice of `f`.

**Reproduces cleanly at `p=7, k=8`** (his own worked example): 4 distinct
residue cycles (the graph is a deterministic function, so this is a
complete enumeration, not a search), lengths `1, 3, 4, 31`; 3 faulty
(`K=67` vs `p^L≈1.58·10²⁶` at `L=31`; `K=8` vs `2401` at `L=4`; `K=4` vs
`343` at `L=3`). A genuine-closed-orbit search (does any actual integer
close a real period-`L` orbit, `X_L = X_0` exactly, not merely a matching
residue pattern — see the operational-definition note below) up to
`x0 < 500,000–770,000` per cycle finds **none beyond the trivial fixed
point `x=1`** — **100% phantom, matching the campaign map's own figure.**

**Does NOT reproduce at small `k` for `p=3`.** No faulty cycles exist at
all for `k=4..9` (only the trivial fixed point). Faulty cycles first appear
at `k=10` (one cycle, `L=26`), persist at `k=11,12`, then **vanish again**
at `k=14, 16` — non-monotonic in `k`. Where they do appear, the same
genuine-closed-orbit search again finds only phantoms (up to ~2 million).
**Offered interpretation, not verified further:** `log₂3`'s closeness to
low-height rationals — the same closeness the entire L-A9 front is built on
— makes `p^L` vs `2^K` a near-tie at small scale for `p=3`, so "faulty"
status is fragile in `k`; `log₂7 ≈ 2.807` sits nowhere near such a tie, so
faulty cycles appear immediately and robustly at `k=8`. This is a plausible
mechanism, offered as an observation for the review, not a proof.

**Operational definitions guessed, recorded flat as gaps (per the brief's
own instruction):**

1. The residue-graph transition (`r → (p·r+1)/2^v mod 2^k`, canonical
   representative only) is shown algebraically to diverge from the true
   quotient dynamics once `v > 0` (a real integer `x = r + m·2^k` reaches a
   *different* next residue depending on `m`, once `v > 0`) — this is
   exactly why a faulty residue cycle need not correspond to any real
   integer trajectory; it is the mechanism the phantom/real distinction
   exists to probe, not an incidental modelling limitation.
2. "Edge realizable" was interpreted, and tested at 20,000 random edges per
   `(p,k)` pair (matching Merle's own reported figure), as: some actual
   integer reaches the designed target residue with the designed
   valuation. This is **true by construction** at the `m=0` lift for every
   edge, so the check (100% pass, every time) is a tautological
   well-formedness confirmation of the graph, not independent evidence —
   recorded as such rather than oversold.
3. "Phantom" was tested as: no actual integer in a bounded search closes a
   genuine period-`L` orbit (`X_L = X_0` exactly). A weaker test — the
   residue *pattern* merely recurring once along some real trajectory,
   without the value itself returning — was considered and rejected as the
   criterion, because for a faulty cycle the real value necessarily grows
   by the very factor `p^L/2^K > 1` that makes it faulty; a residue match
   at step `L` does not mean the integer returned, only that its residue
   class did.
4. All searches are bounded (up to a few hundred thousand to ~2 million per
   cycle); "phantom" is reported relative to that bound, not as a proof of
   non-existence for all integers.

### 6.2 The `θ=1` Cramér–Lundberg boundary

Confirmed exactly by bisection (`p=3`: `θ = 1.000000000000`) and directly
by algebra (`(p+1)/2 = 2 ⟺ p = 3`, no floating point). **Strengthened
beyond the map's own "θ<1 at p=5,7" framing:** at `p=5,7` no nontrivial
positive root exists **at all** — `f(θ) = (p/2)^θ + (1/2)^θ − 2` has
`f'(0) = ln(p/4) ≥ 0` there, so the convex function never dips below its
trivial root at `θ=0` again. Traced to the mean log-step drift
`0.5·ln(p/2) + 0.5·ln(1/2)` changing sign: negative at `p=3` (`−0.1438`,
walk drifts down, finite excursion max) and positive at `p=5` (`+0.1116`,
walk drifts up, infinite excursion) — a cleaner mechanistic explanation of
"finite at `p=3`, infinite at `p=5,7`" than a bare `θ<1` comparison, offered
for the review. **Scope, carried forward:** the surrounding claim that the
excursion tail is exactly `R^{−θ}` under the §75 bijection rests on Merle's
local artifacts and is **not** independently checked here, per the brief's
own instruction.

### 6.3 The two ✓ cross-domain facts

Both verified with fresh code. `2^n ≡ 2 (mod 3)` for every odd `n`, checked
`n=1..4999`, 0 mismatches; `n=0,2,8` confirmed even. The sieve density
formula `(1/2)(2/3)^{k−1}` reproduces `99.743%` decided at `k=14` exactly —
**the closed-form arithmetic is confirmed; the combinatorial sieve argument
that produces this density from `2^n`'s base-3 digit structure is Merle's
own local construction and was not independently reconstructed here**, a
scope boundary matching the `θ=1` note above, recorded rather than glossed.
`log₃2 = 1/log₂3 = 0.630930` confirmed. The `x*=7/3` identities: `(3+3/7)/
(3−3/7) = 4/3` confirmed exactly as a `Fraction`; `log₂(4/3) = 2 − log₂3`
confirmed as an identity (agrees to `1e-12`, and is in fact an algebraic
tautology, `log₂4 − log₂3 = 2 − log₂3`, not an approximation).

`aeh.md` 13.6.7 checked against the map's citation: exists, and the "one
missing genre of theorem" phrase the map's closing paragraph quotes is
present verbatim in that section (checked directly against the wiki page
this session, not reproduced here since it is unchanged and already
public).

### 6.4 The grading tension, adjudicated

Confirmed as flagged in the brief's own Provenance: the map's header says
"Everything here is **Merle-side, one key**" in the same paragraph as "Two
items are theorem-grade and **verified cross-side this round (⊢)**" — and
cross-side verification of the two ⊢ items (§96, `θ=1`) is exactly what
this session has just done a *first pass* of, not what had already happened
before the map was written. The wording overclaims its own timing.
**Proposed fix, one sentence, for the review:** replace "verified cross-side
this round" with **"offered for cross-side verification this round"** — the
map is dated before this review's own §96/`θ=1` checks existed, so
"verified" should record an invitation being taken up now, not a fact
already established when the map was drafted. (This session's own
reconstruction partially discharges the invitation for §96 at `p=7,k=8`,
and records where it does not — see §6.1 — so after this review the
sentence could honestly read "verified cross-side" for the `p=7` instance
specifically, with the `p=3` non-reproduction and the four operational
gaps carried alongside it; that finer wording is offered as an option in
the review draft below rather than mandated.)

---

## 7. The round's paperwork (Queue 7)

### 7.1 The review draft

*(Full text, for the author to post as PR #3's approving review, verbatim
or edited. Register mirrors his own two round-12 reviews: verified-
independently facts first, then the keys the review turns, then the raised
items.)*

> Second key — approving review (round 13, per PROTOCOL §13).
>
> Verified independently on my side, fresh code throughout (two scripts,
> `experiments/merle_r13_check.py` and
> `experiments/merle_r13_peak_replication.py`, 70 checks total — 53 + 17 —
> 0 failures):
>
> **§1 (L-A9, h1–h4).** CONFIRMED, to six decimal places. `c* = 0.961722`,
> `μ* = 1.961722`; the margin is `0.0383` in both single conventions
> (verified structurally, not just numerically — shifting the exponent and
> its Dirichlet floor by the same `+1` leaves the gap invariant). The h1
> factor "2.9" and the h2/la9-findings "2.93" are the same number
> (`2.9343...`) at different rounding, not a discrepancy. The true-dream
> deficits at `μ=2` reproduce exactly (`1.96×`/`2^1.95` at `κ=1`,
> `2.93×`/`2^3.11` at Hurwitz). One correction, kindly: the h4 numbers
> (chord `0.5001`, 30-bit floor `0.32`, `μ>~2.05`) are not new — they are
> exactly what our own `merle_la9_check.py` printed and offer h4 quoted;
> re-measured fresh anyway (independent CF code, dps=5000/7000 canary,
> stable to `2^2000`), and they still reproduce exactly. **The Dirichlet
> half turns two keys as unconditional theorem-grade, single-convention;
> the scissors half stays measured, permanently, on the wider regime — as
> you turned it.**
>
> **§2 (Rhin, `77e3f07`).** CONFIRMED. The commit exists, its diff is
> purely annotative (every deleted line matched by the same text plus a
> retraction marker, checked line by line, nothing removed without
> replacement), and it names our L-A7 record as the cross-adjudication in
> both its commit message and the file's own new header. One flat note:
> `77e3f07` is the tip of `proof-assembly-v1`, not of that repo's `main`
> (which predates it and points readers elsewhere, to
> `collatz-nocycle-lean4`) — the retraction is genuine and exactly where
> your letter says it is, but not discoverable from that repo's own
> README. Worth a one-line pointer if that repo is ever cited again. This
> closes the round-11 warning on our side too.
>
> **§5 (the peak spec).** Peak count (250), mean gap (7.19) and clustering
> (0.831) reproduce your figures exactly on independent CF code — strong
> evidence we have the same underlying sequence. Spectral did not land on
> your frequency=124/5.62× pair (mine: 8.48× at frequency 254) under the
> most natural periodogram reading of the prose spec; the estimator's exact
> normalisation is under-specified (same finding as the drift-check session
> made about this detector before you supplied the fuller spec) — the
> qualitative "a real spectral line" claim replicates, the exact figure
> does not. Corrected null, widened from your named three (log₂5, log₂7,
> π) to six real constants (added ln2, γ, ζ(3); tried and *excluded* e and
> √2/√3 — e has an explicit regular unbounded pattern, not generic, and
> gave a genuine 891× positive control; √2/√3 are quadratic irrationals,
> eventually periodic with bounded quotients, guaranteed zero peaks).
> Clustering: log₂3 sits cleanly inside the band, rank 4 of 7 — clean
> non-finding, survives the corrected footing exactly as the memory clause
> did. Spectral: genuinely marginal — log₂3 is the single highest of 7
> values, rank 1, one-sided p≈0.14 (unremarkable at any conventional
> threshold, but not a clean mid-band result either), and two orders of
> magnitude below the e positive control, so no evidence of a real
> spectral line, but a softer non-finding than clustering's. Both readings
> stated flat; draft ledger wording is in the findings, yours to key once
> you've looked at it.
>
> **§6 (the map, §96, θ=1, the two ✓ facts).** §96's mechanism reconstructed
> independently (not reproduced — your `run_048/049.py` are local): the
> telescoping argument checked and written out, and it reproduces cleanly
> at `p=7,k=8` — 3 faulty cycles, all phantom (no genuine closed integer
> orbit found up to ~500k–770k per cycle, against the four operational
> conventions I had to guess and record — findings §6.1). It does **not**
> reproduce at small `k` for `p=3`: no faulty cycles at all for `k=4..9`,
> appearing only at `k=10–12` and vanishing again at `k=14,16` —
> non-monotonic. Offered mechanism: `log₂3`'s closeness to low-height
> rationals (the same closeness L-A9 is entirely about) makes the
> comparison a near-tie at small scale for `p=3`, unlike `p=7`. `θ=1` at
> `p=3` confirmed exactly, and I'd offer a strengthening: at `p=5,7` no
> nontrivial positive root exists *at all* (not just `θ<1`), traced to the
> mean log-step drift changing sign — a cleaner mechanism than the bare
> comparison. Both ✓ facts confirmed (the sieve's *closed-form arithmetic*,
> not the combinatorial argument producing it, which rests on your local
> construction and I haven't rebuilt). One small header-wording note: "two
> items... verified cross-side this round (⊢)" slightly outran its own
> timing when written — propose "offered for cross-side verification this
> round," or, now that this review exists, "verified cross-side" can stand
> honestly for the `p=7` instance specifically, with the `p=3`
> non-reproduction carried alongside it.
>
> **Two items raised, neither blocking.** (i) h5 is accepted in your
> acceptance sentence but the diff only touches L-A9 — the L-A8 `(d-bis)`
> block still reads "0 of 200 reaching 306" rather than the census line. A
> one-line fix, your own already-agreed text; happy to see it in this PR or
> carried to the next round, your call. (ii) `[THE AUTHOR'S: the §96
> answer]` — whether it earns a place in the note is still open on our
> side; this review's reconstruction is offered as input to that decision,
> not a vote either way.
>
> Diff is three files, mostly additions. Approving.

### 7.2 The NOTE bracket patch

Local-only, per the Rules. Scratchpad clone of the shared repo, branch
`note-grade-resolve` from `main` at `308d6bb` (verified before editing).
One edit, `NOTE-v1.md` line 39, restating the grade sentence to the
post-round-13 state and removing the signing bracket:

- **Before:** "Grade at this writing: one key (Merle — exact arithmetic,
  written-ahead canaries); the second key under review, a split grade
  proposed — the Dirichlet half toward two keys, the measured half
  permanently a measurement. [GRADE AT SIGNING — re-read L-A9 before
  signature.]"
- **After:** "Grade at this writing: two keys on the Dirichlet half (Merle
  — exact arithmetic, written-ahead canaries; Macindoe — clean-room
  derivation, independently verified) — the current-window impossibility is
  unconditional theorem-grade; the measured half permanently a
  measurement."

Nothing else on the page touched (`1 file changed, 1 insertion(+), 1
deletion(-)`). Archived as a portable patch:
`briefs/merle-round13-review-patches/0001-NOTE-v1.md-restate-the-L-A9-grade-sentence.patch`
(`git format-patch main..note-grade-resolve`). **Verified**: applied via
`git am` on a second, pristine clone of the shared repo checked out at
`main` (`308d6bb`, confirmed before applying); applied cleanly, one commit,
tree hash **`81e822f3dbeb188e6aa4a99aa2fc9dc925095c26`**, identical to the
originating commit's own tree hash (checked both ways). PR #3 does not
touch `NOTE-v1.md`, so this patch survives its merge untouched. **The push
and the PR are the author's**; nothing here was pushed or opened anywhere.

### 7.3 The Zenodo metadata note

Read directly, both sources, before drafting (per the brief's instruction
that the note must quote itself correctly): the PDF's own Version note
(`paper/collatz-reduced-v3.pdf`, page 1, and the identical source text at
`paper/collatz-reduced-v3.tex` line 42) reads, for v3: *"v3, August 2026
(drafted; the version-specific DOI on the title page is reserved and this
version is not yet published): after external review, ..."* — confirmed
verbatim identical between the built PDF and its `.tex` source. The version-
history file (`paper/collatz-reduced-version-history.md` lines 61–65)
already records the defect in the same words, and adds: "The Zenodo record's
publication date, 2026-08-03, is authoritative."

**Drafted text for the v3 Zenodo record's additional-notes field**
(execution — the actual Zenodo edit — is the author's, per the window's
Provenance §(i)):

> Note on this file's internal "Version note" section: the v3 entry there
> ("drafted; the version-specific DOI on the title page is reserved and
> this version is not yet published") is a drafting-time self-description
> that was frozen into the PDF at the moment of upload, and — because
> Zenodo files are immutable once a version record is published — could not
> be revised afterward to reflect that publication actually happened. This
> record (DOI 10.5281/zenodo.21730505, published 2026-08-03) *is* the
> publication that sentence describes as still pending. The maintained,
> current version history — what changed in this and every other released
> version — is kept outside the frozen file, at
> `paper/collatz-reduced-version-history.md` in the project's public
> repository (github.com/macindoe/collatz), and is the authoritative record
> for anything this note does not cover.

**Drafted one-line version-history addendum** (to enter once the author has
made the Zenodo edit — not applied to the tracked file in this window, per
the brief: "drafted... not applied"):

> *(Zenodo metadata, [date of edit]):* the v3 Zenodo record's additional-
> notes field was updated to explain the frozen "not yet published"
> Version-note self-description (the defect itself recorded above,
> 2026-08-03); no change to the PDF file, which remains hash-identical to
> `paper/collatz-reduced-v3.pdf`.

### 7.4 HANDOFF item 1

Rewritten on this branch — see the diff to `HANDOFF.md`. Summary of what
moved: both round-12 PRs recorded as merged 2026-08-17 by Merle himself
(recorded as a live convention fact: he holds and uses merge rights); shared
HEAD `308d6bb`; PR #3 recorded open at `ef1742d` awaiting the author's key,
with this review's verdict (pass, both numeric checks and the Rhin
retraction) carried alongside it; the third repo
`ericmerle3789/Collatz-Junction-Theorem` added to the repo table with the
`R201-I3` retraction at `77e3f07` and the branch-locatability note; the peak
replication recorded ours-to-key with this window's verdict (clustering
clean, spectral marginal); the §96/campaign-map offer recorded pending the
author's earns-a-place answer; the Zenodo decision recorded flipped
2026-08-22 with the drafted text's location (§7.3 above); the NOTE bracket's
prepared patch recorded with its path and tree hash. Only item 1 touched, no
other item or file restructured, per the brief and per "Single window this
round; no race."

---

## 8. Compliance

- File edits via the Edit/Write tools only, in this repository and in the
  scratchpad clone (the `NOTE-v1.md` edit, §7.2). No PowerShell
  `Get-Content`/`Set-Content` touched any tracked or scratchpad file this
  session.
- `experiments/encoding_scan.py`: run before the final commit; result
  recorded in the commit that runs it (see the branch's final commits).
- Read-only everywhere outside this repository: fresh clones only, `gh`
  reads only, no push/fork/issue/star/watch/comment/contact, anywhere, this
  session. The one local `git commit` outside this repo (the `NOTE-v1.md`
  patch source, §7.2) is in a throwaway scratchpad clone, never pushed, and
  exists only to produce the portable patch.
- No key turned by this session: the review draft (§7.1) recommends turning
  the second key on the corrected L-A9 entry, but the recommendation is the
  main session's and the author's to act on, per the Rules. Every numeric
  check this session ran passed (70 checks across both scripts — 53 in
  `merle_r13_check.py`, 17 in `merle_r13_peak_replication.py` — 0
  failures); had any failed, this section would say so and the draft above
  would flag rather than approve.
- Nothing merged; nothing pushed; nothing sent anywhere. Drafts and
  recommendations only, as instructed.

---

## 9. Review changes (main session, 2026-08-22) — one numeric correction, applied in place

Both scripts re-run at review from the branch worktree; outputs byte-identical
to the committed `merle_r13_check_output.txt` and
`merle_r13_peak_replication_output.txt` (both scripts are seeded; `fc.exe`
reports no differences). The scripts' own TOTAL lines are **53** and **17**
checks — **70 total**, not the "95" the review draft (§7.1) and the
compliance note (§8) stated; that figure was an arithmetic slip in the
window's own summary, not in any verification. Corrected in both places
before merge, along with a line-wrap that had split
`merle_r13_peak_replication.py` across a quoted line inside the draft. No
other content moved; the delegate's §2.1 correction of the brief's
"new numbers" characterization was checked against `merle_la9_check.py`'s
committed PART 3 output and accepted as written.
