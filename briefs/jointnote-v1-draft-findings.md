# Findings: the joint note's two-page v1, drafted as its own PR package — prepared local-only

Brief: `briefs/jointnote-v1-draft-brief.md`. Branch **`jointnote-v1-draft`**, base SHA
**`fdc9b17`** (the worktree was cut at `0e12894`, one commit behind local `main`, and did
not contain the brief; `git merge main` fast-forwarded it to `fdc9b17` before any work,
per the brief's own instruction; the work branch was then created from that HEAD).

**What this window produced.** The two-page first version of the joint note, `NOTE-v1.md`,
drafted on branch `note-v1-draft` of a scratchpad clone of the shared repository over its
current HEAD; portable patch archived at `briefs/jointnote-v1-draft-patches/`, verified
applying clean on a pristine base with the tree hash matching exactly. **Nothing pushed
anywhere, no PR opened, no interaction with any external repository beyond read-only
clones, one read-only fetch of `refs/pull/1/head`, and `ls-remote`.** The PR is the
author's send after main-session review.

---

## 1. State check

| item | expected | found | verdict |
|---|---|---|---|
| Shared repo HEAD (`ls-remote` + fresh clone, 2026-08-03) | `7c05458` unless PR #1 merged | **`7c05458`** — unmoved | as briefed |
| PR #1 (`refs/pull/1/head`) | open | **open, unmerged**: head `accda4b`, tree `8e9b1eb` (read-only fetch; matches the round-12 record exactly) | no adaptation needed |
| L-A9 grade at `main` HEAD | DRAFT, one key | **`DRAFT — one key (Merle …). Macindoe key invited.`** — unchanged; the split-grade offer (h1–h5) sits on the PR #1 branch only | grade-at-signing marker written for exactly this state |
| `NOTE.md` at HEAD | the skeleton, §0 Gersonides porch | byte-identical to the premise-external record's description; untouched by this window | — |
| L-A8 at HEAD | two keys + kernel key, scoped | key-status lines read in full this session; scope words lifted verbatim (see table rows S39–S41) | — |
| Base for the note branch | `7c05458` | commit `265e156` over `7c05458`, tree **`9e7360e698933126854b06d3a71bbddace54597f`** | — |

## 2. The object

- **File:** `NOTE-v1.md`, new, at the shared repo's root. 61 lines. `NOTE.md` untouched.
- **Branch:** `note-v1-draft` of a scratchpad clone, local-only. One commit, `265e156`
  ("NOTE-v1.md: the two-page first version — the counting dichotomy, the located
  obstruction, the marked apparatus section; NOTE.md stands as the map for the second
  version").
- **Patch:** `briefs/jointnote-v1-draft-patches/0001-NOTE-v1.md-the-two-page-first-version-the-counting-d.patch`.
  **Verified:** applied with `git am` on a second, pristine checkout of `7c05458`
  (identity-only config) — clean apply, working tree clean, resulting tree hash
  **`9e7360e698933126854b06d3a71bbddace54597f`**, byte-identical to the drafting branch's
  tree.
- **Word count:** body (Position through "What this note does not do", excluding the
  title block, signature and references) — **1,300 words** by raw whitespace split;
  **1,249** counting each inline-code formula (`…`) as one word. The brief's target is
  ≤ ~1,200; the residual ~4–8% overage is flagged as decision 5 below with candidate
  cuts, because every remaining sentence traces to a floor item and further cutting
  starts deleting mandated content.
- **Sections** (all eight floor items, in order): title + subtitle → Position (3 ¶) →
  The counting dichotomy → The obstruction, located → The three faces → Claims resting
  on the shared verification apparatus, named → What this note does not do → signature
  block + references.

**Section list, one line each:**

1. **Title/subtitle** — the repository's own name; subtitle = the working title's own
   subordinate clause (flagged, decision 2).
2. **Position** — what the note is (a map, instruments, grades) and is not (excludes
   nothing beyond cited verified ranges); Barina `2⁷¹` with citation; Hercher with both
   clauses and the `m`-vs-`K` axis clause; the register clause in full (not first, not
   sole, not confined to awaiting-audit).
3. **The counting dichotomy** — the label as Merle's contraction of the two published
   phrases, citation attached; upper half = Theorem 4.5, "effective finiteness at every
   period", explicitly not closure; lower half = Theorem 4.6 with the all-`p` closure
   reported at its published home (the v3 *Status of the assessment* paragraph) in one
   sentence, scope inline.
4. **The obstruction, located** — the four-statements-at-four-grades sentence; Theorem
   4.6's closing sentence quoted exactly; the agreed gloss; "located, not overcome".
5. **The three faces** — size / digits / seam, one clause each; "faces precisely because
   they are not independent" once; one deferral line carrying the Gersonides mention.
6. **The marked apparatus section** — the LEDGER named with the two-key defining clause
   and the regime clause; δ8/L-A9 at its exact grade with the bracketed
   `[GRADE AT SIGNING — re-read L-A9 before signature]` marker; the L-A8/T1 fragment at
   its exact scoped language (statement match, dependency structure, committed axiom
   logs, read-not-built, the two continued-fraction glue facts outside the kernel
   claims, no end-to-end claim).
7. **What this note does not do** — no cycle excluded beyond the cited record; the
   model→certainty gap; the parked front (ours) and the conditional scope (his), one
   clause each.
8. **Signature block** — both names; credit line left as `[THE AUTHOR'S: credit wording]`,
   empty, per the standing decision.

## 3. The per-sentence verification table

Every sentence of `NOTE-v1.md`, in file order. **Grade vocabulary:** *published theorem*
(in the frozen v3 PDF/tex), *published text* (non-theorem prose in v3), *external
published* (Hercher/Barina), *ledger* (shared `LEDGER.md` at `7c05458`, entry and status
word stated), *register* (ccchallenge.org as recorded 2026-07-28), *record* (this
repository's verified findings/HANDOFF), *elementary* (verifiable by any number theorist
with no apparatus), *construction* (true of the note itself by construction), *framing*
(organizational statement, agreed between the parties, asserting no mathematics).
**Verified-at:** "tex, this session" means read directly in `paper/collatz-reduced-v3.tex`
in this window; "LEDGER @7c05458, this session" means read directly in the fresh clone;
named findings files are the round records the brief lists as context.

| # | Sentence (abbreviated where long; quotations exact) | Source | Grade | Verified at |
|---|---|---|---|---|
| S1 | Title: "One obstruction, three faces" | shared repo name; `NOTE.md` line 1 | agreed title | clone @`7c05458`, this session |
| S2 | Subtitle: "The Collatz cycle problem between size, digits, and the local–global seam — first version." | `NOTE.md` working title, verbatim clause | agreed working title; **flagged** (decision 2) | clone @`7c05458`, this session |
| S3 | "This is the two-page first version …, confined by agreement to the counting dichotomy and the located obstruction." | Merle R12 §12 proposal + author's acceptance + R12 §10 commitment | record | `merle-round12-letter.md` §12; HANDOFF item 1 |
| S4 | "`NOTE.md` … stands as the map for the second, full version; nothing here supersedes it." | brief instruction; `NOTE.md` untouched in the patch | construction | patch, this session |
| S5 | "This note is a map, not an exclusion: … every claim at a stated grade — theorem, machine-checked statement, or measurement." | his round-10 framing accepted ("maps the resistance"); true of the file | framing + construction | brief §"what is agreed"; the note itself |
| S6 | "It excludes nothing beyond the cited verified ranges." | floor item 2; true of the file | construction | the note itself |
| S7 | "The verified frontier is Barina's: every start below `2⁷¹` reaches 1 [3]." | Barina, J. Supercomputing 81 (2025) | external published | v3 `\bibitem{barina}`, tex this session; `publication.md` pin |
| S8 | "Hercher [2] proves … at least 92 local minima (Theorem 23, `m ≥ 92`, on verified range `704·2⁶⁰`) and more than `1.375·10¹¹` odd members (Corollary 29, needing verification only to `1536·2⁶⁰ = 3·2⁶⁹`)." | Hercher 2023, abstract/Def. 4/Thm 23/Cor. 29 | external published | `jointnote-premise-external-findings.md` item 2 (arXiv v3 read 2026-07-28); `merle-la8-t1-check-findings.md` §(g) |
| S9 | "The machine-checked exclusion below instantiates `2048·2⁶⁰ = 2⁷¹`: the asymmetry runs in Hercher's favour on hypothesis and conclusion alike." | `704 < 1536 < 2048`; conclusion ratio `q₂₃/35031771147 = 3.9258` | record (three integer comparisons + one ratio) | premise-external §2.3, recomputed there in-session; his §11(3) adopts it |
| S10 | "(`m` counts local minima, `K` odd members; only `K` is on the axis of the exclusion below.)" | Hercher's own definitions; the axis clause | external published + record | premise-external item 2.1; his §11(3) adopts the clause |
| S11 | "Machine-checking of the cycle literature is not new here either: … Böhm–Sontacchi 1978 … formalised, audited and accepted; Knight 2026 … being formalised; Eliahou 1993 … Lean 4 formalisation awaiting audit." | ccchallenge.org register | register (as of 2026-07-28; **CHECK-AT-SEND 4**) | premise-external item 1 |
| S12 | "This note contributes location, not precedence." | the whole premise record | framing, supported | both premise findings files |
| S13 | "The dichotomy is Macindoe's, published in [1]." | premise-ours verdict rows 3–4 (Supported); both halves verbatim in v3 | record + published | premise-ours §§3–4; tex, this session |
| S14 | "The label *counting dichotomy* is Merle's contraction of that paper's phrases — 'a sharp dichotomy for counting arguments' and 'the counting-limit dichotomy developed here' — … not as standing terminology." | his §11(1), verbatim commitment; both phrases character-verified in v3 | record + published text | `merle-round12-letter.md` §11; tex lines 38 & 59, this session |
| S15 | Upper half: trim uniform in `p` + effective irrationality measure ⇒ effective finiteness, "`n ≤ n₀(p) = O(p·(log₂3)^p)`" | Theorem 4.5 (`thm:uniform`) | published theorem | tex lines 207–215, this session |
| S16 | "Effective finiteness is the proved statement — not that any period is closed; this note claims no closure." | agreed geometry; 12.8.2 scope | record | his §11(1) ("The sentence will read 'effective finiteness at every period', in your words"); premise-ours §2.3(a) |
| S17 | Lower half: Thm 4.6 first sentence (near-verbatim) + notation gloss + "shows counting cannot do substantially better" | Theorem 4.6 (`thm:staircase`) + abstract | published theorem + published text (quote verbatim) | tex lines 222 & 38, this session |
| S18 | Status sentence: assessment "since been proved in the project record ([1], *Status of the assessment*)": witness at every period, `p ≥ 16` unconditional / `3 ≤ p ≤ 15` finite check / `p ∈ {2,4}` exhibition, `γ` between `3.683012` and `5.140212` | v3 Status paragraph | published text reporting the record's proof, scope inline | tex line 231, this session |
| S19 | "Every witness fails the divisibility conditions `q \| R_r`: 'sharper evidence that counting cannot do better, and no evidence about exclusion' [1]." | v3 Status paragraph, quote verbatim | published text | tex line 231, this session |
| S20 | "A note titled for one obstruction must say which it means." | his §11, adopted | record | `merle-round12-letter.md` §11 |
| S21 | "Macindoe's record carries four statements … at four grades — a proved consumption identity, an organizing heuristic, an organizing observation, and one theorem — and this note's obstruction means the theorem: the closing sentence of Theorem 4.6 …" | premise-ours §5.1 rows a–d; agreed geometry | record | `jointnote-premise-ours-findings.md` §5.1; brief |
| S22 | The quotation: "Uniform cycle exclusion therefore requires the divisibility system — equivalently, rigidity of the closed anchor walk `Σₜ ΔMₜ = 0`." | Theorem 4.6, closing sentence | published theorem, **character-verified** modulo TeX→Unicode rendering (`---` → em dash; `$\sum_t \Delta M_t = 0$` → `Σₜ ΔMₜ = 0`) | tex line 222, this session |
| S23 | Gloss: closed walk in the 2-adic anchor coordinate; counting bounds size, Thm 4.6 caps counting; "arithmetic (divisibility) input, not sharper counting" | v3 §3 (anchor), Thm 4.6, abstract (quote verbatim) | published text | tex lines 38, 222, this session |
| S24 | "Neither record proves that requirement unattainable, or attains it." | premise-ours §5.1 ("It locates, it does not obstruct"); L-A9 honest scope; 12.8.5 | record | premise-ours §5.1; LEDGER @`7c05458`, this session |
| S25 | "The obstruction is located, not overcome." | same | framing, supported | same |
| S26 | "The second version owes each face a full section; here each gets one clause." | structure | construction | the note itself |
| S27 | Size clause: element size; counting, irrationality measures, verified range; the face the dichotomy caps | v3 §4; Hercher/Barina | published + framing | tex §4; refs [2],[3] |
| S28 | Digits clause: closed walk in the 2-adic anchor coordinate; rigidity of that walk [1, §§3–4] | v3 §§3–4; Thm 4.6's walk | published | tex, this session |
| S29 | Seam clause: "`q \| R_r` is a linear condition, so it holds over ℤ exactly when it holds prime by prime — there is no local–global gap; the failure is local, at primes of `q`." | valuation criterion for divisibility (elementary); consistent with `NOTE.md` §4 / L3 (two keys) | **elementary** (spine test: verifiable with no apparatus) + published (`q \| R_r` printed in Prop. 4.1/Thm 4.6) | tex lines 184, 222; NOTE.md §4, this session |
| S30 | "Three faces, not three independent directions: they are faces precisely because they are not independent — each reads the same closure equation in a different completion." | his §11(1) verbatim reason (first two clauses); final clause organizational | record + **framing** (the one interpretive clause in the spine; flagged, decision 7) | `merle-round12-letter.md` §11(1) |
| S31 | Deferral: per-step laws, verified entries, "the elementary front door (Gersonides, 1342/43)" deferred to the second version, mapped by `NOTE.md` | NOTE.md §0; standing citation posture (Gersonides, not Mihailescu) | record; **flagged** (decision 3) | NOTE.md @`7c05458`, this session; HANDOFF standing decisions |
| S32 | Apparatus named: shared `LEDGER.md`; *two keys* defined (independent verification, fresh code or proof, neither derived from the other); "with the regime it was discharged in" | PROTOCOL.md + the two-key convention; regime column = PR #1's PROTOCOL commit | record (**CHECK-AT-SEND 3** on the regime clause) | LEDGER/PROTOCOL @`7c05458`; PR #1 head `accda4b`, this session |
| S33 | δ8 claim: Product-Bound route cannot succeed; "effective exponent `c* ≈ 0.9617`"; Dirichlet floor 2; "shut for every constant, not merely for `log₂3`" | L-A9 entry, claim block | ledger (entry's unconditional half; the la9 window confirmed the arithmetic and the impossibility) | LEDGER @`7c05458` lines 428–432, this session; `HANDOFF` round-12 L-A9 verdict |
| S34 | Scissors: reachable scale at best `X₀^{1/3}`; demanded scale *measured* `X₀^α`, `α = 0.482–0.511` over `[2⁷¹, 2⁴⁰⁰]`; "a finite-range measurement, not a proof" | L-A9 entry, scissors + honest-scope blocks | ledger, at the entry's own measured grade | LEDGER @`7c05458` lines 434, 438, this session |
| S35 | "Nothing in the entry is formalised, and nothing in it excludes a cycle; it closes one proof route." | L-A9 honest-scope block, near-verbatim | ledger | LEDGER @`7c05458` line 438, this session |
| S36 | Grade line: "one key (Merle — exact arithmetic, written-ahead canaries); the second key under review, a split grade proposed — the Dirichlet half toward two keys, the measured half permanently a measurement." | L-A9 status line at `main` HEAD + PR #1's co-edit block | ledger grade at drafting, exact | LEDGER @`7c05458` line 424; PR #1 (`accda4b`) per round-12 PR findings |
| S37 | "[GRADE AT SIGNING — re-read L-A9 before signature.]" | brief mandate | drafting marker (**CHECK-AT-SEND 2**; must be resolved before the PR opens) | brief |
| S38 | T1 statement: "no positive cycle of the odd map with minimum element `≥ 2⁷¹` and at most `3.5032·10¹⁰` odd members — the same count Hercher's `K` measures." | L-A8 closure statement ("no positive cycle with `x_min ≥ 2⁷¹` and length `n ≤ 3.5032·10¹⁰`"); `n` = odd members per offer (c); the figure is the integral window `35031771147` display | ledger (two keys + kernel key, scoped) | LEDGER @`7c05458` lines 354, 363, 365, this session |
| S39 | Chain + "fifteen kernel-checked theorems, zero `sorry`, no user axioms, committed axiom logs, the discharge depending on `propext` alone" | L-A8 chain blocks; 13→15 reconciliation (adds `ceiling_lower`, `ceiling_pinned`); `discharge_all → [propext]` | ledger (kernel claims at his stack's grade; read-not-built stated two sentences later) | LEDGER @`7c05458` lines 341, 350, 387, this session |
| S40 | Glue facts: `convPairs` exactly the in-window convergent denominators; `θⱼ > 1/(qⱼ + qⱼ₊₁)`; "independently confirmed, but outside the kernel claims" | L-A8 "remaining glue … named rather than hidden" + kernel-key scope (i) | ledger, scope words lifted | LEDGER @`7c05458` lines 352, 391, this session |
| S41 | Keys scoped: mathematics clean-room in fresh code; kernel claims by statement match, dependency structure, committed axiom logs, truth as instantiated — read, not built; no Lean toolchain on the second side; "no end-to-end machine checking is claimed or implied" | L-A8 key-status lines, verbatim scope vocabulary | ledger | LEDGER @`7c05458` lines 369, 383, 417, this session |
| S42 | "This window sits strictly inside Hercher's bound, on a stronger verification hypothesis; its value is the machine-checkable chain, not range." | offer (c): ratio `3.9258`; `3·2⁶⁹ < 2⁷¹`; "T1's differential value being the machine-checkable chain" | ledger + record | LEDGER @`7c05458` line 365; premise-external §2.3 |
| S43 | Not-do: no cycle excluded beyond the cited record; model→certainty gap both sides; "Macindoe's cycle front is parked under stated stopping rules, to reopen only with a divisibility-aware idea; Merle's formal cycle exclusions are conditional on Baker-type and verification hypotheses [1, Related work]." | README stopping rules; v3 Related work sentence on `\cite{merle}` | record + published text | README, this session; tex line 59, this session |
| S44 | "The second version owes the reader the faces in full; this one owes only honesty about its size: two pages, one obstruction, three faces, nothing excluded." | structure; honest-scope framing | construction + framing | the note itself |
| S45 | Signature: "Benjamin James Macindoe · Eric Merle" + `[THE AUTHOR'S: credit wording]` | brief; standing decision (credit language is the author's call at drafting time) | drafting placeholder (**must be resolved before the PR opens**; decision 4) | brief; HANDOFF standing decisions |
| R1 | Ref [1]: v3, Zenodo DOI 10.5281/zenodo.21730505, August 2026 | publication record | published; DOI verified **live 2026-08-03** by the round-12 PR session (not re-fetched here; **CHECK-AT-SEND 5**) | `merle-round12-pr-findings.md` §7; `publication.md` |
| R2 | Ref [2]: Hercher, J. Integer Seq. 26 (2023), Article 23.3.5; arXiv:2201.00406 | v3 bibliography + external findings | external published | tex `\bibitem{hercher}`, this session |
| R3 | Ref [3]: Barina, J. Supercomputing 81 (2025), article 810; DOI 10.1007/s11227-025-07337-0 | v3 bibliography | external published | tex `\bibitem{barina}`, this session |
| R4 | Ref [4]: ccchallenge.org, the three register keys with their status badges, "consulted 2026-07-28" | premise-external item 1 | register (**CHECK-AT-SEND 4**) | `jointnote-premise-external-findings.md` |

**Rows not closed in-session, stated plainly.** No row is open, but four rows close on
prior verified records rather than on a fresh look this session, and say so above: S8/S10
(Hercher's printed statements — read directly at the premise-external and la8 windows,
not re-fetched here; nothing in this window's scope authorized new external web reads),
S11/R4 (the register — as of 2026-07-28), R1 (the v3 DOI — resolved live 2026-08-03 by
the round-12 PR session). Everything quoted from v3 was re-read in the tex **this
session**; everything quoted from the ledger was re-read in the fresh clone at `7c05458`
**this session**. The theorem numbering 4.5/4.6 was confirmed structurally this session
(shared counter, §4's environment order: 4.1 elimination, 4.2 size balance, 4.3 ceiling,
4.4 periods 1–3, 4.5 uniform trim, 4.6 staircase), agreeing with the round-12
reconciliation's direct statement.

## 4. Naming rationale, and every flagged decision for the author

1. **File name — `NOTE-v1.md` at the root (recommendation enacted).** Rationale: it sits
   beside `NOTE.md` and sorts adjacent to it; the `-v1` says what it is (the two-page
   first version) without implying replacement of the skeleton, which the header line
   then states outright; and the root is where the repo keeps its four load-bearing
   files. Alternatives if either author prefers: `note/v1.md` (a subdirectory the repo
   does not currently have) or renaming at merge — the patch is a single new file, so a
   rename costs nothing. **The author and Merle may prefer another home; flagged.**
2. **Subtitle.** The note reuses the working title's own subordinate clause — *the
   Collatz cycle problem between size, digits, and the local–global seam* — plus "first
   version". Rationale: it is already both sides' language (his skeleton's working
   title), and inventing a new subtitle in a jointly signed document seemed the wrong
   place for unilateral creativity. Alternatives: no subtitle; or a plainer "a two-page
   joint note". **The author's call.**
3. **The Gersonides porch.** His §0 does not fit inside two pages at full length, so the
   note carries it as **one clause in the deferral sentence** ("the elementary front
   door (Gersonides, 1342/43)"), keeping the porch named, the citation posture honoured,
   and the second version's opening advertised. Options: strike the clause entirely, or
   expand to his §0's single summary line at a cost of ~35 words against an already-over
   budget. **Flagged either way, per the brief.**
4. **The credit placeholder and the name order.** `[THE AUTHOR'S: credit wording]` is
   empty, per the standing decision; nothing was drafted. The signature line reads
   "Benjamin James Macindoe · Eric Merle" — alphabetical, which happens to put the
   author first; name order is itself a credit decision and is **the author's**, with
   Merle's credit-deflection preference on file.
5. **Word count.** Body 1,300 raw / 1,249 formulas-collapsed against the brief's
   ≤ ~1,200. Candidate further cuts, in the order I would make them: (i) S20 ("A note
   titled for one obstruction must say which it means", −10); (ii) the completion clause
   of S30 (−9, see decision 7); (iii) S12 (−6); (iv) the `n₀(p)` display in S15 (−8).
   All four keep the floor intact; nothing else does.
6. **The `K` symbol is used in two senses**, both pinned locally: Hercher's `K` (odd
   members) in the Position paragraph and T1 statement, `[1]`'s `K` (total halvings)
   inside the dichotomy's notation parenthetical. The T1 sentence was reworded to "at
   most `3.5032·10¹⁰` odd members" specifically to avoid an unpinned `n ≤` collision.
   A reviewer may still prefer renaming one of them; flagged.
7. **One interpretive clause in the spine.** "— each reads the same closure equation in
   a different completion" (S30) is the sole sentence-part in the spine that is framing
   rather than citation or elementary reading. It is defensible (archimedean size,
   2-adic digits, prime-by-prime divisibility are the three completions in play) and it
   is the note's only answer to "why *faces*?" beyond the agreed negative clause — but
   it is mine, not a quotation. Strike it if the author wants a spine with zero framing.
8. **The erratum-sequence question he asked (§11 close)** is answered by events — v3 is
   published and the note cites v3 — but his *register* half (Macindoe2026 catalogued at
   the v1 DOI while v3 is canonical) is **not** the note's to fix and remains open on
   the author's side; the note simply cites [1] = v3. Recorded, no action taken.

## 5. Proposed PR description (drafted; not opened anywhere)

**Title:** *The joint note, first version: NOTE-v1.md — two pages, the counting dichotomy and the located obstruction*

**Description:**

> This PR delivers what the round-12 letter promised: the first draft of the joint note,
> as its own pull request, two pages, stating the counting dichotomy and the located
> obstruction and nothing else.
>
> - **New file `NOTE-v1.md`** at the root. `NOTE.md` is untouched and stands as the map
>   for the second version, as v1's header says.
> - **The agreed geometry, enacted:** three faces retained, "independent" dropped, with
>   your reason stated once; *counting dichotomy* introduced as your contraction of the
>   published phrases, citation attached, never free-standing; "effective finiteness at
>   every period", in the published words, with closure explicitly not claimed; the
>   titular obstruction pinned to Theorem 4.6's closing sentence, quoted exactly, with
>   the four-grades sentence saying why that one.
> - **The spine cites only published papers and elementary reading.** The two
>   apparatus-dependent items — the δ8 entry and the machine-checked fragment — sit in
>   their own marked section, each at its exact ledger grade, with the apparatus named
>   and "two keys" defined where first used.
> - **Hercher enters with both clauses** (Theorem 23 and Corollary 29, the verification
>   thresholds in one unit, the asymmetry in his favour on both axes, the `m`-vs-`K`
>   clause) and **the register clause enters in full** (not first, not sole, not
>   confined to the awaiting-audit bucket).
> - **Left open for co-editing:** the subtitle, the Gersonides line, the file name, and
>   the credit line (a bracketed placeholder — the bracket, and the grade-at-signing
>   bracket on the δ8 entry, must both be resolved before this merges).
>
> Second key: your review of this PR, per the accepted one-round-one-PR medium.

## 6. CHECK-AT-SEND markers

1. **Shared HEAD.** Re-verify `7c05458` unmoved by `ls-remote` immediately before the
   author pushes `note-v1-draft`. If PR #1 has merged first (the expected order), the
   patch still applies cleanly to any HEAD that does not itself add `NOTE-v1.md` — it is
   one new file — but re-seat the branch on the new HEAD rather than pushing a stale
   parent.
2. **The L-A9 grade line (the bracketed marker in the note).** Re-read L-A9 at signature.
   If PR #1 has merged and/or Merle has accepted offer h1, the note's grade sentence
   must be restated to the then-current ledger status (e.g. "two keys on the Dirichlet
   half, scoped; the measured half permanently a measurement") and the bracket removed.
   The bracket is a drafting marker and **must not survive into the merged note**.
3. **The regime clause** ("with the regime it was discharged in", apparatus intro). True
   once PR #1's `PROTOCOL.md` commit is merged. If — against expectation — the note lands
   before PR #1, soften to the two-key clause alone.
4. **The register sentence and ref [4].** Re-check the three ccchallenge entries at send;
   statuses move (an audit of the Eliahou formalisation could accept or reject it). Update
   the badges and the "consulted" date to the day of the push.
5. **The v3 DOI.** Verified resolving live 2026-08-03 (round-12 PR session); confirm at
   send.
6. **The two brackets** — `[THE AUTHOR'S: credit wording]` and `[GRADE AT SIGNING …]` —
   are the only non-publishable text in the file. Both are the author's to resolve; the
   PR should not be opened with either still present, or should be opened as a draft PR
   with them called out in the description.

## 7. Compliance

- Worktree base verified and corrected first: cut at `0e12894` without the brief;
  `git merge main` (fast-forward to `fdc9b17`) before any work; branch
  `jointnote-v1-draft` created from `fdc9b17`.
- Shared repo: fresh clone + `ls-remote` only; one read-only `git fetch` of
  `refs/pull/1/head` to confirm PR #1's head and tree. **No push, no PR, no fork, no
  issue, no comment, no interaction of any kind.** The note branch and its commit exist
  only in the session scratchpad; the patch in `briefs/` is the portable record.
- A leftover clone from the round-12 PR session was found in the scratchpad
  (`shared-repo/`, carrying that session's local commits) and was **left untouched**;
  this window used its own fresh clones (`note-v1-clone/`, `pristine-verify/`).
- All file edits via the Edit/Write tools; no PowerShell `Get-Content`/`Set-Content`
  touched any tracked file. `experiments/encoding_scan.py` run before the final commit:
  **RESULT: CLEAN** (recorded in the commit message).
- `HANDOFF.md`, `NOTE.md` (shared), and every pre-existing findings file: untouched.
- No verification script was written: nothing in this window needed computing — the one
  ratio and three integer comparisons the note relies on were verified at their named
  places in earlier findings, and the word counts are recorded above with their exact
  measurement convention.
- Stopping rules: nothing new is proved, no front reopens, the cycle front stays parked;
  the note itself says so in its closing section.
- Not merged; the main session reviews (patch, tree, every reachable table row) and
  merges. Stopped after Record.

---

## Review change (main session, 2026-08-03) — one edit, the patch regenerated

One substantive defect found at review and repaired in place: the δ8 paragraph paired
`c* ≈ 0.9617` with "no irrational has an effective exponent below 2" in one sentence —
the exact convention mix `briefs/merle-la9-check-findings.md` established against the
ledger entry and offer h1 exists to repair. The public note cannot repeat the defect the
same round handed back. The sentence now carries the h1 single-convention form: the
linear-form exponent with its measure equivalent `μ* = c* + 1 ≈ 1.96` beside it, the
floor stated in both conventions (`c ≥ 1`, `μ ≥ 2`), and the honest razor ("by a few
hundredths in the exponent") in place of the implied chasm. Re-verified by fresh
`git am` on a pristine `7c05458`: clean, tree **`1e8847947a5c6bc8956e7bf784694fa2837c542f`**,
superseding the pre-review `9e7360e`. Also re-verified at review directly against the
published tex: the obstruction sentence including its formula, both abstract phrases,
and `γ := K − log₂ q` as the paper's own definition (line 208) — all character-exact.
