"""Junction Theorem preprint, section 3 — the deficit statement read at first hand.

Supports `briefs/junction-public-recon-findings.md` (item 4 of
`briefs/junction-public-recon-brief.md`): the first-hand check of flag 6 of
`briefs/merle-la7-close-check-findings.md` ("is the preprint's `S` our `K`?"),
now that `github.com/ericmerle3789/Collatz-Junction-Theorem` is public and
`paper/preprint_en.tex` can be read.

Source read (read-only clone, HEAD `a57d29e`), `paper/preprint_en.tex`:

  Notation (ssec:notations):
      k >= 1            length of a cycle (number of odd steps)
      S = S(k)          = ceil(k * log2 3)                  "Syracuse height"
      d = d(k)          = 2^S - 3^k                         "crystal module"
      C = C(k)          = binom(S-1, k-1)
      h(p)              = -p log2 p - (1-p) log2(1-p)

  Definition 3.1 (eq:gamma):
      gamma = 1 - h(1 / log2 3)

  Proposition 3.5, "Linear deficit" (eq:deficit):
      log2 d - log2 C >= (S-1) * gamma - eps(k),   eps(k) = O(log k)

Our own L-A7 / margin form (cycles.md-side conventions, `briefs/margin-inequality-proof-findings.md`):

      margin(n) = K - log2 binom(K-2, n-1),  K = ceil(n * log2 3)
      margin(n) >= c_gen * n,  c_gen = L - L*log2 L + (L-1)*log2(L-1),  L = log2 3

Four things are checked, all in exact integer / high-precision arithmetic:

  (A) S(k) as the preprint defines it IS our K(n) under k <-> n:
      ceil(k * log2 3) computed exactly by integer comparison of 2^S vs 3^k.
  (B) gamma * log2 3 == c_gen (the units identity his REQ-MATH-037 asserts),
      to 60 digits, plus the residual.
  (C) The preprint's own inequality AS PRINTED WITHOUT the error term,
      log2 d - log2 C >= (S-1)*gamma, over a range of k: does it hold, and
      with what slack?  (The printed statement carries "- eps(k)"; this
      isolates how much of the statement the error term is actually carrying.)
  (D) The index difference: the preprint counts C = binom(S-1, k-1); our
      L-A7 word count is binom(K-2, n-1).  Both are evaluated and the gap
      log2 binom(S-1,k-1) - log2 binom(K-2,n-1) is reported.

No claim about the preprint's proof is made here.  This script records what
the printed statement says and how it evaluates; the grading of the proof is
not this session's business.

Run: python experiments/junction_public_recon_deficit_check.py
"""

from math import comb

from mpmath import binomial, log, mp, mpf

mp.dps = 60

L = log(3, 2)  # log2 3
GAMMA = 1 - (-(1 / L) * log(1 / L, 2) - (1 - 1 / L) * log(1 - 1 / L, 2))
C_GEN = L - L * log(L, 2) + (L - 1) * log(L - 1, 2)


def S_of_k(k: int) -> int:
    """ceil(k * log2 3), by exact integer comparison — no floating point.

    3^k has bit_length b, so 2^(b-1) <= 3^k < 2^b.  For k >= 1, 3^k is never
    a power of two, so ceil(log2 3^k) = b, i.e. S = b.
    """
    return (3 ** k).bit_length()


def report(title: str) -> None:
    print()
    print(title)
    print("-" * len(title))


def main() -> None:
    failures = 0
    checks = 0

    print("Junction preprint section 3 — deficit statement, first-hand check")
    print("source: ericmerle3789/Collatz-Junction-Theorem @ a57d29e, paper/preprint_en.tex")
    print(f"mp.dps = {mp.dps}")

    # ---- (A) S(k) is K(n) -------------------------------------------------
    report("(A) S = ceil(k*log2 3) is our K = ceil(n*log2 3)")
    mismatches = []
    for k in range(1, 401):
        s_exact = S_of_k(k)
        # our K, computed the way our own record computes it
        k_ours = int(mp.ceil(k * L))
        checks += 1
        if s_exact != k_ours:
            mismatches.append((k, s_exact, k_ours))
    print(f"  k = 1..400, exact-integer S(k) vs ceil(n*log2 3): "
          f"{len(mismatches)} mismatch(es)")
    for k, a, b in mismatches[:5]:
        print(f"    k={k}: exact {a}, ours {b}")
    failures += len(mismatches)
    print(f"  S(3) = {S_of_k(3)}, S(5) = {S_of_k(5)}, S(100) = {S_of_k(100)}"
          "   (preprint prints 5, 8, 159)")
    checks += 1
    if (S_of_k(3), S_of_k(5), S_of_k(100)) != (5, 8, 159):
        print("  MISMATCH against the preprint's printed values")
        failures += 1
    else:
        print("  MATCH against the preprint's printed values")

    # ---- (B) the units identity ------------------------------------------
    report("(B) gamma * log2 3 == c_gen")
    print(f"  gamma            = {mp.nstr(GAMMA, 20)}")
    print(f"  gamma * log2 3   = {mp.nstr(GAMMA * L, 20)}")
    print(f"  c_gen            = {mp.nstr(C_GEN, 20)}")
    resid = abs(GAMMA * L - C_GEN)
    print(f"  |difference|     = {mp.nstr(resid, 5)}")
    checks += 1
    if resid > mpf(10) ** (-50):
        print("  FAIL: not equal at 50 digits")
        failures += 1
    else:
        print("  PASS: equal to within 1e-50 at dps=60")
    print(f"  gamma * (log2 3 - 1) = {mp.nstr(GAMMA * (L - 1), 10)}"
          "   (the S = K - n reading; not c_gen)")

    # ---- (C) the printed inequality without its error term ---------------
    report("(C) log2 d - log2 C >= (S-1)*gamma, as printed minus eps(k)")
    print("   k     S      log2 d - log2 C     (S-1)*gamma        slack")
    worst = None
    neg = 0
    for k in list(range(2, 41)) + [50, 68, 69, 100, 200, 306, 500, 666, 1000, 2000]:
        S = S_of_k(k)
        d = 2 ** S - 3 ** k
        if d <= 0:
            continue
        C = comb(S - 1, k - 1)
        lhs = log(d, 2) - log(C, 2)
        rhs = (S - 1) * GAMMA
        slack = lhs - rhs
        checks += 1
        if slack < 0:
            neg += 1
        if worst is None or slack < worst[2]:
            worst = (k, S, slack)
        if k <= 20 or k in (50, 68, 69, 100, 200, 306, 500, 666, 1000, 2000):
            print(f"  {k:4d} {S:6d}   {mp.nstr(lhs, 10):>16}  "
                  f"{mp.nstr(rhs, 10):>16}  {mp.nstr(slack, 8):>14}")
    print(f"  negative-slack instances: {neg}")
    print(f"  minimum slack: {mp.nstr(worst[2], 10)} at k = {worst[0]} (S = {worst[1]})")

    # ---- (D) the index difference ----------------------------------------
    report("(D) preprint C = binom(S-1, k-1) vs our word count binom(K-2, n-1)")
    print("   k     log2 binom(S-1,k-1)   log2 binom(K-2,n-1)      difference")
    for k in (18, 50, 100, 306, 1000, 2000):
        S = S_of_k(k)
        a = log(binomial(S - 1, k - 1), 2)
        b = log(binomial(S - 2, k - 1), 2)
        checks += 1
        print(f"  {k:4d}   {mp.nstr(a, 12):>18}   {mp.nstr(b, 12):>18}   "
              f"{mp.nstr(a - b, 8):>12}")
    print("  (the difference is log2((S-1)/(S-k)), strictly positive: the")
    print("   preprint's C is the larger count, so its LHS is the smaller)")

    # ---- our own margin, for the record ----------------------------------
    report("(E) our margin(n) = K - log2 binom(K-2, n-1) against c_gen*n")
    print("   n     K       margin(n)        c_gen*n          slack")
    worst2 = None
    for n in (1, 2, 5, 18, 100, 1000, 16266, 190537):
        K = S_of_k(n)
        m = K - log(binomial(K - 2, n - 1), 2)
        r = C_GEN * n
        checks += 1
        if worst2 is None or (m - r) < worst2[1]:
            worst2 = (n, m - r)
        print(f"  {n:6d} {K:6d}   {mp.nstr(m, 10):>14}  {mp.nstr(r, 10):>14}  "
              f"{mp.nstr(m - r, 10):>14}")
    print(f"  minimum slack over the sampled n: {mp.nstr(worst2[1], 10)} at n = {worst2[0]}")
    print("  (1 + log2(log2 3) = "
          f"{mp.nstr(1 + log(L, 2), 12)} is the proved floor, Theorem A)")

    report("Summary")
    print(f"  checks recorded: {checks}")
    print(f"  failures:        {failures}")


if __name__ == "__main__":
    main()
