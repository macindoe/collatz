# Findings: what paper 1 gives toward Williams's open problem (1), and the first letter

Brief: `briefs/williams-letter-brief.md`. Branch `williams-letter`, base `6bb473a` (main at the brief's commit). Draft letter: `briefs/williams-letter-draft.md` (unsent).

**Held:** J. Williams, *A Coordinate System for Collatz Dynamics*, arXiv:2607.01718 v1 (submitted 2 Jul 2026, 21 pp.), fetched 2026-10-19 into a scratch directory outside the repo and read in full. The abs page still shows v1 only; its comments field reads "21 pages, 5 figures, under peer review". Paper 1 numbering is read from `paper/collatz-reduced-v3.pdf` (pdftotext), which is hash-identical to the published v3.

**Numbering correction.** The published v3 numbers the statements Definition 2.1 (reduced map `F`), Proposition 2.2 (block structure), Theorem 2.3 (convergence translation), Theorem 3.3 (global valuation law), Lemma 3.4 (absorption law), Theorem 3.5 (depth closure / entry-depth law), Theorem 3.7 (anchor-increment law). The brief, `briefs/ceiling-ccchallenge-sweep-findings.md` §5 and the docstring of `experiments/williams_coordinate_check.py` all say "Prop. 2.3" and "Thm 2.4". Those are wrong by one. This file and the letter use the v3 numbers.

## Item A — the calibration

**Their problem (1)** (p. 18): when a trajectory exits a skeleton `L_λ` at the boundary, which skeleton does it enter? They grant that each individual transition is elementary to compute. They ask for a closed form, or a complete characterization, of the map sending one skeleton to the next.

**What `F` gives, in their notation.** Take the exit position `(1, b)` of row `k = b + 1` of `L_λ`. Their Corollary 3.9 shows every member of the row exits there. Put

```
s  = v2(λ·3^k − 1)                       [their v2(3n+1) = 1 + s]
λ′ · 2^(a′+s) · 3^(b′) = λ·3^k − 1 + 2^s,   gcd(λ′, 6) = 1
```

so that

```
a′ = v2(λ·3^k − 1 + 2^s) − s,
b′ = v3(λ·3^k − 1 + 2^s),
λ′ = (λ·3^k − 1 + 2^s) / (2^(a′+s) 3^(b′)),
k′ = a′ + b′.
```

Then `(λ′, k′) = F(λ, k)` and `(a′, b′) = (m₊, a₊)`, in paper 1's Definition 2.1. **As a formula this is their Proposition 3.10, rearranged**: take the odd part of `λ·3^k − 1`, add 1, and strip the 2s and 3s. On its own, `F` restates the elementary step. It contributes no closed form for `λ′`.

**What paper 1 adds beyond the formula. There are two pieces, and they are of different weight.**

1. **Adjacent, not an answer: Definition 2.1 with Theorem 2.3.** These make the transition a self-map on rows `(λ, k)`, not on skeletons. Theorem 2.3 then proves two things. The Collatz conjecture holds iff every `F`-orbit reaches `(1, 1)`. Nontrivial cycles correspond bijectively to `F`-cycles other than `{(1,1)}`. Their own sentence reads "a complete characterization of this transition map would give a description of Collatz dynamics in skeleton coordinates". Theorem 2.3 supplies that description, but only *given* the map. It does not characterize the map. The map must be taken on rows, since the entered skeleton depends on `k` as well as `λ`: T6 below finds this for all 667 skeletons tested. Their Proposition 3.10 already makes `λ′` depend on `b`, so this is a formalization, not a discovery.
2. **A genuine partial answer: Section 3.** Section 3 gives exact laws, in `(λ, k)`, for every part of the transition except `λ′` itself:
   - **Exit valuation (Thm 3.3).** If `λ·3^k ≡ 1 (mod 8)`, then `s = 2 + v2(k − M(λ))`. Here `M(λ) = −2 log λ / log 9 ∈ Z₂` is one 2-adic number fixed by the skeleton. Otherwise `s ∈ {1, 2}` is a constant fixed by `(λ mod 8, k mod 2)`. In their terms, the boundary valuation along a skeleton's rows is determined by how many low binary digits `k` shares with `M(λ)`.
   - **Entry position `b′` (Lemma 3.4).** `b′ = 0` for odd `s`. For even `s`, `b′ = min(k, 1 + v3(s))`, except when `k = 1 + v3(s)`. In that case `b′ = k + v3(λ + (2^s − 1)/3^k)`.
   - **Entry position `a′` (Thm 3.5, the entry-depth law).** `a′` is a 2-adic valuation of a difference of 2-adic logarithms (the anchor displacement plus `δ_s = N(1 − 2^s)`) on the lifting classes. Off them it is `1 + v2(k − M(λ))` for `s = 1` and `v2((k−1) − M(λ))` for `s = 2`.
   - Hence the row entered, `k′ = a′ + b′`, also has an exact law.
   - **The skeleton index `λ′`** gets nothing beyond its defining quotient. Only the low 2-adic digits of `M(λ′) − M(λ)` are computable from finite residues (Thm 3.7).

   One calibration on "closed form": these laws are exact and explicit, but they are not shortcuts. Computing `M(λ)` to `j` digits costs about as much as computing the valuation directly. What they offer is structure: how the transition depends on `k` for a fixed skeleton. They do not offer speed.

**Verdict: answers (1) in part.** The part answered is *where* the trajectory lands: the boundary valuation, the entry position `(a′, b′)` and hence the row `k′`. All of these have exact laws in `(λ, k)` through one 2-adic invariant per skeleton (Section 3). The part not answered is the literal question, *which* skeleton `λ′` is entered. There, `F` restates their Proposition 3.10, and Theorem 2.3 is adjacent: it is the "description of Collatz dynamics in skeleton coordinates" they say a characterization would give, and it holds given the map.

**Consequence for the record.** `briefs/ceiling-ccchallenge-sweep-findings.md` §5 item 2 and §6 say open problem (1) "is answered by paper 1's reduced map `F` … together with the equivalence theorem". **That overclaims, and should not be carried into v4 or `publication.md`.** The sweep's proposed `publication.md` wording ("which leaves the row-exit map open; the induced map `F` and its equivalence theorem are paper 1's") is accurate as worded and can stand. If v4 mentions problem (1) at all, the supportable sentence is the verdict above.

## The check

Fresh code, written for this window. It imports nothing from the record's other scripts. Ground truth is the literal full map `C(n) = n/2 or 3n+1`, iterated on integers.

```
python experiments/williams_transition_check.py > experiments/williams_transition_check_output.txt
```

Range: `λ < 2000` coprime to 6 (667 skeletons), rows `1 ≤ k ≤ 80`, **53,360 `(λ, k)` states**. The result is **0 failures, ALL CHECKS PASS** (2026-10-19, about 4.5 min).

- **T1.** The literal diagonal flow from the row top `(k, 0)` reaches the exit `(1, k−1)` with one halving per interior step, over 2,107,720 interior odd steps. Every row member lies on this diagonal, so every member exits identically.
- **T2.** The literal exit equals `F` written in their notation: `s`, the next odd number, and `(λ′, a′, b′)` all agree, on 53,360 states.
- **T3.** Thm 3.3 holds on 13,320 lifting and 40,040 non-lifting states. The maximum is `s = 18`, at `(385, 32)`.
- **T4.** Thm 3.5 gives `a′` on every state. The maximum is `a′ = 17`, at `(1739, 55)`.
- **T5.** Lemma 3.4 gives `b′` on every state: 17,571 states have even `s` with `k ≠ h(s)`, and **221 sit on the boundary branch `k = h(s)`**.
- **T6.** All 667 of 667 skeletons exit into more than one skeleton across their rows. The transition is a map on rows, not on skeletons.
- **T7, a negative control.** The T3 law with the anchor shifted by 2 is rejected on **956 of 956** lifting states (`5 ≤ λ < 300`, `k < 40`).

The anchor `N(u)` is computed independently, bit by bit, from `9^t u ≡ 1 (mod 2^(t+4))` at 192-bit precision. Precision exhaustion raises an error instead of passing silently. The existing `experiments/williams_coordinate_check.py` (the dictionary itself, odd `n ≤ 200,001`) is unchanged. It was not re-run this window, since its committed output is ALL CHECKS PASS. No cycle search, no divisibility test: the README stopping rules are respected.

## For the author to decide

1. **Salutation.** The draft reads "Dear Jennifer Williams". Their title is not stated in the paper, which gives only an ECS, Southampton affiliation.
2. **The personal paragraph and sign-off** are left as bracketed placeholders.
3. **Whether to offer the script.** The draft offers it in one clause.
4. **Provenance sentence.** The draft states the 2023 note and the one-week order of posting neutrally. Cut it if you prefer to say nothing on dates.
5. **The sweep findings' "answers (1)" line** (§5 item 2, §6 item 2). It is superseded by the verdict above, so decide whether to annotate it. The same file uses a gendered pronoun for Williams in places, which is out of this window's scope and is noted only.
6. **Their public code repository is named in the paper. It was not fetched.**
