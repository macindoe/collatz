# Findings: re-verification of stage3.md 11.8.6.3's laws on all 63,000 valid states, ω = 1 included

Brief: `briefs/depth-law-reverify-brief.md`. Branch `depth-law-reverify`, base `3de9d7c`. Date 2026-10-20.

## 1. The run

`experiments/depth_law_reverify.py` — fresh code, imports nothing from the repository, exact integers throughout. One command:

```text
python experiments/depth_law_reverify.py
```

It writes `experiments/depth_law_reverify_output.txt` (byte-identical on re-run) and exits 0 iff every check passes and every negative control bites. Runtime about 8 s.

- **Truth side:** the next state from the definition of `F` (spine.md 5.6): `x_exit = (3^d ω − 1)/2^s`, then `R(x_exit)` by trial division of `x_exit + 1` by 2 and then by 3.
- **Prediction side:** the laws, evaluated from `(ω, d)` and the anchors only. `N(u)` is computed mod `2^256` by bit-by-bit lifting and certified (`9^N(u)·u ≡ 1 mod 2^259`). `M(ω) = N(ω²)` is computed as its own discrete log; the identities `M = 2N(ω)` and `M = 2N(3ω) + 1` are checked separately. Any anchor-side valuation of 224 or more aborts the run, so truncation never decides a comparison. The largest valuation met was far below that.

What is checked, per state: that the next state is valid; the `C` identities of spine 5.6; the branch class (Prop 11.8.1.3.1); `h(s)` by trial division against its formula; the absorption trichotomy (Prop 11.8.6.2.1); the 3-gain trigger. On the lifting classes it also checks the valuation law (`s = 3 + v₂(ε)`, unified `s = 2 + v₂(d − M)`), `v₂(δ_s) = s − 3`, the forced carry (`v₂(ε) = s − 3`, `v₂(ε + δ_s) ≥ s − 2`), Thm 11.8.6.3.3, and Lemma 11.8.6.3.1 directly at `c = 1 − 2^s` (even component). Off the lifting classes it checks Thm 11.8.6.3.5 (`s = 1`, `s = 2`). On every state it checks `m₊ ≥ 1` and Cor 11.8.6.3.6 (`d₊` from the two laws equals the true next depth). It also checks `v₂(δ_s) = s − 3` for `3 ≤ s ≤ 200`, and both worked cases quoted in 11.8.6.3.

**Total: 669,250 checks on 63,000 states, 0 failures.** Max `m₊ = 17` (as the old record said), max `s = 18`; 331 resonant states `d = h(s)` met, 165 of them with extra 3-adic cancellation.

## 2. Totals per residue-parity class

| class `(ω mod 8, d mod 2)` | branch | states | checks | failures |
|---|---|---:|---:|---:|
| 1, even | lifting (`s ≥ 3`) | 7,750 | 124,000 | 0 |
| 3, odd | lifting (`s ≥ 3`) | 8,000 | 120,000 | 0 |
| 1, odd | `s = 1` | 8,000 | 72,000 | 0 |
| 3, even | `s = 1` | 7,750 | 69,750 | 0 |
| 5, odd | `s = 1` | 8,000 | 72,000 | 0 |
| 7, even | `s = 1` | 7,750 | 69,750 | 0 |
| 5, even | `s = 2` | 7,750 | 69,750 | 0 |
| 7, odd | `s = 2` | 8,000 | 72,000 | 0 |

There are **eight** `(ω mod 8, d mod 2)` classes: the two lifting components plus the six off-lifting classes of Thm 11.8.6.3.5. Paper v4 counts them the same way ("the other six classes", line 157). stage3.md line 603 (Cor 11.8.6.3.6: "on all six residue-parity classes") and the line-8 Current state ("on all six residue-parity classes") say "six". That miscounts, or else means the six off-lifting classes. I did not edit either statement; it is listed for the main session (section 5).

## 3. ω = 1: its own verdict

63 states (`d = 1..63`): 31 on the lifting class (`d` even) and 32 on `s = 1` (`d` odd). **784 checks, 0 failures.** `N(1) = M(1) = 0` exactly; the certified discrete log returns 0.

| law | ω = 1 verdict |
|---|---|
| valuation law (11.8.3; unified 11.8.5.6.2) | **Holds as stated.** `ε = n`, so `s = 3 + v₂(n) = 2 + v₂(d)`, exactly. This is the isometry `v₂(9^n − 1) = 3 + v₂(n)`. Only the *imported Baker bound* of 11.8.3.11 excludes ω = 1, because the pair (9, 1) is dependent. The law itself needs no exception (31 checks). |
| target shift (Lemma 11.8.6.3.1) | Holds as stated (31). |
| `v₂(δ_s) = s − 3`, forced carry (Def 11.8.6.3.2, Cor 11.8.6.3.4) | Hold as stated (31 each). Here `ε = n` is an ordinary integer, and the carry against `δ_s` still happens at scale `s − 3`. |
| entry-depth law, lifting (Thm 11.8.6.3.3) | **Holds as stated** (31). `m₊ = 3 − s + v₂(n + δ_s)`; values met: 1, 2, 3, 4, 6. |
| entry-depth law, `s = 1` (Thm 11.8.6.3.5) | **Holds as stated** (32). It degenerates rather than fails: `M(1) = 0` and `d` is odd, so `m₊ = 1 + v₂(d) = 1` on every odd depth (seen at all 32). Nondegeneracy `d ≠ M(1)` holds automatically (`d ≥ 1`). This is the case the theorem's own proof treats when it excludes `(1, 0)`. |
| entry-depth law, `s = 2` | Not reached: ω = 1 has no `s = 2` class. The `(1, 1)` exclusion in the proof is exactly that. |
| absorption (Prop 11.8.6.2.1), 3-gain trigger | Hold as stated (63 each). No resonant state `d = h(s)` occurs at ω = 1 in range. |
| `d₊ = m₊ + a₊` (Cor 11.8.6.3.6) | Holds (63). It includes the fixed point `(1, 1) → (1, 1)` and `(1, 2) → (1, 1)`, the only two depths that return to ω = 1. |

**Verdict:** at ω = 1 every law of 11.8.6.2–11.8.6.3 and the valuation law hold exactly as stated. None of them needs a stated exception or note. ω = 1 is the rational-anchor case: every anchor-side quantity except `δ_s` is an ordinary integer, so the laws reduce to `s = 2 + v₂(d)` (even `d`) and `m₊ = 1` (odd `d`). The only ω = 1 carve-out in the program remains the one already recorded at 11.8.3.11, and it concerns the imported Baker bound, not these laws. The output file lists the full ω = 1 table (`d, s, m₊, a₊ → (ω₊, d₊)`).

## 4. The 62,937 diagnosis

- `63,000 − 62,937 = 63` = exactly one value of ω times the 63 depths. The script confirms: valid states with `ω > 1` number 62,937.
- **But the arithmetic does not single out ω = 1.** Dropping the *largest* value instead gives the same count, since `ω = 2999` is coprime to 6: states with `ω < 2999`, i.e. an off-by-one on the bound, also number 62,937. The count alone cannot tell the two apart.
- **The record does not say.** The figure first appears in draft v075 (`sources/drafts/collatz_reduction_rewrite_v075.md` line 4692). It is absent from v074, which has no 11.8.6.3 verification at all. It is copied verbatim into v076–v078 and stage3.md. No script for it exists in `experiments/` or anywhere in the tree, and no commit message or brief records how it was run (`briefs/v3-external-review-corrections-findings.md` line 224 already noted the missing script).
- One piece of evidence points *against* a deliberate ω = 1 exclusion: the same verification paragraph's first worked case is `(ω, d) = (1, 4)`, an ω = 1 state. Whichever value the original loop dropped, the drop was not a stated scope restriction. Nothing in the laws excludes ω = 1, and this run finds none needed.
- Conclusion: the original count was one ω-value short, either ω = 1 or ω = 2999. Which one is undecidable from the record. The question is now moot: all 63,000 states, both of those included, pass.

## 5. The stage3.md edit, and items for the main session

Edited in place (front matter `updated: 2026-10-20`; status unchanged):

- the "Numerical verification" paragraph of 11.8.6.3, quoted verbatim in the final report;
- the Current-state sentence (line 8): `Independently re-verified numerically (exhaustively on all 63,000 valid states with ω < 3000, 1 ≤ d < 64, ω = 1 included, 2026-10-20 — §11.8.6.3; 8,000 random states re-checked 2026-07-06).`

No law needed an ω = 1 exception, so no statement was touched.

For the main session (not edited):

1. **"six residue-parity classes"**, at stage3.md line 8 (Current state) and line 603 (Cor 11.8.6.3.6). There are eight `(ω mod 8, d mod 2)` classes. Suggested wording: "on all eight residue-parity classes (the two lifting components and the six classes of Theorem `11.8.6.3.5`)". It is a statement-level wording fix, so it is left to you.
2. The paper carries the 62,937 in four places, not two: Remark C.6 (`rem:verify1`, tex line 337), the verification-index row in Appendix G (tex line 740), and ledger rows C-3.5(a) and C-3.6. Replacements are below.

## 6. Replacement sentences for paper 1 (not applied)

**Remark C.6 (`rem:verify1`), `paper/collatz-reduced-v4.tex` line 337, whole paragraph:**

> Each law above was checked by independently written code, with zero discrepancies: the valuation law on $8{,}000$ random states across both lifting components, the entry-depth law exhaustively on all $63{,}000$ valid states with $\w < 3000$, $1 \le d < 64$ ($\w = 1$ included, where every law holds as stated), and the absorption law on $327{,}980$ states ($983{,}954$ comparisons against both this Lemma and its form in the record), with the boundary branch $d = h(s)$, on which $a_+$ is a $3$-adic function of $\w$, and the shallow branch $d < h(s)$ constructed rather than sampled. The records are \texttt{stage3.md} \S11.8.6.3 and that page's status header; the code is \texttt{experiments/depth\_law\_reverify.py} and \texttt{experiments/absorption\_law.py}.

**Appendix G verification index, tex line 740, middle cell, the entry-depth clause:**

> the entry-depth law exhaustively on all $63{,}000$ valid states with $\w < 3000$, $1 \le d < 64$, $\w = 1$ included;

and the last cell: `\texttt{depth\_law\_reverify.py}; \texttt{absorption\_law.py}; \texttt{stage3.md} \S11.8.6.3 and its status header`.

**Ledger row C-3.6 (`paper/collatz-reduced-v4-claims.md`), claim cell:**

> Each law of §3 so far was checked by independently written code with zero discrepancies: the valuation law on 8,000 random states across both lifting components; the entry-depth law exhaustively on all 63,000 valid states with `ω < 3000`, `1 ≤ d < 64`, `ω = 1` included (where every law holds as stated); the absorption law on 327,980 states (983,954 comparisons against both this Lemma and its form in the record), with the boundary branch `d = h(s)` (on which `a₊` is a 3-adic function of `ω`) and the shallow branch `d < h(s)` constructed rather than sampled. Records: `stage3.md` §11.8.6.3 and its status header. Code: `experiments/depth_law_reverify.py`, `experiments/absorption_law.py`.

**Ledger row C-3.5(a), last cell:**

> Remark 3.6: entry-depth law exhaustively on all 63,000 valid states with `ω < 3000`, `1 ≤ d < 64`, `ω = 1` included, zero discrepancies (`depth_law_reverify.py`)

Optional, if the paper wants the stronger fact: the same run also checks the valuation law exhaustively on all 15,750 lifting states in the box. The 8,000-random-state figure could be kept alongside it, or that clause replaced.
