# Findings: L-A5 co-edit prep (merle-la5-coedit)

Delegated session, 2026-07-25. Brief: `briefs/merle-la5-coedit-brief.md`.
Branch `merle-la5-coedit`, base commit `3ed9e47` (the brief commit). Launch
note, for the record: the worktree was cut at `9366d49` (one commit behind the
brief); the branch was created directly from `3ed9e47`, which was present in
the repository — `3ed9e47` is a descendant of `9366d49`, so the brief's
"verify `9366d49` or a descendant" is satisfied. Same pattern as the la5-check
round, recorded flat.

**SHARED REPO NOT PUSHED; push gated on the author's word from the main
session (manual mode).** No pushes anywhere this session. The shared repo
received exactly one LOCAL commit on a local branch of a fresh scratchpad
clone; the patch below is the portable form. **Handbacks: none.**

## Item 1 — shared-repo state verified

Live remote check first (`git ls-remote`), then fresh clone
(`scratchpad\shared-repo-la5`, 2026-07-25): `refs/heads/main` =
`740edb3c4af3720e298f1af048c9fc0b400cd426` (`740edb3`) — **exactly as
expected; not moved.** A leftover clone from the round-8 session existed in
the scratchpad; it was not reused for the prep (fresh clone instead), and its
own `origin/main` fetch also returned `740edb3` (consistency cross-check).
The L-A5 entry at `740edb3` was compared against the verbatim quote in
`briefs/merle-la5-check-findings.md` §(ii): **identical** — no delta, no stop
condition triggered.

Artifact-pin pre-check: `a87b94a` (the la5-check verification commit) exists,
contains `experiments/merle_la5_check.py` + `merle_la5_check_output.txt`, and
is an ancestor of `macindoe/collatz` public `main` (`9366d49`, confirmed via
`ls-remote`) — the block's "commit `a87b94a`, on `main`" resolves publicly.

## Item 2 — the prepared commit

- **Clone:** fresh, unauthenticated, `scratchpad\shared-repo-la5`.
- **Branch:** `la5-coedit`, from `740edb3`.
- **Commit:** `e53630fb31eef66b6c339acf387bf087747b0977` (`e53630f`), author
  and committer `macindoe <begemite0.o@gmail.com>`, `LEDGER.md` only,
  11 insertions, 0 deletions — one commit, appended after the entry's
  artifacts paragraph ("… Open for co-editing.").
- **Patch:** `briefs/merle-la5-coedit-patches/0001-L-A5-Macindoe-verification-record-appended-invariant.patch`
  (committed in-repo; regenerable from the clone if line-ending churn ever
  matters — git's CRLF warning on add is cosmetic).

### The appended block, verbatim

> **Macindoe verification record (2026-07-25) — clean-room, with the exhibit computed.** Independent verification from `cycles.md` 12.6.1's conventions only (no code or text reused from either Merle repository; canaries hand-computed before any sweep). The invariant **confirmed**: `gcd(q, R_r)` rotation-invariant and `C = 1 ⟺ q | R_0` in exact integer form, 600/600 each, both signs of `q`, tuned and untuned. The landscape **consistent at reduced scale** (aperiodic band max `C` 0.24–0.38 at `N = 4,000` per depth; the one-letter collapse reproduced on all three towers), with the `B^j` climb made **exact** via the descent identity [L-A4]: `gcd(q_{B^j}, R_0(B^j)) = G_j · gcd(q_B, R_0(B))`, whence `1 − C(B^j) ~ c/j` — the climb happens for **every** base, divisible or not, and `C(B^j) = 1 ⟺ C(B) = 1` (the L-A4 identity's corollary: repetition approaches `C = 1`; it reaches it only from a cycle). T1/T2 **re-derived clean-room** from the `W0` fold alone: the closed forms match the Lean statements exactly; verified 2,025 + 2,025 exhaustive, 900 + 900 random, and the `R_0`-frame forms (including the position-0 rotation reduction the `W0` frame repairs); corollary 664/664, with all 79 unit-seam cases (`m_2 = 1` resp. `s_1 = 1`) at shared content exactly 1. Lean artifact status, flat: read, statements matching this entry clause-by-clause; no `sorry`, no `native_decide`, no user axioms in the text; not built our side (no toolchain here); a committed `#print axioms` output would close the kernel-3 claim — an invitation, not a demand. Artifact: `macindoe/collatz` `experiments/merle_la5_check.py` with committed output (commit `a87b94a`, on `main`; ~10,372 exact decisions, 0 failures).
>
> **The exhibit, stated flat.** The `−17` cycle's word (`m = (4,3)`, `s = (1,3)`; `q = −139`, `R_0 = 139`) is primitive, untuned, at `C = 1` exactly — and **totally isolated**: shared content 1 with all six adjacent-transfer neighbours, forced by the corollary itself (`gcd(139, 3^3 − 2^3) = gcd(139, 19) = 1`). The separation lemma's showcase: a peak with no shoulders, realized.
>
> Two offers, inside the entry per the co-edit style — acceptance is Merle's call:
>
> - *(offer a — the closing gloss.)* T1/T2 prove adjacency separation — no word is *connected* to `C = 1` by one-unit transfers — not non-existence; unscoped, the `−17` pattern realizes an isolated aperiodic peak, and tuned-scoped, the existence of such a peak is exactly the parked condition `q | R_0`, NOTE §6's residual gap. Offered replacement for the entry's final two sentences: "So content towers have no shoulders: a word at `C = 1` shares at most letter-scale content with every adjacent-transfer neighbour (content `1` at `m = 1`), so no word is *connected to* `C = 1` by one-unit transfers; and repetition, the one road that climbs (`C(B^j) → 1` for every base, per the L-A2 law), reaches `C = 1` at finite height only from a base already at `C = 1` — and is sterile [L-A4]. The *existence* of an isolated aperiodic `C = 1` peak is untouched: it is exactly the parked condition `q | R_0` — NOTE §6's residual gap — and untuned the pattern is realized: the `−17` cycle's primitive word has `C = 1` while sharing content `1` with every neighbour (its seam `3^3 − 2^3 = 19` is coprime to `139`)."
> - *(offer b — domain.)* `C` is `0/0`-undefined at `|q| = 1` — exactly the spent-stock words [L-A3; `cycles.md` 12.6.1.2/12.6.1.3]; a one-clause domain restriction `|q| > 1` (or the convention `C := 1` there, as preferred) closes the interval claim.
>
> **Key status, honestly:** the Macindoe key turns on the invariant, the landscape, and the separation lemma (T1/T2 + corollary) as verified; on the entry's closing gloss it turns **with offer (a)** — the entry reaches **two keys** upon Merle's acceptance of a restatement (his own wording equally welcome). Status stays **DRAFT** with this stated until then.

## Judgment calls

1. **Header wording.** The L-A4 style model opens "Macindoe key turned"; that
   claim is not available here (the key is conditional on the gloss), so the
   block opens "Macindoe verification record … clean-room, with the exhibit
   computed" and carries the key's exact state in the closing **Key status**
   paragraph, per the brief.
2. **Notation harmonization in the quoted restatement.** The findings' long
   form uses the Unicode subscript `R₀`; the shared ledger entry writes `R_0`
   throughout. The two `R₀` occurrences in the quoted restatement were
   harmonized to `R_0` (and likewise `m₂`/`s₁` → `m_2`/`s_1` in our own
   record's unit-seam clause) to match the entry's notation. No word changed;
   this is the "adjusting only what grammar requires" allowance read to cover
   the host entry's notation.
3. **The restatement is embedded as a quoted sentence inside offer (a)**
   (quotation marks, not a block quote) so the ledger keeps one visual level
   of nesting — the L-A4 offers are single bullets; a nested blockquote
   inside a bullet renders inconsistently across viewers. Text is otherwise
   the findings' long form verbatim.
4. **Reduced-scale numbers included** (0.24–0.38 band at `N = 4,000`; three
   towers) rather than bare "consistent at reduced scale" — the brief's
   "keeping every number citable" read as wanting the scale visible so his
   larger-`N` grid is not implied to be replicated at full size.
5. **Fresh clone** rather than reusing the round-8 leftover clone in the
   scratchpad (stale-mirror precedent from the la5-check round; the leftover
   also carried round-8 working branches). Live `ls-remote` checked first.

## Flags

- None new. The three standing flags (gloss overreach, `|q| = 1` domain,
  uncommitted `#print axioms` output) are all carried into the block itself
  as the offers and the flat Lean-status sentence, per the brief.

## What the main session does next

1. Review this block and the patch; on the author's go-ahead, push
   `e53630f` from the scratchpad clone (`shared-repo-la5`, branch
   `la5-coedit` → `main`, fast-forward) in manual permission mode — or
   `git am` the patch onto a fresh clone if the scratchpad has been cleaned.
2. Then the reply draft round (separate brief, per the standing plan).
