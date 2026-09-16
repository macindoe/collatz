# Brief: comb.md 18.7 — the comb path as the itinerary word (η and λ as word statistics), the mean-degree identity, the two determinacies placed on the comb, and the exact digit-transfer law across a door edge (the 3-adic precision loss per door edge is `d − a` digits, sharp) — for a delegated session

**Context required before starting (in order):** `README.md` (strategy and **binding stopping rules** — equidistribution proof effort waits for an idea; measurements may feed the ledger), `AGENTS.md`, `HANDOFF.md` (register norm; delegation pattern; the PowerShell quirk), `comb.md` §18 in full as merged (the peak, the parent rule, Proposition 18.2.3's children and degree, Proposition 18.3.2's corrected distance law, 18.4 completeness, 18.5 the census and its exploratory table), `reverse.md` 14.1.1, 14.2 (the 3-adic anchor `M₃`, Theorem 14.2.4, the exact ternary ledger 14.6.5.2), 14.5.1 (mortality), 14.6.5 (the affine obstruction: the child door's anchor is not a function of the parent's and `s`), 14.10.1 (the cascade step), 14.13 (the KL–LP obstruction; "one digit of precision loss per generation"), 14.14.1 (every edge is `(y, s)`; the dictionary with `C`, `σ = s + m`, `a₊ = a`), `itinerary.md` 14.15.1 (the letter `(m, r)`, Definition 14.15.1.1 of `stratum(y)`, the cylinder theorem 14.15.1.5), `ladder.md` Remark 15.7.6 (bits gained read backward; the door gains `d` ternary digits fixed by `s` alone — the forward reading of what this brief proves on the mirror side), `symbols.md` (registry; `η`, `λ`, peak, comb, the edges), `briefs/peak-comb-brief.md` and its findings (the form of a brief and a findings file; the two corrections to the distance law, so that you use Proposition 18.3.2 as merged).

## Provenance

The author's question of 2026-09-16: how to explore the comb for inter-state determinism along `λ` and `η`, and whether doors need an enumeration like the letter system. The main session's answer, which this brief turns into a section: no new alphabet — the comb's edges *are* the letter system in door coordinates; what the comb adds is one tree on which the forward (2-adic, along door edges) and backward (3-adic, along cascade chains) determinacies sit together, one derivable identity for its level growth, and one exact law at the seam between them. Pre-checked in the main session with throwaway code (not filed; write the script of record from scratch). **Every claim below is a claim to be re-derived and re-verified here, not a fact.** A claim is never confirmed or dissolved by naming its type; corrections carry a re-derivation.

Grade: **formulation**, plus one small proved law (Item D). No front moves. The family frame is not to be used (no columns, no grouping by core, no tears).

## Item A — the path is the word (Lemma 18.7.1)

**Claim.** For a comb node `v` with `F`-orbit `v = v₀, v₁, …, v_η = (1,1)`, let `s_i` be the exit valuation of `v_i` and `a_i` the door index through which the step `v_i → v_{i+1}` enters `v_{i+1}` (`a_i = a₊` of the step, 14.14.1.1; equivalently the `3`-gain). Then the comb path from `v` to the root is, step by step: `⌊(s_i − 1)/2⌋` cascade edges followed by one door edge through door `a_i` of `v_{i+1}`, for `i = 0, …, η − 2`; and for the last step `i = η − 1`, whose exit is the door `1` of the root, `(s_{η−1} − 1)/2` cascade edges and **no door edge** (the lowest sibling on door `1` is the root itself, 18.2.1). Hence

```text
η(v) = number of F-steps,        λ(v) = Σ_{i<η} ⌊(s_i − 1)/2⌋ + (η − 1),
```

which is Proposition 18.3.2(b) with the cascade count made explicit. In itinerary terms: the door `y_i` of the step carries the letter `(m_i, r_i)` with `m_i = D_{i+1} − a_i` and `r_i = s_{i+1}` (Definition 14.15.1.1; reverse.md 14.14.6), so the comb path is the node's itinerary word read from its own door, each letter split into one door edge and a cascade run of `⌊(r − 1)/2⌋` edges. **Worked instance:** `(107,1)`: step 1 exits at `5`, side door `a = 1` of `(1,2)`, `s₀ = 6` — two cascade edges, one door edge; step 2 exits at `1`, `s₁ = 3` — one cascade edge, terminal. `η = 2`, `λ = 4`.

**Grade.** A dictionary lemma; nothing new is computed. Its content is the sentence *`λ` and `η` are word statistics*, so determinism "along `λ` and `η`" is determinism of the letter word — the cylinder theorem at the finite level, the Bridge beyond.

## Item B — the mean degree is 2 (Proposition 18.7.2)

**Claim.** By Proposition 18.2.3, `deg(v) = 1 + D(v) − [top door of v dead]`. Under the backward depth ledger `P(D = j) = 2·3^{−j}` (14.2.4's remark; exact per window by 14.6.5.2) the mean depth is `Σ j·2·3^{−j} = 3/2`, and the top door is dead on half the residue classes (14.5.1), so the mean number of door children is `1` and the mean degree is `2`. This is the level-growth law the census displays (18.5: ratio `2.000` from level `22`; `0.9998` door children per node into level `27`). State it as exact *given the ledger*, and the ledger's applicability to the nodes of a comb level as a calibration (the census's depth distribution matches `2·3^{−j}` to three decimals from level `20`). Measure per level, on a fresh level-by-level enumeration to level `20` (about a million nodes, a second): mean `D`, dead-top-door fraction, mean degree, and the ratio of consecutive level counts.

## Item C — the two determinacies, placed (one paragraph, pointers only)

Along door edges toward the root, the next `k` letters of a node's word are fixed by its door modulo `2^N` — the cylinder theorem 14.15.1.5, i.e. the digit budget (stage4.md 11.8.7.7): finite prefixes are cheap, unbounded ones are the Bridge. Along a cascade chain on a fixed door, everything is exact: the sibling at `s + 2` from the sibling at `s` by 14.10.1, and the depth sequence `d = 1 + v₃(s − M₃(y))` with the exact ternary ledger 14.6.5.2. So on the comb, 2-adic determinacy runs along door edges and 3-adic determinacy along cascade chains, and the only seam is the door edge seen from the 3-adic side — Item D.

## Item D — the digit-transfer law across a door edge (Theorem 18.7.3; the one proved law)

**Setting.** A door edge: parent door `y` (odd, `3 ∤ y`), branch `s₀ ∈ {1,2}` fixed by `y mod 3`, child `(ω, d)` with `2^{s₀} y + 1 = 3^d ω`. The child's own doors are `y'_a = 2^{d−a} 3^a ω − 1`, `a = 0, …, d − 1`.

**Claims to prove.**

1. `d` is determined by `y mod 3^{d+1}` (it is `v₃(2^{s₀} y + 1)`; equivalently `d = 1 + v₃(s₀ − M₃(y))`, 14.2.4).
2. **Top door.** `y'₀ mod 3^j` is a function of `(y mod 3^{j+d}, s₀)`, and **not** of `y mod 3^{j+d−1}`: the map is `y'₀ = 2^d (2^{s₀} y + 1)/3^d − 1`, a unit multiple of the exact quotient by `3^d`, so `j` output digits consume `j + d` input digits, and the dependence on the `(j+d)`-th digit is a bijection, never trivial. **Pre-check:** `2,683` random `(y, s₀, j ≤ 5)` pairs agreeing mod `3^{j+d}` gave equal `y'₀ mod 3^j` in every case; `2,393` pairs agreeing only mod `3^{j+d−1}` (same `d`) disagreed in every case.
3. **Side doors.** `y'_a ≡ −1 (mod 3^a)` for every `a` (the `3^a` factor of `y'_a + 1`), so the low `a` digits are fixed by the door index alone — this is Remark 15.7.6's "gained digits" read on the mirror side; and for `j > a`, `y'_a mod 3^j` is a function of `(y mod 3^{j−a+d}, s₀)`, sharp in the same sense. Derive the exact statement, including what happens at `j ≤ a`.
4. **The reading.** Across a door edge into door `a` of the child, the 3-adic precision budget moves by exactly `−(d − a)` digits (`d` lost to the quotient, `a` gained from the forced `−1`); along a cascade edge nothing moves (the door is fixed). Under the depth ledger the mean loss per door edge at the top door is `E[d] = 3/2` digits. This makes 14.13's "one digit of precision loss per generation" (the KL posture) an exact count per comb edge — and it does **not** make `M₃` propagate: the child door's anchor is a function of finitely many digits of `y` only because the child door itself is (14.6.5's affine obstruction stands, and the theorem says exactly how many digits it costs). Say this flatly, once; propose nothing.

**Boundary cases to settle:** `y = 1` (the root's door; the excluded self-loop at `s₀ = 1`); `j = 0`; the dead top door of the child (`y'₀ ≡ 0 mod 3` — the law still describes `y'₀` as an integer, but it is not a live door; note it).

## Queue

1. **Mathematics first, on paper in the findings.** Items A, B, D proved; C written as pointers. Where a pre-check claim is wrong or needs a boundary case, record the corrected statement and what was wrong, with a re-derivation.
2. **Fresh verification code — `experiments/comb_dictionary.py`, committed with its output.** Imports nothing from any existing script; exact integers at every pass/fail decision; canaries first (`(107,1)`'s path and word; door `1`'s chain; a hand-checked door edge with its digit count). Contents: (a) Item A on `3,000` random states (`ω < 10^6`, `d ≤ 40`): the comb path by the parent rule against the `F`-orbit's letters, the cascade counts, `η` and `λ` by both routes; (b) Item B on a fresh level-by-level enumeration to level `20`: per level mean `D`, dead-top fraction, mean degree, level ratio, and the depth distribution against `2·3^{−j}`; (c) Item D: the top-door law on `5,000` random `(y, s₀, j ≤ 6)` with agreement at `j + d` digits and sharpness at `j + d − 1` (same `d`); the side-door law at every `a < d` on `3,000` random edges with `d ≥ 2`, including the `−1 mod 3^a` fact and the `j−a+d` count with its sharpness; the boundary cases. **One documented command reproduces the committed output in full** (`python experiments/comb_dictionary.py`). Foreground; wait; record counts, ranges, seed, date.
3. **Wiki edits — conservative; content and structure in separate commits.**
   - `comb.md`: new subsection **18.7. The comb as the word: the dictionary, the mean degree, the two determinacies, and the digit-transfer law** — 18.7.1 (Item A), 18.7.2 (Item B), one paragraph for Item C, 18.7.3 (Item D) with its reading paragraph; one verification line per proved claim; the Current-state paragraph gains at most one clause; front matter `updated`.
   - `reverse.md` 14.13: one pointer sentence — the per-generation precision loss is counted exactly per comb edge at comb.md 18.7.3 (pointer only, nothing restated). Front matter `updated`.
   - `itinerary.md`, `ladder.md` 15.7.6: nothing, unless a one-clause pointer to 18.7.1 or 18.7.3 is needed for a reader arriving there — then the smallest clause, and say why.
   - `symbols.md`, `TOUR.md`, `index.md`: nothing (no new symbol or term).
   - `briefs/comb-dictionary-findings.md`: the derivations, what the pre-check got wrong (if anything), the verification record, and a *For the main session at merge* section.
   - **Do not edit** `HANDOFF.md`, `README.md`, `cycles.md`, `aeh.md`, `stage*.md`, `open-problems.md`, `publication.md`, `paper/`, `viz/`, or anything under `sources/`.
4. **Compliance.** Run `experiments/encoding_scan.py` before the final commit and record `RESULT: CLEAN`.

## Record

- `experiments/comb_dictionary.py` + committed output (canaries first; one reproducing command).
- `comb.md` 18.7; the `reverse.md` 14.13 pointer.
- `briefs/comb-dictionary-findings.md`.

## Rules

- Branch **`comb-dictionary`** from your worktree HEAD. FIRST verify the worktree contains this brief (`briefs/comb-dictionary-brief.md`) and that `git log --oneline -1` shows a commit dated 2026-09-16; worktrees are sometimes cut from a stale HEAD — if either check fails, rebase onto local `main` before starting, and state your base SHA in the findings.
- No web access needed; no contact with anyone; no pushes; no edits outside this repository.
- File edits via the Edit/Write tools only — never PowerShell `Get-Content`/`Set-Content`.
- Register: flat, calibrated prose. The ledger is a measured law and is labeled as such wherever Item B leans on it. Heuristics labeled heuristics; nothing labeled proved without the fresh code of Queue 2 **and** a written proof. Nothing proposed.
- Stopping-rule compliance: no equidistribution proof effort; no cycle work; no front reopened.
- Run the script in the foreground and wait for it; do not stop until every commit exists on the branch.
- Do NOT merge — the main session reviews (re-runs the script; re-derives Item D's top-door law and Item B's identity independently) and merges. Stop after Record.
