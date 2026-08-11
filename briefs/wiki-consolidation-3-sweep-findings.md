# Findings: wiki-consolidation-3-sweep — the pass-3 sweep branch (2026-08-12)

Brief: `briefs/wiki-consolidation-3-sweep-brief.md`. Branch `wiki-consolidation-3-sweep`.
**Base SHA `e8a0b65`** (the briefs commit) — the worktree was cut from `d09895c`, one
commit behind; the branch was created at `e8a0b65` before any work began, so it
contains the audit merge `049bda3` the brief requires.

Authority: `briefs/wiki-consolidation-3-audit-findings.md` §2, §3, §4, §7, §8 (§9
consulted for the reserved items). Every proposal was verified against the current
file before applying, located by quoted text; one audit-vs-file discrepancy was
found (item C-5 below), not material, resolved in the file's favor per the
files-win rule. `python experiments/encoding_scan.py` was run before every commit:
**CLEAN each time** (451 tracked files, 0 invalid, 0 BOM, 0 double-encoding), and
the final scan verdict is CLEAN.

Guard rails, confirmed by the diffs: no mathematical statement edited; cycles.md
12.8.5 and the PARKED wording untouched (only cycles.md's `updated:` line and the
one 12.6.1.4(a) sentence changed); README.md's stopping rules (lines 32–38)
untouched (the statistics-door edit is in the following paragraph); HANDOFF.md and
`experiments/` untouched; no network operation of any kind.

`updated: 2026-08-12` was refreshed on every page whose content changed:
index.md, publication.md, ladder.md (A); program.md, stage1.md (B); aeh.md,
anchor-digit-search.md, reverse.md, itinerary.md (C); cycles.md (D). README.md and
TOUR.md carry no front matter, so there was nothing to refresh there.

**Tally: 21 distinct edits proposed to this branch, 21 applied — 17 as proposed,
4 with stated deviations, 0 declined.** (§3 item 4 is the same edit as §2 item 2;
§2 item 7's Lagarias-sweep half was never in scope — it stays open per §9 item 5.)

---

## Commit A `ea0703f` (mechanical)

1. **§2 item 1 — index.md status paragraph, v2→v3. Applied as proposed.**
   Before: "Both papers are published — paper 1 (DOI 10.5281/zenodo.21273548) and
   the mirror paper (DOI 10.5281/zenodo.21303918) — with paper 1's v2 uploaded
   (DOI 10.5281/zenodo.21421120, publication.md)."
   After: "Both papers are published — paper 1 at v3 (DOI 10.5281/zenodo.21730505;
   v1 10.5281/zenodo.21273548, v2 10.5281/zenodo.21421120, publication.md) and the
   mirror paper (DOI 10.5281/zenodo.21303918)." — the audit's proposed clause,
   with the mirror-paper clause of the original sentence retained around it.
2. **§2 item 6 — index.md Pages-table publication.md row. Applied as proposed.**
   Status cell "sweep complete" → "novelty assessment (dated snapshot); papers
   published at v3". The "align the two" half of the proposal is satisfied by
   commit C's status-field replacement on publication.md itself.
3. **§2 item 11 — index.md aeh row. Applied with deviation (placement).** The
   audit says "append"; the row lists contents in section order, so
   "unconditional base case (13.2.4)" was inserted after "precise ensemble
   formulation (13.2)" rather than appended after "(13.6)".
4. **§2 item 5 — publication.md status surfaces. Applied, sequenced across A and
   C (stated deviation).** Line 7 (Current-state callout): "…landscape, with
   targeted checks continuing as the paper is finalized." → "…landscape, a dated
   snapshot as of 2026-08-03." The front-matter `status:` got the interim fix
   "targeted checks ongoing" → "a dated snapshot (2026-08-03)" in A, then the
   full short-standard replacement in C (§3 item 2) — the same line is touched by
   both commits because the brief assigns item 5 to A and the trim to C; after A
   the page nowhere reads as live.
5. **§2 item 7, measure half — publication.md pre-submission checklist. Applied
   as proposed.** The measure item moved from "still open" to the
   completed-items list with its pin sites: "the concrete irrationality measure
   chosen, pinned and published (Rhin 1987 — cycles.md 12.5.3/12.7.5/12.8.2,
   stage1-synthesis.md 11.8.3.11)". Pin sites re-verified in-tree before writing
   (cycles.md line "Measure, pinned. G. Rhin's effective bound … 1987";
   bridge.md's verification line names the same four sites). The
   Lagarias-bibliographies half remains in "still open" untouched, per §9 item 5.
6. **§4 item 1 — ladder.md 15.4 mis-homed pointer. Applied as proposed.**
   "(stage4.md, `11.8.5.6`)" → "(stage2.md `11.8.5.6`; consolidated as the
   Bridge, bridge.md §16)". Resolver confirms §11.8.5 → stage2.md.

Observation, recorded and not edited (not proposed by the audit): publication.md's
pinned-citations bullet for the `log_2 3` measure still says "Exact constant to be
chosen at writeup" — superseded by the same Rhin 1987 pin, but an edit there was
out of this brief's scope. Left for a future pass.

## Commit B `43f6467` (judgment — before/after quoted)

7. **§2 item 3 — program.md 11.8.8 strategy line. Applied as proposed (audit
   wording verbatim).**
   Before: "In brief: the cycle ladder (§12) is not climbed per period; work
   there serves only the uniform trim lemma."
   After: "In brief: the cycle ladder (§12) is retired and the front parked
   (12.8.5); it reopens only under README's stopping rule."
8. **§2 item 4 — stage1.md 11.8.4.5 checkpoint tail. Applied per the audit's
   content.** No formula touched: the `C = 3^d ω - 1 + 2^s` and
   `d_+ = v_2(C) - s + v_3(C)` displays above the ledger are unchanged, as is the
   "read only as a checkpoint" paragraph below it.
   Before:
   > Thus the conversion from valuation theory to reduced dynamics is only
   > partially complete:
   >
   > ```text
   > completed:
   >     parity of s,
   >     3-gain
   >
   > still open:
   >     control of C,
   >     laws for d_+,
   >     eventual refinement of ω_+
   > ```
   After:
   > The conversion from valuation theory to reduced dynamics is now closed at
   > the valuation level, on all residue classes:
   >
   > ```text
   > completed:
   >     parity of s,
   >     3-gain,
   >     control of C and the laws for d_+ (11.8.6 — stage3.md)
   >
   > open:
   >     the odd core ω_+ — by 11.8.5.6 the anchor increment
   >         (per-step laws proved, stage4.md; the unbounded-depth
   >         residue is the Bridge, bridge.md §16)
   > ```
   The "closed at the valuation level, on all residue classes" phrasing is
   stage3.md's own front-matter claim; the open item matches stage4.md's status
   ("per-step results proved; open residue → bridge.md §16").
9. **§2 item 8 — TOUR.md v2-note rows. Applied; v2-era facts preserved as
   historical per §9 item 6.**
   Line 22, before: "…— is what the published v2 note describes, and is kept
   there as the superseded formulation."
   After: "…— is what the v2 release note described, kept as the superseded
   formulation at v2's frozen DOI; v3 (2026-08-03) replaces that note with the
   *Status of the assessment* paragraph, which reports the proof and is the
   current print-side pointer."
   Line 14 parenthetical, before: "(see below — the paper's own hedge sentence
   is unchanged; the wiki carries the proof)". After: "(see below — the paper's
   own hedge sentence survives in v3, whose *Status of the assessment* paragraph
   reports the proof; the wiki carries it)". Both rest on the audit's in-tree
   verification against `paper/collatz-reduced-v3.tex` (hedge sentence survives;
   Status paragraph reports the proof).
10. **§2 item 9 — TOUR.md "assessed" vocabulary entry. Applied (the optional
    clause, taken because the brief lists items 8–9 together).**
    Before: "…remains stated that way *in print*; the wiki has since proved
    it…" After: "…remains stated that way *in print* (the assess sentence
    survives in v3, which additionally reports the proof's existence); the wiki
    has since proved it…" — the divergence sentence itself is kept; it is still
    the page's point.

## Commit C `b8b9495` (convention trims — before/after quoted where judgment-grade)

11. **§3 item 1 — aeh.md `status:`. Applied as proposed** (the audit's trimmed
    form verbatim): `status: hypothesis FORMALIZED (13.2.1); unconditional base
    case PROVED (13.2.4, every θ < 1/4); calibrated clean within three stated
    limits (13.4–13.5); genericity form proved (13.6); proof effort parked per
    stopping rules`. Everything dropped (~1,400 characters) is carried by the
    Current-state callout on the same page, re-checked clause by clause before
    the trim.
12. **§3 item 2 — publication.md `status:`. Applied as proposed:** `status:
    novelty assessment, dated snapshot (2026-08-03); papers published — paper 1
    v3 DOI 10.5281/zenodo.21730505, mirror DOI 10.5281/zenodo.21303918`. The
    dropped clauses (Inselmann/Tao verdict summary, v2 DOI) are in the
    Current-state callout and the AEH verdict, and v2's DOI is in the staircase
    verdict bullet and index.md's status paragraph.
13. **§3 item 3 — anchor-digit-search.md `status:`. Applied as proposed**
    (approved at review despite the audit's "borderline"): `status: executed
    search, clean at every endpoint (17.7.1–17.7.5; M(ω) not 2-automatic)`. The
    five batteries stay enumerated in the Current-state callout.
14. **§3 item 5 — reverse.md 14.14.5.4 theorem-header stamp. Applied with
    deviation (files-win).** The audit's proposed keep-clause ("a strengthening
    of 14.14.5.1–.3: one law covering both cases…") does not appear in the
    file; the file's actual mathematical clause was kept instead and only the
    date/branch/brief provenance dropped. Recorded as the one audit-vs-file
    discrepancy found; not material (same intent — keep the mathematics, drop
    the provenance).
    Before: "**Theorem 14.14.5.4 (the total two-case metric law).** *(Added
    2026-07-15, branch `block-map`, per `briefs/block-map-brief.md`, item 3 — a
    strengthening of the tightness paragraph above, which stands and is not
    being repaired.)*"
    After: "**Theorem 14.14.5.4 (the total two-case metric law).** *(A
    strengthening of the tightness paragraph above, which stands and is not
    being repaired.)*"
15. **§3 item 6 — itinerary.md remark-title stamp. Applied as proposed.**
    Before: "**Remark (liveness is not assumed at intermediate doors — review
    addition, 2026-07-16).**" After: "**Remark (liveness is not assumed at
    intermediate doors).**" Remark body untouched.

## Commit D `6c4d1f2` (its own commit, correspondence-adjacent)

16. **§2 item 2 / §3 item 4 — cycles.md 12.6.1.4(a) ledger-status sentence.
    Applied as proposed.** One sentence replaced; the diff was read whole before
    committing and shows exactly two changed lines in the file — the
    front-matter `updated:` (refreshed per the brief's deliverable rule) and the
    one paragraph line, within which only the target sentence differs. The Merle
    credit prose immediately before it is byte-identical. The whole remark,
    before and after (the change marked; every unmarked character is identical
    in both versions):

    > **Remark 12.6.1.4 (descent: repeated-word profiles carry no new cycles; the numerator is multiplicative under repetition).** The rotation numerator of `12.6.1` is multiplicative along profile repetition, and the multiplicativity is exactly the seam gap's. Let `B = (m_t, s_t)_(t<ℓ)` be any profile with entries `>= 1` — no closure imposed, no tuning, either sign of `q` — and let `P = B^k` (`k >= 2`) be `B` repeated `k` times, a profile of period `kℓ`. Write `n_B = Σ m_t`, `K_B = Σ s_t + n_B`, `q_B = 2^(K_B) - 3^(n_B)`; then `n_P = k·n_B`, `K_P = k·K_B`, `q_P = 2^(k·K_B) - 3^(k·n_B)`. Exactly:
    >
    > ```text
    > R_0(B^k) = R_0(B) · G_k,     G_k := Σ_(c=0)^(k-1) 3^((k-1-c)·n_B) · 2^(c·K_B),
    > ```
    >
    > and `G_k` is precisely the geometric factor of `x^k - y^k = (x - y)·Σ_c x^c y^(k-1-c)` at `x = 2^(K_B)`, `y = 3^(n_B)`, so `q_P = q_B · G_k` as well: numerator and seam gap grow by the *same* positive integer factor, `R_0(B^k) = R_0(B)·(q_P/q_B)`.
    >
    > **Proof.** Index `P`'s blocks as `cℓ + t` (`c < k` the copy, `t < ℓ` the position) and track the two exponents of `12.6.1`'s term `3^(M)·2^(S)·(2^s - 1)`. The `3`-exponent: `M_(cℓ+t)(P) = (k-1-c)·n_B + M_t(B)` — the `m`-mass strictly to the right of position `cℓ+t` is the `k-1-c` whole copies to its right plus `B`'s own tail. The `2`-exponent: unrolling `σ_j = s_j + m_(j+1)` gives `S_t = Σ_(j<t) s_j + Σ_(j=1)^(t) m_j`, and any `cℓ` consecutive indices of an `ℓ`-periodic sequence sum to `c` full periods, so `S_(cℓ+t)(P) = c·(Σ s + n_B) + S_t(B) = c·K_B + S_t(B)`. The last factor is periodic outright, `s_(cℓ+t) = s_t`. So term `cℓ+t` of `R_0(P)` is `3^((k-1-c)·n_B)·2^(c·K_B)` times term `t` of `R_0(B)`; summing over `t` inside each copy and then over `c` gives the display, and the `q` factorization is the elementary identity quoted. ∎
    >
    > Three consequences, flat. *(a) Descent.* Cancelling the common nonzero factor `G_k`: `q_P | R_0(P) ⟺ q_B | R_0(B)`. A repeated-word profile satisfies the parked divisibility condition iff its strictly smaller base does, so a cycle on `P` forces a cycle on `B`: no repeated-word family contains a *new* cycle. This is shared-ledger entry L-A4 — found by Eric Merle (correspondence 2026-07-24, his 3,600/3,600 exact checks over tuned periodic draws; entry seeded one key, his); the multiplicative identity above is this repository's clean-room re-derivation, which came out one strength level up — his entry states the biconditional in the tuned regime, while the identity needs no tuning hypothesis at all (every profile with entries `>= 1`, both signs of `q`, like `12.6.1.1`'s recurrence). **[BEFORE:]** Ledger status, honestly as of this writing: our key turn on L-A4 is prepared and pending the author's review of the shared-repo push. **[AFTER:]** Shared-ledger status: L-A4 at two keys (2026-07-25), with the kernel key on the structured half. **[end of change]** *(b) L-A2 one level up.* `gcd(q_P, R_0(P)) = gcd(q_B·G_k, R_0(B)·G_k) = G_k·gcd(q_B, R_0(B))` — the repeated-word gcd law of shared-ledger entry L-A2 re-derives in one line; "the fixed-point inheritance of L-A2, one level up" (his phrase) is accurate. *(c) Primitivity.* A cycle whose profile is a proper power `B^k` descends to a cycle on `B`; iterating, any cycle descends to one whose profile is **primitive** — not a proper power of a shorter word, the correct vocabulary for a finite word. In particular a minimal, hence any new, cycle has a primitive profile. The correspondence's "genuinely aperiodic" (Merle, 2026-07-24) is exactly this statement read at finite length. Census consistency: `-17`'s word is primitive (`12.6.1.2`).
    >
    > *Calibration.* This closes a structured refuge and opens nothing: every repeated-word profile's divisibility question collapses to its base's, so the residual content of the parked condition `q | R_0` lives entirely on primitive profiles — exactly where `12.6.1.2` already located the known nontrivial instance. No exclusion beyond the descent itself is added, no route to one is proposed, and the front stays parked (`12.8.5`; README stopping rules).
    >
    > *Verified* (fresh independent code, `experiments/merle_round8_check.py`, 2026-07-24; imports nothing from any Merle repository; exact integer arithmetic at every pass/fail decision): identity, `q`-factorization, and biconditional checked at every draw over three grids — exhaustive bases of length `1..3` with entries in `{1,2,3}`, `k ∈ {2..5}` (3,276 pairs; the 24 divisible bases all inherit upward); 300 random bases of length `4..6`, entries `1..8`, `k ∈ {2,3,4}`; and the tuned mirror of his grid (`n ∈ {24,36,60}`, 720 draws) — 4,296 `(B,k)` pairs, `12,888` exact checks, `0` failures. Canaries: trivial-cycle inheritance `([1],[1]) → B^2` (`q = R = 7`), the `(-5)`-shore square (negative-`q` inheritance), and a non-cycle square.

    The replacement's facts are the audit's, sourced to HANDOFF lines 31/35 and
    the §1(a) item-7 ledger line (L-A4 two keys 2026-07-25, ContentDescent
    kernel key on the structured half); it deliberately points nowhere new, per
    §4 item 5 (HANDOFF is the ledger-state surface).

## Commit E `3c576ad` (approved candidates)

17. **§2 item 10 — README.md statistics-door base-case clause. Applied.** This
    is an author-level edit on the author's map page: approved at review, and
    **the author's push gate is the final veto** — if the author strikes it, the
    rest of the branch stands on its own. One sentence inserted before
    "Conditional theorems record exactly what AEH buys…":
    "The hypothesis has an unconditional base case (aeh.md 13.2.4): inside the
    digit budget — every horizon rate `θ < 1/4` block per bit — it is a theorem
    at every block length, and the hypothesis proper is exactly what lies past
    that budget."
    The stopping-rules block above it (lines 32–38) is untouched.
18. **§3 item 7 — anchor-digit-search.md §17.8/§17.9 retitle only. Applied; 17.9
    with deviation.** §17.8: "(scoped 2026-07-12; executed — results in
    §17.7.1)" → "(executed; kept as the search's specification)" — the audit's
    wording exactly; the body's own first line still carries the results
    pointer. §17.9 is not fully executed (only the first visualization tier is
    built), so "executed" would overstate: "(scoped 2026-07-12; first tier built
    — `viz/anchor_digit_visualizer.html`, §17.7.1)" → "(first tier built —
    `viz/anchor_digit_visualizer.html`, §17.7.1; kept as the search's
    specification)". The collapse option was not taken on either section;
    section numbers and bodies untouched.

## Commit F `d71ca07` (structure: briefs/ supersession headers)

19. **§7 item 1 — `briefs/staircase-allp-construction-findings.md`. Applied as
    proposed** (the audit's wording, formatted as a one-line blockquote under
    the title to match the precedent on `briefs/staircase-allp-findings.md`,
    with a bold lead "Pre-rewrite numbering.").
20. **§7 item 2 — `briefs/staircase-status-audit-findings.md`. Applied as
    proposed** (bold lead "Superseded as drafts."; the audit's wording, "the
    author's P2 call" spelled out).
21. **§7 item 3 — `briefs/junction-repo-recon-findings.md`. Applied; wording
    composed per the audit's specification** (the audit prescribed content —
    "one line naming both successors and stating the posture sentence stands" —
    not verbatim text): reachability superseded by
    `briefs/junction-public-recon-findings.md`, the self-audit by
    `briefs/junction-followup-recon-findings.md`, posture sentence stands.
22. **§7 item 4 — `briefs/staircase-allp-diophantine-findings.md`. Applied as
    proposed** (approved for symmetry with item 1): the one pre-rewrite
    sub-number use ("recipe of `12.8.6.2`–`12.8.6.3`", §3 — location verified
    in-file before writing), the applied-record restatement, and the clause
    that the availability theorem cited is unchanged.

    Nothing else in any briefs/ file was touched; this findings file is its own
    commit, after F, so F's diff is exactly the four headers.

---

## Stopped on / escalations

None. The single audit-vs-file discrepancy (item 14) was resolved in the file's
favor and is recorded above; it did not change what the edit does. Nothing
material contradicted the audit, and no edit required touching a guarded surface.
