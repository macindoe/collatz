# Findings: round-9 co-edit prep (merle-round9-coedit)

Delegated session, 2026-07-25. Brief: `briefs/merle-round9-coedit-brief.md`
(commit `69eebdd`). Branch `merle-round9-coedit`, base commit `69eebdd` (the
brief commit — the worktree was cut at `e71e81e`, an ancestor; the branch was
created directly from `69eebdd`, present in the shared object store, so the
"`69eebdd` or a descendant" condition is satisfied exactly).

**SHARED REPO NOT PUSHED — push gated on the author's explicit go-ahead
relayed by the main session. No pushes anywhere this session, to any remote.**
The shared repo received exactly one LOCAL commit on a local branch of a fresh
scratchpad clone; the patch below is the portable form. **Handbacks: none.**

## Item 0 — shared-repo state verified

Live `ls-remote` first, then fresh clone (`scratchpad\shared-repo-round9`,
2026-07-25): `refs/heads/main` =
`81431c754c634b66c057fb784c0f25d844288c71` (`81431c7`) — **exactly the brief's
expected pin; not moved.** No stop condition triggered. The L-A4/L-A5/L-A6/
L-A7 entry texts at `81431c7` were read in full before editing; the L-A6 and
L-A7 texts match the verbatim quotes in `briefs/merle-la6-check-findings.md`
§1(ii) and `briefs/merle-la7-mu-check-findings.md` §1 respectively.

**Artifact-pin pre-check, with one flag.** The three cited wiki commits all
exist on the main lineage (each an ancestor of `69eebdd`) and contain exactly
the named script + committed output:

- `38b7595` — `experiments/merle_la6_check.py` + `merle_la6_check_output.txt`;
- `e7a3696` — `experiments/merle_la7_check.py` + `merle_la7_check_output.txt`;
- `00f7bbc` — `experiments/merle_contentdescent_check.py` +
  `merle_contentdescent_check_output.txt`.

**Flag (pre-push condition):** public `macindoe/collatz` `main` is still at
`e71e81e` (round-8 reply state; checked by `ls-remote` this session) — the
round-9/10 merges (`08b1547`, `13ba557`, `716b94a`, `69eebdd`) are not pushed
yet, so none of the three pins resolves publicly *today*. The pins are correct
on the lineage and will resolve once wiki `main` is pushed to `716b94a` or
later. **Before (or with) the shared-repo push, the author should push wiki
`main`** — otherwise the ledger's "commit …, on `main`" links dangle. Same
pre-check the L-A5 round ran (`a87b94a` resolved then because main had been
pushed); recorded here as a condition, not a handback, since the shared-repo
push is gated anyway and the fix is the author's routine main push.

## Item 1 — the prepared commit

- **Clone:** fresh, unauthenticated, `scratchpad\shared-repo-round9`
  (identity set repo-local to `macindoe <begemite0.o@gmail.com>`, the
  established co-edit author).
- **Branch:** `round9-coedit`, from `81431c7`.
- **Commit:** `641a5306bc5f301f9f02587a8e7a3e1a0b1ee1aa` (`641a530`),
  `LEDGER.md` only, **26 insertions / 1 deletion** — the single deletion is
  the date-stamp appended to *our own* L-A5 Key-status line (the line is
  modified, nothing removed); every other change is a pure append. No prose
  of his is touched anywhere.
- **Patch:** `briefs/merle-round9-coedit-patches/0001-Round-9-co-edits-L-A6-Macindoe-key-turned-scoped-cen.patch`
  — verified this session: `git am` on a pristine `81431c7` checkout applies
  clean and reproduces `641a530`'s tree identically (empty `git diff`).
- **Diff summary by entry:** L-A4 +2 lines (statement-match record); L-A5
  1 line modified + 4 added (date-stamp; one minor offer); L-A6 +11 lines
  (key turned + offers (a)–(d) + key-status); L-A7 +8 lines (verification
  record + re-source offer + conditional key-status).

## Item 2 — the prepared LEDGER blocks, verbatim

### L-A4 — appended after the "Lean key on the structured half" block

> **Macindoe statement-match on the Lean key (2026-07-25), recorded:** all five ContentDescent statements verified clean-room against the 12.6.1.4 identity and the L-A2 law, with `G_k` confirmed as the 12.6.1.4 cofactor — recursive = closed = `q`-cofactor at every pair (`macindoe/collatz` `experiments/merle_contentdescent_check.py` with committed output, commit `00f7bbc`, on `main`; 4,541 exact checks, 0 failures; read-not-built — no toolchain our side, kernel-3 resting on his committed logs).

### L-A5 — the Key-status line's appended date-stamp (the 1-deletion line), then the minor offer

The Key-status paragraph is unchanged up to its final period, then gains:

> *(Condition met, 2026-07-24: restatement accepted at `49351e5` — two keys, per the header.)*

Appended after it:

> One minor offer (Macindoe, 2026-07-25) — acceptance is Merle's call:
>
> - *(minor — the wall rider.)* "no isolated `C = 1` peak on the positive shore" → "no isolated **primitive** `C = 1` peak on the positive shore": read standalone, the forced powers of `+1` are literal positive-shore isolated `C = 1` words (the trivial square `((1,1),(1,1))` has `q = R_0 = 7`, `C = 1`, and unit seams `3¹ − 2¹ = 2¹ − 1 = 1`, so shared content 1 with every neighbour); read in place the anaphora is unambiguous — the two-word precision closes it.

### L-A6 — appended after the entry's artifacts paragraph ("… Open for co-editing.")

> **Macindoe key turned (2026-07-25) — scoped: census and realizability exact, budgets and tail as replicated model computations, the reading at its assessed grade.** Independent verification with fresh code from `cycles.md` 12.6.1/12.6.1.1's conventions only (no code or text reused from either Merle repository; predictions printed before any sweep; canaries = the four known cycles' words hand-computed first): **424 recorded checks over the census's 816,871 words, 0 failures.** The census **exact-confirmed** in his domain: exactly the 18 hit words and nothing else; frame agreement `q | B ⟺ q | R_0` at 816,870/816,870 words, both directions — and at full gcd level (`gcd(|q|, B) = gcd(|q|, R_0)` at every word). **Completed our side to ALL `S` at `n ≤ 14`: the complete census is 23 words** (13 trivial powers + 6 `(−5)`-powers + the `−17` orbit's 2 + its square's 2), so the qualitative claim — freebies + `−17` orbit + L-A4-forced powers, nothing else — holds **unconditionally** at `n ≤ 14`, a strengthening: by the ghost lemma below plus the cycle product identity `2^K = Π_t (3 + 1/x_t)`, a south hit forces `S ≤ 8` for `n ≤ 14` (every possible south hit was already inside his window), and a north extension hit forces `x = 1` — the trivial powers at `(j, 2j)`, `j = 10..14`, each verified `B = q` directly. Budgets and tail **replicated digit-exact, as model computations** (exact necklace counts, two methods agreeing on every cell): south `λ = 1.1175`, north `λ = 2.6447` (his 1.12/2.64); tail tranches identical at all four decimals over his window; dominant cells matching his list cell for cell. **The ghost identity is proved exact our side** — the telescoping lemma `3·B(W) + q = 2^{σ_0} · B(shift W)` (`q = 2^K − 3^n`) holds for every σ-word with entries `≥ 1`, and `B(W)` is **odd** for every word; hence for `x = B(W)/q` the valuation `v_2(3x+1) = σ_0` is **forced** at every step — "a formal hit IS a real cycle" is a theorem, not a measurement (verified 1,364 exhaustive + 400 random words; all 23 census hits realize as exact true-map orbits; 350/350 fresh ghost draws). The calibration reading (south winnings = budget; north residual `~0.005` as odds attached to the wall) is left **at his own assessed grade, explicitly** — nothing our side raises or lowers it. Artifact: `macindoe/collatz` `experiments/merle_la6_check.py` with committed output (commit `38b7595`, on `main`).
>
> Offers, inside the entry per the co-edit style — acceptance is Merle's call:
>
> - *(offer a — domain clauses.)* The census "18" is the `S ≤ 9` window count with the `n ≥ 2` start (of the three freebies only `−5`'s word is in-domain), and the budgets/tail live on the near-tuned band `S ≤ int(0.5849625·n) + 3` — load-bearing: outside it the formal budget does not decay while realizable size collapses (the REQ-016 size artifact). One clause naming the window and the band closes it; the all-`S` completion at `n ≤ 14` (23 words, ghost + product-identity argument) is offered as the closure.
> - *(offer b — the mechanism sentence.)* The exact ghost lemma `3·B(W) + q = 2^{σ_0} · B(shift W)` (`B(W)` always odd — his `v_2(ghost) = 0` — so the itinerary is forced at every step) offered in place of "300/300 random words": the filter's mechanism as a stated identity rather than an empirical rate.
> - *(offer c — the residual's cut.)* The north residual `≈ 5·10⁻³` is the tail sum at the cut `n ≥ 61` (his OUT-023: `0.0049 + 0.0001`); the committed script computes no verification-bound criterion, so pinning the cut in the entry grounds "beyond the verified range" in the artifact.
> - *(offer d — minor.)* "known" before "in existence" (true on the known ×3−1 list; universality is exactly what the falsifier sentence carries); primitive-only units for `P(0)` if preferred (`λ_prim = 1.0502` south / `2.4282` north, `P(0)` 0.350/0.088 — same story, cleaner units); and `27/17` is a semiconvergent (the mediant of `8/5` and `19/12`) with the top south cell by budget `(24,38)` and `(53,84)` second — "convergent anchors" covers both loosely.
>
> **Key status:** **two keys** — the census and the realizability filter exact on both sides (his measured grades upgraded: the census exact-confirmed and completed, the filter a proved lemma), the budgets and tail as replicated model computations (exact necklace counts matching his approximation at all printed decimals), and the calibration reading at its assessed grade on both sides, exactly as the entry labels it.

### L-A7 — appended after the entry's artifacts paragraph ("… Open for co-editing.")

> **Macindoe verification record (2026-07-25) — replication digit-exact; the flagged μ source re-checked.** Independent replication with fresh code (μ a parameter throughout; exact integer arithmetic for every `q` and word count; his script read for operational definitions only, never run): `C₀ = −5.774` at `n = 2`, the ingredient slack `14.483` at `n = 2`, the tail table at all seven cuts, and the headline cut exact (min `N` for `< 5.2·10⁻⁴` = **600**) — all matching his committed output. **The μ source, re-checked as the entry itself flags, stated flat:** `5.125` is Salikhov 2007's effective irrationality measure of **`ln 3`** (Dokl. Akad. Nauk 417 (2007), no. 6, 753–755; English transl. Doklady Mathematics 76 (2007), no. 3, 955–957; superseded even for `ln 3` by Wu–Wang 2014, `5.1163051`, J. Number Theory 142 (2014), 264–273) — not of `log₂3`, and no measure of that strength is published for `log₂3`; as committed, the headline "`< 5.2·10⁻⁴` beyond `n = 600`" survives only under the transplanted exponent with the fitted constant. The citable effective ingredient for `log₂3` is **Rhin 1987** (Proposition, p. 160, Progress in Mathematics 71: `|u₀ + u₁·ln 2 + u₂·ln 3| > H^(−13.3)`; the printed Collatz-side precedent is Simons–de Weger 2005, Acta Arith. 117, Lemma 12), under which **the same construction closes: total ticket mass provably `< 5.2·10⁻⁴` beyond `n ≈ 2233`, exact finite computation below** — the instrument intact, the ruler re-sourced. "Effectively finite at every scale" is TRUE under every sourced row, down to the guaranteed two-log fallback (Gouillon 2006, a constant floor, crossing `~7.36·10⁸`). Artifact: `macindoe/collatz` `experiments/merle_la7_check.py` with committed output (commit `e7a3696`, on `main`).
>
> Offer, inside the entry per the co-edit style — acceptance is Merle's call:
>
> - *(offer — the re-sourced ruler.)* Replace the ingredient line by the Rhin 1987 / Simons–de Weger 2005 citation; restate the bound as `R(n) ≤ −c_gen·n + 13.3·log₂ K₀ + C₀` with explicit `C₀ ≈ 2.06` (+3 repair bits for the best-cell → both-shore-mass step, measured `< 1.94`); restate the consequence as "provably `< 5.2·10⁻⁴` beyond `n ≈ 2233`; exact computation below" (`n ≤ 2000` already exists on both sides; the 2000→2233 strip is a finite computation of the same kind); and re-derive or drop the `n ≈ 550` crossing sentence — neither natural reading reproduces it our side (per-scale bound < 1 ticket at `n = 372`; cumulative tail < 1 at `N = 440`). Two further ingredients, named so the "modulo published ingredients" ledger is complete: the for-all-`n` margin inequality `margin(n) ≥ c_gen·n` (verified `n ≤ 2000`, min `2.84` at `n = 2`; elementary, not yet proved anywhere), and the south-side floor `ε'_n` for the both-shore step (our slack `70.1` at `n = 3`; unchecked in the committed artifact).
>
> **Key status, honestly:** the Macindoe key turns on the replication (digit-exact) and on the construction **with the re-sourced ingredient** — the entry reaches **two keys** upon Merle's acceptance of a re-sourcing (his own wording equally welcome). Status stays **DRAFT** with this stated until then. The honest-scope paragraph stands untouched — it is correct as written, including "sharper measures only improve `C₀`".

## Judgment calls

1. **His status headers untouched.** L-A6's "DRAFT — one key … Macindoe key
   invited" and L-A7's header stay as he wrote them; our key state lives in
   the appended Key-status paragraphs — the L-A4 precedent exactly (his
   header there still reads "DRAFT — one key" while our appended block ends
   "Status: **two keys**"). Header updates are his edit to make.
2. **The L-A5 date-stamp is an edit to our own paragraph** (brief item 3(ii)).
   The item heading says "offers only", but the DRAFT-conditional sentence is
   *our own* appended text, not his prose; the brief's "(ii) date-stamp our
   now-satisfied conditional" was read as the instruction it is, executed as
   a pure append to the sentence (nothing deleted), producing the commit's
   single modified line. Everything touching *his* prose is an offer.
3. **Gouillon crossing written `~7.36·10⁸`**, the findings' verbatim value
   (sensitivity table row G), not the brief's rounded `~7.4·10⁸` — per the
   hard rule that every number is copied from the findings files exactly.
4. **The transplant sentence included** ("as committed, the headline …
   survives only under the transplanted exponent with the fitted constant"):
   the brief's "do not soften" instruction read as requiring the sensitivity
   verdict stated flat, in the findings' own words (shortened from
   "transplanted, unsourced exponent"), so the re-source offer's motivation
   is in the entry rather than only in our private record.
5. **L-A6 all-`S` argument compressed to one line** per the brief ("the
   one-line ghost + product-identity argument"): the `S ≤ 8` south bound and
   the `x = 1` north enumeration are stated with the findings' numbers; the
   full derivation stays in `briefs/merle-la6-check-findings.md` §2(a).
6. **`≈ 7%` vs primitive units:** offer (d) presents `λ_prim` as "if
   preferred" and does not restate his 7% as wrong — the findings grade it
   "same qualitative story; cleaner units", and the offer carries exactly
   that.
7. **Author identity** set repo-local to `macindoe <begemite0.o@gmail.com>`
   (the `e53630f` precedent); the machine had no global git identity.

## Flags

- **Pre-push condition (item 0):** the three artifact pins (`38b7595`,
  `e7a3696`, `00f7bbc`) do not resolve on public wiki `main` yet (public
  `main` = `e71e81e` at this session's `ls-remote`); the author's wiki-main
  push to `716b94a`+ must accompany or precede the shared-repo push.
- No other flags. Every number and citation in the prepared blocks was
  located verbatim in `briefs/merle-la6-check-findings.md`,
  `briefs/merle-la7-mu-check-findings.md`, or
  `briefs/merle-la5-closure-findings.md` before use; no stop-and-hand-back
  was triggered.

## What the main session does next

1. Review the blocks and the patch. **Author pushes wiki `main` (≥ `716b94a`)
   so the pins resolve publicly.**
2. On the author's go-ahead: push `641a530` from the scratchpad clone
   (`shared-repo-round9`, branch `round9-coedit` → `main`, fast-forward over
   `81431c7`) — or `git am` the patch onto a fresh clone if the scratchpad
   has been cleaned. If the shared repo has moved past `81431c7` by then,
   re-seat first (the round-8 precedent).
3. The round-9 reply draft is a **parallel session** (its own brief in
   `69eebdd`); this session makes no claim on it.
