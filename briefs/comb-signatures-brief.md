# Brief: comb.md 18.9 — branching signatures: the shape of a node's subtree as a function of its residues, the per-node digit budget that fixes it, the exact signature modulus, and a search for any grouping of states finer than residue classes — for a delegated session

**Context required before starting (in order):** `README.md` (strategy and **binding stopping rules** — no cycle search of any kind; equidistribution proof effort waits for an idea; measurements may feed the ledger), `AGENTS.md`, `HANDOFF.md` (register norm; delegation pattern; the PowerShell quirk), `comb.md` §18 in full as merged — especially 18.2.3 (children and degree), 18.5 (the census), 18.7.3 (the digit-transfer law: across a door edge into door `a` of a child of depth `d`, `v₃(y'_a − ỹ'_a) = v₃(y − ỹ) − (d − a)`), 18.8 (the negative control; the rules are sign-blind), `reverse.md` 14.7 (digit-determinacy, the 3-adic mirror), 14.6.5.2 (the exact ternary ledger per window), 14.10.1 (the cascade step: child depth `1` when the node's depth is `≥ 2`, `1 + v₃(4ω − 1)` when it is `1`), 14.13 (the residue-class program's obstruction), `ladder.md` Remark 15.6.7 (the one-step total-variation measurement at the noise floor — the comparable prior for Item C) and 15.7.6, `stage4.md` 11.8.7.7 (the digit budget), `symbols.md`, `briefs/comb-dictionary-brief.md` and `briefs/signed-comb-brief.md` with their findings (the form; the corrections already made).

## Provenance

The author's question of 2026-09-17: the point of cataloguing the comb is to find deterministic behaviour that groups reduced states; is there a way to search for patterns in how the comb branches? The main session's answer, pre-checked with throwaway code (not filed; write the script of record from scratch): a node's subtree shape is a function of its depth and its core's 3-adic residue, with a per-node digit budget that follows from 18.7.3 — and the open, cheap question is whether any grouping *finer* than residue classes predicts branching. **Every claim below is a claim to be re-derived and re-verified here, not a fact.** A claim is never confirmed or dissolved by naming its type; corrections carry a re-derivation. Grade: **formulation** plus measurements; no front moves; nothing proposed; no cycle searched; no family-frame vocabulary (no columns, tears, or grouping by core — grouping here is by residue class and by signature, which are different things and must be kept apart in the prose).

## Item A — the level-1 branching laws (Lemma 18.9.1)

For a node `(Ω, D)` with doors `y_a = 2^{D−a} 3^a Ω − 1`, `0 ≤ a < D`, and exit `y`, the depths of its children are:

- **cascade child** (branch `s + 2` on `y`): `1` if `D ≥ 2`; `1 + v₃(4Ω − 1)` if `D = 1` (14.10.1);
- **door child through door `a ≥ 2`**: depth **exactly `1`** — because `y_a ≡ 2 (mod 3)` gives `s₀ = 2`, and `4y_a + 1 = 3·(2^{D−a+2} 3^{a−1} Ω − 1)` with the bracket `≡ −1 (mod 3)` once `a ≥ 2`;
- **door child through door `a = 1`**: depth `1 + v₃(2^{D+1} Ω − 1)`;
- **door child through the top door `a = 0`** (when alive, `y_0 ≢ 0 (mod 3)`): depth `v₃(2^{s₀} y_0 + 1)` with `s₀ ∈ {1,2}` by `y_0 mod 3`, i.e. `v₃(2^{s₀+D} Ω − (2^{s₀} − 1))`.

**Pre-check:** the `a ≥ 2` and `a = 1` laws on `13,485` door children of random states, `0` failures. Prove all four, and state the corollary: **the branching of a node to one level — which doors are alive, the branch `s₀` on each, and every child's depth up to any cap `J` — is a function of `D` and `Ω mod 3^J`**, and only the top door, the `a = 1` door and (at `D = 1`) the cascade child can have depth above `1`. Reconcile in one sentence with 18.5's finding that the depth distribution across a level matches `2·3^{−j}` (the doors with `a ≥ 2` are a minority of door children; check the share and say it).

## Item B — the signature and its digit budget (Definition 18.9.2, Proposition 18.9.3)

**Definition.** The **signature to depth `k` with cap `J`** of a node is its rooted subtree to `k` comb levels with every edge labelled by type (cascade, or door with its index `a` and branch `s₀`), every dead door and excluded self-loop recorded, and every child labelled by its depth capped at `J` (`d ≥ J` recorded as one symbol); cores are not part of the signature. So the signature is the *shape* of the subtree, and two nodes with equal signatures branch identically to depth `k` up to the cap.

**Claim (sufficient budget).** Define recursively `B(v, 0) = 0` and

```text
B(v, k) = max( J,  max over live children c of v of  [ B(c, k−1) + cost(v → c) ] ),
cost(door edge into door a, child depth d')  = d' − a,
cost(cascade edge, child depth d')           = d' − D(v).
```

Then the signature of `v` to depth `k` is a function of `(D(v), Ω mod 3^{B(v,k)})`. **Proof sketch to complete:** a door `y_a mod 3^m` is a function of `Ω mod 3^{m−a}` (from `y_a + 1 = 2^{D−a} 3^a Ω`); the exit `y mod 3^m` is a function of `Ω mod 3^{m−D}` (from `y = (3^D Ω − 1)/2^s`, the low `D` digits of `y` being fixed by `s` alone — 15.7.6); a child's core `mod 3^n` is a function of its door `mod 3^{n+d'}` (18.7.3, the exact quotient by `3^{d'}`); compose along every path, take the maximum, and note the level-`1` labels need `J` digits by Item A. **Pre-check:** at `k = 1, 2, 3` (`J = 3`), pairs of nodes with equal `D` and cores agreeing modulo `3^{B}` had equal signatures in `991 / 1011 / 995` of `991 / 1011 / 995` cases; pairs agreeing to one digit fewer differed in only `94 / 196 / 206` of those — so **the budget is sufficient but not sharp per node**. Note the sign of the cascade cost: `d' − D` is negative whenever `D ≥ 2` (the node's own depth subsidises its cascade child), and `v₃(4Ω − 1)` when `D = 1`.

**The exact signature modulus.** For a node, define `M(v, k)` as the least `M` such that every node `(Ω', D)` with `Ω' ≡ Ω (mod 3^M)` has the same signature to depth `k` — computable exactly by testing the `3^{M}`-lifts at the last digit (there are only two other residues to test at each candidate `M`, and by ultrametricity the property is monotone in `M`; prove that monotonicity, or measure it if it fails). Measure `M(v,k)` against `B(v,k)` over the census nodes of a few levels: the distribution of `B − M`, how often they coincide, and which structural feature accounts for the slack (a capped depth needs fewer digits than its true value; a maximum over paths overcounts on all but the binding path). Report flat; if a corrected exact formula suggests itself, state it as a conjecture with the evidence, not as a theorem.

## Item C — the search: is any grouping finer than residues? (the one open measurement)

For levels `λ ∈ {10, 12, 14, 16, 18}` of the positive comb and `k ∈ {1, 2, 3, 4}`, `J = 3` (and `J = 4` at `k ≤ 2`):

1. **Coincidences.** Count nodes whose signatures are equal to depth `k` but whose cores differ at the exact signature modulus `M` of either node (with equal `D`). By Item B these are exactly the pairs that agree in shape *without* agreeing in the residue that fixes the shape. Compare the count with what independent draws from the same signature distribution would give (the expected number of equal-signature pairs under independence, from the signature frequencies themselves). If the observed rate is at the independent rate, no grouping finer than residues is visible at that depth; say so flatly. If it is above, characterise the coincident pairs (do they share a 2-adic residue? a depth pattern? a door word?) — this is the only outcome that would be new.
2. **The 2-adic probe.** Conditional on `(D, Ω mod 3^M)`, is the signature independent of `Ω mod 2^m` for `m ≤ 8`? The signature is a 3-adic object by construction, so conditional independence is expected; a dependence would mean the forward (2-adic) coordinate carries information about the backward (3-adic) branching, which the record has never seen. Test by a contingency count per level; report the largest deviation and its significance level, flat.
3. **Signature ledgers.** The number of distinct signatures per level against the number of residue classes `(D, Ω mod 3^M)` occupied; the frequency of each depth-`1` signature across a level against the product of the per-edge laws of Item A under the depth ledger `2·3^{−j}` (a predicted frequency for each shape); and whether, in a fixed door's window of `3^k` consecutive branches (14.6.5.2's setting), the *signatures* of the nodes are exactly counted the way their depths are — an exact signature ledger per window, or only a statistical one. This is where a new exact law is most likely to live, because 14.6.5.2 is already exact one level down.

**Prior, stated in the section:** ladder.md 15.6.7 measured the successor core's residue after a step and found it at the sampling noise floor; the expectation for Item C.1–C.2 is the same. The section is written so that a clean negative is a result: it closes "patterns in the branching beyond residues" on the comb to the tested depth.

## Verification: `experiments/comb_signatures.py`

Fresh code, imports nothing from any existing script (`peak_comb.py`, `comb_dictionary.py`, `signed_comb.py` exist and are not to be imported or copied); exact integers at every pass/fail decision; canaries first (the children of `(7,3)`, `(1,2)`, `(5,2)` with their depths by Item A's formulas; the signature of `(1,2)` to depth `2` written out by hand in the findings and matched). Contents: (a) Item A's four laws on `5,000` random states (`Ω < 10^6`, `D ≤ 30`) against direct computation, and the corollary (level-`1` signature a function of `(D, Ω mod 3^J)`) on `2,000` pairs at `J ∈ {2,3,4}` with sharpness reported; (b) Item B: the budget's sufficiency on `1,500` pairs per `k ≤ 4`, the exact modulus `M` computed per node on `2,000` nodes per level with the `B − M` distribution; (c) Item C in full, with the independence baselines computed from the data, not assumed; wall-clock kept to a few minutes (the level-`18` positive comb has `124,068` nodes; signatures to depth `4` on all of them is affordable; sample if it is not, and say so). **One documented command reproduces the committed output in full** (`python experiments/comb_signatures.py`). Foreground; wait; record counts, ranges, seed, date, wall clock.

## Wiki edits — conservative; content and structure in separate commits

- `comb.md`: new subsection **18.9. Branching signatures** — 18.9.1 (Item A, the four laws and the corollary), 18.9.2–18.9.3 (the signature and its budget; the exact modulus and the `B − M` measurement), 18.9.4 (Item C, the three measurements, each with its baseline and one flat sentence of reading), 18.9.5 standing (what is now known about grouping states by branching: exactly the residue classes to the measured depth, or whatever C found); one verification line per proved claim; the Current-state paragraph gains at most one clause; front matter `updated`.
- `reverse.md` 14.7: one pointer sentence (the per-node digit budget of the backward branching, in comb coordinates, is comb.md 18.9.3; pointer only). Front matter `updated`.
- `symbols.md`: one row for **signature** (`sig_k^J(v)` or the notation you choose) and one for the budget `B(v,k)` and modulus `M(v,k)` if the page uses them as symbols; check the collision index (`B`, `M` both have rows — choose glyphs that do not collide, or index them, and say which).
- `TOUR.md`, `index.md`, `itinerary.md`, `ladder.md`, `viz/`: nothing.
- `briefs/comb-signatures-findings.md`: derivations, what the pre-check got wrong (if anything), the verification record, the reading of Item C, and a *For the main session at merge* section.
- **Do not edit** `HANDOFF.md`, `README.md`, `cycles.md`, `aeh.md`, `stage*.md`, `open-problems.md`, `publication.md`, `paper/`, or anything under `sources/`.
- Run `experiments/encoding_scan.py` before the final commit and record `RESULT: CLEAN`.

## Record

- `experiments/comb_signatures.py` + committed output (canaries first; one reproducing command).
- `comb.md` 18.9; the `reverse.md` 14.7 pointer; the `symbols.md` rows.
- `briefs/comb-signatures-findings.md`.

## Rules

- Branch **`comb-signatures`** from your worktree HEAD. FIRST verify the worktree contains this brief (`briefs/comb-signatures-brief.md`) and that `git log --oneline -1` shows a commit dated 2026-09-17; worktrees are sometimes cut from a stale HEAD — if either check fails, rebase onto local `main` before starting, and state your base SHA in the findings.
- No web access needed; no contact with anyone; no pushes; no edits outside this repository.
- File edits via the Edit/Write tools only — never PowerShell `Get-Content`/`Set-Content`.
- Register: flat, calibrated prose. A negative in Item C is a result and is written as one; a positive is characterised, not celebrated. The depth ledger is a measured law wherever it is used as a baseline. Nothing proposed; no cycle search; no front reopened.
- Run the script in the foreground and wait for it; do not stop until every commit exists on the branch.
- Do NOT merge — the main session reviews (re-runs the script; re-derives Item A's `a ≥ 2` law and Item B's budget composition independently; reads Item C's baselines) and merges. Stop after Record.
