# Findings: verification of the pruned paper (v3 round 6, the last gate)

**Branch.** `v3r6-prune` at `0e50afb`; `main` at `29ecb1b`. Worked in `c:\Users\Ace\Documents\Collatz`
on the branch, no worktree. **Read-only on every tracked file; this findings file is the only write.**
No `git` write operation of any kind was performed (`git reflog` head is still `0e50afb`, the apply
delegate's commit). The rebuild modified `paper/collatz-reduced-v3.pdf`; it is not committed.

**Headline.** The prune did not lose a claim, a qualification, or a theorem. Every numbered
environment is byte-identical to `29ecb1b` except `Remark 3.6`, which was the intended cut; the
`gathered` display is byte-identical; the six prohibited claims are absent; all eleven survival-table
rows are located in `cycles.md` §12.8.6; the build is clean at 15 pages and the pin verifies
positively and negatively. **But the round introduced one factual regression** — the compression at
`paper` L399–400 collapsed a pre-round-*accurate* two-part Inselmann attribution into a joint claim
that is false of `Cor. 1.4` — and two smaller scoping losses. **Merge after three named fixes.**

---

## 1. Defect list, most severe first

### D1 — HIGH. The Inselmann pair: a correct attribution was broken by this round

**Where.** `paper/collatz-reduced-v3.tex` L398–402 (PDF p. 13):

> "…it is a theorem without the hypothesis and a stronger one: Inselmann's `\cite[Cor.~1.4,
> Thm.~1.10]{inselmann}`, cited in Related work, **is two-sided, uniform in the time, unconditional**,
> and runs to `4.8188…` times the classical range…"

**What is wrong.** Against `briefs/v3r3-inselmann-horizon-findings.md` §§1.3, 1.5, which quote the
source page by page:

* **Cor. 1.4** (p. 4) is `{ m : T^{⌊log₂ m/(1−log₂√3)⌋}(m) ≤ m^ε }` of natural density `1` — a
  **one-sided** upper bound, at **one** time (the endpoint), in `T`-time.
* **Thm. 1.10** (p. 5) is `{ m : ∀ 0 ≤ k ≤ (log₂(4/3))^{-1} log₂ m : (3/4)^k m^{1−ε} ≤ Syr^k(m) ≤
  (3/4)^k m^{1+ε} }` — the **two-sided** envelope, **uniform in the time**, in Syracuse steps.

So "two-sided" and "uniform in the time" are both false of `Cor. 1.4`. ("unconditional" and the
`4.8188…` ratio are true of both — the ratio is unit-free, per the same brief §5.)

**This is a regression, not an inherited flaw.** At `29ecb1b` the same passage read:

> "…is Inselmann `\cite[Cor.~1.4]{inselmann}`; his `\cite[Thm.~1.10]{inselmann}` is stronger than
> anything Hypothesis~5.1 yields here, **being two-sided, uniform in the time, and unconditional**…"

which attributes the two properties to `Thm. 1.10` alone and is correct. C13's compression merged the
two citations and carried the adjectives across. Nothing else in the paper now says what `Cor. 1.4`
is: it is named exactly once (L399), and Related work cites `\cite{inselmann}` without any theorem
number.

**Minimal repair** (the apply delegate's own proposal, which I have checked against the source and
endorse) — replace the clause with:

```
Inselmann's \cite[Cor.~1.4, Thm.~1.10]{inselmann}, cited in Related work, are unconditional and run
to $4.8188\ldots$ times the classical range at which this section's cylinder count stops, the two
measured in the same units, the second two-sided and uniform in the time.
```

A fuller alternative, one clause longer, also names what `Cor. 1.4` is: "…the second two-sided and
uniform in the time, the first the one-sided descent below `$m^{\varepsilon}$` at the corresponding
`$T$`-time."

---

### D2 — MEDIUM. The equivalence paragraph lost the agent of "given mass 0"

**Where.** `paper` L273–274 (PDF p. 11).

* At `29ecb1b`: "…with `$\dagger$` carried through and given mass `$0$` **by** `$\pi^{(L)}_{k,D}$`,
  converges in total variation…"
* Now: "…with `$\dagger$` carried through and given mass `$0$`, converges in total variation…"

**What is wrong.** The participial phrase now attaches to *the empirical distribution*, so the
sentence most naturally reads as an instruction to give `†` zero *empirical* mass. That is materially
wrong and would make the statement vacuous on that coordinate: the whole content of the
budget clause is that `†` carries positive empirical mass whose *frequency vanishes* (the paper says
so explicitly at L321–322). It is the **target** law that gives `†` mass `0` — exactly as
Hypothesis 5.1 states it, "`$B[w] = 0$` for any `$w$` containing `$\dagger$`". Two words carried the
distinction and they were cut.

**Minimal repair.** Restore `by $\pi^{(L)}_{k,D}$`.

---

### D3 — MEDIUM. `aeh.md` now contradicts itself, and two other pages contradict `aeh.md`

This is brief item 3(b), confirmed and widened.

| location | how many limits it names |
|---|---:|
| `aeh.md` L2, front-matter `status:` (changed by `d03f1ea`) | **three** — `L ≤ 2`, pooled adjudicating runs, altitude guard |
| `aeh.md` L8, *Current state* blockquote | **one** — "Bulk uniformity stands unqualified at block lengths `L ≤ 2`, which is as far as the campaign reaches." |
| `aeh.md` L151, §13.5 *Status: resolved* | **one** — "Bulk uniformity stands **unqualified** at every tested depth and cell, at block lengths `L ≤ 2`…" |
| `README.md` L40 | **two** — `L ≤ 2` and the pooling |
| `bridge.md` L71 | **one** — `L ≤ 2` |
| `paper` L428 | **three**, and the word "unqualified" does not occur (0 case-insensitive matches) |

`AGENTS.md` L24 (the status-change workflow) requires the owning page's *front matter*, its *Current
state* paragraph, **and the statement itself** to move together; only the front matter moved.
`AGENTS.md` L42 (the periodic status pass) says other pages' claims are diffed against the owning
page's front matter and "Any mismatch is a bug" — `README.md` and `bridge.md` are both mismatches now.
`AGENTS.md` L16 ("every fact lives in exactly one page") is the reason they restate it at all.

**Which document is more conservative.** The paper. "No residual discrepancy was detected … under the
stated protocol and within three limits" is strictly weaker than "uniformity stands unqualified", and
it names all three limits in full. The paper is now aligned with `aeh.md`'s front matter and ahead of
`aeh.md`'s body, `README.md` and `bridge.md`.

**What should change.** Not the paper. Bring the three body sentences up to the front matter: `aeh.md`
L8 and L151 to the front matter's three-limit form (L151 may keep its `13.6.4`(q1) pointer);
`README.md` L40 to add the altitude guard (it already has two of three); `bridge.md` L71 to point at
`aeh.md` 13.5 rather than restate, per `AGENTS.md` L16. That is a wiki edit, out of this round's
scope — but it is a live inconsistency inside one page, which the discipline forbids, and it was
created by this round's commit `d03f1ea`.

---

### D4 — MEDIUM-LOW. "the exact window chain" is now an object the paper never introduces

**Where.** §6 Discussion, `paper` L432 (PDF p. 14): "transfer-operator analysis of the exact window
chain".

C7 cut the only sentence in the document that named a window chain ("The stationary law of the exact
window chain is a `~1%`-accurate model…"). Every remaining occurrence of "chain" in the paper is
something else: "Collatz chain" (author's note, L45), Wirsching's "Markov chain on `[0,1] × Z_3^×`"
(L58), "facts chain together" (L155), "the block chain sees the Syracuse chain" (L234). The paper
calls Theorem 3.8's object "the depth-`k` window" and never "the exact window", so the design pass's
checkpoint reasoning ("it reads as the chain of Theorem 3.8's exact windows, which the paper does
define") requires the reader to assemble a name the paper does not use.

**Minimal repair.** "transfer-operator analysis of the chain of exact depth-`$k$` windows
(Theorem~`\ref{thm:onestep}`)". Note the design pass's warning still stands: do **not** rewrite it into
a claim about a stationary law.

---

### D5 — MEDIUM-LOW. The status paragraph's retired-route pointer misses the route it names

**Where.** `paper` L230 (PDF p. 9): "the note added in v2 and **the continued-fraction route it
named** are in the release description and at `\S12.8.6.3` there."

Checked in `cycles.md`: **`12.8.6.3`** (L364–366) is the *profile-plus-correction recipe* — the
rounded geometric profile and the bounded local search. The **continued-fraction / semiconvergent
route** is not there; it is at **`12.8.6.1`, *Superseded formulation*** (L329): "This statement
previously routed availability through the continued fraction of `L` … semiconvergents `n_j = q_(k-1)
+ j·q_k` … and it named as its open gap a closed-form bound on the multiplicative gap…". The v2 note
named both halves ("semiconvergents … select the exponent `n`, a rounded geometric profile builds the
climb, a bounded correction closes the last bits"), so the sentence's own noun phrase points at the
wrong subsection.

This is sharper than the item the design pass handed back at its §8.4 (`12.8.6.3` vs `12.8.6.3–.4`);
neither pass caught it.

**Minimal repair.** `at \S12.8.6.1 and \S12.8.6.3 there` (or `\S12.8.6.1--\S12.8.6.4`, which also
picks up the `p = 22` instance record).

---

### D6 — LOW-MEDIUM. "a stronger density notion" is asserted, explained nowhere, pointed at nowhere

**Where.** `paper` L380–382 (PDF p. 12): "…Inselmann `\cite{inselmann}` crossing it unconditionally
for the trajectory envelope and the first moment, in step time and **by a stronger density notion
rather than a sharper count**."

C14 cut the parenthetical that defined it (`*`-density) after landing the fact in `aeh.md` §13.3.2 —
correctly, and the landing is verified present at the pin. But the surviving sentence carries **no
pointer**, so a claim about a third party's proof technique now stands in the paper with no support
and no address, unlike every other wiki-backed claim in §5.

**Minimal repair.** Append `(\texttt{aeh.md} \S13.3.2)`.

---

### D7 — LOW-MEDIUM. Thm 1.6's content was removed, but the argument still turns on it

**Where.** `paper` L402–406 (PDF p. 13): "His `\cite[Thm.~1.6]{inselmann}` is what carries his own
passage from `$T$`-time to Syracuse time; the further passage to block time needs … a two-letter
statistic of the parity word that **neither theorem supplies**…"

At `29ecb1b` the preceding sentence stated what Thm 1.6 says ("that odd steps occupy half the schedule
to the same horizon"). It is gone, and Related work does not state it either. The reader is now asked
to accept a *negative* claim about a theorem whose statement the paper never gives. (`aeh.md` §13.3.2
does carry it — "Thm `1.6` bounds the density of the one-letter pattern `1` and gives nothing about
`10`" — but the paper's sentence has no pointer to §13.3.2 at that clause.)

**Minimal repair.** Either restore the half-clause ("a first-moment statement about odd steps") or
append the `\texttt{aeh.md} \S13.3.2` pointer, which would also fix D6 in the same sentence group.

---

### D8 — LOW. *bottom regime* is italicised at first use and glossed only at its second

`paper` L298 (p. 11) — first occurrence, `\emph{bottom regime}` with a bare `aeh.md` §13.1 pointer and
no gloss. `paper` L422 (p. 13) — second occurrence, `\emph{bottom regime}`, glossed in full ("the
fixed drainage basin of small integers, where deviations reach `$z=41$`…"). C15 deliberately kept the
Calibration copy and cut the horizon copy, but the horizon copy is the **first** one a reader meets,
and the emphasis signals a definition that is not there. Cheapest fix: swap which copy carries the
gloss.

### D9 — LOW. The same sentence is said twice, four lines apart, on page 9

* L224 (*Sharpness evidence and assessment*): "The assessment has since been **proved in the project
  record, at a scope and a shape stronger than assessed here**; the status paragraph below states what
  was proved, where, and at what scope."
* L230 (*Status of the assessment*): "…the assessment above has since been *proved* **in the project
  record, at a scope and a shape stronger than it claims**, and is not reproduced here…"

Both are correct; the redundancy is new in effect, because C6b's cross-reference now points at a
paragraph that opens by repeating the sentence containing it. Separated only by the 4-line Remark 4.7.
Optional: trim L224 to "…; the status paragraph below states what was proved, where, and at what
scope."

### D10 — LOW. `P(s = j) = 2^{-j}`'s one-line justification went, and is not in the design's cut list

`paper` L239 now reads "Under `$\pi_{k,D}$`, unconditionally: `$P(s = j) = 2^{-j}$` at every `$j < D$`,
the mass beyond the cap…". At `29ecb1b` it read "… at every `$j < D$` **(four of eight classes give
`$s=1$`, two give `$s=2$`, and the lifting shells are geometric)**, the mass beyond…". The
parenthetical is reconstructible from Theorem 3.3, which lists exactly those classes — so nothing is
lost that a reader cannot rebuild — but the removal is **not itemised anywhere in the design pass's
cut list** (C7–C17). It rides inside the §3.7 whole-section drop-in, which means C17's claim of "no
content removed, wording only" is not accurate for this item. Recorded so the round's own ledger is
complete, not because a repair is required.

### D11 — LOW (source hygiene). Version note and Author's-note heading are now one source paragraph

The blank line between `paper` L42 and `\subsection*{Author's note}` (L43) was lost in C1's
replacement. It renders correctly (PDF p. 2 shows a proper heading), and no other paragraph boundary
in the file changed. Cosmetic.

### D12 — RELEASE BLOCKER, not a paper defect

Two sentences — L42 ("The repair history, item by item, is in this version's release description") and
L230 ("…are in the release description and at `\S12.8.6.3` there") — point at a Zenodo release
description that does not exist. This is the **author's binding decision**, recorded verbatim at
`briefs/v3r6-prune-apply-brief.md` L10, and the apply delegate applied it correctly. Consequences to
carry forward: (i) v3 cannot be released until that description is written; (ii) the v2-era record pin
`72ec88e` and the six itemised definition/statement repairs that the old version note enumerated now
exist **only** in that unwritten document and in `briefs/v3r6-prune-apply-findings.md` §4. Nothing in
the repository holds them.

**Pre-existing, unchanged by this round, recorded only so a later pass does not mistake them for new:**
"door-letter alphabet" (L239) and "the door" (L428) are never defined in the paper; `$\pi_{k,D}$` is
used in §1 (L55) and Related work (L58) before its §5 definition — both are forward pointers into a
named section, and the Related-work one predates the round; `\label{prop:elim}` lost its only `\ref`
when the version note was compressed (harmless — Proposition 4.1 is still numbered and stated).

---

## 2. Orphan report — the end-to-end read

Read the built PDF page by page as a document, then the source. **No cross-reference fails to
resolve.** Mechanically: 26 labels defined, **0 undefined `\ref`**, **0 `\cite` without a `\bibitem`**,
**0 `\bibitem` uncited**; the build log carries no `LaTeX Warning`, no "undefined", no "multiply
defined", no rerun request. Every deictic pointer was traced by hand:

| pointer | resolves to |
|---|---|
| L224 "the status paragraph below" | `\paragraph{Status of the assessment (August 2026).}`, L230 — same page (p. 9) ✔ |
| L224 "the witnesses exhibited above", L230 "as the instances above do" | Theorem 4.6's `p = 7` staircase and the 84 instances at `p = 6` ✔ |
| Hyp. 5.1 "in the sense defined below" | *protected / consistent / admissible*, L304–309 ✔ |
| L309, L364 "the bound above" / "the altitude bound above" | the `$\log_2 x_{\mathrm{exit}}(n-1) \ge \log_2 x - S_n$` bound, L294–296 ✔ |
| L283 "to every frequency above" | `$f_N(w,x)$` in Hypothesis 5.1 ✔ |
| L145 "Each law above" | §3's valuation / entry-depth / absorption laws ✔ |
| L386 "the cap's single tail cell above" | the tail cell of L239 ✔ |
| L42 "reported as proved there" | the project record ✔ |

**Orphans that are real, all listed above as defects:** D4 (used-but-never-introduced: "the exact
window chain"), D6 and D7 (used-but-never-explained: "a stronger density notion"; Thm 1.6's content),
D8 (introduced-after-use: *bottom regime*), D2 and D10 (claims whose scoping/justifying clause went),
D5 (a pointer that does not cover what its own noun phrase names), D9 (a non-sequitur of repetition
rather than of logic).

**No passage reads as a non-sequitur.** The two places where connective tissue was thinnest both hold:
the `(ω ≡ 1 (8), d odd) → d_+ = 1` example at L239 survives C8 without its justification, but a reader
can rederive it from Theorem 3.3 (`s = 1` on that class), Lemma 3.4 (`s` odd ⟹ `a_+ = 0`) and
Theorem 3.5 (`m_+ = 1 + v₂(d − M(ω))`, and `d − M(ω)` is odd there) — all three printed earlier in the
same paper. And the base-case paragraph's "and with the concentration … it yields the hypothesis
outright" survives C10's removal of the Chernoff derivation with the rate and the vanishing point both
kept verbatim.

---

## 3. The six-claim sweep — done independently on the source and the extracted PDF text

| # | prohibited claim | verdict | evidence |
|---|---|---|---|
| 1 | AEH supplies the mean exponent / `E_B[m+r] = 4` past the digit budget | **ABSENT** | four occurrences, each scoped: L308 the *definition* of consistent; L314 "under `$B$` a block spends `$\mathbb{E}_B[m+r] = 4$`" (a statement about `B`); L316–320 "Where the cylinder count runs it is more, **and unconditionally: for `$\tau<1$`** … converges to `$4$` (`aeh.md` Lemma 13.2.4(g))"; L372–374 the clock's "only through the mean exponent per block …, **a conversion available here precisely because the word is exactly `$B$` here**". Denial intact and byte-identical in substance at L320–326: "`$T_N^{-1}\sum_{n<T_N}(m_n+r_n) \to 4$` **does not follow there and can fail by any amount**", closed by L330–332 "a theorem about orbits below the budget, **and not a consequence of the hypothesis above it**". |
| 2 | AEH converts a horizon into blocks per bit / carries Inselmann's endpoint into block units | **ABSENT** | see the block-time paragraph below. |
| 3 | the finite bound is about a word beginning at the sampled start | **ABSENT** | L341–346 is **byte-identical** to `29ecb1b` and says the opposite: "That fact is about the word beginning at `$x$` itself, while `$\ell_0$` is the letter of the block *after* the start's own; it is applied here to the *extended* `$(n+1)$`-letter word … of whose law the one displayed is a marginal." The `gathered` display below it is byte-identical, `$S_{n+1}$` on both lines. |
| 4 | bulk uniformity stands unqualified | **ABSENT** | `grep -c -i unqualified` on the `.tex` = **0**. Replaced at L428 by "No residual discrepancy was detected … within three limits the campaign does not reach past", all three named in full. (The word survives in `aeh.md` L8/L151, `README.md` L40, `bridge.md` L71 — D3.) |
| 5 | `13.6.4`'s union-bound mass is exact | **ABSENT** | `13.6.4` occurs once, L277, as the equivalence ("a deterministic dictionary between letters and labelled window blocks"). No mass, bound or exceptional event is attributed to it. The only "union" left, L394–397, says the union over all scales **is not controlled**. |
| 6 | any conditional drift consequence | **ABSENT** | two denials, both byte-identical to `29ecb1b`: L239 "window equidistribution at each fixed `$(k,D)$` does not control the means of the unbounded `$m_+$` and `$s$`, so **no drift or contraction statement about orbits follows from it**"; L398 "The descent consequence is **not stated here**, because it is a theorem without the hypothesis and a stronger one". |

### The block-time correction: do the survivors say what the cut copy said?

The apply delegate reports it verified copies 1 and 3 before cutting copy 2. Confirmed, and there are
in fact **three** surviving carriers, not two:

* **Copy 1 — Related work, L58** (byte-identical to `29ecb1b`, whole paragraph unchanged): "All of
  these horizons are counted in steps, and their reading in the reduced blocks of Section 5 is not
  free: it divides by a mean number of steps per block which is a theorem of the cylinder count inside
  the digit budget and, past it, neither a theorem nor a consequence of Hypothesis 5.1."
* **Copy 3 — ledger paragraph, L403–409**: "…the further passage to block time needs the frequency
  with which a Syracuse step ends a block, a two-letter statistic of the parity word that neither
  theorem supplies and that `$\pi_{k,D}$` does, so it is not available to underwrite the hypothesis:
  inside the digit budget it is a theorem of the cylinder count (`aeh.md` Lemma 13.2.4(g)), and past
  it neither a theorem nor a consequence of the hypothesis (`aeh.md` §13.2.3)."
* **Copy 4 — the horizon paragraph, L326–332** (not counted by the design pass): "Hence
  `$4\theta<\tau<1$` is `$\theta<1/4$` and `$4\theta<\tau<4.8188\ldots$` is `$\theta<1/\beta$` … —
  **arithmetic on the definition of consistency**, with the divisor in either block reading the mean
  of the target law: a theorem about orbits below the budget, and not a consequence of the hypothesis
  above it."

The cut copy 2 said three things: (i) Inselmann's horizons are in step time; (ii) the `4.8188…`
*factor* is unit-independent; (iii) the *endpoints* `1/4` and `1/β` read as blocks per bit only after
dividing by the mean exponent per block, a theorem inside the budget and neither a theorem nor a
consequence of Hypothesis 5.1 past it. **(i)** is carried by copy 1 ("counted in steps") and by L311
("stated for the one-division map — the same unit, nothing converted"). **(ii)** is carried by copy 4,
which prints the identity `$4/\beta = (1-\log_2\sqrt3)^{-1}$` explicitly. **(iii)** is carried in full
by copies 1, 3 and 4, with copy 3 the strongest (it names *why* — the two-letter statistic — and gives
both wiki addresses). **Nothing the cut copy said is missing.** The only remaining "blocks per bit" in
the paper is the clock's, at L372, with its scoping clause attached in the same sentence.

---

## 4. The eleven-claim survival table — checked in full, myself, in `cycles.md`

Checked against the file, not against the design pass's table. All eleven located. `cycles.md` has
**no commits since `9d9d1ec`** (`git log 9d9d1ec..HEAD -- cycles.md` empty), so the paper's in-text
record URL is still current.

| # | claim | located at | ✔ |
|---|---|---|---|
| 1 | `8 − 5·log₂3 = 0.0751874964…`, arc `[0.0415, 0.1169390665…]`, "any 66 consecutive integers" | `12.8.6.1` statement L303 (`θ := 8 - 5L = 0.0751874964...`), L307–308 (`δ_hi = 0.1169390665...`, `δ_lo = 0.0415`); proof L325 "**66 consecutive integers suffice and 61 do not**" | ✔ |
| 2 | window `[L^p, 1.05·L^p]` holds `0.05·L^p` integers, `79` at `p=16`, first period supplying 66 | `12.8.6.1` proof L325, one sentence: "holds `0.05·L^p` integers — exactly `50` at `p = 15` and `79` at `p = 16` — so `p = 16` is the first period supplying 66 consecutive integers" | ✔ |
| 3 | partial quotients / badly-approximable dead end | `12.8.6.1` *Superseded formulation* L329: "the multiplicative gaps in the convergent chain *are* the partial quotients, so a uniform bound on them is exactly the assertion that `L` is badly approximable" | ✔ |
| 4 | additive offset `1/(L−1) = 1.70951` per block, no correction step | `12.8.6.2` title L333 ("explicit construction; no correction step") + statement L354 ("satisfies `q <= R_r` at **every** rotation `r` — with no correction step") + *The shape…* L358 ("**geometric plus a fixed `1/(L-1) = 1.70951` per block**") | ✔ |
| 5 | `p ≥ 16` unconditional, `3 ≤ p ≤ 15` finite check, `p ∈ {2,4}` by exhibition | `12.8.6.1` L311 ("every period `p >= 16`") and L317 (the widened-scale finite check; `p ∈ {2,4}` outside reach, both windows shown empty of integers); *Scope, and what is not covered* L378 | ✔ |
| 6 | `γ ∈ [3.683012, 5.140212]`, no `p`-dependence | `12.8.6.1` display L314 with L317 "**both ends absolute constants, uniform in `p`** — no `p` occurs in either"; `12.8.6.2` *Scope, exactly* L360 "no `p`-dependence at all"; both constants reprinted at L378 | ✔ |
| 7 | end to end at `p ∈ {3,…,26}`; construction verified through `p = 32` | `12.8.6.2` *Verified* L362: `staircase_gamma_upper.py` "(`23` periods over `p ∈ {3, 5, ..., 26}`, end to end)", `staircase_allp_diophantine.py` (`p = 3...26`), "`p = 31` and `p = 32` beyond that". **The paper's status paragraph prints neither range**, so nothing in the paper depends on this row — confirming the apply delegate's refinement | ✔ |
| 8 | "from `p = 8` upward not one working witness is a convergent or semiconvergent denominator" | `12.8.6.4` *The two `p = 22` rows*, L376, final sentence — verbatim | ✔ |
| 9 | v2 route: semiconvergents, rounded geometric profile, bounded correction | **split across two subsections**: the semiconvergent/continued-fraction half at `12.8.6.1` *Superseded formulation* L329; the profile-plus-correction half at `12.8.6.3` L364–366 ("It is kept because the published v2 note names it"). See **D5** — the paper points only at `12.8.6.3` | ✔ (location refined) |
| 10 | v2 range `p ∈ {2,…,23}`, `γ/log₂p ∈ [1.828, 3.643]`; `p = 22` at `n = 25217`, `n = 31202`, `13` and `8` moves | Prop `12.8.6.4` display L371 (`p ∈ {2, 3, ..., 23}`, `γ / log_2 p ∈ [1.828, 3.643]`); *The two `p = 22` rows* L376 (`n = 25217`, `γ = 11.186`, `13` moves; `n = 31202`, `γ = 14.746`, `8` moves, "both inside `[1.828, 3.643]`") | ✔ |
| 11 | every configuration a size-passer only, all fail `q ∣ R_r` | `12.8.6` preamble L301 ("Every configuration constructed here is a **size-passer only**: all were tested against the divisibility system `q \| R_r` at every rotation and **all fail**"); `12.8.6.4` L374 ("none passes"); *Scope…* L378 ("**no evidence at all about exclusion**") | ✔ |

**Numbers recomputed, not recalled** (Python, double precision): `log₂3 = 1.584962500721156`;
`8 − 5·log₂3 = 0.07518749639…`; `1/(log₂3 − 1) = 1.70951129135…`; arc length
`0.1169390665 − 0.0415 = 0.07543906650 > θ` ✔; `0.05·(log₂3)^15 = 50.033` → 50 integers and
`0.05·(log₂3)^16 = 79.300` → 79 ✔; `Γ* = 1.05·L(L−1) + 1/(L−1) + 1 = 3.683012100…` ✔;
`−log₂(1 − 2^(−Γ*)) = 0.116939066…` ✔; `−log₂(1 − 2^(−0.0415)) = 5.140211486…` ✔. Also, for the
paper's §5: `β = 2(2−log₂3) = 0.830074999`, `1/β = 1.204710420` ✔, `4/β = (1−log₂√3)^{-1} =
4.818841679` — an exact identity ✔, and `1 − β/4 = log₄3 = 0.792481250` — exact ✔.

Also verified for `Remark 3.6`: every count the paper dropped is in `stage3.md` — `8,000` (status
header L8), `62,937` with `ω < 3000`, `d < 64` (L613), and `327,980` / `266,680` / `ω < 20,000`,
`1 ≤ d ≤ 40` / `60,000` / `ω < 2^64`, `d ≤ 200` / `1,300` / `983,954` / `3,196` / `880` at
`d ∈ {1,2,3}` / `533` / `420` (all in §11.8.6.3 *Verified*, L506).

---

## 5. What must not have moved — verified against `29ecb1b`

Method: `git show 29ecb1b:paper/collatz-reduced-v3.tex` versus the working file, both normalised to
LF (git stores LF; the checkout is CRLF), then every `\begin{env}…\end{env}` block matched by its
`\label` and compared **byte for byte**.

**Every numbered environment: IDENTICAL, except `Remark 3.6`.**

```
def:reduced  IDENTICAL      lem:absorption IDENTICAL     prop:elim     IDENTICAL
prop:block   IDENTICAL      thm:depth      IDENTICAL     cor:size      IDENTICAL
thm:equiv    IDENTICAL      rem:verify1    *** the C5 cut ***          lem:ceiling   IDENTICAL
lem:squaring IDENTICAL      thm:deltaM     IDENTICAL     thm:smallp    IDENTICAL
thm:vlaw     IDENTICAL      thm:onestep    IDENTICAL     thm:uniform   IDENTICAL
                            prop:budget    IDENTICAL     thm:staircase IDENTICAL
                                                         rem:staircase IDENTICAL
                                                         hyp:aeh       IDENTICAL (1616 chars)
                                                         lem:routing   IDENTICAL
```

Environment counts unchanged in every class (theorem 8→8, proposition 2→2, lemma 4→4, corollary 1→1,
definition 2→2, hypothesis 1→1, heuristic 1→1, remark 3→3), so **nothing is renumbered**: Definition
2.1 … Theorem 2.3, Definition 3.1 … Remark 3.10, Proposition 4.1 … Remark 4.7, Hypothesis 5.1,
Lemma 5.2, all as before, confirmed on the rendered pages.

**The other protected items, byte-compared:**

| item | verdict |
|---|---|
| the round-5 `gathered` display | **BYTE-IDENTICAL** (`\begin{gathered} … \end{gathered}`, on its two deliberate lines, `S_{n+1}` in both) |
| Hypothesis 5.1 | BYTE-IDENTICAL |
| the two-sided law (the `$\hat B$` definition, its `13.6.3`(iii)/`13.6.5` pointer, and the `Remark 1.13, footnote 4 of arXiv v7` locator) | BYTE-IDENTICAL (603 chars) |
| the `W_{k,D}` display | BYTE-IDENTICAL |
| "product names exactly two clauses" scoping | BYTE-IDENTICAL |
| the base-case statement ("Hypothesis 5.1 is a *theorem* for every admissible `(τ,θ)` with `τ<1`, equivalently for every horizon rate `θ<1/4`, at every block length") and its "assembly is Lemma 13.2.4" pointer | BYTE-IDENTICAL |
| the extended `(n+1)`-letter-word passage (R5) | BYTE-IDENTICAL |
| the drift denial (opening paragraph) | BYTE-IDENTICAL |
| "the same unit, nothing converted" | BYTE-IDENTICAL |
| the `13.2.4(g)` scoping sentence | BYTE-IDENTICAL |
| the shell-scale / triangular-array pair | BYTE-IDENTICAL |
| the closing scope paragraph | BYTE-IDENTICAL |
| **Related work and provenance**, whole paragraph (4,547 chars) | BYTE-IDENTICAL — including Wirsching's Haar-vs-`2^{-a}` distinction, Thomas's `N^{0.9999}`, Rackl, and the provenance/priority statement |
| **the author's prefatory note** | BYTE-IDENTICAL (1,116 chars) |
| **the responsibility and verification protocol** (Appendix A) | BYTE-IDENTICAL apart from the pin `1663d30 → 881c92e` (1,307 chars both) |
| **Theorem 4.4's proof outline** | BYTE-IDENTICAL (1,049 chars) |
| Contributions paragraph, §6 Discussion, bibliography | BYTE-IDENTICAL |
| the "past that range" passage | **wording-compressed** (C17's listed item); every clause preserved — vanishing `†` frequency, "not a bound on a sum over its complement", full-weight budget-exhaustion block, unbounded letter, uncontrolled `o(T_N)` tail, and the `→ 4` denial verbatim |

Citation usage: no `\bibitem` became uncited; `inselmann` 6→5 references, accounted for exactly by
C13's merge of two `\cite[…]` into one. `\label{prop:elim}` lost its only `\ref` (it lived in the old
version note) — harmless, D12 note.

### The Remark 3.6 deviation — adjudicated

The settled drop-in read "with **the two branches on which `$a_+$` is a `$3$`-adic function of `$\w$`**
constructed rather than sampled." The apply delegate narrowed it to "with the **boundary branch
`$d = h(s)$`, on which `$a_+$` is a `$3$`-adic function of `$\w$`,** and the shallow branch
`$d < h(s)$` constructed rather than sampled."

**The design's text was wrong; the landed text is right.** Three independent confirmations:

1. **Lemma 3.4 as printed.** `a_+ = 0` (`s` odd); `= min(d, h(s))` (`s` even, `d ≠ h(s)`);
   `= d + v₃(ω + (2^s−1)3^{−d})` (`s` even, `d = h(s)`). `ω` appears in exactly one case — the
   boundary `d = h(s)`. On the shallow branch `d < h(s)` the value is `min(d,h(s)) = d`, independent
   of `ω`.
2. **The paper's own pre-round text.** At `29ecb1b` Remark 3.6 read: "**Because `$a_+$` is a
   `$3$`-adic function of `$\w$` on the boundary branch `$d = h(s)$`**, that branch is constructed
   rather than sampled … and the shallow branch `$d < h(s)$` likewise." The landed text preserves that
   semantics exactly; the design's would have contradicted five rounds of settled text.
3. **`stage3.md` §11.8.6.3 L506.** "The resonant branch `d = h(s)` is **constructed rather than
   sampled** … as is the shallow branch `d < h(s)` (`533` states, `420` built)", with the reason given
   as "the two agree by accident whenever `v_3(ω + β) = 0`, so incidental sampling of that branch is
   not equivalent to testing it" — i.e. the `ω`-dependence lives on the boundary branch.

Cost: ten tokens. **Endorsed.** Two riders. (a) `stage3.md` calls it the **resonant** branch; the
paper calls it the **boundary** branch. Both print the identifier `d = h(s)`, so the pointer resolves,
but the vocabularies differ. (b) Theorem 3.7 (L151) and §5 (L234) both say flatly "`$a_+$` is a
`$3$`-adic function of `$\w$`" with no branch qualification, and Theorem 3.7 sits **directly beneath**
Remark 3.6 on PDF p. 6. Both are pre-existing and both mean something weaker and correct ("`a_+` is
determined `3`-adically, not by the finite `2`-adic residue window"), but the newly narrowed Remark now
sits three lines above an unqualified restatement of the same phrase. Not a defect; worth one glance
if a later pass touches either.

---

## 6. Build, layout and pin

### Build — rebuilt from clean

Deleted `.aux`, `.log`, `.out`, then three `pdflatex -halt-on-error -interaction=nonstopmode` passes.

| pass | exit | pages | bytes |
|---|---|---|---|
| 1 | 0 | 15 | 402,577 |
| 2 | 0 | 15 | 417,117 |
| 3 | 0 | 15 | 417,117 |

* **Overfull boxes: 0.** (`grep -i overfull` on the log: no match.)
* **Underfull boxes: 1** — `Underfull \hbox (badness 1067) in paragraph at lines 459--460`, the
  `\bibitem{lagarias}` entry ("J. C. La-garias, The 3x+1 prob-lem: an an-no-tated bib-li-og-ra-phy,
  I--II, arXiv math/0309224,"), on **page 15**. Pre-existing; the design pass recorded it in the
  repository's own log before the round.
* **Unresolved references or citations: 0.** No `LaTeX Warning` of any kind in the log;
  `Package rerunfilecheck Info: File 'collatz-reduced-v3.out' has not changed` — the run is converged
  at pass 2/3.
* **Page count: 15**, exactly the design pass's measured Plan B and the apply delegate's report.
* **Content-identical to the committed PDF: YES.** `pdftotext -layout` output of the rebuild and of
  the committed `881c92e`-lineage PDF differ in **zero** lines. Binary: same size (417,117 bytes),
  **66 bytes differ** — the `/CreationDate`, `/ModDate` and `/ID` fields only.

### Layout — every one of the 15 pages rendered at 110 dpi and looked at

**No stranded heading, no split display, no widow or orphan line, no equation in a margin.** Page by
page:

| p | contents | note |
|---|---|---|
| 1 | title, abstract, `\subsection*{Version note}` + 5 lines of it | the heading has 5 lines of body under it before the footnote rule — not stranded |
| 2 | version-note tail, Author's note (complete), §1 Introduction, Contributions | clean; "Author's note" renders as a proper heading despite D11 |
| 3 | roadmap, **Related work and provenance** (Wirsching "siblings in shape" present, mid-page) | dense but even |
| 4 | Related-work tail, §2, Def 2.1, Prop 2.2 + proof, Thm 2.3 opening | displays intact |
| 5 | Thm 2.3 proof, §3, eq. (1), Def 3.1, Lem 3.2, Thm 3.3, Lem 3.4 with its 3-case display | the `cases` display sits whole at the page foot |
| 6 | Lem 3.4 proof, Thm 3.5 + display + proof, **Remark 3.6**, Thm 3.7 + display | see the Remark-3.6 rider above |
| 7 | Thm 3.7 proof, Thm 3.8 + proof, Heuristic 3.9, Remark 3.10, §4, Prop 4.1 + display | clean |
| 8 | Prop 4.1 proof, Cor 4.2, Lem 4.3, **Thm 4.4 + proof outline**, Thm 4.5 + three displays | three displays on one page, all whole |
| 9 | Thm 4.5 proof tail, **Thm 4.6**, Sharpness paragraph, Remark 4.7, **Status of the assessment** | the densest page; the `\url{…9d9d1ec/cycles.md}` breaks inside the URL and stays inside the text block; D9's repetition is visible here |
| 10 | §5 opening (whole), the `W_{k,D}` display, Hypothesis 5.1 opening | the display sits mid-page |
| 11 | Hyp 5.1 body + its two displays, equivalence, one-limit, horizon paragraphs | both displays whole; *bottom regime* first-use is here (D8) |
| 12 | budget tail, base case, the **`gathered` display**, clock paragraph | the two-line `gathered` display is mid-page and unsplit |
| 13 | ledger paragraph (D1 is here), **Calibration**, Lemma 5.2, calibration tail | Lemma 5.2 whole on the page |
| 14 | calibration tail, §6 Discussion (whole), Appendix A (whole), References heading + 4 entries | the "References" heading has four entries under it — not stranded |
| 15 | bibliography [5]–[18], ending ~2/3 down | the underfull `lagarias` box is entry [12] here; no last-line-alone artefact |

### The pin `881c92e` — verified with `git show`, never the working tree

**Positive.** Every wiki section and script the paper names is **defined** at the pin (checked by
heading/statement pattern, not by substring):

* `stage3.md` §11.8.6.3 ✔
* `cycles.md` §12.2.3, §12.5.2, §12.5.3, §12.6.1, §12.6.2, §12.7.4, §12.7.5, §12.8.6, §12.8.6.3 ✔ (9/9)
* `aeh.md` §13.1, §13.2, §13.2.3, Lemma 13.2.4, Proposition 13.2.5, §13.3.2, §13.4, §13.5,
  Lemma 13.6.3, Theorem 13.6.4, Proposition 13.6.5, Remark 13.6.6 ✔ (12/12)
* `itinerary.md` §14.15.1.5 ✔
* `experiments/absorption_law.py`, `anchor_increment.py`, `one_step_propagation.py`,
  `period1_cycles.py`, `period2_cycles.py`, `period3_cycles.py` — all present at the pin ✔ (6/6)

And the two things this round landed are in the pinned tree: `git show 881c92e:aeh.md` contains the
`*`-density sentence (1 match) and the three-limit status line (1 match); `git show
881c92e:paper/collatz-reduced-v3.tex` contains the pruned paper (1 match on "Status of the
assessment").

**Negative.** At the **old** pin `1663d30`: `*`-density sentence — **0** matches; three-limit status
line — **0** matches; `UNQUALIFIED` status line — **1** match; pruned paper — **0** matches. The old
pin could not have supported the pruned paper's pointers, which is exactly why the bump was necessary.
A deliberate bogus anchor (`99.99.99`) returns 0, so the search is not matching everything.

**Structure.** `881c92e` touches only `paper/collatz-reduced-v3.{tex,pdf}`; `91f76e0` changes exactly
one line (the pin) plus the rebuilt PDF; `d03f1ea` changes exactly two lines of `aeh.md`. Note the
normal chicken-and-egg: `881c92e`'s own Appendix A still reads `1663d30`, because the pin naming it
lands in the child commit. That is the same pattern as the previous round's pin (`6a9183a → c2d465a`,
"the commit that contains the round") and is what the brief asked for.

---

## 7. Housekeeping

* **UTF-8 integrity.** Every touched file decodes as UTF-8, no BOM, no `U+FFFD`, and a repo-wide
  mojibake sweep (`Ã`, `â€`, `Î¸`, `â‰¤`) finds hits only inside earlier round *briefs* that quote
  those byte sequences as test patterns. Glyph counts in `aeh.md`, `29ecb1b → HEAD`: `≤` 68→68,
  `—` 197→198, `ε` 34→34, `θ` 77→78, `τ` 66→66, `†` 9→9, `β` 16→16, `π` 31→31, `ω` 43→43, `σ` 22→22,
  `δ` 10→12, `Σ` 33→33, `₂` 52→52, `√` 9→9, `⌊` 6→6, `≥` 80→80, `⊥` 7→7. The three deltas (`—`+1,
  `θ`+1, `δ`+2) are exactly the inserted `*`-density sentence's own glyphs. Clean.
* **No renumbered anchors.** `aeh.md`'s heading set is identical `29ecb1b → HEAD` (the only differing
  line is `13.3.2`'s body, which gained the `*`-density sentence in place). `cycles.md`, `stage3.md`
  and `itinerary.md` are untouched by the round. The paper's theorem numbering is unchanged (§5 above).
* **No change logs in tracked pages.** The round's additions contain no dated diary entry, no "was X,
  now Y" prose, no branch narration. Net compliance **improved**: two dated notes ("Note added in v2
  (July 2026)", "(Correction, 2026-08-01.)") were replaced by one current-status paragraph. The
  `aeh.md` `status:` field stays one clause plus pointers, per `AGENTS.md` L18.
* **Cross-page status pass** — the one failure is **D3** (`aeh.md` internally, plus `README.md` L40 and
  `bridge.md` L71 against `aeh.md`'s front matter). No other page the round touched makes a claim about
  another page's front matter that has drifted. `publication.md`'s status line ("v3 DRAFTED and
  UNPUBLISHED, DOI 10.5281/zenodo.21730505 reserved") is consistent with the new version note.
* **The two paper-only passages the design pass said to keep are still present.** `1 - \beta/4 =
  \log_4 3` at L378 (PDF p. 12), and Wirsching's "The two programmes are nonetheless **siblings in
  shape**…" at L58 (PDF p. 3). Both intact, both still absent from the wiki — so a future trim must
  land them first, exactly as C14 was handled here.

---

## 8. Merge recommendation

**Merge after named fixes.**

The round did what it set out to do: 18 pages to 15, typography untouched, every theorem statement
byte-identical, every correction from rounds 2–5 located in the post-cut file, the survival table
verified in full, a clean build, and a pin that verifies both ways. There is no reason to reject it.

**Required before merge — three one-sentence edits in `paper/collatz-reduced-v3.tex`:**

1. **D1**, L399–400 — split the Inselmann pair. A paper whose whole v3 premise is "each statement and
   scope word brought back into line with the record" must not ship a compression that made an
   attribution *less* accurate than the version it replaced.
2. **D2**, L274 — restore `by $\pi^{(L)}_{k,D}$`.
3. **D5**, L230 — widen the retired-route pointer to `\S12.8.6.1` and `\S12.8.6.3`.

**Strongly recommended in the same pass** (one clause each, no page-count risk — the page is 13 lines
short of full at p. 12 and the bibliography page has ~200 pt of slack): **D4** (name the window chain
the paper actually defines), **D6** and **D7** (one `aeh.md` §13.3.2 pointer fixes both).

**Optional:** D8, D9, D10, D11.

**Not for this branch:** **D3** is a wiki edit (`aeh.md` L8/L151, `README.md` L40, `bridge.md` L71) and
should be its own commit; **D12** is the author's, and blocks *release*, not merge.

Re-verify after the fixes: rebuild and confirm still 15 pages, since D1's repair adds roughly one line
to a paragraph that ends 6 lines above the p. 13 foot.

---

## 9. What I could not check — mandatory

1. **The primary sources.** I did not read Inselmann arXiv:2402.03276, Tao (Forum Math. Pi 10 (2022)
   e12) or its arXiv v7 footnote 4, Terras, Everett, Korec, Wirsching, Thomas, Steiner, Eliahou,
   Simons–de Weger, Hercher, Rhin, Yu, Bugeaud–Laurent, Barina, Merle, Chang or Rackl. **D1's verdict
   rests entirely on `briefs/v3r3-inselmann-horizon-findings.md`**, which states it read the source
   page by page and quotes Cor. 1.4 and Thm. 1.10 verbatim with page numbers. If that brief
   mis-transcribed either statement, D1 is wrong. Everything else about the citations — that
   `\cite[Thm.~1.1]` at L311 correctly names the `T`-time two-sided envelope, that Thm 1.6 is the
   one-letter parity moment — rests on the same brief.
2. **The mathematics of `cycles.md` §12.8.6.** I verified that all eleven claims are *located* there
   and recomputed every constant the paper prints. I did **not** re-derive Theorem 12.8.6.1's
   three-distance sweep criterion (I did not recompute `maxgap(13)` or `maxgap(12)`), nor
   Theorem 12.8.6.2's five proof steps, nor run any script in `experiments/`.
3. **`aeh.md`'s own results.** Lemma 13.2.4, Proposition 13.2.5, Theorem 13.6.4 and Proposition 13.6.5
   were verified to *exist at the pin as stated objects*. Their proofs were not checked, and I did not
   verify that Theorem 13.6.4 really is the deterministic dictionary the paper says it is, nor that
   13.6.5's exact values (`19/63`, `2/63`, `20/63`) are correct.
4. **No network.** The Zenodo DOIs (10.5281/zenodo.21730505 reserved, 10.5281/zenodo.21421120 for v2),
   the GitHub URLs including `…/blob/9d9d1ec/cycles.md`, and whether a v3 release description exists
   anywhere outside the repository — none were resolved.
5. **The author's intent on D9, D10 and the Remark 3.6 wording.** I adjudicated the Remark 3.6
   deviation as mathematically correct; whether the author accepts the ten extra tokens is his call.
   The design pass's five undecided items (its §8) remain undecided and I did not decide them.
6. **The design pass's page measurements.** I confirmed the built artefact is 15 pages. I did not
   re-measure the `pt` figures in its §1 tables, so its per-passage savings are taken on trust.
7. **Rendering resolution.** Pages were inspected at 110 dpi. Defects below that scale — hairline rule
   misalignment, sub-point kerning, a single overlapping glyph — would not show. The `\hbox` log is the
   backstop and it is clean.
8. **Not attempted, per the brief:** `open-problems.md` 11.12, the deferred prefix result, and any
   `aeh.md` change beyond assessing what this round landed.
