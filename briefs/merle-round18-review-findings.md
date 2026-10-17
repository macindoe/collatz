# Findings: round-18 review window — PR #8 verified (the L-A10 amendment, the reading note, the collatz-lab.org collaboration block clause by clause), Gersonides' year settled to the sources, Knight's citation settled, review drafted unposted

Brief: `briefs/merle-round18-review-brief.md`. Branch **`merle-round18-review`**.

**Base SHA: `66295183bab76b235e356d922fc53c25b83309d9`** (the brief's own commit on `main`). The worktree was cut at `946e0d8`. `git merge --ff-only 6629518` was run first and was a clean fast-forward.

Register: flat, calibrated prose. Every number carries its named source or this session's derivation, and every amendment carries its source. No correspondent tooling is recorded here: his PR body's last line is omitted, per the standing policy. Nothing outward was done: no review, comment, push or email. Only read-only `gh`, fresh clones into the scratchpad, and web reads.

Reproduce the check (from the repository root, network required):

    python experiments/merle_r18_check.py > experiments/merle_r18_check_output.txt

Result: **65 checks, 0 failures**, 2026-10-18. A second run gave byte-identical output.

---

## 1. Provenance, as verified (2026-10-18)

| item | brief | actual (own clone / `gh`) | status |
|---|---|---|---|
| PR #6 | merged by Merle 2026-10-02 | MERGED `2026-10-02T06:48:33Z` by `ericmerle3789`, merge commit `bb1510e69c5e…` | match |
| PR #7 | merged by Merle 2026-10-02 | MERGED `2026-10-02T06:48:50Z` by `ericmerle3789`, merge commit `474125de06e1…` (base retargeted to `main` after #6) | match |
| pre-merge `2dbb364` on `round-16` | applies our two round-16 notes | "Round 16, pre-merge: the review's two notes applied.", 3 files `+3/−3` (LEDGER, campaign map, R16 letter); the L-A8 block now names `q₂₂` for `0.5727` | match |
| shared repo `main` HEAD | — | **`474125d`** (the PR #7 merge) | — |
| PR #8 | open, `031c454`, one commit, base `main`, `+136/−0`, three files, no reviews or comments | OPEN, head `031c454f54c5…`, parent `474125d`, `+3/0` LEDGER, `+72/0` block, `+61/0` letter; `reviews: []`, `comments: []`, `MERGEABLE` | match |
| branches | — | `round-18` `031c454`, `round-17` `afabf89`, `round-16` `2dbb364`, `round-15` `f882132`, `round-14` `d5cc7f1`, `round-13` `f336e57`, `round-12` `accda4b`, `note-v1-draft` `96ccadf` | recorded |
| his Lean repo | `8cb8a98` (check) | **moved to `e80b63e`**: `50d0a1c` and `e80b63e`, 2026-10-02, "Erratum 2026-10-02: …". Four files: `README.md`, `experiments/README.md`, `recheck-v4.34/RECHECK.md` (the build command corrected to name the six modules), `rounds/README.md` (round 11 §13 recorded as adopted). No Lean file changed. | recorded flat |
| his Junction repo | `8bcee67` (check) | **moved to `710dfaf`**: one commit, 2026-10-02, "README states the repository proves no cycle exclusion", `README.md` `+17/−1` | recorded flat |

His letter names `bb1510e` and `474125d`; both were confirmed from our own `gh` read and clone, not taken from the letter. Both repository movements are part of his §3 errata. Neither touches anything of ours.

---

## 2. Item A — the two ledger amendments

### 2.1 L-A10 (A.1) — holds

- At `031c454`, L-A10 equals the entry at `474125d` plus exactly one line, placed directly beneath its `Key status: one key (Merle).` line. No line was removed or altered, and every other entry is byte-identical (script PART 1).
- The added line quotes "The second key turns on L-A10." `gh pr view 4 --json reviews` shows exactly one APPROVED review by `macindoe` (`2026-09-12T14:45:58Z`), and its body contains that sentence verbatim.
- The head of the ledger gains the reading note and one blank line, nothing else. **Verdict: holds.** The second key is offered in the review.

### 2.2 The reading note (A.2) — correct as to the five, incomplete as a rule

For each entry at both SHAs (script PART 2; identical at both SHAs except L-A10's added line), the table gives the opening line, the last `Key status` occurrence, and our record's standing (HANDOFF item 1, "Ledger state").

| entry | opens with | last `Key status` occurrence (or the governing `Status` sentence) | our record | reads correctly under "last `Key status` line"? |
|---|---|---|---|---|
| L1 | `**Claim as proposed:**` | none; `Status: corrected (both directions)` | corrected | rule does not reach it |
| L2 | `**Claim:**` | none; `Status: two keys (2026-07-16)` | two keys | rule does not reach it |
| L3 | `**Claim:**` | none; `Status: two keys (2026-07-17)` + "Macindoe key turned on the correction" | two keys, correction accepted | rule does not reach it |
| L-A1 | `DRAFT — for co-editing` | none; "Status: both keys turned on the mathematics; Lean artifact pending" (in the DRAFT body), then "Lean key now turned … both keys" | two keys + kernel | rule does not reach it |
| L4 | `DRAFT — for co-editing` | none, and no `Status:` either; "Both keys turned at measured grade" in the body | two keys, measured | rule does not reach it |
| L-A2 | `DRAFT — for co-editing` | none; "Status: **two keys**" in the Merle key-turn | two keys | rule does not reach it |
| L-A3 | `DRAFT — for co-editing` | none; "Status: **two keys**" in the co-edit block | two keys | rule does not reach it |
| L-A4 | `DRAFT — one key` | none; "Status: **two keys**" inside our key-turn paragraph | two keys | **named by him, but there is no later `Key status` line to govern** |
| L-A5 | `Two keys (…)` | "Key status, honestly: … *(Condition met, 2026-07-24 … two keys)*" | two keys | yes, via the condition-met note |
| L-A6 | `DRAFT — one key` | "Key status: **two keys**" | two keys | yes |
| L-A7 | `DRAFT — one key` | "Key status (2026-07-26): two keys, scope stated." | two keys | yes |
| L-A8 | `DRAFT — one key` | **"Key status on this block: one key (Merle); Macindoe's invited"** (the round-16 block); before it, "Kernel key status (2026-07-28): two keys" | two keys, including the round-16 block (our approving PR #6 review, 2026-09-26) | **no — the last line reads one key** |
| L-A9 | `DRAFT — one key` | **"Key status: split grade, turn-with-offer … The entry's status stays DRAFT until offer h1 is accepted."**, with no condition-met note. h1's acceptance (Merle, 2026-08-17, "Second key: this round-13 pull request's review turns it") sits *above* it. | Dirichlet half two keys (our PR #3 review, 2026-09-03: "The Dirichlet half turns two keys as unconditional theorem-grade, single-convention; the scissors half stays measured, permanently") | **no — the last line reads DRAFT pending** |
| L-A10 | `Seeded at one key …` | "Key status: one key (Merle)." with the round-18 italic amendment beneath | two keys | **only if the rule reads the amendment beneath the line** |
| L-A11 | `**Claim.**` | "Key status: two keys" | two keys | yes |

Findings:

1. **The five he names are exactly the set that opens `DRAFT — one key`** (script: `['L-A4','L-A6','L-A7','L-A8','L-A9']`). That part holds.
2. **Not covered by his list:** four entries open with a different superseded line, `DRAFT — for co-editing` (L-A1, L4, L-A2, L-A3), and L-A10 opens "Seeded at one key".
3. **Eight entries have no `Key status` line** (L1, L2, L3, L-A1, L4, L-A2, L-A3, L-A4), so the literal rule does not reach them. L-A4 is among his five, but its two keys are carried by a `Status:` sentence, not by a later `Key status` line.
4. **Three entries misread under the literal rule:** L-A8 (the round-16 block's one-key line is behind the record, the same kind of lag L-A10 had), L-A9 (no condition-met stamp), and L-A10 (the line itself still reads one key).

Our PR #6 review carries no explicit sentence turning the round-16 block's key; its turn is the APPROVED state under the heading "Second key — review (round 16 …)". The review draft therefore supplies the sentence for the record. A rewording of the note, with two line notes, is offered in the review (§8). **Verdict: the second key is offered on the note as written, with the rewording non-blocking. That is a judgment the author may tighten to turn-with-offer (§9).**

---

## 3. Item B — the collaboration block, clause by clause

Checked against `LEDGER.md` at **`474125d`** (his `main`) and our own record. The literature was read at source where stated (§3.1).

| # | clause | source | verdict | proposed wording (if amended) |
|---|---|---|---|---|
| 1 | header: "Per PROTOCOL §7 (publication by common agreement)" | `PROTOCOL.md` at `474125d`: §7 "Publication" exists | holds | — |
| 2 | "Since July 2026" | L1 header "correspondence 2026-07-16"; repo public 2026-07-24 (HANDOFF) | holds | — |
| 3 | "Benjamin Macindoe (independent researcher; *Reduced coordinates for the Collatz map*, v3, DOI 10.5281/zenodo.21730505)" | Zenodo API: v3 is the latest of three versions; title "Reduced coordinates for the Collatz map: exact per-step laws, …" — the block's title is the main title exactly, subtitle omitted; creator "Macindoe, Benjamin James" | holds (naming as written: the author's decision) | — |
| 4 | "each statement is checked independently on both sides, in fresh code that borrows nothing from the other side (a Lean kernel key on Merle's side for the formalised entries)" | our kernel keys are read-not-built throughout (L-A4 statement-match 2026-07-25; L-A7 `marginTarget` 2026-07-26; L-A8 kernel key 2026-07-28; the 40-declaration re-check read, round-16 findings §3); L4, L-A6's reading, and L-A9's scissors half are measured or assessed grade | **amend** | "in fresh code that borrows nothing from the other side, at the grade its entry states (some entries are measured, not proved). For the formalised entries the Lean proofs are Merle's; on Macindoe's side their statements and committed axiom logs are read and matched against the mathematics, not rebuilt." |
| 5 | "Errors are not deleted: each correction names who erred and who corrected." | ledger head ("corrections extend an entry rather than rewriting it"); L1, L3, L-A8 amendments | holds | — |
| 6 | repository line, `NOTE-v1.md` "a working note, not a publication" | `NOTE-v1.md` present at `474125d` | holds | — |
| 7 | L1: "Merle's proposal; each side refuted one claim of the other; status *corrected*" | L1 Status block | holds | — |
| 8 | L2: "Macindoe's staircase; Merle's key in fresh code"; L4: "Merle; cross-checked on both sides; measured grade" | L2 Status; L4 body "Both keys turned at measured grade" | holds | — |
| 9 | L3: "Merle's proposal, re-run and refined by Macindoe; corrected by Merle on 2026-07-24, Macindoe's key on the correction" | L3 Status (our sharpening), REQ-MATH-017 correction, "Macindoe key turned on the correction (2026-07-24)" | holds | — |
| 10 | L-A1: "simultaneous independent discovery; Lean: Merle: the p divisibility conditions of a cycle reduce to one" | L-A1 body and Lean block | holds | — |
| 11 | L-A2 "Merle's proposal, its elementary cause closed by Macindoe" / L-A4 "Merle's statement, Macindoe's multiplicative identity; Lean: Merle": "a new cycle, if any, is primitive" | L-A2 ("closed with complete elementary cause", our `prime-local-probe-findings.md`); L-A4 key-turn (identity `R_0(B^k) = R_0(B)·G_k`), ContentDescent `cycle_iff` | holds | — |
| 12 | L-A3: "Macindoe's candidate; margin quantified by Merle" | L-A3 (B) block: "quantification seeded Merle-side (REQ-MATH-014); asymptotic constants closed Macindoe-side", accepted 2026-07-25 | **amend** | "margin quantified by Merle, its asymptotic constants by Macindoe" |
| 13 | L-A5: "Merle, Lean; framework and final gloss: Macindoe. It does not prove 'the wall': the cycle −17 realises an isolated peak." | L-A5: the fixed-point-denominator frame Macindoe's; gloss per our offer (a); "the `−17` cycle is precisely such a peak, realized on the negative shore"; the wall restated as "no isolated `C = 1` peak on the positive shore". Script: `n = 7`, `K = 11`, `q = −139`, `gcd(139, 19) = 1`. | **amend** (without the shore it reads as a counterexample to the wall) | "the cycle −17 realises an isolated `C = 1` peak, on the negative shore" |
| 14 | L-A6: "Exact census for n ≤ 14 (Merle; completed by Macindoe, who proved the phantom identity)" | L-A6: our all-`S` completion (23 words); "**The ghost identity is proved exact our side**" (`3·B(W) + q = 2^{σ₀}·B(shift W)`); Merle's block: "the 2-adic ghost identity"; "phantom" occurs in this ledger only in L-A10 (the census objects) | **amend** | "who proved the ghost identity" |
| 15 | L-A7: "Margin inequality, proved twice: in the Lean kernel with constant 1/13 (Merle), on paper with the exact constant (Macindoe)" | L-A7 Key status 2026-07-26 ("at the rational `1/13` in his kernel artifact, at the true `c_gen` in ours"); script: `c_gen = 0.0793186…`, `1/13 = 0.0769… < c_gen`; our side reads `DeficitLemma` without building it (covered by #4) | holds | — |
| 16a | T1: "(L-A8; Lean: Merle; the missing half found by Macindoe)" | L-A8 2026-07-27/28 block: "The **lower half** `3^(p+1) < 2^K` was found missing in the Macindoe round-10 audit … and it was **proved afterwards**, as `ceiling_lower`" (Merle) | **amend** (as written it reads as if we proved it) | "the ceiling's missing lower half found by Macindoe's audit, proved by Merle" |
| 16b | "no positive cycle with least element ≥ 2⁷¹ and length ≤ 4.95·10¹⁰ (direct route, round 16)" | script: exact floor `49547666543`, integral (kernel canary) window `49542405870`; `4.95·10¹⁰` ≤ both (true under-statement, 3-s.f. rounding); L-A8 round-16 block: "a cycle of the odd map with `n` elements" | **amend** ("length" is the number of odd terms) | "at most 4.95·10¹⁰ odd terms" |
| 16c | "This is weaker than Hercher 2023 (1.375·10¹¹)" | Hercher, arXiv:2201.00406 / JIS 26 (2023) 23.3.5, abstract (read 2026-10-18): the bound "at least `K ≥ 1.375·10¹¹`" odd members is reached by proving that verification to `1536·2⁶⁰ = 3·2⁶⁹` suffices. Bařina's `2⁷¹` meets the premise (script). Corrigendum dated 2026-06-14 (PDF read 2026-10-18) repairs a step in the proof of Theorem 21, statement unchanged. `q₂₃ = 137528045312 → 1.375·10¹¹`. His own home page states it "together with Barina's verification". | **amend** | "weaker than what Hercher 2023 gives together with Bařina's verification (at least 1.375·10¹¹ odd terms)" |
| 16d | "Kernel statements read, not built, on Macindoe's side; two continued-fraction facts and one cancellation remain in prose." | L-A8 round-16 block: the multiples cancellation is "the third named, unformalized step". It is the same third fact our round-16 findings §2.2 checked ("Multiples cancellation", five `(j,t)` instances). Our 2026-07-28 kernel key also names `LegendreApprox.lean`'s missing axiom probe as outside it; his `e80b63e` README says "Each file except `LegendreApprox.lean` ends with `#print axioms`". | holds; one clause added for completeness | "…remain in prose, and `LegendreApprox.lean` carries no axiom probe" |
| 16e | T1 listed under "Established (two keys)" | our approving PR #6 review 2026-09-26; the ledger's own block line still reads one key (Item A) | holds (the ledger lags, not the block) | — |
| 17 | L-A9: "Merle; convention corrected by Macindoe … closed by Dirichlet's strict inequality, with a margin of about 0.04 in the exponent. The other half is measured only." | L-A9 h1 (ours), accepted 2026-08-17; script: `c* = 0.961722`, margin `1 − c* = 0.038278` → "0.0383", 1-s.f. "0.04"; the ledger itself writes "≈ 0.038" | holds ("about 0.038" would match the ledger's own figure; optional) | — |
| 18 | L-A10: "No altitude computed on a finite quotient decreases (Merle; not formalised)" | L-A10 claim and scope ("not in Lean"); two keys with PR #8 | holds | — |
| 19 | L-A11: "(Merle; reformulation by Macindoe): the balanced cycle is excluded by Knight's theorem (*Discrete Math.* 349 (2026), 114812) combined with L-A2" | L-A11: "wording Macindoe's, round-15 review — accepted", "the factor-2 accounting between the two routes is his"; Knight at Crossref (§3.1): vol. 349, issue 3, issued 2026-03, art. 114812; our round-15 adjudication of the L-A2 reduction | **amend** (issue missing; year right) | "*Discrete Math.* 349(3) (2026), 114812" |
| 20 | Records: "re-checked on a patched kernel (Lean 4.34.0, after lean4#14576): 40 declarations, standard axioms only (round 16)" | round-16 findings §3 (40 lines, all within kernel-3, read) | holds (our side's reading scope covered by #4) | — |
| 21 | Records: "Round 17 corrected our own round-14 retraction: the phantom census at p = 7, k = 8 stands, exhaustive for L ≤ 11" | round-17 findings §5 (330 faulty, 0 realised, `L ≤ 11` exhaustive) | holds | optional "(330 faulty cycles, 0 realised)" |
| 22 | "What none of this does: exclude a cycle beyond the published bounds (Bařina's verification to 2⁷¹; Hercher 2023)" | Bařina, J. Supercomputing 81 (2025), art. 810 (our paper's citation) | holds | — |
| 23 | "The site would show it in English and French, same content." | — | **flag** | the review says our approval covers the English only |
| 24 | "Attributions follow each entry's own header and its last `Key status` line" | Item A: the literal rule misreads L-A8/L-A9 | flag only | his attributions came out right regardless |

### 3.1 Literature, read at source or not

- **Knight.** Crossref record of DOI `10.1016/j.disc.2025.114812`, read 2026-10-18 (in the script): "Collatz high cycles do not exist", Kevin Knight, *Discrete Mathematics* **349**, issue **3**, article **114812**, `issued` / `published-print` 2026-03, DOI registered 2025-09-24 (copyright line "© 2025 Elsevier"). `doi.org` resolves to Elsevier PII `S0012365X25004200`. The ScienceDirect page returned 403, so it was not read beyond the publisher's deposited metadata. **Settled: *Discrete Math.* 349(3) (2026) 114812.** The block's year is right and it lacks only the issue. **Our record is wrong**: it gives "(2025)", the DOI-registration and online year. The shared ledger's L-A11 says the same, in his file.
- **Hercher.** arXiv abstract page (journal ref JIS 26, Issue 3 (2023), Article 23.3.5) read 2026-10-18; the JIS article page and its corrigendum PDF ("Corrigendum, June 14 2026") downloaded and read 2026-10-18.
- **Bařina.** Not re-read this window. Our paper's bibliography carries J. Supercomputing 81 (2025), art. 810, DOI 10.1007/s11227-025-07337-0.

---

## 4. Item C — Gersonides' year

### 4.1 Source record (read 2026-10-18)

| source | what it says | held? |
|---|---|---|
| S. Simonson, *The Mathematics of Levi ben Gershon, the Ralbag* (Stonehill College; PDF at `u.cs.biu.ac.il/~tsaban/Pdf/MathofLevi.pdf`, file dated 2005) | p. 3: "*De Numeris Harmonicis,* completed in 1343, was commissioned by Phillip de Vitry, Bishop of Meaux." p. 6: "This book was written in 1343, a year before Levi died … Philip immediately had it translated from Hebrew into Latin. The original Hebrew is now lost." No evidence for the date is given. Note 15 sends the reader to Chemla & Pahaut for a fuller description, and to Carlebach 1910 for translations. (By contrast, Simonson dates *Maaseh Hoshev* to Nissan 1321 / Elul 1322 by colophons, p. 5. No colophon is cited for *De numeris harmonicis*.) | **held, read in full** |
| *Encyclopaedia Judaica*, "Levi ben Gershom", Scientific Work section, unsigned (via encyclopedia.com) | "In 1343, Levi composed a second book on arithmetic for Philip of Vitry, bishop of Meaux. Only the Latin translation of the book has been preserved, under the title *De numeris harmonicis* …" | held (web text) |
| J. Samsó, "Levi ben Gerson", *Complete Dictionary of Scientific Biography* (via encyclopedia.com) | "In 1342 Levi wrote De harmonicis numeris, of which only the Latin translation survives." | held (web text) |
| Wikipedia, "Gersonides" | "In 1342, Gersonides wrote *On Sines, Chords and Arcs* … One year later, at the request of the bishop of Meaux, he wrote *The Harmony of Numbers*" (that is, 1343); the cited source is a popular blog post | tertiary, held |
| Britannica, "De numeris harmonicis" (topic page) | a search-result snippet gives 1343; the page returned 403 | **not held** |
| *Gersonides' Afterlife* (philarchive `COHAFR-2`) | a search-engine summary says the treatise was completed in 1342, with de Vitry's request during his stay at the papal court, late 1342 to early 1343; the page returned 403 | **not held** (summary only, unverified) |
| J. Carlebach, *Lewi ben Gerson als Mathematiker* (Berlin: J. Lamm, 1910) | the edition of *De numeris harmonicis* (pp. 125–144 per a citation in a search result); the place where an explicit or colophon date would be found | **not held** |
| K. Chemla & S. Pahaut, "Remarques sur les ouvrages mathématiques de Gersonide", in G. Freudenthal (ed.), *Studies on Gersonides*, Brill 1992, 149–191 (citation as given in Simonson's notes) | — | **not held** |
| Primary dating (colophon, Hebrew-calendar year) | none found. The Hebrew original is lost (Simonson), so any internal date would be the Latin translation's own. | not found |

### 4.2 Recommendation: **"1342/43"**

The secondary sources split (DSB/Samsó: 1342; EJ and Simonson: 1343), and none of those held gives evidence for its choice. The one account suggesting a mechanism (not held) places the commission at the papal court across the turn of 1342–43, which would explain the split. That is an inference, not a reading. "1342/43" is also what both sides keyed into L-A3, and what his `/cycles/` page now says ("En 1342 (ou 1343 selon les sources)"). If a single year is ever wanted, Carlebach 1910 is the source to read first.

### 4.3 Our own occurrences (script PART 4; tracked files, excluding this window's)

- **"1342/43" (19):** `cycles.md:138`, `TOUR.md:35`, `HANDOFF.md:55`, and 16 in `briefs/` (round-5 check brief and findings, round-5 reply brief :19, round-7 findings, jointnote files, literature-dictionary findings, wiki-consolidation-3 audit findings; full list in the output).
- **"1343" (5):** **`viz/cycle_anchor_gateway.html:706`** (public-facing badge "sealed: Gersonides, 1343"), `briefs/cycle-gateway-viz-brief.md:24`, `briefs/merle-round5-reply-brief.md:23`, `briefs/merle-round6-record-brief.md:9`, `briefs/wiki-consolidation-sweep-brief.md:46`.
- **"1342" (1):** `briefs/merle-round5-check-findings.md:372` ("treats Gersonides' 1342 result", describing Ribenboim).

Nothing was fixed in this window. The main session should change the viz badge to "1342/43". The briefs are session records and are best left as written.

---

## 5. Item D — his §3 (for information)

- **collatz-lab.org, read 2026-10-18** (home; `/cycles/`; `/research-ledger/`; footer "Cartography · v0.9.0 · 2026-10-02"). Nothing misstates our work. The home page names Benjamin Macindoe as an open collaborator ("since July 2026: shared public repository and a ledger of results checked on both sides"), and as author of *Reduced coordinates for the Collatz map* (DOI `…21730505`) and of the interactive cycle gateway. Its "seven pull requests merged, including rounds 16 and 17 on 2 October 2026" matches `gh` (PRs #1–#7 merged). Its Hercher sentence ("Hercher (2023) together with Barina's verification already implies … at least 1.375·10¹¹ odd terms") is the wording proposed for the block. `/cycles/` gives "Le cadeau de Gersonides (1342/43)", "En 1342 (ou 1343 selon les sources)", and credits Macindoe with the reminder of the Gersonides link (consistent with our record: the posture arose in our round-5 verification). `/research-ledger/` links the shared repository and makes no key claims.
- **Salikhov.** "Salikhov's 5.125 is a measure of `ln 3` (your catch, L-A7)" matches our record (`briefs/merle-la7-mu-check-findings.md` §2.1; `experiments/merle_r13_check.py` PART 3: "Salikhov 2007's 5.125 is mu(ln 3)").
- His April theorem's erratum and his repositories are his; not adjudicated.

---

## 6. Item E — "PROTOCOL §13"

`PROTOCOL.md` at `474125d` has sections 1–7 only (script). The rule is §13 of his round-11 letter, `rounds/R11-merle.md` in his Lean repo ("## 13. A PROPOSAL ABOUT THE MEDIUM …", line 799; archived on our side in `briefs/merle-round12-letter.md` §13), and his `rounds/README.md` now records it as adopted. We wrote "PROTOCOL §13" in **13 places, all in `briefs/`**. Among them are the headings of our posted reviews: round 13 (`briefs/merle-round13-review-findings.md:52`, `:561`), round 14 (`:854`), round 15 (`briefs/merle-round15-review-findings.md:211`), and rounds 16/17 (`briefs/merle-round16-17-review-findings.md:161`, `:183`). The others are in briefs and quoted ledger text. No wiki page carries it. Separately, **`HANDOFF.md` item 1 described `PROTOCOL.md` as containing "§13 the PR medium"**, which is wrong. That is corrected in this window's Item F, since the file belongs to it. Also outside our files: L-A9's acceptance block in the shared ledger says "per PROTOCOL §13". It is his text, noted in the review. Recommendation: the review accepts his offer and cites R11 §13. No change to the briefs (they are records). Future reviews use "R11 §13" until `PROTOCOL.md` carries the rule.

---

## 7. Item F — HANDOFF item 1

Brought current in place (separate commit), changing no line count before line 55, so the script's occurrence listing stays reproducible:

- PRs #6 and #7 are recorded merged (`bb1510e`, `474125d`, 2026-10-02, after `2dbb364`), and `main` HEAD is `474125d`.
- PR #8 is open at `031c454`, with this window's verdicts and our review prepared, not posted.
- The L-A8 and L-A10 bullets now say "on `main`", with the ledger's lagging key lines noted as offered in the draft. The L-A9 bullet notes its missing condition-met stamp.
- Knight's year is corrected to 2026 in item 1's three mentions.
- `PROTOCOL.md`'s contents are described correctly (§1–§7; the PR medium at R11 §13).
- Repo current values: branch heads, Lean `e80b63e`, Junction `710dfaf`.
- The site DOI pin now reads v3 (the author's decision, 2026-10-18).

Every gated clause stays in its pre-posting form: "prepared, not posted", and "two keys once the review is posted / PR #8 merges".

---

## 8. The review

Staged verbatim at `briefs/merle-round18-review-body.md` (UTF-8, no BOM). That file is the one to post; the text below is the same, quoted:

> Second key — review (round 18, per R11 §13).
>
> Verified independently on my side, fresh code throughout (`experiments/merle_r18_check.py`, 65 checks, 0 failures; imports nothing of yours; reads `LEDGER.md` from a fresh clone at `474125d` and at `031c454`, and recomputes every number of the block that our record can reproduce).
>
> **The L-A10 amendment.** Confirmed: one added line directly beneath the entry's `Key status` line; nothing else in L-A10, and nothing in any other entry, changes; the sentence it quotes, "The second key turns on L-A10.", is verbatim in my approving review of PR #4 (2026-09-12). Second key turned.
>
> **The reading note.** The five entries it names are exactly the five that open with `DRAFT — one key`. Read literally, though, "an entry's status is its last `Key status` line" still misreads three entries and does not reach eight:
>
> - **L-A8.** The last `Key status` occurrence is the round-16 block's own "Key status on this block: one key (Merle); Macindoe's invited". My approving review of PR #6 (2026-09-26) turned that key without saying so in a sentence, so for the record: the second key turns on L-A8's round-16 direct-route block.
> - **L-A9.** The last `Key status` line still says the entry "stays DRAFT until offer h1 is accepted". h1 was accepted in your block of 2026-08-17, which sits above that line, and my round-13 review (PR #3, 2026-09-03) turned the key: "The Dirichlet half turns two keys as unconditional theorem-grade, single-convention; the scissors half stays measured, permanently". A condition-met note under the line, as L-A5 and L-A7 carry, would close it.
> - **L-A10.** The `Key status` line itself still reads one key; the two keys are in the italic amendment beneath it, which the rule should say it reads.
> - **L1, L2, L3, L-A1, L4, L-A2, L-A3, L-A4** carry no `Key status` line at all. Their status is a `Status:` sentence (L-A4's sits inside my key-turn paragraph); L4 has neither, only "Both keys turned at measured grade" in its body. L-A1, L4, L-A2 and L-A3 also open with a superseded `DRAFT — for co-editing` line, and L-A10 with "Seeded at one key".
>
> A wording that reads every entry as our record does, yours to adjust:
>
> > **Reading note (Merle, 2026-10-02, round 18).** An entry's status is its last status statement — a `Key status` line or, in the earlier entries, a `Status:` sentence — read together with any dated amendment or condition-met note beneath it. Several entries still open with the line of their first version (`DRAFT — one key`: L-A4, L-A6, L-A7, L-A8, L-A9; `DRAFT — for co-editing`: L-A1, L4, L-A2, L-A3; L-A10's "Seeded at one key"); those opening lines are kept as written, and the later statement governs.
>
> Second key turned on the reading note. The rewording and the two line notes (L-A8's round-16 block, L-A9) are offered for a later round and are not blocking.
>
> **The collaboration block.** Approved for collatz-lab.org with the amendments below. Each clause was checked against `LEDGER.md` at `474125d` and against our own record; the amendments are factual only, and the wording is otherwise yours. The approval covers the English text. I cannot check the French, so keeping it in step is yours.
>
> 1. **The method sentence.** "in fresh code that borrows nothing from the other side (a Lean kernel key on Merle's side for the formalised entries)" → "in fresh code that borrows nothing from the other side, at the grade its entry states (some entries are measured, not proved). For the formalised entries the Lean proofs are Merle's; on Macindoe's side their statements and committed axiom logs are read and matched against the mathematics, not rebuilt." Every kernel key on my side has been read-not-built (L-A4, L-A7, L-A8, and the 40-declaration re-check), and L4, part of L-A6, and L-A9's scissors half are at measured or assessed grade.
> 2. **L-A3.** "margin quantified by Merle" → "margin quantified by Merle, its asymptotic constants by Macindoe". This is the entry's own attribution in block (B): quantification seeded on your side (REQ-MATH-014), the constants `c_gen`, `c_strat` closed on ours, accepted 2026-07-25.
> 3. **L-A5.** "the cycle −17 realises an isolated peak" → "the cycle −17 realises an isolated `C = 1` peak, on the negative shore". The entry restates the wall as "no isolated `C = 1` peak on the positive shore". Without the shore, the sentence reads as a counterexample to it.
> 4. **L-A6.** "who proved the phantom identity" → "who proved the ghost identity". The entry calls it the ghost identity, `3·B(W) + q = 2^{σ₀}·B(shift W)`, in both your block and my key-turn. In this ledger "phantom" names L-A10's census objects.
> 5. **T1 (L-A8).** Three changes, the rest as written:
>    - "the missing half found by Macindoe" → "the ceiling's missing lower half found by Macindoe's audit, proved by Merle". The entry's 2026-07-27/28 block says exactly that: found missing in the round-10 audit, proved by you as `ceiling_lower`.
>    - "length ≤ 4.95·10¹⁰" → "at most 4.95·10¹⁰ odd terms". The window bounds `n`, the number of odd elements. 4.95·10¹⁰ is a true under-statement of both the exact floor `49547666543` and the kernel canary's `49542405870`.
>    - "weaker than Hercher 2023 (1.375·10¹¹)" → "weaker than what Hercher 2023 gives together with Bařina's verification (at least 1.375·10¹¹ odd terms)". Hercher proves that verification to `3·2⁶⁹` suffices for that bound; `2⁷¹` meets it. Your own home page already states it this way. His 2026-06-14 corrigendum repairs a step in the proof of his Theorem 21 and changes no statement.
>
>    And one clause added to the scope sentence: "…two continued-fraction facts and one cancellation remain in prose, and `LegendreApprox.lean` carries no axiom probe". This is the one item my 2026-07-28 kernel key named outside itself, and your own 2026-10-02 README erratum says the same.
> 6. **L-A11.** "*Discrete Math.* 349 (2026), 114812" → "*Discrete Math.* 349(3) (2026), 114812". The year is right; the issue is missing.
>
> Everything else holds as written, each clause against its entry: "since July 2026"; L1, L2, L3, L4, L-A1, the L-A2/L-A4 line, L-A7 (`1/13` in the kernel, the exact `c_gen = 0.0793…` on paper), L-A9 ("about 0.04" is `0.0383` rounded) and L-A10 (two keys with this PR); both Records; and the closing sentence with Bařina's `2⁷¹`.
>
> **Your four open points.**
>
> 1. **Gersonides' year.** "1342/43" is right as it stands. The sources split: the *Dictionary of Scientific Biography* (Samsó) gives 1342, and the *Encyclopaedia Judaica* and Simonson give 1343. None of those I could read cites a colophon or a Hebrew-calendar year, and the Hebrew original is lost. "1342/43" is also what L-A3 carries on both keys.
> 2. **The DOI.** Keep v3, `10.5281/zenodo.21730505`. It is still the latest version, and pinning the version is the practice on both sides.
> 3. **The team section.** As you wrote it.
> 4. **The entries.** The amendments above.
>
> **PROTOCOL §13.** Agreed. Please add the pull-request rule to `PROTOCOL.md` in a later round; until then I cite R11 §13, as this review does. My earlier reviews also wrote "PROTOCOL §13", as does L-A9's acceptance block of 2026-08-17.
>
> **One citation for the ledger.** L-A11 cites Knight as *Discrete Math.* 349(3) (2025). The publisher's Crossref record gives volume 349, issue 3, March 2026, article 114812; the 2025 in DOI 10.1016/j.disc.2025.114812 is its registration year. The block's "(2026)" is right, and L-A11's "(2025)" is worth correcting in a later round. Our own record carries the same error, and we are correcting it on our side.
>
> **§3, for information.** Read. Nothing on collatz-lab.org (home, `/cycles/`, `/research-ledger/`, read 2026-10-18) misstates our work, and "Salikhov's 5.125 is a measure of `ln 3`" matches our L-A7 record. Your Lean repository is at `e80b63e` and the Junction repository at `710dfaf`; both moved since round 17 in README and notes files only.
>
> Thank you for the housekeeping, and for asking before the block went up.

Its structure:

1. The L-A10 amendment: key turned.
2. The reading note: key turned, with the four-bullet analysis of Item A, the proposed rewording, and the explicit record sentence for L-A8's round-16 block.
3. The collaboration block: approved with six factual amendments (Item B rows 4, 12, 13, 14, 16a–d, 19), with the rest listed as holding, and the approval limited to the English text.
4. The four open points: Gersonides 1342/43 per §4; DOI v3 pinned; naming as written; the entries are the amendments.
5. PROTOCOL §13: offer accepted, R11 §13 cited.
6. Knight's year in L-A11: correction offered, and ours acknowledged.
7. §3: one paragraph.
8. One line of thanks.

---

## 9. For the main session at merge

**Corrections to our own pages (flagged, not applied, except where this window owns the file):**

1. **Knight's year.** It is 2026, not 2025 (*Discrete Math.* 349(3) (2026) 114812). Fixed here in `HANDOFF.md` item 1 (three mentions). Still "2025" in `briefs/merle-round15-review-findings.md` (lines 1, 171, and 217, the last being our posted round-15 review text; lines 51, 63 and 83 quote his round-15 text) and in a comment at `experiments/merle_r15_check.py:337`. Those are records and may be left with a one-line note, at the main session's discretion. The shared ledger's L-A11 is his file, and the correction is offered in the review.
2. **Gersonides.** `viz/cycle_anchor_gateway.html:706` badge "sealed: Gersonides, 1343" → "1342/43". The briefs at §4.3 are records, left as they are.
3. **"PROTOCOL §13".** Nothing to edit in briefs. `HANDOFF.md` item 1's description of `PROTOCOL.md` is corrected here.

**Clauses to flip after posting.** In `HANDOFF.md` item 1:

- "our approving review is prepared, not posted (`briefs/merle-round18-review-body.md`)" → "POSTED <date/time> under `macindoe`".
- L-A10's "two keys once PR #8 merges" stays until his merge.
- The L-A8/L-A9 "offered in the round-18 review draft" → "raised in the round-18 review".

**For the author to decide:**

1. **The reading-note key.** The draft turns the second key on the note as written, with the rewording and two line notes non-blocking. The alternative is turn-with-offer: the key turns on the rewording or the line notes. The draft's choice rests on the five he names being exactly right, and on his attributions coming out right.
2. **Block amendments 1 (method) and 5d (`LegendreApprox`).** Both are calibration to our record, not error corrections in his facts. They may be softened or dropped if the author prefers to leave his description of method as written.
3. **The naming** ("Benjamin Macindoe (independent researcher; …)"), as written per the author's decision of 2026-10-18. The v3 creator field reads "Macindoe, Benjamin James", consistent.

**Wiki consequences:** none. No wiki page carries Knight's citation, L-A8's window, or the reading rule.

---

## 10. Compliance

- Branch `merle-round18-review`, base `6629518` (after `git merge --ff-only 6629518` from `946e0d8`).
- Read-only throughout. Fresh clones into the scratchpad of the shared repo, his Lean repo and his Junction repo; `gh pr view` (PRs #3, #4, #6, #7, #8) and `gh pr list`; web reads (collatz-lab.org, Crossref, Zenodo, arXiv, JIS, encyclopedia.com, Wikipedia, Simonson's PDF). No review, comment, push, email, fork or star. No command was denied.
- His PR body's tool footer is not recorded here or in the review.
- Files were edited with Write/Edit and Python file writes (LF, UTF-8). The script's output was redirected in Bash, never via PowerShell `Set-Content`.
- Reproduction: `python experiments/merle_r18_check.py > experiments/merle_r18_check_output.txt` → 65 checks, 0 failures, byte-identical on re-run (2026-10-18).
- Encoding scan before the final commit: see the commit message of the last commit on this branch.
