# Findings: landing the repair history (v3 round 6, closing)

**Branch.** `v3r6-prune`, worked in `c:\Users\Ace\Documents\Collatz`, no worktree, no branch switch,
no push, no merge, no rebase. Four commits on top of `43e7db2`:

| commit | what |
|---|---|
| `3c22589` | `paper/collatz-reduced-version-history.md` (new) + one `AGENTS.md` Layers entry |
| `d438d78` | paper: the version note's closing sentence, and the `L231` gloss |
| `225d4d3` | Appendix A record pin `f9b07b1` → `d438d78`, in its own commit |
| this file's commit | the round's briefs and findings |

**Headline.** The v2 pin `72ec88e` and the six itemised repairs are in the repository. **Four claims
in the round's working documents were wrong or stale and are corrected; two real v3 changes they
omit are added.** The `L231` gloss was affordable and is in — four words, and it also removes a
collision with Section 5's own defined term *admissible*. Build **15 pages**, zero overfull boxes,
zero LaTeX warnings. The pin verifies positively and negatively with `git show`, with a bogus control
returning nothing.

---

## 1. Where the file went, and why there

**`paper/collatz-reduced-version-history.md`.**

* **Not a wiki page.** `AGENTS.md` L18 bars change logs, dated journals and "was X, now Y" prose from
  the pages, and a version history is that genre by definition. The brief settles this and I did not
  reopen it.
* **`paper/` is where its subject lives.** The file describes `collatz-reduced-v1/v2/v3`, all of
  which are in `paper/` or (v1, frozen) in `sources/paper/`. Nothing else in the repository is about
  the paper *as a document* rather than about the mathematics.
* **The name is scoped.** `paper/` holds two papers — `collatz-mirror-v1` as well as
  `collatz-reduced-v*` — so a bare `version-history.md` would be ambiguous. The name matches the
  `collatz-reduced-*` family it belongs to.
* **It is one file, not a per-version set.** The whole point is that a reader with one frozen PDF can
  see the other versions in one place.

### The `AGENTS.md` line

One entry appended to **Layers**, for `paper/`, which was not listed at all. It does three things:

1. names the layer;
2. names the version-history file and says **why it is the exception** to the no-change-logs rule —
   released versions are frozen at DOIs, so a past state of a published PDF cannot be read back at a
   commit the way any wiki page can. Without this, a later hygiene pass would read the file as a
   violation and delete it, which is precisely the failure this round exists to repair;
3. bounds it — it records the paper, not the mathematics; where a claim's standing has moved, the
   owning wiki page is still the authority.

**Appended as item 6, not inserted after `experiments/`.** Committed briefs cite the list *by
number* — `briefs/v3r3-record-apply-brief.md` and `briefs/v3r3-record-apply-findings.md` say
"AGENTS.md, Layers 3" for `experiments/`, and `briefs/v3r3-verify-findings.md` says "AGENTS.md,
Layers 4" for `README.md`. Inserting would have silently invalidated three committed references.
Appending costs an odd reading order and nothing else.

`AGENTS.md` L3 still says "three layers" over a five-item (now six-item) list. Pre-existing;
out of scope; not touched.

---

## 2. What I verified in the history text, and what I corrected

Source material: `briefs/v3r6-prune-design-findings.md` §5 and `briefs/v3r6-prune-apply-findings.md`
§4, which carry near-identical release-notes blocks. **Nothing was copied on trust.**

### Verified against the record

| claim | checked against | verdict |
|---|---|---|
| `72ec88e` exists and carries `cycles.md` §12.8.6 in its v2-era state | `git cat-file -t`, `git show 72ec88e:cycles.md` | ✔ — it is the `p22-record-update` merge; §12.8.6 there is the contiguous `p ∈ {2,…,23}` record with the `p = 22` resolution |
| `9d9d1ec` is the current record pin for `cycles.md` §12.8.6 | `git log 9d9d1ec..HEAD -- cycles.md` empty | ✔ (re-confirmed; verify and fix both had it) |
| the whole v2 note — the three-part recipe, `p ∈ {2,…,23}`, `γ/log_2 p ∈ [1.828, 3.643]`, the `p = 22` episode, `n = 25217`/`n = 31202`, `13` and `8` moves, the named gap | `paper/collatz-reduced-v2.tex` L219–223, read verbatim | ✔ every clause, word for word |
| the v2 version note's own items | `paper/collatz-reduced-v2.tex` L36 | ✔ subtitle, note, "no theorem or universal claim strengthened", DOI |
| the `merle` subtitle was actually missing in v1 | `sources/paper/collatz-reduced-v1.tex` L253 vs v2 L261 | ✔ v1 prints "…a conditional formal proof in Lean 4"; v2 adds ", with documented structural obstructions" |
| the staircase numbers: `8 − 5·log_2 3`, the arc, `66`, `0.05·(log_2 3)^p`, `79` at `p = 16`, `1/(log_2 3 − 1) = 1.70951`, `[3.683012, 5.140212]`, the `p ≥ 16` / `3 ≤ p ≤ 15` / `p ∈ {2,4}` split, the partial-quotient dead end, "from `p = 8` upward not one working witness…" | `cycles.md` §12.8.6.1, §12.8.6.2, §12.8.6.4, *Scope, and what is not covered* | ✔ all located, several verbatim |
| Theorem/Definition/Proposition numbers are stable v1 → v2 → v3 | environment order in all three sources | ✔ Definition 2.1, Theorem 3.3, Theorem 3.8, Proposition 4.1, Theorem 4.5, Theorem 4.6 are the same objects in every version |
| the six repairs, **on both sides** | v2 source vs v3 source | ✔ see below |
| the calibration limits and `2.6%` / third decimal | `paper` L431 | ✔ |
| the single-visit reading is strictly weaker | `aeh.md` 13.6.4(q1) and front matter | ✔ "the single-visit marginal (13.2.2 at `L = 1`) being strictly weaker" |
| the DOIs — v1 `21273548`, v2 `21421120`, v3 `21730505` reserved | the three title pages, `README.md` L3, `publication.md` L2/L39 | ✔ |

**The six repairs, checked in both directions** (the working documents assert the v3 state only):

| item | v2 printed | v3 prints |
|---|---|---|
| Definition 2.1 | "`ω` odd, `3∤ω`, `d ≥ 1`" — no positivity | "`ω` odd **and positive**" |
| Theorem 3.3 | `s ≤ C(ω)(log d)^2` | `s ≤ C(ω)(1 + log d)^2` |
| Theorem 3.8 | "From the residues of Theorem 3.7 (the *depth-`k` window*) alone" | "…the residues of Theorem 3.7 **together with the stratum labels** `(s, σ, a_+)`" |
| Theorem 4.5 | `n ≤ n_0(p) = O(p(log_2 3)^p)`, `n_0` never defined | `n ≤ n_0(p)`, the solution of a displayed equation, **then** the order estimate |
| digit budget | `\begin{proposition}[digit budget]` | `\begin{heuristic}[digit budget]` |
| Proposition 4.1 | `σ_j` used, never defined; `M_t` unglossed | `σ_j = s_j + m_{j+1}` at its point of use, and `M_t` explicitly "unrelated to the anchor `M(ω)`" |

### Corrected — four claims

1. **"Five rounds of external review." Dropped.** It is not verifiable as written and the counting is
   genuinely ambiguous: `briefs/v3r2-aeh-formulation-brief.md` calls its round the "Second external
   review", `briefs/v3r6-prune-design-brief.md` calls *this* round "The fifth external review", and
   `v3r5-shifted-word` was a repair pass rather than a review — so the number is a claim about
   process, not about the paper, and it was written against `main = 29ecb1b`, before this round
   landed. The file says "after external review", which is what the paper's own version note says and
   what I can check.
2. **"Theorem 4.6 stands exactly as written in v1 and v2."** Not true as a statement about the text:
   v1 and v2 close the theorem environment with "…and we assess (supported by the verified instances,
   though not proved here for all `p`) that it passes all size conditions with `γ = O(log p)` for
   every `p`", and v3's environment does not contain that clause — the working document's own next
   bullet says so. Narrowed to the claim: "Theorem 4.6 claims exactly what it claimed in v1 and v2:
   it is neither strengthened nor weakened, and its statement is not restated", with the clause's move
   recorded under *Presentation*.
3. **"the printed `(log d)^2` was vacuous at `d = 1`."** It is not vacuous, it is **false**: at
   `d = 1` it asserts `s ≤ 0`. `briefs/v3-external-review-corrections-findings.md` L99–101 records the
   actual provenance — the record's statement carries a `d ≥ 2` guard which the paper dropped on
   import. The file says that.
4. **"End to end verified at `p ∈ {3,…,26}`."** `cycles.md` §12.8.6.2 *Verified* says
   `staircase_gamma_upper.py` covers "`23` periods over `p ∈ {3, 5, …, 26}`" — 23 values over a
   24-value range, i.e. `p = 4` excluded, which is exactly the period §12.8.6.1 puts outside the
   construction's reach. The file says "over the periods from `3` to `26` (apart from `p = 4`)".

### Added — two v3 changes neither working document carries

5. **The citation audit.** Merged into `main` as `v3-citation-fixes` (`b2e0b92`, `c5ef0e6`,
   `ed79d4a`) and therefore part of v3, but absent from both release-notes blocks. One bullet under
   *Attributions and citations*: `llmcollatz` gains its author, and `terras`, `steiner`, `hercher`
   and `barina` each gain a locator, none of which corrects an error. Checked against the commit
   messages, the three bibliographies, and the rendered page 15.
6. **This round — the prune itself.** Both blocks were written before the prune landed and describe
   v3 as of `29ecb1b`. Left alone, the history would have implied the *Note added in v2* is still in
   the paper — a stale claim of exactly the class the brief warned about, in the file whose job is to
   prevent them. A *Presentation* section now records: the assessment clause moved out of Theorem
   4.6's environment; the v2 note and its correction replaced by one *Status of the assessment*
   paragraph; and 18 pages → 15, with what was compressed and where each cut passage now lives.

### The six retracted claims

Swept on the new file and on the edited `.tex`. **All six absent.**

| # | claim | in the history file |
|---|---|---|
| 1 | AEH supplies `E_B[m+r] = 4` / the exponent mean past the budget | one occurrence, a denial ("Section 5 does not claim…") |
| 2 | a horizon converted into blocks per bit | **0 occurrences**; the phrase survives once in the paper, at L374, the clock's, with its scoping clause attached and untouched by this pass |
| 3 | the finite bound is about a word beginning at the sampled start | the extended `(n+1)`-letter form is stated and the other explicitly denied |
| 4 | bulk uniformity unqualified | `grep -ci unqualified` = **0** in both files |
| 5 | `13.6.4`'s union mass exact | `13.6.4` not named; the only "union" says the union over all sampling scales "is a triangular array that no per-scale statement controls" |
| 6 | any conditional drift consequence | "The section states **no** descent or contraction consequence of Hypothesis 5.1" |

---

## 3. The version note's new sentence

Replaced (`paper` L42, one sentence, the note not re-expanded):

> The repair history, item by item, is in this version's release description.

with

> The repair history, item by item, is at `\texttt{paper/collatz-reduced-version-history.md}` in the
> project record, and in this version's release description.

**Both, not instead.** The repository copy is what makes the sentence true today; the release
description stays because the author's plan is unchanged and Zenodo receives the same text. Nothing
in the paper now depends on a document that does not exist.

**No `\url` and no commit pin in the sentence**, deliberately: a pin inside the version note would
have to name the commit that contains the version note, which is circular, and Appendix A is the
paper's standing device for exactly this. The pin now names a commit whose tree holds the file
(§6 below).

**Renders on one line** inside the note; the `\texttt` path does not break and page 2's *Author's
note* heading is not disturbed.

---

## 4. `L231` — the gloss is in

**Decision: applied, four words.** The brief made it optional; two things made it cheap and worth it.

* The paragraph said "below **the target arc's length**". The arc is never named in the paper, so
  neither is the quantity it constrains. It now reads "below the length of the target arc for
  `⌈n log_2 3⌉ − n log_2 3`", which is the record's own quantity (`cycles.md` §12.8.6.1's `δ(n)`) and
  makes the whole sentence self-explaining: the reader can see why `8 − 5·log_2 3` being *shorter
  than an arc* is the point.
* The paragraph said "contain **an admissible exponent** `n`". That is not merely undefined — it
  **collides** with Section 5, which defines *admissible* as a property of a pair `(τ, θ)` (three
  further occurrences, L269, L310, L368). The paper now says "contain an `n` landing in that arc",
  which needs no definition and frees the word.

The paragraph is not re-expanded, its record address (`cycles.md` §12.8.6 with the `9d9d1ec` URL) is
unchanged, and Theorem 4.6, Remark 4.7 and the *Sharpness* paragraph are untouched. Rendered on
page 9 and read: `\lceil…\rceil` sets correctly and the paragraph flows.

---

## 5. Build

Rebuilt from clean (`.aux`, `.log`, `.out` deleted), three `pdflatex -halt-on-error
-interaction=nonstopmode` passes, then rebuilt again after the pin edit.

| | result |
|---|---|
| passes | 3, exit `0` each, converged (`rerunfilecheck`: `.out` has not changed) |
| **page count** | **15** — unchanged, before and after the pin edit |
| overfull boxes | **0** |
| underfull boxes | 1 — `Underfull \hbox (badness 1067)`, the `\bibitem{lagarias}` entry on page 15. Pre-existing; recorded in the repository's own log before the round |
| `LaTeX Warning` | **0 of any kind** |
| undefined references / citations | **0** |
| encoding | `AGENTS.md`, the new `.md`, the `.tex`: UTF-8, no BOM, no `U+FFFD`, no mojibake |

**One layout change, checked.** The added words push the **References** heading from page 14 to
page 15, which now carries all eighteen entries; page 14 ends with Appendix A complete. Pages 1, 2, 9,
14 and 15 were rendered at 120–130 dpi and looked at: no stranded heading, no split display, no
widow, no orphan.

---

## 6. The pin `d438d78` — verified with `git show`, never the working tree

`d438d78` is the paper commit. Its tree carries the landed history file (via its parent `3c22589`)
and the version note that points at it. The pin itself lands in the child `225d4d3` — the same
chicken-and-egg pattern as `6a9183a → c2d465a`, `881c92e → 91f76e0` and `f9b07b1 → eb3f4c4`.

**Positive**, at `d438d78`: the history file is in the tree and contains `72ec88e` (1 hit) and all
six repair items (6/6); `paper/collatz-reduced-v3.tex` contains the pointer to it (1 hit) and the
`L231` gloss (1 hit); `AGENTS.md` contains the Layers entry (1 hit).

**Negative**, at the superseded pin `f9b07b1`: the history file **does not exist**
(`git show` fails); the paper's pointer to it — **0**; the `AGENTS.md` entry — **0**; the `L231`
gloss — **0**; and the two superseded strings are still there — "is in this version's release
description" **1**, "an admissible exponent" **1**. The old pin could not have supported the repaired
version note, which is why the bump was necessary.

**Control.** A deliberately bogus probe (`ZZQQNOTHERE`) at the new pin returns 0, and `13.99.99` is
not found in `aeh.md` at the pin, so the searches are not matching everything.

**The paper's other pointers still resolve at the new pin.** Spot-checked 16 wiki anchors and all six
`experiments/*.py` at `d438d78`: 22/22 found. The fuller check is inherited rather than repeated, and
soundly: `git diff --name-only f9b07b1 d438d78` is exactly `AGENTS.md`,
`briefs/v3r6-fix-findings.md`, `paper/collatz-reduced-v3.{tex,pdf}` and the new history file — **no
wiki page and no script differs between the two pins**, so the fix pass's 24/24 anchors and 10/10
files carry over unchanged.

---

## 7. Found and not fixed

1. **`paper` L231 still routes the v2 note to the release description.** "…the note added in v2 and
   the continued-fraction route it named are **in the release description** and at `\S12.8.6.1` and
   `\S12.8.6.3` there." The same argument that moved the version note applies, and the swap is two
   words. **Left alone deliberately**: the brief scoped task 2 to the version note's closing
   sentence, D12 is the author's decision and was fenced off from the fix pass, and — unlike the
   version note before this round — that sentence already carries a live record address in its own
   clause, so it does not *depend* on the unwritten document. **One sentence for the author to
   rule on.**
2. **`AGENTS.md` L3 says "three layers" over what is now a six-item list.** Pre-existing and not
   mine to restructure.
3. **The brief says six untracked brief files; there are seven**, because `v3r6-history-brief.md`
   itself was written after the count. All are committed, with this file, in the `briefs:` commit.
4. **Carried forward from the fix pass, unchanged**: the abstract's "lifting classes" used before
   Theorem 3.3 defines it; "door-letter alphabet" and "the door" never defined in the paper;
   `π_{k,D}` used in §1 and Related work before §5; `stage3.md`'s *resonant* branch versus the
   paper's *boundary* branch; `\label{prop:elim}` and five other labels unreferenced.
5. **D12's release blocker is not closed by this round.** v3 still cannot be *released* until the
   Zenodo release description is written. What is closed is the repository's side of it: the pin and
   the six repairs are no longer only in working documents.

## 8. What I did not check

The primary sources (Inselmann, Tao, Terras, Everett, Korec, Wirsching, Thomas, Merle and the rest —
so the history's attribution bullets rest on `briefs/v3r3-inselmann-horizon-findings.md`,
`briefs/v3r2-*-findings.md` and `briefs/v3-citation-audit-findings.md`, as verify's and fix's did).
The mathematics of `cycles.md` §12.8.6 — I located every claim the history states and checked every
constant it prints against the record's own text, but re-derived nothing and ran no script in
`experiments/`. `aeh.md`'s proofs. The network: no DOI, no GitHub URL, and no Zenodo release
description was resolved. Whether the author wants item 1 of §7 changed.
