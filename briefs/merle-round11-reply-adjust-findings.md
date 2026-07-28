# Findings: the round-11 reply adjusted for the all-`p` closure and two record defects

Brief: `briefs/merle-round11-reply-adjust-brief.md`. Branch `merle-round11-reply-adjust`.
**Base SHA `912f708`** — the worktree was cut from the stale session-start HEAD `2225b68`,
which does not contain the brief; the branch was re-cut at `912f708` before anything was read
or changed.

Five per-item commits. **Not merged** — the main session reviews and merges. **Nothing sent**;
sending is the author's. Nothing pushed, and no interaction of any kind with his repositories.
`cycles.md`, `paper/`, `sources/`, `experiments/`, `viz/` and every wiki page are untouched:
the only tracked files this branch writes are `briefs/merle-round11-reply-draft.md`, this
record, and one paragraph of `HANDOFF.md`.

`python experiments/encoding_scan.py`: **CLEAN**. Every edit was made with the Edit/Write
tools; PowerShell touched no tracked file.

---

## 1. What was added, and where

Two new sections, both inserted between *Item 4 — one theorem to hand back* and *The joint
note*, in that order, so that the joint-note section can refer back to them.

**(a) *Two defects in our own record, both ours to hand back*.**

* The `σ` defect gets three paragraphs. It says without hedging that our page carried a defect
  in the frame he works in — Remark 12.6.1.1's transport recurrence is L-A1, kernel-verified on
  his side — and that it could have misled him. It gives the correct convention
  `σ_j = s_j + m_(j+1)` with the shift named as essential, and records that the Proposition had
  it only 112 lines upstream in the `m`-solved direction.
* The substance is that **every structural guardrail is blind to it**, and all four are named:
  the trivial-cycle canary (`σ = 2` under both readings, `4^p − 3^p` either way), `K` as a
  cyclic sum, 12.6.1.4's repetition multiplicativity together with the ghost identity, and the
  transport recurrence itself — 1685/1685 under **both** conventions, with the telescoping
  reason written out rather than asserted, and the observation that both readings are cyclic
  rearrangements of the same multiset so both give `Σσ = K`.
* The canary is **offered as a tool, not as a warning about his artifacts**: three tiers, the
  published identity first (kept precisely because it accepts both), then the recurrence with
  `σ_r` spelled out, then the external `gcd = 7`. The conditional is on the artifact
  (*"if any of your artifacts build `R_r` from a profile rather than inheriting it"*), never on
  his competence.
* The `p = 92` figure is one short paragraph, per the brief: `n₀(92) = 4.78·10^21` against the
  `~10^18` the prose carried, the cause named (Theorem 12.8.1's bare rate `1.585^92 = 2.53·10^18`
  with Corollary 12.8.2's ≈1,890 factor dropped), the table recorded as right throughout, and
  nothing downstream moving.

**(b) *The staircase at every period — proved, with the scope attached*.**

* Origin is **one clause**, as briefed: his letter asked for the contribution sentence, the
  premise check found the sharpness half exactly half proved, the arc that followed is ours.
* Construction B and availability are stated as **two theorems with hypotheses**, with (H0) and
  (H1) named as hypotheses in the sentence that states the result. The missing constant —
  the additive `1/(L−1) = 1.70951` per block — is explained mechanically, together with why the
  `Θ(p)` shortfall makes any `O(1)`/`O(log p)` bound on the old move count unobtainable, and
  the greedy-versus-partial-sum negative control (29/29 against 6/29 at the same `n`).
* The availability half is written at the **sharp maxgap criterion**, stated as an iff, with
  both minimal sweeps (`J = 13`, 66 integers; `maxgap(12)` failing) and the window counts.
  The span argument ("14θ ≥ 1") that earlier drafts inherited appears nowhere.
* **Scope, in its own paragraph:** `3.683012 ≤ γ ≤ 5.140212`; unconditional for `p ≥ 16`;
  `3 ≤ p ≤ 15` by finite check at `κ ≤ 1.70`; `p ∈ {2,4}` outside Construction B's reach with
  the reason given (`Γ(2,n) = n + η`, `Γ(4,n) = 0.196191n + 1.507147 + η`, and their canonical
  windows `[2.512, 2.638]`, `[6.311, 6.626]` holding no integer). Then the three further limits
  that belong to the true statement: `Γ` conservative by `0.6`–`0.9` bits, the verification
  ceiling at `p ≈ 32` named as a limit on the check and not the theorem, and `3.683012` as the
  method's own floor.
* **What it does not settle** is its own paragraph: size-passers only, all failing `q | R_r` at
  every rotation, 12.8.5 unchanged at any grade, front still parked.
* **His pincer** is its own paragraph and is written as the brief asks: the `p = 22` episode a
  property of the candidate list and not of `log₂3`; his hypothesis named that cause and both
  closing candidates; 12.8.6.4's credit stands unchanged; the new route not needing it stated
  in terms as *the same diagnosis made general*, not a demotion. The old route is then recorded
  as closed **in the other direction** — a characterized obstruction (uniform gaps = badly
  approximable), with the semiconvergent repair's own failure (`a₁₅ = 1` after `q₁₃ = 190537`).
* Verification closes the section, with each script's independence and check count.

## 2. What was adjusted, and why it had gone stale

| passage | what changed | why |
|---|---|---|
| header, base line | second base note added: adjusted per the adjust brief, base `912f708` | new pass |
| header, *Verification* | a second paragraph: the six new records, `cycles.md` §12.8.6 read **as it now stands**, and the constants recomputed at 60 digits this session | the new material |
| header, *Two bracketed fields* | wiki-`main` pin now given as `9fdaa0f` at first drafting and `912f708` at this pass, still **CHECK AT SEND TIME**, with a note that it moves again on merge | main moved twice |
| joint note, *"Already published"* | the clause *"everything it claims is in the v2 note"* | false since the rewrite: §12.8.6 now carries a proof appearing in no published version |
| joint note, the two-loose-fits lead | now says the first stands and the second has closed | one of the two moved |
| joint note, second bullet | rewritten; carries the published-record clause | the sharpness half closed |
| *Where everything lives* | six new records with check counts, the four sub-numbers of §12.8.6, the pin | new material |
| *Where everything lives*, last line | "five findings records" → "the records named here" | there are eleven now |

**The published-record clause, exactly as briefed.** The `thm:staircase` hedge **stands as
printed** — "not proved *here*" is a statement about the paper and a later proof elsewhere does
not falsify it. What is superseded is the v2 note's identification of the remaining gap, wrong
on both halves, and the erratum correcting **only** that sentence is described as **drafted, not
issued**. The frozen-commit pointer is named as the mitigation. This sits in the joint-note
section because that is where he needs it: he may cite the paper, and should know which sentence
is which.

## 3. What was deliberately left alone

1. **The four placeholders** — personal opening; his personal paragraphs; the joint note's
   contribution sentence together with the answer to his three proposals; personal closing.
   Untouched and empty; verified in the diff, which contains no `+`/`−` line touching any of
   them.
2. **No contribution sentence, no wording for one, no outline, no genre proposal**, in the new
   material or anywhere else. The new sections state facts about our own result and stop; the
   joint-note section reports which premise moved and stops.
3. **Nothing offered for the ledger.** The staircase result is reported, not seeded — no ledger
   entry is proposed, invited or hinted at, and the reply says nothing about where the result
   might live in the shared repository. The header states this explicitly so a reviewer can see
   it was a decision.
4. **Every existing paragraph that is still accurate** — the ceiling repair, the one-sidedness
   sharpening, the repositories and the recon posture, the prior-art section, the hygiene pass,
   the four negatives, Item 4's theorem hand-back, and the remainder of the joint-note section
   (the phrase, the first loose fit, "three independent directions", the obstruction grades,
   `NOTE.md`'s current state, Face I's missing entry, `ccchallenge.org`, Hercher, the `v1` DOI
   catalogue item). Character for character; the diff touches nine hunks and no others.
5. **The first loose fit's bullet**, specifically: what we published is *effective finiteness at
   every period*, not "counting closes every period". Unchanged, and the lead sentence now names
   it as the one that stands.
6. **The four header flags**, including the `1.43823` → `1.43803265928…` correction of our own
   record. Nothing this pass found bears on any of them.
7. **The co-edit's `[PENDING]` shared-repo SHA.** A parallel session's work, not claimed here.
8. One sentence was **removed** rather than kept: *"The word 'provably' attaches to the first
   sentence and not to the second."* It was true when written and is false now — "provably"
   attaches to both halves, which is the whole point of the change.

## 4. Verification — every number checked at its named place, then recomputed

Read before drafting: the brief, the draft end to end, the six findings files the brief names,
and **`cycles.md` §12.8.6 as it now stands** (the section was rewritten at `bbedf91`, after three
of those findings files were written; where the two disagree the page wins, and the page is what
the reply describes).

Recomputed from scratch at 60 decimal digits, in this session, before anything entered the draft:

```text
theta = 8 - 5*log2(3)          0.0751874963942190927...
Gamma*                         3.68301210072111484...
delta_hi                       0.11693906650908335...
delta_hi - theta               0.04175157011486425...   (so delta_lo = 0.0415 sits inside)
-log2(1 - 2^-0.0415)           5.14021148607255300...   (rounded up: 5.140212)
1/(L-1)                        1.70951129135145477...
L-1 = log2(3/2)                0.58496250072115618...   (equal, as claimed)
maxgap(11)                     0.17293753966358997...   (fails both arcs)
maxgap(12)                     0.09775004326937088...   (two-sided fails)
maxgap(13)                     0.07518749639421909... = theta exactly
two-sided arc length           0.07543906650908335...   ( > theta )
0.05*L^15, 0.05*L^16           50.03..., 79.30...
Gamma(2,.)  coeff / const      1.0 / 0.0                (i.e. n + eta)
Gamma(4,.)  coeff / const      0.19619119786... / 1.50714688945...
L^2, 1.05*L^2                  2.51210..., 2.63771...   (no integer)
L^4, 1.05*L^4                  6.31067..., 6.62621...   (no integer)
CF of log2 3, q0=q1=1          q9 = 15601, q13 = 190537, a15 = 1
1.585^92                       2.5275e18
n0(92) / 1.585^92              1890.4
25217 = 15601 + 9616           yes;   31202 = 2*15601   yes
```

All agreed with `cycles.md` §12.8.6 and with the findings files at their named places.

The `σ` claims were re-derived independently, in fresh code written in this session:

* trivial-cycle identity `R = 4^p − 3^p` at `p ∈ {1,2,3,4,7}` — **passes under both readings**;
* `gcd(q, R_r)` at 12.8.3's `p = 7` seed — `{7}` correct, `{1}` misread, at every rotation;
* transport recurrence with `σ` read **self-consistently** with the implementation —
  1653/1653 under both conventions on this session's own draw (the findings' draw gives
  1685/1685: same fact, different draw; the reply quotes the findings' figure, which is the
  named place);
* transport recurrence with `σ_r` **spelled out** as `s_r + m_(r+1)` — correct convention
  1672/1672, misreading 143/1672, failing first at `r = 0`.

## 5. Numbers I could not verify at their named place — one, and it is minor

`experiments/staircase_allp_construction.py` publishes **no total check count**: its committed
output ends at `total failed checks: 0` and its findings file names no figure. The reply
therefore writes *"0 failures"* for that script and gives counts only for the two that publish
them (`92` and `45`) and for `record_defects_check.py` (`40`). Nothing else in the added
material lacked a named place.

Two further items recorded rather than used:

* `briefs/staircase-gamma-upper-findings.md`'s two printed upper bounds pointed the wrong way
  (`Γ* ≤ 3.683012100721`, `θ ≤ 0.075187496394` are truncations, hence lower bounds). That was
  repaired on `main` at `61cebc8` before this pass; the reply prints values with an ellipsis and
  rounds only in the direction the claim needs.
* `briefs/staircase-status-apply-findings.md` §2.1 records `Γ(5,17)`/`Γ(6,17)` recomputed as
  `3.7414`/`3.2396` against the gamma-upper findings' `3.750`/`3.256`. Neither figure enters
  `cycles.md` and neither enters the reply.

## 6. For the reviewer

1. That the scope travels with **every** statement of the result, not only with the paragraph
   that owns it. Three places state it: the added section's headline sentence (which carries
   `p ≥ 16` / finite check / `p ∈ {2,4}` inline), its dedicated *Scope* paragraph, and the
   joint-note section's second bullet (inline again). A fourth, the section heading, points at
   the scope rather than stating it.
2. That the pincer paragraph reads as credit rather than as demotion, which is a register
   judgment and the one place in this pass where register is load-bearing.
3. That the `σ` paragraph offers the canary without implying anything about his artifacts.
4. That the diff touches only the nine hunks listed in §2 (`git diff 912f708 -U0`).
5. The wiki-`main` pin: it is `912f708` here and **will be wrong the moment this merges**. It
   is marked CHECK AT SEND TIME in both places it appears.
