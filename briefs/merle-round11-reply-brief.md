# Brief: round-11 reply — business paragraphs only — for a delegated session

**Context required before starting (in order):** `README.md`, `AGENTS.md`, `HANDOFF.md` item 1, and this round's five findings files, which are the authority for every number, SHA and citation you write: `briefs/merle-r11-ceiling-audit-findings.md`, `briefs/junction-public-recon-findings.md`, `briefs/merle-r11-hygiene-check-findings.md`, `briefs/jointnote-premise-ours-findings.md`, `briefs/jointnote-premise-external-findings.md`. Also `briefs/merle-round10-reply-draft.md` for register and shape.

**Where a brief and a findings file disagree, the findings file wins.**

## What you are answering

Two letters from Merle, both 2026-07-27, quoted in full in `HANDOFF.md` item 1's round-11 record and in the round's briefs. The first is long and covers: the repository question answered, the `ceiling_lower` repair, our corrections accepted, two upgrades accepted, the Stirling warning answered with a reciprocal disclosure, a hygiene pass, four negative measurements, and his opening of the joint note. The second, an hour later, supersedes one paragraph: he made four repositories public.

## What this session writes, and does not

**Business paragraphs only.** The personal opening and closing, and anything answering his personal paragraphs, are the author's own — mark them as bracketed placeholders and write nothing in them. His letter's personal content this round is substantial (his training, the retraction, the "not a debt" symmetry, his own two false alarms in one week). **Do not answer any of it, and do not gloss it.**

**Two absolute exclusions:**

1. **Do not write the joint note's contribution sentence, and do not propose wordings for it.** He asked the author directly, and framed it as the thing that decides whether the note should exist. The reply carries the *facts* the premise check established and leaves a clearly marked placeholder for the author's sentence.
2. **Do not propose an outline, a spine, or a genre for the note.** Carry facts and answer what he asked. Round 10 deliberately proposed no outline; this round carries the premise-check results, which is different.

## What the reply carries

Work from the findings files; every number must be verified at its named place before you write it.

1. **The ceiling repair, verified rather than taken.** The round-10 mismatch is closed and closed further than we offered — he removed `hceil` from all four downstream signatures rather than discharging it. Say what we actually checked, because he will want to know it was checked and not accepted: all four signatures recorded verbatim at `5c9b663` and at HEAD, and every route by which a hypothesis can leave a printed signature and still travel — renamed, weakened, structure/class field, hoisted into a section `variable`/`include`/`omit` — closed one at a time, the last because `T1Structure.lean` declares no such command in its 482 lines. `ceiling_lower` unconditional in pure ℕ with `∏x > 0` proved in-file, `ceiling_pinned` exactly the two bounds, axiom logs 13 → 15 exact, DeficitLemma 10 of 10, `sorryAx` absent, the RETRACTED block standalone and where he says. **190 exact checks, 0 failures. No handbacks anywhere this round on the Lean side.**

2. **The gift: the one-sidedness sharpening.** Because `ceiling_lower` is now a theorem, a positive cycle sits only on convergents *above* `log₂3`; `q₂₂` is below, `q₂₃` above, so the first admissible north-shore scale is `q₂₃ = 137,528,045,312` — exactly Hercher's underlying threshold. His frame-prediction point lands harder than he claimed it. Ours to hand over, and it tightens *our* sentence, not his.

3. **The repositories.** Thank him for making them public and say why it mattered in his own terms (a formalisation nobody can open is a claim, not a contribution) — briefly, once. Then report the completed recon, in this order and this register:
   - What **confirmed**: the overclaim and the rewrite, verbatim; the scope banner, stronger than he described; the `k ≥ 69` clause; the two asymptotic programs; the licence account in every particular. His self-audit's substance stands.
   - What **did not match**, flat and kind, with the round-10 posture explicitly carried over — *absence of a public copy was never evidence against his account, and it is not now*: no `AUDIT_V9` in any ref of any of the four (the series stops at V8, whose 2026-03-07 verdict is the same shape three months earlier — **state this as a resemblance, not an identification**); no `STATUS.md` by that name, the role filled by `VERIFICATION.md`; and the rewrite's one straggler, `docs/PROOF_ASSEMBLY.md`, still closing *"No gap remains. The proof is unconditional for all k ≥ 3"* about the module the rest of the repository marks INVALID. That last is the one with practical consequence and should be given plainly, as the small thing it is.
   - **`LegendreApprox.lean`**: home confirmed, the diff we had recorded as NOT PERFORMED now performed — Junction copy upstream by five months, not byte-identical, the entire difference a two-line reordering of `open Real`, nothing in T1 turning on it.
   - **Flag 6 upgraded**: the preprint *defines* `S = ⌈k log₂3⌉`, so `S` is our `K` on the definition and not merely on the units argument. Two flat differences newly visible: the `− ε(k)` term, `ε = O(log k)`, dropped in his own REQ-MATH-037 transcription (read without it the inequality fails at 8 sampled `k`, worst `−4.485` at `k = 306`, all at convergents), and his `binom(S−1,k−1)` sitting `→ 1.43803` bits (the brief carried `1.43823`, copied from the findings; the closed form is `1.43803265928…`) above our `binom(K−2,n−1)`.

4. **His prior art, volunteered by us.** `PROOF_ASSEMBLY.md` §10.5, dated 17 March 2026: the dangerous `k` confined to convergent denominators of `log₂3` — the L-A8/T1 frame-prediction point, months before our rounds, on his side. He has not claimed it. **We should say it first**, plainly, with the date and the document, and with no priority language in either direction. Also record flat, so the two are never conflated later: his Range Exclusion is our uniform-trim geometry in other coordinates, and his `3^(−0.415k)` is **not** our `1.585^(−p)` — `3^0.415 = 1.5777` is `3^(2−log₂3)` while `1.585` is `log₂3` itself, and his exponent counts odd steps where ours counts blocks. The proximity is a coincidence of two constants.

5. **The hygiene pass.** Everything reconciled; nothing failed; all five scripts run here and reproducing their committed outputs. Specifically:
   - **`5.17× at j = 21` is correct.** We queried the index and we were wrong; say so in one sentence without ceremony. The stale index survives elsewhere: two different `q₂₁` in `T1Structure.lean` (lines 188 and 433) and the pre-054 `δ` in the same docstring — the sweep reached the Python and not the Lean comments.
   - **The `053` argument holds, with a precision that is a compliment**: monotonicity is valid and needs no hypothesis, but it yields `≥ 22`, not `= 22`; the equality is a separate computation at a margin of only `2.0039×`, where a factor-3 slip would have moved the answer. He ran it. The admissible set being an up-set in `j` makes his sentence general.
   - The citation claim confirmed: no altered `θ_j`/`δ` figure is cited in the shared ledger or in our correspondence.
   - **The `OUT-052` `(d-bis)` deletion**, given as the one item with a live consequence: the ledger's own L-A8 seed block cites its `median 15601` figures and the repaired script no longer produces them. Offer the remedy he himself used for 043/055/056.
   - Cor. 29's `X₀ ≥ 3·2⁶⁹`: promised, not landed. One clause, no complaint.

6. **The four negatives.** Received as offered — flat, claiming nothing.
   - His **retraction confirmed on a common footing**: the four autocorrelations reproduce *exactly* once read as the lag-1 correlation of `log aᵢ` (on raw partial quotients the same series give an order of magnitude less — infinite variance under Gauss–Kuzmin). One scope clause, put as a clause and not a correction.
   - The **chi-squared `0.00103` as a question, not a dispute**: it is a normalised distance, not a statistic (1.08–22.1 across natural binnings) and not a p-value (which would mean rejection — the opposite of his letter). Give the readings and ask which.
   - His **scoping of the golden-ratio result accepted as he wrote it** — it closes statistical-peculiarity arguments and does not touch effective diophantine input. That distinction is right and our own use of Rhin 1987 depends on it.
   - **The theorem hand-back**, the round's substantive gift: `Σᵢ log₂(1 ± 1/(3xᵢ)) = K − n·log₂3` exactly, on all four real cycles both shores — the seam identity one step at a time, so his third face is right and stronger than he states it. With the two flat corrections: "exactly `n·δ`" is a sharp bound, not an identity (equality only at the extremal cycle; on `−17`, `0.188` against `0.396`); and what is exact is **`D(x_min) = δ·(1 + 1/(27x_min²))`**, so `δ` is the per-step drift at the minimum element, sitting strictly *below* it, its factor 2 being the two-shore symmetry — where our own la8 derivation had got that 2 from a crude two-bound. **Verify that direction character by character**: it was written backwards once this round and corrected at merge. Add the `x = 1` corollary as ours. `x* = 7/3` is exact and unique but its carrying identity is a tautology — say so gently, it is the one place his letter overreads its own find.

7. **The joint note — facts only, and then hand over.** He asked one question and made three proposals. The reply reports what we checked and stops:
   - **"Already published": yes.** Both halves are paper 1 v1 (DOI 10.5281/zenodo.21273548) §4, Theorem 4.5 and Theorem 4.6, unchanged in v2. The mirror paper carries none of it.
   - **The phrase is his**, a faithful contraction of our published *"a sharp dichotomy for counting arguments"* and *"the counting-limit dichotomy developed here"*. Worth telling him, since he is proposing to put it in a referee's mouth.
   - **Two places where the fit is looser than his sentence implies**, and these are the ones a referee would find: "counting closes every period" overstates what we published, which is *effective finiteness* at every period; and the sharpness half is **exactly half proved** — the no-extension statement is a theorem by exhibited witness, while the all-`p` `γ = O(log p)` claim carries our own published hedge *"though not proved here for all p"*, unchanged in v2.
   - **"Three independent directions"**: the three faces are his architecture; our own record counts the faces of the difficulty as **two** ("cleanly in two, and only two, places"), and its characteristic move is to identify rather than separate them (12.8.4 "the same problem"; 13.6.7 "two faces of one missing genre"). "Three" survives — the drift was never one of them — but *independent* is not established by anything of ours. Give this as information, not as a veto.
   - **`NOTE.md` as it stands**: no occurrence of "dichotomy"; no abstract for a position paragraph to sit in (the opening is §0); the mapping-and-instruments genre already partly present at §7.
   - **Face I's missing ledger entry**, raised because his own header rule requires it: the δ8 impossibility has no entry in `LEDGER.md`, though the claim is in the shared README and `NOTE.md` §2/§6, and the entry §2 cites — L1 — reads `corrected`, not `two keys`. Faces II and III are clean at two keys with kernel keys on top. **This is his to seed and we have not touched it.** Note also that L-A5–L-A8 are cited nowhere in `NOTE.md`, including L-A8/T1 — the very thing a machine-checked-fragment clause would rest on.
   - **`ccchallenge.org`, all four numbers confirmed** on 2026-07-28, and his self-correction supported *twice over*: besides `Eliahou1993` at "Ready to be audited", the register's single accepted formalisation is `BohmSontacchi1978` — itself a cycle-existence paper — and `Knight2026` is being formalised. Steiner, Simons–de Weger and Hercher all listed with zero formalisations.
   - **Hercher**: `m ≥ 92` confirmed at Theorem 23, his own symbol, counting local minima — a different count from `K`, and only `K` is on the note's axis. His "strictly weaker verification hypothesis" clause is right in direction and now established for both his numbers: in units of `2^60`, Thm 23 needs 704, Cor. 29 needs 1536 = `3·2^69`, our exclusion instantiates 2048 = `2^71`.
   - One item that is ours to fix, mentioned once: `Macindoe2026` is catalogued there from the **v1** DOI while our hosting decision pins v2.
   - Then the **placeholder**: `[THE AUTHOR'S — the contribution sentence, and the answer to the three proposals]`. Write nothing inside it.

8. **The where-everything-lives map**, as every round carries: findings files, scripts and their check counts, the wiki `main` pin, and the co-edit's shared-repo SHA. The co-edit is a **parallel session's** work and is not claimed here — carry its push SHA as `[PENDING: shared-repo push — SHA to be filled at send time]`, and mark the wiki-`main` pin **CHECK AT SEND TIME** (it must be public first or no artifact pin resolves).

9. **Record** (branch commits, per item):
   - `briefs/merle-round11-reply-draft.md` — the draft, with the bracketed placeholders clearly marked and a short header listing every number cited and where it was verified.
   - `HANDOFF.md` item 1 — ONE scoped paragraph. A sibling session (`merle-round11-coedit`) edits item 1 in parallel; keep to your own lines.

## Rules

- Branch **`merle-round11-reply`**. Verify your worktree HEAD contains this brief; if not, rebase onto the `main` SHA given in your launch instructions, and state the base SHA in the draft header.
- Per-item commits. Do **not** merge — the main session reviews and merges. **Nothing is sent; sending is the author's.**
- No pushes anywhere; no interaction with his repositories.
- **Register (the author's explicit preference): flat, calibrated prose. No excitement inflation.** Heuristics labelled heuristics. Where he was right, say so once. Where he was wrong, say it once, flatly, and move on — no moral, no reassurance, no second pass. He has already done more self-correction in one letter than most correspondents do in a year; the reply does not comment on that, it just matches it.
- Encoding: Edit/Write tools only; run `experiments/encoding_scan.py` before your last commit.
- Stop after item 9.
