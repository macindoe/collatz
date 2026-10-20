# Findings: scope-drift check of paper 1 v4, readability round 5 (option A)

**Branch and base.** Branch `paper1-v4-readable-5-check`, cut at **`678ebff`** (the merge of the round-4 check record; it carries round 5's content commit `ee20c3a` and the 63,000 restatement `4ee9029`). The comparison base is round 4 at `190b6af`. Baseline: the claims ledger `paper/collatz-reduced-v4-claims.md` at `678ebff`. It differs from the ledger at `190b6af` only in rows C-3.5(a) and C-3.6 (the 63,000 restatement). Method as in the round-4 check (`98665e3:briefs/paper1-v4-readable-4-check-findings.md`): every sentence of the plain abstract, the Symbols page and §§1–8 that changed between `190b6af` and `678ebff` and states a fact, a credit, a scope or a provenance claim is mapped to the ledger row(s) behind it. Done 2026-10-20. The `.tex` was not edited; nothing went outward.

**Verdict in one paragraph.**
- **All eight fixes are applied with at least their scope.** That is the round-4 check's four and cold read 3's four. Cold read 3's item (d) is superseded: the count is now 63,000 and the PENDING-REVERIFY markers are gone.
- **52 changed sentences checked: 51 keep their row's scope, 1 changes it, 0 have no row.** The one change states as fact what the lock grades as heuristic: §4 "Why it matters", "each decided step uses up binary digits … and nothing restores them". Four optional wording notes follow (§3.7).
- **Moved text.** Each guided account (Appendices C, D, E) is round 4's §4, §5 or §6 with exactly a listed set of edits applied, word for word (4, 9 and 12 edits). Two of the edits are not recorded in §7e. Neither changes a claim: "proves that they go no further" → "why they go no further", and "three-block threshold" → "three-block bound".
- **Formal statements.** With the guided accounts removed, Appendices A–I and the Technical summary differ from round 4 in exactly five lines: the three appendix lead-ins, Remark C.6 and Appendix G's first row. All 19 formal statement environments are identical. The abstract, the Version and Author's notes, and §§2–3 are identical.
- **63,000.** All three places say "all 63,000 valid states … ω = 1 included". Remark C.6 and Appendix G name `experiments/depth_law_reverify.py`. The App C guided account names no script: it points to Remark C.6 and to Appendix G for the scripts. The committed output says 63,000 states, `ω = 1` checked separately (63 states, 784 checks, 0 failures), and "669250 checks on 63000 states, 0 failures".
- **Worked numbers.** All recomputed in fresh code. Part E has 29 checks, 0 failures. The whole script runs **74 checks, 0 failures; 11 negative controls, all rejected.**

---

## 1. The eight fixes

Part A of `experiments/paper1_v4_readable5_check.py` requires each new wording at `678ebff` and requires each old wording to be absent from the whole `.tex`.

| Fix | Asked for | At `678ebff` | Verdict |
|---|---|---|---|
| R4-1 | §1: "not the same as saying that almost no orbits misbehave" | verbatim in §1's not-claimed bullet; "weaker than saying" is gone | applied, full scope |
| R4-2 | "older and broader" attached to digits of 2-adic logarithms | App E guided account carries the check's own wording verbatim. §7 now reads "the digits of 2-adic logarithms of whole numbers, of which the anchors are instances". "Older and broader" occurs twice, in the guided account and in App E's formal text, both after "2-adic logarithms", and never in §§1–8 | applied, full scope |
| R4-3 | the Lemme 4 comparand | App D guided account: "larger throughout this range than 2 to the power (n times the shrinking factor)"; the bare form is gone | applied, full scope |
| R4-4 | drop ", which the sharper control set aside" | gone everywhere; item (2) ends "both artifacts of including small starting values;" | applied, full scope |
| CR3-a | "halvings, beyond the first" | §1 (ii), §4, the App C guided account and the Symbols row for `s`; the old "the number of halvings that end each block" is gone | applied, full scope (four places) |
| CR3-b | the `p = 7` staircase marked as v3's instance, outside part (i)'s bracket | in §5 and in the App D guided account. v3's `.tex` carries `m = (4,7,9,15,23,35,1)` with `γ = 6.74`. The ledger bracket C-4.6(i)a is `3.683012 ≤ γ ≤ 5.140212`. Recomputed `γ = 6.743758`, outside it. "Found by an earlier search" matches `experiments/uniform_trim.py`, the C-4.6(iv) script: a seeded, jittered search at `p = 5, 6, 7` | applied, full scope |
| CR3-c | §8 split | three sentences as recorded in §7e; "hence the row entered" is gone | applied, full scope (C-RW.23) |
| CR3-d | 62,937 | superseded by `4ee9029`: no PENDING-REVERIFY marker and no 62,937 remain in the `.tex`; the rebuilt PDF shows "63,000" on pp. 15, 17, 38 and no "62,937" | applied (superseded by the re-run) |

Cold read 3 item 41 ("Apply it to the staircase, whose γ is at most about 5.14") still reads "the staircase" in the App D guided account. It now sits inside the part (i) bullet, after the instance has been marked as outside the family, so it is no longer contradictory. Optional: "the staircases of part (i)".

**Verdict: 8/8 applied, none narrower than asked.**

## 2. Unchanged text and formal statements (part B)

- **Identical:** the plain abstract, the Version note and Author's note, and §§2–3.
- **Appendices.** From `\appendix` on, with the three guided accounts cut out, exactly five non-blank lines differ from round 4:
  - the lead-ins of Appendices C, D and E ("It opens with a guided account …");
  - Remark C.6: exactly two edits. The count clause becomes "63,000 … `1 ≤ d < 64` (`ω = 1` included, where every law holds as stated)", and `depth_law_reverify.py` is added to the code sentence;
  - Appendix G's first row: the same two edits.
- **Formal statements:** all 19 theorem, proposition, lemma, corollary, definition, hypothesis and heuristic environments are identical to round 4.
- **Control:** a one-character edit inside Theorem C.5 is detected.

**Verdict: the formal statements of B–E are unchanged. The only content edits outside the guided accounts are the `4ee9029` restatement in Remark C.6 and Appendix G.**

## 3. Sentence-by-sentence verdicts (§§1–8, Symbols page; the abstract is unchanged)

"Same" means the sentence restates the named row(s) with the row's quantifiers and scope words, or with a gloss the row supports. Navigation sentences are checked but not counted. All of them resolve:
- **Symbols page.** It says `p` also appears in "`p`-adic" in the Author's note (true). It says the appendices use `q`, `γ`, `X₀` and `p₁(X₀)` of App D's guided account (all four occur there). The four rows dropped from the table are used nowhere in §§1–8 (checked), and "`m`-cycle" no longer occurs in §§1–8.
- **How to read.** "§§4, 5, 6 are one page each". The PDF at `678ebff` puts §4 on p. 8, §5 on p. 9 and §6 on pp. 9–10. Appendices C, D and E each open with a guided account.
- **"The full account" paragraphs.** Each lists contents that the guided account actually carries.

### 3.1 Section 1 (2)

| # | Sentence (abridged) | Rows | Verdict |
|---|---|---|---|
| I-1 | (ii) "One exact rule gives the number of halvings, beyond the first, that end each block." | C-3.3, C-Int.6 | same (CR3-a) |
| I-2 | not-claimed bullet: "that is not the same as saying that almost no orbits misbehave" | N-15, C-5.exc | same (R4-1) |

### 3.2 Section 4 (14)

| # | Sentence (abridged) | Rows | Verdict |
|---|---|---|---|
| A-1 | three things decide where the orbit goes next: `s`, the absorption, the next entry depth | C-3.5(a) (`d₊ = m₊ + a₊`), C-2.1 | same (round 4's sentence, now the guided account's opening) |
| A-2 | "The paper gives an exact rule for each (Thm C.3, Lemma C.4, Thm C.5)" | C-3.3, C-3.4, C-3.5 | same |
| A-3 | sort into eight kinds by `ω mod 8` and the parity of `d` | C-3.3 | same |
| A-4 | "On six kinds s is a fixed number, 1 or 2" | C-3.3(b) | same (all valid states `ω < 3001`, `d ≤ 40`) |
| A-5 | lifting kinds: `s ≥ 3`, "2 plus the number of lowest binary digits on which d agrees with a fixed binary pattern belonging to ω, its anchor" | C-3.3(a), C-3.1 | same (10,000 lifting states, anchor `M(ω) = N(ω²)` mod 2⁶⁴, 0 mismatches) |
| A-6 | "A factor of 3 is gained exactly when s is even" | C-3.4 | same (`ω < 601`, `d ≤ 20`) |
| A-7 | finitely many digits with three numbers either predict the next step exactly or say, correctly, that the next burst is deep; never wrong (Thms C.7, C.8) | C-3.7, C-3.8 | same |
| A-8 | "One step is completely described." | C-D.1, C-Abs.2 | same |
| **A-9** | "But each decided step uses up binary digits of the starting number, and nothing restores them." | C-3.9(a)(c), C-Int.13 | **scope changed** (§4) |
| A-10 | "This accounting, stated as a heuristic and not proved (Heuristic C.9), suggests that no finite window of digits can decide an orbit's whole future without further input — statistical (§6) or about the structure of cycles (§5)" | C-3.9(e), N-1 | same |
| A-11 | "the difficulty sits in one place: where the digits of the anchors come from" | C-Int.14 | same |
| A-12 | `ω = 1`: anchor all zeros; on `d` even, `s` = 2 + trailing zeros of `d` | C-3.3(a)(d) | same (`N(1) = 0` recomputed) |
| A-13 | `(1,2)`: `d = 10₂`, one trailing zero, `s = 3`; `3·5 + 1 = 16` halves four times | C-3.3, C-2.2 | same (recomputed) |
| A-14 | `(7,1)`: kind (7, odd), `s = 2`, even, so a factor of 3: `5 + 1 = 6 = 2·3` | C-3.3(b), C-3.4 | same (recomputed) |

### 3.3 Section 5 (15)

| # | Sentence (abridged) | Rows | Verdict |
|---|---|---|---|
| C-1 | a cycle of `p` blocks multiplies by 3 `n` times and halves `K` times | C-4.setup | same (def) |
| C-2 | "Returning to the start forces 2^K to be only slightly larger than 3^n — because the `add 1' in each step pushes the number up a little" | C-4.1(a), C-4.2 | same. Optional note (§3.7 a) |
| C-3 | "Counting (`size') arguments use only this closeness." | C-4.5(b), the paper's own definition (App D "Size") | same. Optional note (§3.7 b) |
| C-4 | classically a bound, the uniform trim (Rozier 1991; SdW 2005), on how large `n` can be for `p` blocks | C-4.5(a), C-RW.14, N-3 | same |
| C-5 | "it weakens exponentially as p grows, and with Rhin's theorem it leaves only finitely many candidates at each p" | C-Abs.9, C-4.5(c)(d) | same |
| C-6 | rederives the bound by another route; rederives no cycles other than 1, 4, 2, 1 at one to three blocks; proves the weakening cannot be avoided by size arguments | C-4.5.cr, C-4.4, C-Abs.10, C-4.6(i)d | same |
| C-7 | staircases pass every size test, every starting block, from 3 blocks on (16 by proof, 3–15 by computer check; 2 and 4 examples); and from an explicit threshold on with every number at least a given size | C-Abs.11, C-Abs.12, C-4.6(i)a–c, C-4.6(iii)a, N-19 | same (the bracket is dropped here, which weakens nothing). Optional note (§3.7 c) |
| C-8 | "certain whole numbers built from it must divide others" | C-4.1(c) | same |
| C-9 | "The staircases pass every size test, and every one tested fails these divisibility conditions." | C-4.ver(c), C-4.6(iv), N-9 | same |
| C-10 | ruling out cycles uniformly in the number of blocks needs divisibility, as Halbeisen–Hungerbühler concluded for length | C-4.6.close, C-Abs.14 | same |
| C-11 | "Every statement about the staircases concerns how far size arguments reach; none bears on whether cycles exist." | C-4.ver(d), N-9 | same |
| C-12 | the seven-block example: `n = 94`, `K = 94 + 55 = 149`, "(each block halves once per step, n times in all, plus its exit valuation, 55 in all)" | C-4.6(iv) | same (recomputed; `K = Σ(m_t + s_t)`) |
| C-13 | first six climb, the last falls 49 extra halvings: an ever-growing orbit's profile bent into a loop | C-4.7, C-Abs.11 | same |
| C-14 | "It passes all seven size tests, yet fails the divisibility conditions, so it is not a cycle." | C-4.6(iv) | same: 7/7 size conditions hold and `q ∣ R_r` at 0 of 7 rotations. Checked against the rational fixed point of the block map, and against the trivial cycle, where both conditions hold |
| C-15 | v3's instance, found by an earlier search, Theorem D.6(iv); not of part (i)'s family (3.68–5.14); "this one's is 6.74" | C-4.6(iv), C-4.6(i)a | same (CR3-b; `γ = 6.743758`) |

### 3.4 Section 6 (12)

| # | Sentence (abridged) | Rows | Verdict |
|---|---|---|---|
| H-1 | a letter is the pair (entry depth, exit valuation) | C-5.1 | same (def) |
| H-2 | Terras's picture: independent coin-toss counts, each part 1 w.p. ½, 2 w.p. ¼, … | C-5.1 (`B[w] = Π 2^{−(m+r)}`), C-Int.16 | same |
| H-3 | the conjecture: budget, horizon, every admissible choice of the two multiples, patterns of every finite length, all but a vanishing proportion of starts | C-5.1, C-5.adm, C-Abs.15 | same. Optional note (§3.7 d) |
| H-4 | "Part of it is proved: while the orbit has done fewer halvings than the start has binary digits, the conjecture holds, because the start's own digits fix its first blocks exactly (… proof assembled in the project record, Appendix G)" | C-5.thm (`τ < 1`, every word length), C-5.base, C-Abs.17 | same |
| H-5 | "Beyond that it is a conjecture, and its consequences are proved on the condition that it holds." | C-Abs.16 | same |
| H-6 | under the coin model a factor of 3 has chance ¼ + 1/16 + … = ⅓, because that happens exactly when the exit valuation is even | C-5.piledger, C-3.4 | same (the uncapped model; the cap caveat belongs to `π_{k,D}`) |
| H-7 | facts about the model, not about orbits; no statement that orbits drift downward follows | C-5.piledger, N-11 | same |
| H-8 | "typical orbits keep following the model after the start's own digits have been used up" | C-5.clock | same |
| H-9 | "It says nothing about where any single orbit ends up." | N-15, C-5.exc | same |
| H-10 | the running example's letters `(3,1), (1,2), (1,3), (1,1)` | — (worked) | same (recomputed from the orbit of 7) |
| H-11 | `(1,2)` has chance ½ × ¼ = ⅛ | C-5.1 | same |
| H-12 | the test campaign's "four apparent anomalies all dissolved under sharper controls" | C-5.cal, C-Abs.18 | same |

### 3.5 Section 7 (6)

| # | Sentence (abridged) | Rows | Verdict |
|---|---|---|---|
| O-1 | one step under exact control: the anchor governs it, apart from the absorption with its own exact law; windows decide without error | C-D.1 | same |
| O-2 | one difficulty seen from two sides: statistical (Hyp E.1), divisibility of Prop D.1 "which size alone cannot decide (Thm D.6)" | C-D.2 | same |
| O-3 | "The staircase belongs to both sides." | C-D.2, C-4.7 | same |
| O-4 | arithmetic statements beyond the size level, needed by any uniform exclusion; "for instance, that a cycle's anchors are rigid, since going once round a cycle they return to where they started and their changes add up to zero" | C-D.3 | same (the lock's "rigidity of closed anchor walks, since a cycle's anchors return and `Σ ΔM_t = 0`", nearly word for word) |
| O-5 | windows succeeding one another, treated as a chain (transfer operators) | C-D.3 | same |
| O-6 | "any progress on the digits of 2-adic logarithms of whole numbers, of which the anchors are instances (Appendix C) — a problem this paper inherits rather than creates" | C-D.3, P-29, C-D.1, C-Abs.2 | same (C-D.1 itself calls the anchor "one 2-adic logarithm"; `M(ω) = −2 log ω / log 9`) |

### 3.6 Section 8 (3)

| # | Sentence | Rows | Verdict |
|---|---|---|---|
| P-1 | "Williams's open problem (1) … asks for the map sending one skeleton to the next, and Section 4 answers it in part." | C-RW.23 | same |
| P-2 | "It gives exact laws for where a trajectory leaving a row lands — the exit valuation and the entry position, and hence which row is entered." | C-RW.23 | same |
| P-3 | "It gives no law for which skeleton is entered: on that question, F only restates Williams's Proposition 3.10." | C-RW.23 | same |

**Totals: 52 sentences. 51 same, 1 scope changed, 0 unsupported.**

### 3.7 Optional wording notes (no scope change)

- **(a) C-2.** Round 4's sentence, kept in the guided account, said "but only by a little, and by less the larger the cycle's numbers are". C-4.2 makes the closeness depend on the size of the elements. §5's "only slightly larger" drops that dependence; for the trivial cycle, 4 against 3 is not slight. Optional fix: "… to be only slightly larger than 3 to the power n when the numbers are large --- because …".
- **(b) C-3.** The size conditions of Prop D.1 are `q ≤ R_r` for every rotation, and those involve the whole configuration, not only `γ`. "Use only this closeness" matches the guided account's definition ("arguments from how close …"). Optional: "Counting (`size') arguments are arguments from this closeness alone."
- **(c) C-7.** "For 2 and 4 blocks, passing examples without that range": §5 states no range of closeness before this point, so "that range" has no antecedent. The abstract's version follows its bracket. Optional: "for 2 and 4 blocks, passing examples only".
- **(d) H-3.** "Show the coin frequencies … in all but a vanishing proportion of starts" omits the tolerance of C-5.1 ("for every `ε > 0`"). The guided account keeps it. Optional: "show the coin frequencies, to within any fixed tolerance, …".

## 4. The one scope change, with its fix

**A-9, §4 "Why it matters": "But each decided step uses up binary digits of the starting number, and nothing restores them."**
- **Ledger:** C-3.9(a) and (c) grade the consumption, and the claim that nothing regenerates it, as **heuristic**. C-3.9(a) says the digits suffice (Thm C.7, proved); "that they are also needed is part of the heuristic". C-Int.13 says the accounting "*indicates* that each decision consumes digits irreversibly". The abstract, §1 and the guided account all keep the hedge.
- **Problem:** the sentence states consumption and non-restoration as fact. The heuristic label arrives only in the next sentence ("This accounting, stated as a heuristic …"), and it reads as attaching to the conclusion about windows, not to this premise.
- **Fix:** "But, by an accounting stated as a heuristic and not proved (Heuristic~\ref{prop:budget}), each decided step uses up binary digits of the starting number, and nothing restores them; this suggests that no finite window of digits can decide an orbit's whole future without further input --- statistical (Section~\ref{sec:aeh}) or about the structure of cycles (Section~\ref{sec:cycles})."

## 5. Moved text: the guided accounts against round 4's §§4–6 (part C)

The test does not look for any wording. It takes round 4's §4, §5 and §6 (whitespace normalised), applies a listed set of edits, each matching exactly one place, and requires the result to equal the guided account of C, D or E. Every word-level difference is printed in the output.

| Appendix | Round-4 words → guided words | Edits | Of which |
|---|---|---|---|
| C | 1,495 → 1,486 | 4 | header (the move); CR3-a; a self-pointer dropped; `4ee9029`'s count with "`ω = 1` included" |
| D | 2,211 → 2,238 | 9 | header; "section" → "account"; a self-pointer dropped; CR3-b's sentence; R4-3; two pointers → "below"; **two not recorded in §7e** |
| E | 1,863 → 1,863 | 12 | header; "section" → "account"; seven pointers → "below"/dropped; a self-pointer dropped; R4-2; R4-4 |

**The two unrecorded edits, both in App D:**
1. "This section explains what the classical counting arguments achieve against cycles, and **proves that** they go no further" → "This account explains … and **why** they go no further". No claim changes: the guided account explains, and the formal part that follows proves (C-Abs.10).
2. "none of them falls below that three-block **threshold**" → "… that three-block **bound**". This is the round-4 check's optional note on C-13, applied. The quantity is the same (C-4.6(iv)).

**Control:** a one-number change in App D's guided account (0.698 → 0.689) breaks the equality.

**Verdict: the guided accounts are the round-4 main text verbatim apart from the listed edits. All but two are declared in §7e or follow from the move, and the two that are not change no claim.**

## 6. The 63,000 sentence (part D)

| Place | 63,000 | `ω = 1` included | Script named |
|---|---|---|---|
| App C guided account, "Checks" | yes ("all 63,000 valid states with ω below 3000 and d below 64, ω = 1 included") | yes | **no**: "(Remark C.6)" and "Appendix G lists the scripts" |
| Remark C.6 | yes ("ω < 3000, 1 ≤ d < 64 (ω = 1 included, where every law holds as stated)") | yes | yes, `experiments/depth_law_reverify.py` |
| Appendix G, first row | yes (same wording) | yes | yes, `depth_law_reverify.py` |

- **Ledger:** rows C-3.6 and C-3.5(a) say the same, with the script named.
- **Committed output** (`experiments/depth_law_reverify_output.txt` at `678ebff`):
  - "valid states checked: 63000";
  - a separate `ω = 1` block, "states: 63; checks: 784; failures: 0";
  - "TOTAL: 669250 checks on 63000 states, 0 failures; controls 9/9 bite; verdict PASS".
- **Fresh count:** 1,000 values of `ω` × 63 depths = 63,000. Control: 62,937 is rejected as the full count.
- **Fresh law check:** Theorem C.5's entry-depth law and `d₊ = m₊ + a₊` hold on all 63 states `(1, d)`, `1 ≤ d < 64`, with `δ_s = N(1 − 2^s)` computed by 2-adic discrete log. Control: dropping `δ_s` fails on 31 of them.

**Verdict:** the count and the `ω = 1` clause are right in all three places, and the output says so. The script is named in two of the three. The guided account names no script for any law; it defers to Remark C.6 and Appendix G. If the brief meant "named in all three", one optional insertion closes it: "(Remark~\ref{rem:verify1}; \texttt{experiments/depth\_law\_reverify.py})".

## 7. Worked numbers (fresh code)

`experiments/paper1_v4_readable5_check.py` was written for this check from the paper's text: Definition C.1, Theorem C.5, Proposition D.1 and the main text. It imports nothing from the repository. It uses exact integers and Fractions. It reads the TeX, the ledger, v3's TeX and the depth-law output from git at pinned commits. One command, under a second:

    python experiments/paper1_v4_readable5_check.py

It writes `experiments/paper1_v4_readable5_check_output.txt` and exits 0. **74 checks, 0 failures; 11 negative controls, all rejected.**

**§4**
- the eight-kind rule on every valid state with `ω < 3001`, `d ≤ 40`;
- the anchor rule on 10,000 lifting states;
- `M(1) = 0`;
- `(1,2)`: `d = 10₂`, `s = 3 = v₂(9 − 1)`, and `16` halves four times to 1;
- `13 → (7,1)`, kind (7, odd), `s = v₂(20) = 2`, exit 5; `40` halves three times;
- `5 + 1 = 6 = 2·3`, next state `(1,2)` with `a = 1`; `(5 + 1)·4 = 24 = 21 + 3`;
- gain iff `s` even.

**§5**
- `n = 94`, `Σs = 55`, `K = 149 = Σ(m_t + s_t)`;
- `q = 2^149 − 3^94 > 0`;
- `γ = K − log₂ q = 6.743758`, outside `[3.683012, 5.140212]`;
- all 7 size conditions `q ≤ R_r` hold, and `q ∣ R_r` at 0 of 7 rotations;
- `R_r/q = (x_r + 1)/2^{m_r}` from the rational fixed point of the block map, at every rotation;
- the trivial cycle has `R = q = 1`.

This evaluates one printed configuration and the trivial cycle; it is not a search.

**§6**
- the orbit of 7's letters: `(3,1), (1,2), (1,3), (1,1)`, then `(1,1)` forever;
- `P(1,2) = ½·¼ = ⅛`;
- `¼ + 1/16 + … = ⅓` exactly.

**Controls rejected:**
- a one-character edit in Theorem C.5;
- an undeclared number change in App D's guided account;
- 62,937 as the full count;
- the `ω = 1` entry-depth law without `δ_s`;
- the letter `(2,1)` in place of `(1,2)`;
- `K = 148`;
- `P(1,2) = 1/6`;
- `s = 1` at `(7,1)`;
- the staircase with last exit valuation 48 (`q < 0`) or 60 passing every size condition;
- an anchor of `ω = 3` with one digit flipped.

## 8. Record

- Branch `paper1-v4-readable-5-check`, cut at `678ebff`.
- Deliverables: `experiments/paper1_v4_readable5_check.py`, its output, and this file.
- Not edited: the `.tex`, the PDF, the ledger, and every wiki page. Nothing was pushed.
