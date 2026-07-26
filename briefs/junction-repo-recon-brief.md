# Brief: Junction Theorem repository — recon and self-audit confirmation (light session)

**Context required before starting (in order):** `AGENTS.md`, `HANDOFF.md` item 1 (round-10 paragraphs), `briefs/merle-lean-r10-audit-findings.md` (the `LegendreApprox.lean` section — this repo is that file's provenance).

## Why this exists

Merle's second round-10 letter reports, unprompted, that he audited his own older repository — the **Junction Theorem** work, a preprint from spring 2025 he had set aside — against the standard this correspondence holds, and that **its headline did not survive**. His account, to be confirmed:

- The README claimed an **unconditional** proof of no cycles for all `k ≥ 3`.
- Its own technical document says something weaker: **two asymptotic programs, each with a named unclosed gap beyond `k = 200`**; the preprint itself states complete exclusion needs an extra hypothesis for `k ≥ 69`.
- His words: *"The mathematics inside was sound; the shop window was ahead of the shop."*
- Remediation he reports: README and STATUS rewritten to match the technical documents, a scope banner added, `native_decide` reliance flagged (compiler-trusted, not kernel-trusted) for the large finite ranges, the range beyond `k = 50000` marked **OPEN**, and a plain-words statement that the repository does **not** prove the Collatz conjecture. Audit record committed as **`AUDIT_V9`**.
- He also says the deficit lemma we now care about is proved there (**Junction Theorem preprint §3**, entropy form, constant `γ` with `γ·log₂3 = c_gen`), but *not in a form our ledger could accept*: `native_decide`, two `sorry`s in the asymptotic assembly, Simons–de Weger as an axiom.

This matters to us for three reasons: it is the **provenance** of the deficit lemma; its `LegendreApprox.lean` is **imported by the T1 chain** we just audited; and the honesty of the self-audit is itself relevant to how our reply treats the whole round.

**This is recon, not an audit of the mathematics.** We are confirming that his description of his own repository is accurate. Do not attempt to verify the Junction Theorem's proofs, and do not grade the work.

## Queue

1. **Locate and clone (read-only, scratchpad).** The repo is under his handle `ericmerle3789`; find it by listing his public repositories (bounded web/`gh` access is granted **for this item only**: locating and reading his public repos, nothing else — no contact with anyone, no other browsing). Record the repo name, HEAD SHA, and the commit that carries `AUDIT_V9`.

2. **Confirm the self-audit, point by point.** For each bullet above, record **verbatim** what the current README/STATUS/banner actually says, and — via `git log`/`git show` — what it said **before** the audit commit. State for each: confirmed as described / differs (with the difference quoted) / not found. Read `AUDIT_V9` in full and record its own summary of what it found. Particular care on: the plain-words "does not prove the Collatz conjecture" sentence; the `native_decide` flag; the `k = 50000` OPEN marking; and whether the technical document's two named gaps are stated where a reader would meet them.

3. **The deficit lemma's provenance.** Locate the entropy-form deficit statement (preprint §3 and/or its Lean form) and record it **verbatim**, with the definition of `γ` and of the units (per unit of `S` rather than per unit of `n`). Record exactly the caveats he names: which parts use `native_decide`, where the two `sorry`s sit, and whether Simons–de Weger genuinely appears as an axiom (`axiom` declaration — quote it). Cross-check the unit conversion against flag 6 of `briefs/merle-la7-close-check-findings.md` (the suspicion that the preprint's `S` is our `K`) and settle it if the source makes it settleable.

4. **`LegendreApprox.lean`.** Confirm this file's home is this repo, record its claimed axioms/`sorry` status here, and diff it against the copy in the `one-obstruction-three-faces-lean` repo (HEAD `5c9b663`) — identical or not, stated flatly.

5. **Record:** `briefs/junction-repo-recon-findings.md` — the confirmations point by point with quotations, the deficit-lemma provenance record, the `LegendreApprox` diff verdict, and one short closing paragraph on whether his account of his own repo is accurate as given. **No script needed** unless a diff or count wants one. Then **one scoped paragraph** in `HANDOFF.md` item 1.

## Rules

- Branch **`junction-repo-recon`** from your worktree HEAD (verify it contains this brief; state the base SHA). Per-item commits; do NOT merge.
- Read-only outside this repo; no pushes; no forks; no issues, comments, or any other interaction with his repositories; web/`gh` access bounded to item 1's purpose.
- **Register discipline matters here more than usual.** This is a record of a correspondent's voluntary self-correction. Report it flatly and without commentary — no praise, no grading, no editorializing about the original overclaim. If something he described is not as described, record that with the same flatness.
- No reply paragraphs, no ledger text, no key turns. Stop after item 5.
