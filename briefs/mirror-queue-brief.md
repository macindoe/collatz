# Brief: mirror-theorem queue (for a delegated session)

**Context required before starting:** read `README.md`, `AGENTS.md` (binding), `reverse.md` (§14), and Section 3 of `paper/collatz-reduced-v1.tex` (the forward laws being dualized).

**Task:** dualize the forward per-step machinery to the reverse direction, one theorem at a time. The forward/backward duality table (reverse.md 14.3) is the dictionary: 2↔3, `s`↔`d`, `N(ω)`↔`M₃(y)`, mirror isometries as listed.

**Queue, in order:**
1. **Dual digit-determinacy lemmas.** Forward versions: paper Thm 3.5 proof, facts (a)-(c). Backward: which 3-adic residues of `(y, s)` determine the predecessor's `(ω, d)` truncations, to which depth. State and prove the three mirror facts.
2. **Dual low-order increment law.** Forward: ΔM mod 2^k from graded residues. Backward: Δ(3-adic anchor) along a backward step — expected form: graded 3-adic residues, with the frozen-2-adic phenomenon (reverse.md 14.5 discussion / the `ω ≡ 3^(−d)` freeze) appearing as the mirror of something; identify what.
3. **Dual one-step trichotomy.** Forward: depth-k window decides next step, error-free, undecided rate ~2^(−(k+1)). Backward: a 3-adic window on `(y, s)` should decide the predecessor's coarse data with undecided rate ~3^(−j)-flavored. State, prove, verify.
4. **Dual ladder (from ladder.md §15).** Forward ladder relates `(ω,d)` and `(ω,d+1)` at fixed core. The mirror question: relate predecessors at adjacent `s` (fixed door). Expected: an exact dichotomy gated by the 3-adic anchor. Derive it.

**Rules (non-negotiable, from AGENTS.md):**
- Every claim verified with independently written code before being labeled proved; record counts/ranges/seeds in the page and in AGENTS.md's verification record.
- Failures and dead ends are recorded, not deleted.
- Numbering: new results go in reverse.md as 14.7+ (or a new mirror.md §16 if volume warrants), never renumber existing anchors.
- Work on branch `mirror-queue`, commit per theorem, do NOT merge to main — the main session reviews.
- If a dual theorem is false or has no clean mirror, that is a result: record the obstruction precisely and move on. Do not force analogies.
- No new fronts, no scope expansion. If something interesting-but-off-brief appears, note it in a `briefs/mirror-queue-findings.md` list and continue.

**Definition of done:** the four items each have a statement + proof + verification record + honest status, on the branch, with clean commits.
