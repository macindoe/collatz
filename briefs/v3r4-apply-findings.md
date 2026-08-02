# Findings: the round-4 apply phase — the subtraction landed, the prefix result parked

**Branch.** `v3r4-review-round4`, from `6ead133`. Three commits, in the order the brief specifies:
`123683d` (record), `e634513` (paper), `ff7c999` (the pin, alone). No push, no merge, no rebase, no
worktree. Nothing was refused.

**Design.** `briefs/v3r4-clock-findings.md`, Option 1, as ruled — **minus** its §7.8 (`13.2.6`) and §7.9
(`13.3.2`'s first reason), which the author deferred. That deferral is the only source of deviation from
the drop-in text, and every deviation below traces to it.

---

## 1. Site by site

Line numbers are the file's own, verified against the file before each edit; the design findings' numbers
were correct throughout.

### `aeh.md`

| # | site | what landed | deviation from the §7 drop-in, and why |
|---|---|---|---|
| 1 | L67 — Inselmann's window read in blocks per bit | "its block-per-bit reading needs that average as a statement about orbits: a theorem inside the digit budget (`13.2.4`(g)), and past it neither a consequence of the letter statistics asserted here nor independent corroboration of them" | §7.10 routes the past-budget case through `13.2.6`'s prefix form. With `13.2.6` deferred there is nothing to route to, so the clause states the negative only. The retracted half — "is a consequence of the letter statistics asserted here" — is gone either way |
| 2 | L69 — `13.2.3`'s gap sentence | §7.4 verbatim | only the trailing pointer `(13.2.6)` dropped. `O(1)` → `O_P(1)`, the gap named as `s_n − s_0`, and where it is and is not negligible |
| 3 | L83 — the Inselmann ceiling bullet | §7.1 **verbatim** | none. The three unsupported claims are gone; what remains is Thm `1.1`'s quantified range, Cor `1.4`'s endpoint, and a scope decision named as such |
| 4 | L84 — the consistency bullet | consistency as compatibility with the target law; `13.2.4`(g) below the budget; above it, the vanishing frequency of `†` and nothing more, with the failure mechanism in one line | §7.2's `τ ↓ 4θ` prefix pin and its `13.2.6` pointer removed (deferred). §7.2's Fatou/`τ/θ` trap also omitted — it is new positive material, and round 4 adds one item only. Kept: the single-letter construction (`cT_N` at the budget-exhausting block, the following `o(T_N)` in the cemetery), so the negative claim "can fail by any amount" is checkable on the page without a numbered proposition |
| 5 | L86, L88–91, L93 — lead-in, two-range fence, closing sentence | §7.3, with row 2's annotation and the closing clause restated | §7.3 ends both with "only `13.2.6`'s prefix form says an orbit realizes it". Landed as "nothing here says an orbit realizes it past the budget" and "past it the record carries no orbit statement supplying it". Row 1's annotation is §7.3's verbatim, `13.2.4`(g) included |
| 6 | L98 — `13.2.4`(a)'s index | `P_B(S_(n+1) ≥ J)` → `P_B(S_n ≥ J)` | none. The proof below it and the base-case display at L61–62 already state the sharp form; this was the only site carrying the loose one |
| 7 | L104–108 — `13.2.4`(g), new, appended after (f) | §7.6 **verbatim** | one formatting normalization: `S_{T_N}` → `S_(T_N)`, the page's convention for compound subscripts. No anchor renumbered; (g) appends to the existing lemma and is the only item added |
| 8 | L110 — Corollary `13.2.4.1` | §7.7 **verbatim** | none. It now quantifies over `τ` and uses (g) to identify the tallied word with the letter word — the step it was previously missing |
| 9 | L122 — `13.3.1`'s budget clause | §7.11 **verbatim** | none |
| 10 | L124 — `13.3.2` | **UNCHANGED** | §7.9 deferred by the author. As written it is conservative and true |
| 11 | L8 — the Current-state blockquote | **UNCHANGED** | §7.12's only change is the prefix-drift clause (`13.2.6`). With that deferred, the existing sentence — "There is no drift or contraction consequence: equidistribution at each fixed `k` does not deliver one, and the corresponding trajectory statement is unconditionally known anyway (13.3.2)" — is exactly what `13.3.2` still says. Editing it would either claim the deferred result or contradict `13.3.2` |
| 12 | L207 — `13.6.4`'s residual cell | "of `π_{k,D}`-mass" → "of `π_{k,D}`-mass **at most**" | see §2 |

### `paper/collatz-reduced-v3.tex`

| # | site | what landed | deviation |
|---|---|---|---|
| 13 | L322–329 | §7.13, restated | its `13.2.6` sentence — the prefix mean pinned "once `τ` is taken down to `4θ`" — replaced by the negative alone: past the budget the hypothesis "supplies less, and only about frequencies", a vanishing frequency of `†` "is not a bound on a sum over its complement", and the Cesàro statement "does not follow there and can fail by any amount". The closing clause reads "a theorem about orbits below the budget, and not a consequence of the hypothesis above it" |
| 14 | L385–387 (now L397–400) | "a theorem where the cylinder count runs (`aeh.md` Lemma 13.2.4(g)) and, past it, is neither a theorem nor a consequence of Hypothesis 5.1 (`aeh.md` §13.2.3)" | §7.14 points past-budget at `13.2.6`; landed pointing at `13.2.3`, where the corrected consistency bullet now lives |
| 15 | L393–394 (now L406–408) | §7.15 **verbatim** | none |
| 16 | L246 | **UNCHANGED** | §7.16's only change is the prefix caveat (`13.2.6`). The sentence as printed — "window equidistribution at each fixed `(k,D)` does not control the means of the unbounded `m_+` and `s`, so no drift or contraction statement about orbits follows from it" — is already the subtraction's own position, and it mirrors the frozen `13.3.2` |
| 17 | L447 (now L461) | the pin, `677a76a` → `e634513` | committed alone, as `ff7c999`. See §4 |

No numbered theorem's claim was strengthened, weakened or renumbered. `hyp:aeh` itself is untouched, symbol
for symbol; only the prose around it moved.

### `publication.md`

| # | site | what landed | deviation |
|---|---|---|---|
| 18 | L29 | "a two-letter statistic that Thm 1.6 does not give, that the classical cylinder count supplies unconditionally only inside the digit budget (aeh.md `13.2.4`(g)), and that `13.2.1` does not itself assert past it (aeh.md `13.2.3`)" | §7.17's middle clause cites `13.2.6`; landed with the same shape but the negative in place of the prefix form |
| 19 | L41 | **UNCHANGED** | §7.17 rewrites it to record the prefix drift consequence. With that deferred, the printed sentence — "**Claim no descent or drift consequence for AEH** (aeh.md `13.3.2` carries none)" — is correct, and it is the sentence `13.3.2` still supports. Nothing in the repository now claims a drift consequence for AEH |

---

## 2. The `13.6.4` union bound

**Landed: "of `π_{k,D}`-mass" → "of `π_{k,D}`-mass at most `(D+1)·2^(−(D−1))`".** The exact expression was
the other option offered and was not taken.

The arithmetic, checked rather than recalled. Under `13.6.3`(v), `s` is geometric(1/2) on `{1,2,…}` and
`σ_n = s_n + m_n` is a sum of two independent such, so `P(σ_n ≥ D) = D·2^(−(D−1))` and
`P(s_(n+1) ≥ D) = 2^(−(D−1))`; the printed `(D+1)·2^(−(D−1))` is their sum, i.e. the union bound, and the
intersection it double-counts has mass `D·2^(−2(D−1))`.

Two reasons for "at most" over the exact figure. First, the cell's only use in the proof is as an upper
bound — the next clause reads "each `L`-letter frequency is within `L(D+1)·2^(−(D−1))` of the corresponding
block frequency at every `D`", which is valid unchanged and is all the argument consumes, since the
definition quantifies over every `D` and the bound goes to `0` either way. Second, the exact mass depends on
the independence of `σ_n` and `s_(n+1)`, which holds under `13.6.3`(v) but is an extra hypothesis to carry
in a sentence whose job is to bound a residual; "at most" needs nothing. The proof is unaffected in either
reading, and no downstream number changes.

---

## 3. The two `open-problems.md` entries, as landed

New section **`11.11`, "What AEH's budget clause supplies past the digit budget"**, appended after `11.10`;
the front-matter `scope:` field records it as post-monolith. `11.11` and not `11.9`: the front matter
records that `11.10` "was recorded as 11.9 in pre-2026-07-23 briefs", so `11.9` is deliberately vacant and
reusing it would collide with stale citations.

The section opens by stating what `13.2.3` now records — unconditional inside the budget, frequency-only
past it, no Cesàro mean — then poses two questions and points at `briefs/v3r4-clock-findings.md` §2 and §7.8
for the drafted argument. Neither is claimed; the section says so, and says `13.3.2` stands as written until
the first closes.

**Open question 1 — may `τ` be taken down to `4θ`, and what does the in-budget prefix carry if it may?**
States the drafted argument in full shape (the `Λ_N/T_N → τ/θ` upper bound from block `n*−1` being tallied;
the Fatou lower bound of `4` from the `L = 1` letter marginals; `τ_k = θ(4 + 1/k)` admissible; the diagonal
in `k`; `Σm/T_N → 2`, `Σs/T_N → 2`, `−β` per block along the prefix) and names the hinge: whether the
quantifier is to be read with `τ` arbitrarily close to `4θ` or with slack bounded away from it. Closure is
checkable in either direction — a reason inside the record to prefer a fixed slack, which deletes the
statement; or the quantifier defended *plus* the prefix statement written out at it, the altitude step's
per-step `O(1/x_exit)` error included. It also records that the clause is unmeasured: no run reports the
across-orbit distribution of `S_(n*−1)/T_N` at `τ/θ` near `4`.

**Open question 2 — does `13.3.2`'s first reason need rescoping, and if so to what?** Conditional on 1 by
construction: if 1 closes negatively, `13.3.2`'s first reason is already exactly right; if affirmatively, it
is incomplete over the admissible family and is restated as a fixed-pair statement, with the second reason
becoming load-bearing — which it can carry, admissibility capping `τ` at `4.8188…`, Inselmann's own horizon.
Recorded explicitly: nothing about `13.3.2`'s second reason or its conclusion is in question either way.

---

## 4. The pin

**`677a76a` → `e634513`**, committed alone as `ff7c999`, after the record (`123683d`) and the paper
(`e634513`).

`677a76a` is an ancestor of `276b87c` (checked with `git merge-base --is-ancestor`), which is round 3's own
residuals commit, so the old pin sent a reader checking `13.2.4` or `13.6.4` to pre-correction proofs.
`e634513` is this round's record-and-paper commit and is a descendant of both.

**Verification of Appendix A's claim before committing** — "every wiki section and script named in this
paper is cited at commit `e634513`". The paper's named references were extracted from the tex rather than
recalled: `aeh.md` §13.1, §13.2.3, Lemma 13.2.4, Lemma 13.2.4(g), Corollary 13.2.4.1 (via Lemma 13.2.4),
Proposition 13.2.5, §13.3.2, §13.4, §13.5, §13.6.3(iii), §13.6.3(v), Theorem 13.6.4, §13.6.5;
`itinerary.md` §14.15.1.5; `stage3.md` §11.8.6.3; `cycles.md` §12.2.3, §12.6.1, §12.8.6; and the six named
scripts `experiments/{period1,period2,period3}_cycles.py`, `one_step_propagation.py`,
`anchor_increment.py`, `absorption_law.py`. Every file and every anchor is present at `e634513`, checked by
`git show` against that commit and not against the working tree. Present **in corrected form**, checked
positively and negatively: `13.2.4`(a) prints `P_B(S_n ≥ J)` and no occurrence of `P_B(S_(n+1)` remains;
`13.6.4`'s residual cell reads "at most"; the consistency bullet reads "compatibility with the target law";
and neither the retracted "exactly `E_B[m + r] = 4` in Cesàro form" nor "No `τ ≥ 4.8188…` is protected"
survives anywhere in the file.

The two other commit pins in the paper (`72ec88e` and `9d9d1ec`, both in the v2/v3 version notes and both
pointing at `cycles.md` §12.8.6 as it stood when each note was written) are deliberate historical pins in
published-note text and were not touched.

---

## 5. Build report

`pdflatex -halt-on-error -interaction=nonstopmode`, three passes, run twice — once after the paper edits and
once after the pin. Final state:

| pass | exit | output |
|---|---|---|
| 1 | `0` | 17 pages, 434,853 bytes |
| 2 | `0` | 17 pages, 434,853 bytes |
| 3 | `0` | 17 pages, 434,853 bytes |

* **Page count 17**, unchanged from the pre-round build (`pdfinfo` on the committed PDF at `6ead133`: 17).
  Nothing was pruned and nothing needed to be.
* **Box warnings: zero overfull.** One underfull `\hbox` (badness 1067) at tex L484–485. **Pre-existing and
  unrelated:** it sits in the `\thebibliography` block (the `lagarias` bibitem), and rebuilding `HEAD`'s tex
  in a scratch directory reproduces the same warning at the same badness, at L470–471 — the 14-line shift is
  exactly this round's insertions above it.
* **Unresolved references: none.** The log carries no `LaTeX Warning` of any kind — no undefined reference,
  no undefined citation, no rerun request. `rerunfilecheck` appears only in the package banner.
* **The changes are in the artifact.** From `pdftotext` on the built PDF: "Consistency is compatibility with
  the target law rather than a claim about orbits"; "aeh.md Lemma 13.2.4(g), whose two error terms are
  precisely the two clauses of admissibility"; "is not a bound on a sum over its complement"; "does not
  follow there and can fail by any amount"; "not a consequence of the hypothesis above it"; "neither a
  theorem nor a consequence of Hypothesis 5.1"; "all but o(TN) of them within the budget"; "cited at commit
  e634513". The three replaced strings are absent: "part of Hypothesis", "all of them within the budget.
  Evaluating", "a mean the hypothesis itself supplies". (`pdftotext` drops math-mode `τ`, `θ`, `†`, `β` from
  its extraction; that is an extraction artifact — the glyphs render in the PDF.)
* **Encoding.** All four edited files decode as UTF-8 with no BOM and no `Ã`/`Â`/`â€` sequences; `≤`, `—`,
  `ε`, `θ`, `τ`, `†`, `β` all present at their expected counts in `aeh.md`. Every edit was made with the
  Edit tool; no `Get-Content | Set-Content` and no PowerShell redirection was used anywhere.

---

## 6. Found and not fixed

Reported, per the brief, rather than repaired.

1. **`aeh.md` `13.3.2`: "the endpoint `1/β` in block units is this page's own hypothesis, not his theorem".**
   Same genre as the L84 claim this round retracts — reading `4.8188…` `T_1`-steps per bit as `1/β` blocks
   per bit needs the Cesàro mean, which the hypothesis does not supply past the budget. It is not false as
   written: its function in the sentence is to *refuse* the endpoint to Inselmann, not to claim it for AEH,
   and the surrounding sentences already say the exact source for the two-letter statistic is Terras's
   cylinder count "whose range is precisely the `θ < 1/4` frontier". But a fifth reviewer may read it as the
   retracted claim. `13.3.2` is frozen this round by the author's ruling; this belongs to the round that
   reopens it, alongside `open-problems.md` `11.11`(2).
2. **`paper` L419 (now L432–433): "it is therefore a consequence of Hypothesis 5.1 and not available to
   underwrite it".** The same shape, and defensible for a different reason: the sentence names the
   *frequency* with which a Syracuse step ends a block, which is a one-letter marginal of `B` and genuinely
   is asserted by the hypothesis. What is not asserted is the *passage to block time* the sentence
   introduces, which needs the mean. Not on the list; left as printed.
3. **`paper` L321 cites `\cite[Thm.~1.10]{inselmann}` for protection**, but protection is stated in the
   budget count `S_n`, which is `T_1`-time; Thm 1.1 is the `T_1`-envelope. `aeh.md` L82 cites both.
   `\cite[Thms.~1.1 and~1.10]{inselmann}` would match. The design flagged this as optional (§7.18) and it is
   not on the apply list.
4. **`aeh.md` L58 says "for every `J ≥ 1`"** where `13.2.4`(a) and the paper both say `J ≥ 2`. At `J = 1`
   the bound is vacuous rather than false, so nothing is wrong. §7.18, likewise not required.
5. **`aeh.md` `13.6.3`(i)(a)'s "(irrelevant to every Cesàro limit below)"** — checked against the new
   `13.2.3` sentence, which now says the same one-index offset *is* material at the boundary of the tallied
   set. The two are consistent: `13.6.3`(i)(a)'s "below" is `13.6`'s frequency limits, where a fixed one-index
   offset moves nothing, while `13.2.3` localizes the one place a sum over an unbounded letter is at stake.
   No edit made.

Nothing else in the sweep still carries the retracted claim: `"own content"`, `"13.2.1 itself asserts"`,
`"in Cesàro form"` and `"all of them within budget"` have no occurrence in any tracked page.

---

## 7. What did not land, and where it went

`13.2.6` (design §7.8) and the rescoping of `13.3.2`'s first reason (§7.9) are **not in the record**, per
the author's deferral. They are in `open-problems.md` `11.11` as two checkable questions, with the drafted
argument pointed at in `briefs/v3r4-clock-findings.md` rather than restated, so nothing is lost and nothing
is claimed. The reviewer's pruning plan was likewise deferred to a separate round and no content was cut:
the paper is the same 17 pages it was.
