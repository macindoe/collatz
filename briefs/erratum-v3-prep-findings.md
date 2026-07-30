# Findings: erratum-v3-prep — the v2 note's correction, packaged as a Zenodo v3, prepared for the author's upload (2026-07-30)

Brief: `briefs/erratum-v3-prep-brief.md`. Branch `erratum-v3-prep`.
**Base SHA `9d9d1ec`** — the worktree was cut at the stale `3eab8f1`, which does not
contain the brief; `main` was merged (fast-forward to `9d9d1ec`) before any work began,
and the branch was cut there.

Per-item commits; nothing merged, nothing pushed anywhere. `publication.md`, `cycles.md`,
`HANDOFF.md` and `sources/` untouched; `paper/` gains the v3 files only. The Zenodo
upload and the wiki-`main` push are the author's alone.

| commit | what |
|---|---|
| `1acafbc` | seed `paper/collatz-reduced-v3.tex`, byte-identical to published v2 (the v1→v2 pattern, step one) |
| `bd3d202` | the correction paragraph; date line and Version note carry upload placeholders |
| `0548b2c` | `paper/collatz-reduced-v3.pdf` built (sandbox temp dir, artifact copied in) |
| `e888cd1` | **OPTIONAL** — the σ clause in Proposition `prop:elim`, declared in the Version note, PDF rebuilt; drop this one commit to drop both |
| (this commit) | this record |

`python experiments/encoding_scan.py`: **RESULT: CLEAN** (run before the final commit;
figures in §8). Every edit was made with the Edit/Write tools; PowerShell touched no
tracked file. LaTeX was built in the scratchpad sandbox and the PDF copied in, per the
HANDOFF quirk (the mount locks aux files).

---

## 1. Item-1 verification: every number in the drafted correction, against the merged record

Method: each constant recomputed independently at 60 dps (mpmath, in-session) and read
at its named place in `cycles.md` §12.8.6 as merged; the committed certifier for all of
them is `experiments/staircase_gamma_upper.py` (45 checks, 0 failures, exact rationals).

| draft's number | merged source | recomputed | verdict |
|---|---|---|---|
| `8 − 5log₂3 = 0.0751874964…`, positive | `12.8.6.1` (`θ`) | `0.0751874963942190…` | MATCH (page's own rounding) |
| smaller than the target arc | `12.8.6.1` proof: arc length `0.0754390665… > θ` | `0.0754390665090833…` | MATCH — but "arc" → "arc's length", deviation D2 |
| 66 consecutive integers | `12.8.6.1` proof: `J = 13` two-sided, "66 suffice and 61 do not" | maxgap criterion as stated | MATCH |
| arc `[0.0415, 0.1169390665…]` | `12.8.6.1` (`δ_lo`, `δ_hi`) | `δ_hi = 0.1169390665090833…`; `δ_hi − θ = 0.0417515701…` so `0.0415` sits inside | MATCH |
| `1/(log₂3 − 1) = 1.70951` per block | `12.8.6.2`, "The shape, and the constant that was missing" | `1.7095112913514547…` | MATCH |
| `p ≥ 16` unconditional / `3 ≤ p ≤ 15` finite check / `p ∈ {2,4}` by exhibition | `12.8.6.1` statement; the Scope paragraph | — | MATCH |
| `3.683012 ≤ γ ≤ 5.140212` | `12.8.6.1` display | `Γ* = 3.6830121007211…` (printed bound truncated down — valid direction); upper `5.1402114860725…` (printed bound rounded up — valid direction) | MATCH |
| "with candidates drawn from the whole window the same construction closes every period tested" | `12.8.6.4` ("the hole was a property of the candidate list, not of `log₂3`"; "under `12.8.6.1`'s statement the episode does not arise"); `12.8.6.2` *Verified* | — | SUPPORTED IN SUBSTANCE, NOT AS WORDED — deviation D4 |
| pointer "the current record is `cycles.md` §12.8.6" | — | — | pinned per brief item 3 — deviation D6 |
| window count from `16` onward ("far more than 66") | `12.8.6.1` proof: exactly `50` at `p = 15`, `79` at `p = 16` | `50` / `79` exact | FALSE AS WORDED at `p = 16` (79 vs 66 is not "far more") — deviation D3 |

### Every deviation from the §5 draft, with its reason

The §5 draft (`briefs/staircase-status-apply-findings.md`) is the starting text; the
merged page wins where they differ. Eight deviations:

**D1 — the date marker.** Draft: `(Correction, 2026-07-29.)`. Shipped:
`(Correction, [date --- set at upload].)`. The brief's item 3 assigns the date to the
author at upload.

**D2 — "smaller than the target arc" → "below the target arc's length".** An arc is a
set; the comparison is to its length. The merged page's own *What is consumed* clause
says "positive and below the arc's length".

**D3 — the window-count sentence.** Draft: "the scale window contains far more than 66
integers at every period from 16 onward". At `p = 16` the window holds exactly 79
integers — more than 66, not "far more". Shipped the merged page's own facts: "the scale
window at period `p` holds `0.05·(log₂3)^p` integers — 79 at `p = 16`, growing
geometrically — so `p = 16` is the first period supplying 66 consecutive integers."

**D4 — the "every period tested" sentence, pinned and disambiguated.** Draft: "with
candidates drawn from the whole window the same construction closes every period
tested." Three problems. (i) The brief requires the ranges pinned. (ii) "The same
construction" is ambiguous between Construction B and the superseded recipe — and the
merged page's only whole-window claim about the *superseded* procedure covers
`p = 24…28` run to completion with `p = 29…35` capped (`12.8.6.4`), so under that
reading "every period tested" is not supported. (iii) "Closes" could read as exclusion.
Shipped: "under the availability statement the episode does not arise — from `p = 8`
upward not one working witness is a convergent or semiconvergent denominator — and the
corrected construction supplies a passing size-condition witness at every period tested
(end to end at `p ∈ {3,…,26}`; the construction itself verified through `p = 32`)."
Sources: `12.8.6.4` (the episode sentence, verbatim substance), `12.8.6.2` *Verified*
(certified `n` at every `p ∈ {2,…,30}` outside `{2,4}` plus `p = 31, 32`; end-to-end
evaluators `staircase_allp_diophantine.py` `p = 3…26` and `staircase_gamma_upper.py`,
23 periods over `p ∈ {3,5,…,26}`). "Supplies a passing size-condition witness" is the
published note's own vocabulary.

**D5 — the γ bracket rescoped off `p ∈ {2,4}`.** The draft's trailing "at `γ` between
the absolute constants…" grammatically covered the whole list including `{2,4}`. The
merged `12.8.6.1` claims the bracket for `p ≥ 16` and "the same bracket" for the
`3 ≤ p ≤ 15` exhibits — it makes no bracket claim for `{2,4}`. Shipped order: the
bracket attaches to `p ≥ 16` and the finite check; `{2,4}`, outside the construction's
reach, follow it, covered by direct exhibition and nothing more.

**D6 — the repository pointer, pinned.** Draft: "The current record is `cycles.md`
§12.8.6 of the project repository." Shipped:
`\url{https://github.com/macindoe/collatz/blob/9d9d1ec/cycles.md}` — the proposed pin,
**CHECK AT UPLOAD** (§4 below). The v2 note's own published pin (`72ec88e`) stays in
place, unedited, one sentence above.

**D7 — one sentence added (stopping-rule clause).** "Every constructed configuration
remains a size-passer only and fails the divisibility conditions `q | R_r`, as the
instances above do: sharper evidence that counting cannot do better, and no evidence
about exclusion." The brief's stopping-rule compliance line says the correction text
itself states that nothing reopens the cycle front; the §5 draft carried no such clause.
Wording is the merged Scope paragraph's and the `12.8.6` preamble's, not new prose.

**D8 — two wording adjustments.** "The gap named in this note" → "The gap named above"
(the correction sits inside the note; the deixis is now internal). And the
badly-approximable equivalence gains its reason — "those gaps are the partial quotients
of `log₂3`" — from the merged superseded-formulation paragraph; without it the
equivalence stands unexplained in print.

Not deviated: "closed by replacing the route rather than completing it"; the
`1/(log₂3 − 1)` offset sentence ("absent from the profile described above", "removed
from the argument rather than bounded"); the scope composition sentence; the silence on
the hedge — all as drafted, all verified against the merged text.

---

## 2. Item-2 verification: the published sentence, verbatim

Checked character-for-character by exact substring match against
`paper/collatz-reduced-v2.tex` (in-session script; both `True`):

> The remaining gap is the one already named: no proved closed-form bound on the multiplicative gap between consecutive correctly-signed semiconvergent runs --- the bound that would certify no period is skipped --- and the $p = 22$ episode is a demonstration that this gap bites in practice, not only in principle.

It is the **third-from-last sentence** of the note's closing paragraph (five sentences;
the gap sentence is #3, followed by the hedge sentence and the pointer sentence), as the
§5 draft says. The pointer sentence, also verbatim:

> The construction, the verified instance record, and the diagnosis of the remaining gap are recorded at \texttt{cycles.md} \S12.8.6 of the project's public repository (\url{https://github.com/macindoe/collatz/blob/72ec88e/cycles.md}).

— pinning `72ec88e`, as the draft says. Lineage: the gap sentence, the pointer, and the
whole "Note added in v2" are **absent from the frozen v1**
(`sources/paper/collatz-reduced-v1.tex`; checked by the same script) — the note is
v2-only material, consistent with the Window-D record.

---

## 3. The v3 LaTeX: pattern, placement, and what changed

**The v1→v2 pattern, inspected** (`git log --follow`): archive the old version to
`sources/paper/` as a pure move (`4f5e843`), seed the new as a byte-identical copy
(`1462774`), edit, build, and stamp the version DOI in the tex at upload (`d59eec9`).
Followed with one deliberate exception: **the archival move of v2 to `sources/paper/`
is not performed here** — this session's rules hold `sources/` immutable and give
`paper/` the v3 files only. The pure move `paper/collatz-reduced-v2.{tex,pdf}` →
`sources/paper/` belongs to the author/main session at or after upload, mirroring
`4f5e843`.

**Placement decision.** The gap sentence sits mid-paragraph, followed by two more
published sentences (the hedge, the pointer). Splitting that paragraph would move
published text, so "immediately followed" is implemented at the nearest paragraph
boundary that leaves every published sentence byte-identical: the correction is its own
paragraph directly after the note's closing paragraph, before Section 5, opening with
the *(Correction, …)* marker. In the built PDF the v2 note ends and the correction
begins on **page 9**; nothing else moved (Section 5 still opens on the same page).

**What changed in the tex (commit `bd3d202`), exhaustively:**
1. `\date` line: `v3, [month] 2026 · DOI: [v3 DOI --- set at upload]` (the v2 pattern
   stamps the real DOI at upload).
2. Version note: a v3 clause appended (factual, names the correction, states "The
   original sentence stays in place; no theorem, proof, or other text changes",
   DOI placeholder). The v1 and v2 clauses are byte-identical to published v2.
3. The correction paragraph (§1's text with deviations D1–D8).

Nothing else. The published gap sentence, the hedge sentence, and the v2 note's own
`72ec88e` pointer are untouched and visible above the correction.

**The build (commit `0548b2c`).** MiKTeX pdflatex, two passes, in the scratchpad sandbox
(the repo mount locks aux files — HANDOFF quirk), artifact copied in. 11 pages. Five
recovered `maketitle` errors appear in the log — **inherited, not introduced**: the
published v2 tex builds with the identical five (the `\date` line's `\;\cdot\;` is
math-mode material in text; TeX recovers by inserting `$`). Recorded flat; repairing it
would change published-adjacent text for no reader-visible reason.

---

## 4. The CHECK-AT-UPLOAD pin

The correction's pointer pins **`9d9d1ec`** — current local `main` at this session's
base, whose `cycles.md` §12.8.6 is the settled text the correction reports.

**CHECK AT UPLOAD:** `https://github.com/macindoe/collatz/blob/9d9d1ec/cycles.md` must
resolve publicly before the record goes live — the round-9/10/11 co-edit pattern
exactly: **the author pushes wiki `main` first.** Any push of `main` at `9d9d1ec` or any
descendant makes the pin resolve (a blob URL resolves for any public commit, tip or
not). If at upload time the author prefers pinning the then-current public `main`
instead, the SHA lives in exactly one place in the tex (the correction's final sentence)
— edit, rebuild, upload; §12.8.6 has not changed since the apply merge, so either pin
resolves to the same settled text.

---

## 5. The σ clause — OPTIONAL, the author decides at upload (commit `e888cd1`)

**The check the brief asked for first:** the tex's `Definition~\ref{def:reduced}`
pointer does *not* already cover the point of use. `def:reduced` defines `σ = v₂(C)`
and `m₊ = σ − s` per step, and the *proof* of Proposition 4.1 cites it — but the
statement's `S_t = Σ_{j<t} σ_j` precedes the proof, and the natural local misreading
`σ_j = m_j + s_j` reproduces every structural identity attached to the proposition
except the recorded `gcd(q, R_r) = 7` canary
(`briefs/record-defects-repair-findings.md` item (i): every guardrail depends on `σ`
only through `Σσ = K`, which both readings share). So the pointer covers the derivation,
not the use, and the one-clause repair has content.

**The clause** (mirroring the wiki's `12.6.1` repair): "…and
`S_t = \sum_{j<t}\sigma_j`, with `σ_j = s_j + m_{j+1}`, indices cyclic (the step's
`σ = v₂(C)`, `m₊ = σ − s`, of Definition~`def:reduced`; the shift is essential,
`m_{j+1}` and not `m_j`)." The Version note's v3 clause is amended in the same commit so
the changelog declares it, and the PDF is rebuilt (clause lands on page 7; the
correction stays on page 9). Dropping the one commit drops clause, declaration, and
rebuilt PDF together, leaving `0548b2c`'s artifact as the upload PDF.

**The trade-off, stated honestly:** we told Merle the erratum corrects only the gap
sentence (round-11 reply, as adjusted: "an erratum correcting only that sentence is
drafted, not issued"). Including a definitional clause is defensible — it is notation,
not mathematics; the changelog declares it; and it repairs in print the same defect
already repaired on the wiki and said plainly to Merle as a defect in our record. But it
makes the v3 do *two* things where the reply said one. That call is the author's, not
this session's and not the main session's.

---

## 6. The upload package

### 6.1 Zenodo steps (checklist)

1. **Gate:** push wiki `main` (at `9d9d1ec` or a descendant) public; verify
   `https://github.com/macindoe/collatz/blob/9d9d1ec/cycles.md` resolves and §12.8.6
   reads as merged.
2. **Decide the σ commit** (`e888cd1`): keep or drop at merge. Both states are
   self-consistent (tex + declaration + PDF travel together).
3. On the existing record page (the one carrying DOI 10.5281/zenodo.21421120), choose
   **New version** — same concept record, one canonical object. Do **not** create a new
   record; do **not** edit or delete the v1/v2 depositions or their files.
4. Zenodo reserves the v3 DOI before publishing. **Stamp the tex** (the `d59eec9`
   pattern): the reserved DOI + real month into the `\date` line and the Version note's
   v3 clause, the real date into the correction marker
   `(Correction, [date --- set at upload].)`. Three placeholder sites, no others —
   grep the tex for `set at upload` and `[month]` to confirm none is left.
5. **Rebuild** (two pdflatex passes, in a temp dir — the mount locks aux files) and
   upload `collatz-reduced-v3.pdf` as the new version's file; remove the inherited v2
   PDF from the new version's file list.
6. Metadata: version `v3`; publication date; the changelog paragraph (§6.2) in the
   description's version note / "Additional notes"; title, authors, license unchanged.
7. Publish. Verify the v3 DOI resolves and the concept DOI ("Cite all versions" on the
   record page) now lists v1, v2, v3.
8. Back in the repo (author/main session, after the DOI exists): commit the stamped tex
   + rebuilt PDF (the `d59eec9` pattern); apply the `publication.md` block (§6.4);
   optionally perform the archival pure move of v2 to `sources/paper/` (`4f5e843`
   pattern).

### 6.2 Proposed metadata changelog text (one factual paragraph)

> v3 appends a dated correction to the "Note added in v2" in Section 4. The note's
> identification of the remaining gap is superseded on both halves: candidate
> availability is proved with no continued-fraction input (any 66 consecutive integers
> supply a candidate exponent), and a corrected explicit construction satisfies all p
> size conditions with no correction step. The sharpness claim of Theorem 4.6 is
> thereby established at every period — unconditionally for p ≥ 16, by finite check for
> 3 ≤ p ≤ 15, p ∈ {2,4} by exhibition — with γ between the absolute constants 3.683012
> and 5.140212. The original sentence remains in place; no theorem or proof changes.
> Current record: cycles.md §12.8.6 of the project repository.

If the σ commit ships, append: *"One notational clause is added in Proposition 4.1,
defining σ_j at its point of use."*

### 6.3 Canonical-citation line for the round-12 reply

> The published record is amended: paper 1 is at v3 (version DOI
> [10.5281/zenodo.NNNNNNNN — minted at upload]), one canonical object under the concept
> DOI ([shown as "Cite all versions" on the record page]); the correction sits in
> Section 4's v2 note, the original sentence kept in place above it.

Flat note for the reply, as briefed: the ccchallenge `Macindoe2026` entry is catalogued
from the v1 export (DOI 10.5281/zenodo.21273548); the reply states the canonical DOI
rather than chasing the register.

### 6.4 Proposed `publication.md` update block — DRAFTED, NOT APPLIED

`publication.md` moves only after the DOI exists. Two edits:

*Front matter, `status:` line* — append after "(paper 1 v2 DOI 10.5281/zenodo.21421120)":

```
; paper 1 v3 DOI [v3 DOI] (the v2 note's gap sentence corrected in place)
```

*The "Uniform trim + staircase sharpness (12.8)" bullet* — replace its last two
sentences ("The standing recommendation for the published record is unchanged … no v3
yet. … **v2 is published** …") with:

```
**v3 is published** (DOI [v3 DOI], [date]): a dated correction appended to the v2
note — the gap sentence stays in place, verbatim, and the correction reports the
all-`p` closure at its scope (unconditional `p ≥ 16`; finite check `3 ≤ p ≤ 15`;
`p ∈ {2,4}` by exhibition; `3.683012 ≤ γ ≤ 5.140212`), silent on the hedge, with the
repository pointer pinned to a public commit carrying the settled §12.8.6. The
`thm:staircase` hedge ("not proved *here*") remains a true statement about the paper
and is untouched. **v2 remains published** (DOI 10.5281/zenodo.21421120): subtitle fix
and the contiguous `p ∈ {2,…,23}` evidence note, the repository pointer pinned at
`72ec88e`.
```

If the σ commit ships, add to the v3 sentence: "; one notational clause added in
Proposition 4.1 (σ_j defined at its point of use), declared in the version note".

---

## 7. Register and scope checks

- The correction states what closed, at what scope, and where the record is — nothing
  more. No excitement vocabulary; every "proved" carries its scope inline.
- Silent on the hedge: `thm:staircase`'s "not proved here" is not quoted, glossed, or
  touched.
- No new results imported: every sentence of the correction is a report of
  `cycles.md` §12.8.6 as merged; the mathematics lives there.
- The stopping-rule clause is in the correction text itself (deviation D7).
- No reply paragraphs drafted; nothing for the ledger; no pushes.

## 8. Encoding scan

`python experiments/encoding_scan.py` run immediately before this record's commit:
**RESULT: CLEAN** — 358 tracked files, 0 invalid UTF-8, 0 BOMs, 0 double-encoding
signatures (the v3 tex's em-dashes and the findings' `≤`/`γ`/`σ` included).
