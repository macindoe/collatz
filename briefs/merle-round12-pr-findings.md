# Findings: the round-12 response as the first PR — co-edit + letter + protocol, prepared local-only

Brief: `briefs/merle-round12-pr-brief.md`. Branch **`merle-round12-pr`**.

**Base SHA: `df5841d5064a9485fd40baea81f643b1359b87ef`** ("brief: the round-12 PR window ...").
The worktree was cut at the stale `6ffe4638adcec5dd474de70c8a2432355030560e` — one commit
behind local `main`, missing this very brief — and was fast-forwarded to `df5841d` by
`git merge main --ff-only` before anything was read, per the brief's setup step and the
launch instruction. `df5841d` is local `main`'s tip at the time this session started, and
it contains `briefs/merle-round12-pr-brief.md`.

Register: flat, calibrated; corrections of ours stated as ours with mechanisms;
findings that run against Merle delivered kindly and factually. Per the brief's
verification standard, every number below carries its named source; where a source
disagreed with the brief, the source won (no such disagreement was found this session).

---

## 1. State check (Queue item 1)

**Shared repo `macindoe/one-obstruction-three-faces`:** `git ls-remote ... HEAD` →
**`7c05458777caf2a57a42a0dd20b3e4ddb77a66bf`** — exactly the brief's expected HEAD (his
L-A9 hash fix). **Unmoved.** Nothing of his has landed since; no adaptation needed, no
new letter to react to.

**Wiki `main` (`github.com/macindoe/collatz`):** `git ls-remote ... HEAD` →
**`6ffe4638adcec5dd474de70c8a2432355030560e`**. This is the brief's minimum expected pin
(`6ffe463`) exactly. All six context sources are confirmed as ancestors of this public
commit (`git merge-base --is-ancestor <file's last commit> 6ffe463`, run individually
per file, all returning true):

| source | last-touching commit | ancestor of public `6ffe463`? |
|---|---|---|
| `briefs/merle-la9-check-findings.md` | `4facca3` | YES |
| `briefs/merle-r12-drift-check-findings.md` | `66c5e2e` | YES |
| `briefs/merle-la7-rhin-check-findings.md` | `62bd826` | YES |
| `briefs/junction-followup-recon-findings.md` | `8efbf93` | YES |
| `briefs/erratum-v3-prep-findings.md` | `c654fa0` | YES |
| `paper/collatz-reduced-version-history.md` | `169bf6a` | YES |

So every findings file and the version history this window assembles from is already
public and resolvable at or before the live wiki `main` HEAD. No CHECK-AT-SEND marker is
needed for the *state check* itself; the letter's own where-everything-lives map still
carries a CHECK-AT-SEND marker on the pin because the remote can move between now and
the author's actual send (see §7 below).

**Fresh scratchpad clone of the shared repo** (`macindoe/one-obstruction-three-faces`),
read-only `git clone`, confirmed at `7c05458`; a second, untouched copy (`pristine-base`)
kept for patch verification. No fork, no issue, no pull request, no comment, no push, no
write of any kind against the remote; local branch `round-12` created only in the
scratchpad clone.

---

## 2. Load-bearing arithmetic recomputed in-session, at controlled precision

Per the brief's verification standard, the following were re-derived or spot-checked in
this session rather than transcribed from memory, cross-checked against the named
findings file:

- **L-A9 conventions.** `μ* = c* + 1`: at `c* = 0.9617` (his figure, `κ = 1/ln2`),
  `μ* = 1.9617`, matching `merle-la9-check-findings.md` §3 step 5 (`μ* = 1.9617` at
  `κ = 1/ln2`) to four digits. The dream-deficit re-derivation at `μ = 2, κ = 1`:
  `k_max = (3κ·ln2·X₀)^{1/μ}` at `X₀ = 2⁷¹` gives a ratio to Hercher's `K_H = 1.375·10¹¹`
  of **1.96** (la9 findings §4.2's own figure), independently sanity-checked by taking
  the reported `μ=3` deficit `7159.5` and the width-one-power-of-`k` relation
  `7159.5^{1/(μ_hi-μ_lo)}`-style consistency (both figures traced to §4.2, not
  re-derived from raw floating arithmetic in this session beyond the ratio check above).
- **The rotation/staircase arithmetic (§9).** `θ = 8 - 5·log₂3`: with `log₂3 =
  1.5849625007211562...` (standard double-precision value, cross-checked against
  `cycles.md`'s own printed `θ = 0.0751874964...`), `8 - 5·1.5849625007211562 =
  0.0751874964...` — matches to the printed digits. `13θ = 0.977437...`, `14θ - 1 =
  0.0526249...` — both consistent with the findings' printed values
  (`13θ = 0.97744 < 1`; `14θ − 1 = 0.0526249495`). The identity
  `13(14θ−1) + 14(1−13θ) = 1`: expanding, the `θ` coefficient is `13·14 − 14·13 = 0` and
  the constant is `−13+14 = 1` — confirmed algebraically in this session, matching
  `merle-r12-drift-check-findings.md` §4.1 row 12.
- **The D(x)/δ series.** With `u = 1/(3x)`, `D(x) = (2/ln2)·artanh(u) = (2/ln2)(u +
  u³/3 + u⁵/5 + u⁷/7 + ...)`, so `D(x)/δ_x = 1 + u²/3 + u⁴/5 + u⁶/7 + ...` with
  `δ_x = 2u/ln2`. Substituting `u = 1/(3x)`: coefficient of `1/x²` is `1/(3·9) = 1/27`;
  of `1/x⁴` is `1/(5·81) = 1/405`; of `1/x⁶` is `1/(7·729) = 1/5103` — confirmed
  algebraically in this session, matching `merle-r12-drift-check-findings.md` §1.1
  exactly (the denominators are `(2k+1)·9^k`).
- **The Rhin exponent conversion.** `H = K₀ ≤ nβ+1` gives `K₀^{-13.3} ≥
  (nβ)^{-13.3}(1+1/(nβ))^{-13.3}`, so dividing by `n` costs exactly one power of `n`:
  `ε_n/n > c/n^{14.3}`, i.e. `μ_eff = 13.3 + 1 = 14.3` — confirmed algebraically in this
  session, matching `merle-la7-rhin-check-findings.md` §2(b) step 4. This is the "+1
  conversion" the letter's §2 cites as a cross-check against L-A9's own `μ* = c*+1`
  convention gap — both are the same *kind* of step (a height/linear-form exponent
  becoming a per-index measure exponent costs one power), independently arising in two
  different adjudications; the letter states this as a structural parallel, not a
  claim that the two `+1`s are numerically the same quantity.

No arithmetic in this window was transcribed from a findings file's *prose* without
either recomputing it or confirming it against that file's own worked derivation
section (never against a headline number alone).

---

## 3. The shared-repo branch: commits, patches, verification

Prepared **local-only**, in a scratchpad clone of `macindoe/one-obstruction-three-faces`
at verified HEAD `7c05458`. Branch `round-12`. **Nothing pushed; no PR opened; no
interaction with the remote beyond the initial read-only clone and `ls-remote`.**

| commit | file | what |
|---|---|---|
| `3dda4be14ad0341c5e2ffa657f77a13426c0fc7c` | `PROTOCOL.md` | the regime column, §4(d), accepted |
| `229a9bfc791521bf5de125f220a647300675357b` | `LEDGER.md` | L-A9 split-grade key turn + h1–h5; L-A8 two corrections; L-A7 Rhin adjudication |
| `31e1266c449924951152ed4366b820db89253869` | `rounds/R12-macindoe.md` | the round's letter, business paragraphs only |

**Branch tip:** `31e1266c449924951152ed4366b820db89253869`.
**Branch tip tree hash:** `822afb808105adfbc2c09ef9aeb10e7b39914fa6`.

### 3.1 Portable patches, archived at `briefs/merle-round12-pr-patches/`

- `0001-PROTOCOL.md-the-regime-column-Merle-s-proposal-round.patch`
- `0002-LEDGER.md-round-12-co-edit-L-A9-split-grade-key-turn.patch`
- `0003-rounds-R12-macindoe.md-the-round-12-letter-business-.patch`

Generated by `git format-patch 7c05458..round-12` in the scratchpad clone. All three
verified UTF-8, LF line endings, no BOM (checked byte-level in this session).

### 3.2 Patch-verification result: clean apply, tree hash matches exactly

A second, untouched clone of the shared repo (`pristine-base`, at `7c05458`, branch
`main`, confirmed clean) was branched to `round-12-verify` and the three patches applied
in order with `git am`. **All three applied cleanly** — one cosmetic warning only
(`new blank line at EOF`, one line, `0001-...patch`; `git am` still applied it without
`--reject` or manual intervention, and the resulting tree is byte-identical to the
original, so this is not a real defect, just whitespace-check noise). The resulting
tree hash:

```
822afb808105adfbc2c09ef9aeb10e7b39914fa6
```

— **identical** to the `round-12` branch's own tree hash above. The verification clone
and its `round-12-verify` branch were deleted after the check (`git checkout main; git
branch -D round-12-verify`); `pristine-base`'s `main` is back at bare `7c05458`, untouched.

### 3.3 What each file's addition says, one line each

- **`PROTOCOL.md`** — one bullet added to §3 ("The claims ledger"): beside the two keys,
  each entry now records the regime it was discharged in, and any asserted equality
  records a second regime chosen against it; attributed to Merle's round-12 §4(d),
  accepted, second key = this PR's approving review. No other section touched.
- **`LEDGER.md`, L-A9** — a Macindoe verification record (50 checks, 0 failures,
  clean-room) confirming the Dirichlet half as unconditional theorem-grade *conditional
  on offer h1* (the grade line's convention-mixed margin repaired) and the scissors half
  as measured *permanently* (proving `α > 1/3` is itself `μ(log₂3) ≤ 3`-hard); offers
  h1–h5 drafted verbatim from `merle-la9-check-findings.md` §6.4. Status stays DRAFT
  pending his acceptance of h1, per the brief and per the findings' own recommendation
  (§6.3 there: "no key turned here").
- **`LEDGER.md`, L-A8** — two correction blocks, both accepted as ours, both dated and
  mechanism-named, drafted verbatim from `merle-r12-drift-check-findings.md` §1.4 and
  §2.4: the `D(x_min) = δ(1+1/(27x_min²))` display was a truncation, not an identity
  (what is exact is the strict chain `D(x) > δ(1+1/(27x²)) > δ`); and the paired
  "44 decimal places" diagnosis is refuted by scale-invariance (the summed ratio is
  `0.4755266037564546…` at every scale, not converging to 1).
- **`LEDGER.md`, L-A7** — one short adjudication record, no key turn needed (already
  two keys): grade (a), 13.3 CONFIRMED for exactly what the chain consumes, via the four
  carriers of `merle-la7-rhin-check-findings.md` §2; BILAN_R201's premise refuted, its
  trigger (R200's `(log)²` transcription) real; no number in the entry moves.
- **`rounds/R12-macindoe.md`** — the letter, twelve business sections in the brief's
  specified order (§5 first, L-A9, Rhin, §4 acceptances, §9, §10 silence, §§1–2,
  two small corrections, erratum, §12 business half with both placeholders left empty,
  §13 answered by the object itself, where-everything-lives map). No personal
  opening/closing. Full text: see the patch or the branch file directly (verbatim
  archive, not reproduced a second time here per the brief's by-patch-reference option).

---

## 4. Wiki-side: `cycles.md` 12.8.6.1 (item 5)

**One edit, on this repo's `merle-round12-pr` branch, separate from the shared-repo
work**, at commit **`e586d356983bae56738f53072d924358a1545724`** (short: `e586d35`).
Placed exactly where drift
findings §4.2 specifies: a new italic-marker paragraph between *What is consumed.* and
*Superseded formulation…*, plus one clause appended to the pre-existing *Verified*
paragraph citing `experiments/merle_r12_drift_check.py`. Text is the findings' own
drafted block, transcribed without alteration (unicode math symbols matched to the
page's existing convention, which the findings block already used). Nothing else on the
page moved (`git diff --stat cycles.md` → `1 file changed, 3 insertions(+), 1
deletion(-)`, the one deletion being the boundary line's join, not content removal).

**Pin used in the letter and the ledger:** `e586d35`. Per the brief, this is **the pin
to re-check at merge** — the main session re-pins both the letter (§5's
`cycles.md` reference) and the ledger (§4(d) correction block, which also cites this
commit) if the actual merge SHA differs from `e586d35`.

---

## 5. PR title and description (drafted; not opened anywhere)

**Title:** *Round 12: the L-A9 split-grade key, the regime column, and the round's letter*

**Description:**

> This PR is the first enactment of §13's accepted proposal — one round, one pull
> request, the second key the approving review.
>
> Carries:
> - `rounds/R12-macindoe.md` — the round's letter, business paragraphs only, opening the
>   `rounds/` convention on this side (mirroring `rounds/R11-merle.md` in the Lean repo).
> - `LEDGER.md` — the round-12 co-edit: **L-A9** (the δ8 impossibility) offered for a
>   split-grade key turn — the Dirichlet half unconditional theorem-grade, conditional on
>   offer h1 (the grade line's convention-mixed margin repaired); the scissors half
>   measured, permanently. Two corrections to our own **L-A8** hand-back, accepted as
>   ours (the `D(x_min)` display was a truncation, not an identity; the paired
>   44-decimals diagnosis is refuted by scale invariance). A short adjudication record on
>   **L-A7**'s Rhin re-source warning — grade (a) confirmed, no number moves.
> - `PROTOCOL.md` — the regime column, entered by Merle's own §4(d) proposal and
>   accepted: beside the two keys, each claim records the regime it was discharged in,
>   and any asserted equality records a second regime chosen against it.
>
> What needs your key: **L-A9's Dirichlet half** (offer h1 first — the grade line needs
> restating in one convention before the claim it protects can be a two-key theorem);
> **the regime column itself**, whose second key is this pull request's approving
> review; and, in the ordinary sense every co-edit block asks for it, **the two L-A8
> correction blocks**.
>
> Your prose is untouched everywhere in both files; every addition is either a new block
> or an offer inside an existing one, per the established co-edit style.

---

## 6. Register and content summaries

**The letter's twelve sections, one line each (content only; full text in
`rounds/R12-macindoe.md` or patch 0003):**

1. §5 answered first — binning convention confirmed exactly his; REQ-067 divergence at
   index 385 verified in full, `0.00078` and all six comparison numbers to the digit.
2. The L-A9 verdict — arithmetic flawless, conclusion confirmed and strengthened, the
   grade line's margin does not survive (convention mix, one-power-of-`k` gap, the
   `μ=3` dream deficits), Barina label corrected, α width-dependence and the straddle at
   1/2 noted; split-grade key offer pointed at the ledger; the `+1`-conversion
   cross-check with the Rhin adjudication noted.
3. The Rhin answer — grade (a) confirmed via four carriers; BILAN retired; L-A7 unmoved;
   the one open boundary (p.160's own threshold, unread) carried forward.
4. The §4 acceptances as ours — the truncation, the refuted 44-decimals diagnosis, the
   credit record (factor-2 jointly arrived at, corollary his/proof ours) — one sentence
   each, mechanism named.
5. The §9 answer — all fourteen claims confirmed; the plateau and its `J=26` fall;
   "cost not failure" priced exactly; incorporation into `cycles.md` 12.8.6.1 at `e586d35`.
6. The §10 answer — the silence confirmed real and total on two of three clauses;
   memory clause retained on the corrected footing; clustering/spectral retained with a
   scope clause, his side, pending his detector spec; stopping rules explicitly do not
   bar replication.
7. The §§1–2 answer — all three round-11 not-founds closed at full weight, carried
   nearly verbatim from the junction follow-up recon's own reply-material paragraph, the
   7→15→18 count handed back as a fourth instance of his own finding.
8. Two small corrections — the 3,175-byte CRLF mechanism; the §10.2 fifteen-quotients
   correction.
9. The erratum answer — v3 published 2026-08-03, DOI 10.5281/zenodo.21730505 (verified
   live, see §7 below); the drafted-erratum-to-full-revision delta stated in his own §2
   vocabulary; citation guidance (v3 for the dichotomy phrases and the Theorem 4.6
   obstruction sentence, both verified verbatim in the published tex; v2 for the
   superseded contiguous-evidence note); the frozen Version-note self-description
   self-reported at full grade.
10. The §12 answer, business half — the two-page-note shape accepted, erratum
    precondition met; both author placeholders (`[THE AUTHOR'S: the pen]`,
    `[THE AUTHOR'S: the cost answer]`) left empty, nothing drafted for either.
11. §13 answered by the object itself — one paragraph: this PR is the acceptance
    enacted, the regime column his to key as well.
12. The where-everything-lives map — six sources with their check counts, the v3 DOI,
    the wiki `main` pin with its CHECK-AT-SEND marker.

**The three ledger blocks, one line each:** L-A9 gets a ~340-word verification record
plus five offers (h1–h5), split-grade, DRAFT pending h1's acceptance. L-A8 gets two
short correction paragraphs (the truncation repair; the scale-invariance refutation),
both already at "accepted as ours," no key-status change (the entry was already two
keys and stays two keys — these are corrections to prose inside an already-keyed entry,
not new claims). L-A7 gets one adjudication paragraph, no key-status change (already
two keys), no number moved.

**The protocol column, one line:** a single new bullet in `PROTOCOL.md` §3, attributed
and dated, stating the rule and its rationale (two round-12 errors, one per side, both
made and caught in the same regime); nothing else in the file restructured, per the
brief's explicit instruction.

---

## 7. Pins and CHECK-AT-SEND markers

| pin | value | status |
|---|---|---|
| Shared repo base HEAD | `7c05458` | Verified this session via `ls-remote`; unmoved from the brief's expectation. |
| Wiki `main` (cited in the letter's map and used for the state check) | `6ffe463` or later | Verified this session via `ls-remote`, resolves exactly at `6ffe463`. **CHECK AT SEND TIME** carried in the letter itself, because the remote can move between this session and the author's actual send — this is a live-resolution caveat, not a doubt about the current state. |
| `cycles.md` 12.8.6.1 commit (this repo) | `e586d35` | This session's own commit, on `merle-round12-pr`. **Not** a CHECK-AT-SEND marker in the "might not resolve" sense — it is a **re-pin-at-merge** marker per the brief: both the letter and the L-A8 correction block in the ledger cite `e586d35`; if the main session's merge produces a different SHA for this commit (e.g. via rebase), both citations must be updated to the real merge SHA. |
| v3 DOI | `10.5281/zenodo.21730505` | Verified **live** this session via `WebFetch` against `https://doi.org/10.5281/zenodo.21730505` (redirects to the Zenodo record): title matches, version explicitly "v3", publication date 2026-08-03, listed as "is new version of" the v2 DOI. No CHECK-AT-SEND marker needed; this is a resolved, published, immutable record. |

---

## 8. What could not be verified this session, with reasons

- **Rhin 1987's own printed hypotheses on p. 160** (whether any explicit threshold `H₀`
  is stated) — the 1987 volume (Progress in Mathematics 71) remains paywalled from this
  session, exactly as recorded in round 9 and round 10. Both published applications used
  in the adjudication (Simons–de Weger 2005, arXiv:2205.10582) apply the Proposition
  thresholdless from moderate heights, and L-A7's own use needs only `H ≥ 952`, so
  nothing here is load-bearing for any conclusion drawn — carried forward as an open
  boundary, not a gap in the adjudication.
- **Whether Barina's live project-counter page ever displayed `2075·2⁶⁰`** — the value
  is script-rendered on an external page and unarchived; `merle-la9-check-findings.md`
  §2 recorded this as unverifiable, not disputed, and this session did not attempt a new
  check (the letter's offer h3 routes around the question rather than resolving it,
  since the citable, stable, paper-stated bound `2⁷¹` is what matters for the ledger).
- **Whether the Zenodo record's metadata note about the frozen Version-note defect has
  been added** — per the version-history file and the letter, that remedy is the
  author's own pending action, not something to check for in advance of his doing it.
- Everything else load-bearing in this window was either recomputed in-session (§2
  above), verified at its named place in a findings file, or verified live against the
  actual repository/DOI (state check, §1; DOI resolution, §7).

---

## 9. Compliance

- File edits via Edit/Write tools only, in both this repository and the scratchpad
  clone; no PowerShell `Get-Content`/`Set-Content` touched any tracked or archived file.
- `experiments/encoding_scan.py` run before the final commit in this repository:
  **RESULT: CLEAN** (see the commit history on `merle-round12-pr`; re-run immediately
  before this findings file's own commit as well).
- Shared repo and both of Merle's repositories: read-only clones and `ls-remote` only,
  in the session scratchpad. No push, no fork, no issue, no comment, no star, no watch,
  no follow, and no interaction of any kind beyond that, anywhere, this session.
- Nothing merged on this branch; the main session reviews and merges. Nothing pushed
  anywhere; no PR opened anywhere — the push and the PR are the author's send, gated on
  his go-ahead, per the brief.
- `HANDOFF.md`, `publication.md`, and every pre-existing findings file: untouched.
