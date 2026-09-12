# Brief: two loose ends from the author's session of 2026-09-13 — the tree from 1 realizes every finite letter word (itinerary.md, under 14.15.2), and the family-frame weak conjecture with its reduction to orbit merging (open-problems.md 11.14) — for a delegated session

**Context required before starting (in order):** `README.md` (strategy and **binding stopping rules** — no per-period cycle search; the cycle front reopens only with a divisibility-aware idea), `AGENTS.md` (house norms: nothing is labeled proved without independently written verification code; no change logs in tracked files; every fact lives in exactly one page; content and structure in separate commits), `HANDOFF.md` (register norm; the delegation pattern; the PowerShell quirk), `spine.md` §9.8 (the reduced map `F`, states `(ω, d)`, the numerator `A(ω,d) = 3^d ω − 1 = 2^s e`, the exit `e`, the next state through `e + 1 = 2^m 3^a Ω`), `itinerary.md` 14.15.1–14.15.2 (the letter alphabet `{(m,r) : m,r ≥ 1}`, the cylinder theorem 14.15.1.5 with its modulus, Corollary 14.15.1.6, the full-shift statement 14.15.2, and the three-notion separation remark near the end of the page — the new lemma sits between "finite symbolic legality" and the next notion there), `reverse.md` 14.1.1 (predecessors; every odd integer is the door of exactly one state) and 14.6 (the tree from `1` and its density bound), `ladder.md` 15.1–15.2 and 15.6–15.7 (the ladder dichotomy, the braid, the kick, the tear afterlife, the guaranteed neighbours), `stage2.md` 11.8.5.6 (the fiber-versus-orbit bridge — the family frame's own name for the global question), `open-problems.md` 11.12–11.13 (the form of an open entry phrased so that closure is checkable; 11.13 is the most recent and the model), `symbols.md` (registry), `index.md` (resolver granularity), and `briefs/top-door-lineage-brief.md` with its findings file (the form of a brief, a findings file and a per-item commit stream on this repository, and the merge-time seams the main session expects to be listed).

## Provenance

Two questions from the author's session of 2026-09-13, pre-checked in the main session with throwaway code (deliberately not filed; you write the script of record from scratch). Every claim below is **a claim to be re-derived and re-verified here, not a fact**.

### Item A — the tree's language is the full shift (a lemma; expected easy)

**Claim.** For every finite letter word `W = ((m_0,r_0),…,(m_{n−1},r_{n−1}))` there is a positive odd integer `x` whose itinerary begins with `W` **and whose orbit reaches `1`**. 14.15.2 says every finite word is realized by some integer; this says every finite word is realized inside the tree from `1`. The tree is symbolically indistinguishable from the integers at every finite level.

**Expected proof.** (i) By 14.15.1.5 the cylinder of `W` is an arithmetic progression `x ≡ a (mod 2^N)` — take `N` from the theorem as stated, not from a guess (the main session's first guess `N = Σ(m_i + r_i)` was too small; each "exactly `m`" and "exactly `r`" costs a bit). (ii) Over the cylinder the composite of the word's steps is one affine map `x ↦ (3^k x + C)/2^N` with `k = Σ m_i` odd steps, so the set of outputs, as `t ≥ 0` runs over the progression `x = a + 2^N t`, is the odd members of an arithmetic progression `c' (mod 3^k)`, i.e. the full class `c' (mod 2·3^k)` above `c'`. (iii) The odd predecessors of the powers of `4`, the numbers `(4^i − 1)/3`, all reach `1` (`(4^i−1)/3 → 4^i → 1`), are odd, and cover every residue class modulo `3^k` as `i` runs over a period of length `3^k` (`4` generates `1 + 3Z₃` modulo `3^{k+1}`; checked exactly for `k ≤ 6` in the pre-check), unboundedly often. (iv) Pick one in class `c'` at least `c'`, solve for `t`, and `x = a + 2^N t` has word `W` and reaches `1` because its orbit passes through that number. Write the proof; if any step needs a boundary case (the parity in (ii), the sign of `t`), record it.

**Pre-check.** 300 random words of length `1..4` with entries `1..3`: every cylinder confirmed an arithmetic progression at modulus `2^{S+2n}` and every one contained a member reaching `1`; the covering (iii) exact for `k = 1..6`.

**Grade.** A lemma about the finite level; it moves no front. Its content is the calibration sentence: local statements in letter language are provable because cylinders are fat (arithmetic progressions), and the digit budget (stage4.md 11.8.7.7) is the same fact read as a limitation. Say that flatly, once.

### Item B — the family-frame weak conjecture and where it lands (an open entry)

**The statement (W).** A *family* is a core `ω` with all its depths, the states `(ω, d)`, `d ≥ 1`; its integer members are `2^m 3^a ω − 1` with `m ≥ 1`, `a ≥ 0` (the doors of `(ω, m+a)`, reverse.md 14.1.1). W: **for every core `ω` some depth `d` has `(ω, d)` reaching `(1,1)` under `F`.** The conjecture says every depth does; W is weaker; W does not imply the conjecture. The trivial cycle is the depth-`1` member of the trivial family, which is why the author has always thought in this form.

**Three equivalent readings, to be proved equivalent:** (a) the exit sequence `e(ω,d)`, `d ≥ 1`, contains a member of the tree; (b) the backward tree from `(1,1)` visits every core at some depth; (c) over all odd `x` in the tree, the numbers `(x+1)` stripped of their `2`s and `3`s cover every integer coprime to `6`.

**Why the record's tools do not reach it.** The family has density zero, so the density bound of 14.6 (and the literature's `x^{0.84}`) says nothing; the digit budget says no window decides membership; the conjecture implies W trivially.

**What the ladder does to it (pre-checked).** By 15.1.1 adjacent exits off-spike are one orbit, so W is about the exits at spike depths, one orbit per kick. Two regimes:

- *Cores `ω ≡ 5, 7 (mod 8)`* have no anchor and every spike has `s = 2` (first-layer classification; the pre-check saw no `s > 2` on these classes). Their spike-depth exits obey `e(ω, d+2) = T(6·e(ω,d) + 1)` — the kick `6e + 1` then one Collatz step (672 cases, 0 failures; note the order: kick first, step second). W on these classes says some member of that explicit sequence, growing by about `4.5` per two depths, lies in the tree.
- *Cores in the lifting classes `ω ≡ 1, 3 (mod 8)`* have kick heights read off the anchor digits. For a kick of height `s ≥ 3`, the kicked exit `3·2^{s−1}e + 1 = 4X + 1` with `X = 3·2^{s−3}e`, and the classical identity `T(4X+1) = T(X)` (since `3(4X+1)+1 = 4(3X+1)`) makes its orbit merge at once with the orbit of `X`, hence with the orbit of `3e` (3,000 cases, 0 failures). So on these classes the family's tree membership hangs on whether the orbits of `e` and `3e` merge.

**The wall, stated.** "Do the orbits of `x` and `3x` merge?" would follow from the conjecture and is open on its own. Measured: on 1,347 random odd `x < 2·10^6` coprime to `3`, the orbits of `x` and `3x` meet above `1` within 400 steps in 1,247 cases and only at `1` in the rest — generic, and with no local law. W is weaker than the conjecture but of the same kind: an explicit thin sequence must meet a dense set, and no technique exists for that shape. Record this as the calibration; propose nothing.

**Flat note.** The trivial family is trivial only at depth `1`: its deeper exits `e(1,d)` are the odd parts of `3^d − 1` (`1, 1, 13, 5, 121, 91, 1093, …`), and whether every one of them reaches `1` is open — the conjecture restricted to that thin sequence.

**Grade.** An open entry phrased checkably, in the 11.13 style; no front moves; the fiber-versus-orbit bridge of stage2.md 11.8.5.6 is its name in the record, and 11.14 is that bridge's weakest global form.

**Stopping-rule compliance:** identities and measurements on orbits; no cycle search of any kind, no per-period anything; no equidistribution proof effort; no front reopened.

## Queue

1. **Mathematics first, on paper in the findings.** Item A's proof in full, with the cylinder modulus taken from 14.15.1.5 as stated. Item B: the three readings proved equivalent; the two regime facts (the `s = 2` classes' recurrence; the `4X+1` merge on kicks of height `≥ 3`) proved from 15.1.1 and the identity; the flat note's identification of `e(1,d)`. Where a pre-check claim is wrong or needs a boundary case, record the corrected statement and what was wrong; **a claim is not dissolved by naming its type** — every correction carries a re-derivation.
2. **Fresh verification code — `experiments/tree_language_families.py`, committed with its output.** Imports nothing from any existing script (the main session's scratchpad code does not exist for you); exact integers at every pass/fail decision; canaries first (`(1,1)`; a few hand-checked words and their cylinders; `(4^i − 1)/3` reaching `1`). Contents: (a) the covering of residue classes mod `3^k` by `(4^i − 1)/3`, exact, `k ≤ 7`; (b) random words: cylinder = arithmetic progression at the theorem's modulus, and a member reaching `1` found by the proof's own construction (step (iv)), not by search — that is the check that the proof is constructive; (c) the `s = 2` classes: no `s > 2` on a large sample and the depth-two recurrence; (d) the `4X + 1` identity on kicks; (e) the `x` versus `3x` merging measurement with the bound printed; (f) the trivial family's exits as the odd parts of `3^d − 1`. **One documented command reproduces the committed output in full** (`python experiments/tree_language_families.py`). Run it in the foreground and wait for it. Record counts, ranges, seed, date.
3. **Wiki edits — conservative; content and structure in separate commits.**
   - `itinerary.md`: a new **Lemma 14.15.2.1 (the tree's language is the full shift)** directly after the full-shift statement of 14.15.2, with its proof and one verification line; one clause added to the three-notion separation remark placing the lemma between finite symbolic legality and the next notion. Front matter `updated`; the Current-state paragraph gains at most one clause.
   - `open-problems.md`: a new entry **11.14. Does every family reach the trivial family?** in the form of 11.13: the statement, the three readings, the two regimes and the reduction to `x` versus `3x` merging, the measurement, the calibration, the flat note on the trivial family, and the stopping-rule paragraph. Front matter `scope` gains the 11.14 clause in the existing style; `updated`.
   - `stage2.md` 11.8.5.6: one pointer sentence to 11.14 as the bridge's weakest global form — pointer only, nothing restated. Front matter `updated`.
   - `ladder.md`: nothing, unless the `s = 2` recurrence of the no-anchor classes is not derivable in one line from 15.1.1 as stated — then one sentence under 15.2, and say why.
   - `TOUR.md`, `symbols.md`: nothing (no new term, no new symbol; "family" is used in ladder.md 15.7 already — cite that usage).
   - `index.md`: add 11.14 only if the resolver lists at that granularity; 11.13 was not added, so expect not.
   - `briefs/tree-language-families-findings.md`: the derivations, what the pre-check got wrong (if anything), the verification record, and a *For the main session at merge* section (front-matter seams; the pointer from stage2.md).
   - **Do not edit** `HANDOFF.md`, `README.md`, `cycles.md`, `reverse.md`, `aeh.md`, `publication.md`, `paper/`, or anything under `sources/`.
4. **Compliance.** Run `experiments/encoding_scan.py` before the final commit and record `RESULT: CLEAN` in the findings.

## Record

- `experiments/tree_language_families.py` + committed output (canaries first; one reproducing command).
- `itinerary.md` Lemma 14.15.2.1 and the remark clause; `open-problems.md` 11.14; the `stage2.md` pointer sentence.
- `briefs/tree-language-families-findings.md` as specified.

## Rules

- Branch **`tree-language-families`** from your worktree HEAD. FIRST verify the worktree contains this brief (`briefs/tree-language-families-brief.md`) and that `git log --oneline -1` shows a commit dated 2026-09-13 or later; worktrees are sometimes cut from a stale HEAD — if either check fails, rebase onto local `main` before starting, and state your base SHA in the findings.
- No web access needed; no contact with anyone; no pushes; no edits outside this repository.
- File edits via the Edit/Write tools only — never PowerShell `Get-Content`/`Set-Content` (see HANDOFF quirks; the repo's `—`/`≤`/`₃` are destroyed silently).
- Register: flat, calibrated prose. The lemma moves no front; the open entry proposes nothing. Heuristics labeled heuristics; nothing labeled proved without the fresh code of Queue 2 **and** a written proof.
- Record obstructions; if the lemma's step (ii) or (iii) fails as stated, say where and stop on that item.
- Run the script in the foreground and wait for it; do not stop until every commit exists on the branch.
- Do NOT merge — the main session reviews (re-runs the script, re-derives the lemma, reads 11.14 for checkability) and merges. Stop after Record.
