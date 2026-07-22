"""Verification for cycles.md Remark 12.6.1.3 (the spent |q| = 1 stock as the
rational-anchor instance of the digit-match ceiling) and the one-clause pointers
in anchors.md 17.4/17.5 and bridge.md 16.4.4.

Fresh, independent implementation (2026-07-23). Imports nothing from
experiments/merle_round5_check.py or experiments/ladder_targetshift.py.
Exact integer arithmetic at every pass/fail decision.

Checks, in order:
  A. The four elementary capacity laws at targets +-1:
       v2(3^k - 1) = 1 (k odd), = 3 + v2(k/2) (k even);
       v2(3^k + 1) = 2 (k odd), = 1 (k even);           for 1 <= k <= 4000.
     Identification of the even minus-case with the c = 1 global law 11.8.4.1
     at omega = 1 (N(1) = 0): v2(3^(2n) - 1) = 3 + v2(n - 0).
  B. Exhaustive |2^K - 3^n| = 1 window, 1 <= K, n <= 500: exactly
     (K, n, q) in {(1,1,-1), (2,1,+1), (3,2,-1)}.
  C. The sign pairing and demand = capacity equality at the three stock points:
     q = 2^K - 3^n = +1 pairs with v2(3^n + 1) = K, q = -1 with v2(3^n - 1) = K,
     exact equality in all three cases; and the linear demand 2^(K+1) > 3^n.
  D. The exact integer closure: the even minus-case forces 3^n <= 4n + 1
     (checked to fail for 3 <= n <= 100000, with the gap monotone at the
     boundary); the odd minus-case forces 3^n = 3; the plus-case forces
     3^n <= 3. Hence n <= 2 and the enumeration is the stock.
  E. The shifted-target reading at the target c = 17 (q = -17; c == 1 mod 8,
     so the anchor lemma applies): v2(9^j - 17) = 3 + v2(j + N(17)) for
     1 <= j <= 2000, with N(17) computed mod 2^64 by an independent
     digit-by-digit discrete log, calibrated against the published values
     N(17) = 38, N(25) = 245, N(33) = 236 (mod 2^8) (stage1-synthesis.md,
     after 11.8.3.6.6).
  F. gcd(q, 6) = 1 for q = 2^K - 3^n on a grid (K, n <= 60) — the
     multiplicative-independence side condition (3 never divides q) for the
     Bugeaud-Laurent pin 11.8.3.11 at alpha_2 = -1/q, |q| > 1.
  G. Bounded general-q texture (measurement, not a law): record matches
     max_{n <= 4000} v2(3^n + q) for q in {5, -5, 7, 23, -139}, reported and
     checked against the soft ceiling 2*log2(4000).
"""

from math import gcd, log2

FAILURES = []


def v2(x: int) -> int:
    assert x != 0
    return (x & -x).bit_length() - 1


def check(label: str, ok: bool, detail: str = "") -> None:
    if not ok:
        FAILURES.append((label, detail))
        print(f"  FAIL {label} {detail}")


# ---------- A. capacity laws at +-1, and the omega = 1 anchor-law reading ----
def check_A(KMAX: int = 4000) -> None:
    p = 1  # 3^k
    for k in range(1, KMAX + 1):
        p *= 3
        minus, plus = v2(p - 1), v2(p + 1)
        if k % 2 == 1:
            check("A.minus.odd", minus == 1, f"k={k} v2={minus}")
            check("A.plus.odd", plus == 2, f"k={k} v2={plus}")
        else:
            check("A.minus.even", minus == 3 + v2(k // 2), f"k={k} v2={minus}")
            check("A.plus.even", plus == 1, f"k={k} v2={plus}")
        if k % 2 == 0:
            # 11.8.4.1 at omega = 1: s = 3 + v2(n - N(1)) with N(1) = 0, d = 2n
            n = k // 2
            check("A.law-at-1", minus == 3 + v2(n - 0), f"n={n}")
    print(f"A: capacity laws at +-1, k <= {KMAX}: "
          f"{'PASS' if not FAILURES else 'see failures'}")


# ---------- B. exhaustive |2^K - 3^n| = 1 window ----------------------------
def check_B(BOUND: int = 500) -> None:
    expected = {(1, 1, -1), (2, 1, 1), (3, 2, -1)}
    found = set()
    pow3 = [1]
    for _ in range(BOUND):
        pow3.append(pow3[-1] * 3)
    pow2 = [1]
    for _ in range(BOUND):
        pow2.append(pow2[-1] * 2)
    for K in range(1, BOUND + 1):
        for n in range(1, BOUND + 1):
            q = pow2[K] - pow3[n]
            if q in (1, -1):
                found.add((K, n, q))
    check("B.window", found == expected, f"found={sorted(found)}")
    print(f"B: exhaustive |2^K - 3^n| = 1, K, n <= {BOUND}: found {sorted(found)}")


# ---------- C. sign pairing + demand = capacity at the stock -----------------
def check_C() -> None:
    stock = [(1, 1, -1), (2, 1, 1), (3, 2, -1)]
    for K, n, q in stock:
        check("C.identity", 2**K - 3**n == q, f"(K,n,q)=({K},{n},{q})")
        # sign pairing: 2^K - 3^n = q  <=>  3^n + q = 2^K  <=>  v2(3^n + q) = K
        # (equality, not just >=: the quotient is the unit 1)
        check("C.pairing", v2(3**n + q) == K, f"(K,n,q)=({K},{n},{q})")
        # explicit: q = +1 reads v2(3^n + 1), q = -1 reads v2(3^n - 1)
        if q == 1:
            check("C.plus", v2(3**n + 1) == K, f"n={n}")
        else:
            check("C.minus", v2(3**n - 1) == K, f"n={n}")
        # linear demand: K >= n log2(3) - 1, exact form 2^(K+1) > 3^n
        check("C.demand", 2 ** (K + 1) > 3**n, f"(K,n)=({K},{n})")
    print("C: sign pairing + demand=capacity equality at the 3 stock points: done")


# ---------- D. exact integer closure -----------------------------------------
def check_D(NMAX: int = 100000) -> None:
    # even minus-case: 3^n - 1 = 2^K forces K = 3 + v2(n/2), i.e.
    # 3^n = 1 + 8 * 2^(v2(n/2)) <= 1 + 8*(n/2) = 4n + 1. Fails for all even n >= 4.
    p = 9  # 3^n at n = 2
    check("D.even.n2", p == 4 * 2 + 1, "n=2 meets 3^n = 4n+1 with equality")
    for n in range(3, NMAX + 1):
        p *= 3
        if p <= 4 * n + 1:
            check("D.closure", False, f"n={n}: 3^n <= 4n+1")
    # gap monotone at the boundary: 3^n - (4n+1) increasing for n >= 2
    check("D.monotone", all(3 ** (n + 1) - (4 * (n + 1) + 1) > 3**n - (4 * n + 1)
                            for n in range(2, 50)))
    # odd minus-case: K = v2(3^n - 1) = 1 forces 3^n = 2^1 + 1 = 3, n = 1.
    # plus-case: K = v2(3^n + 1) <= 2 forces 3^n = 2^K - 1 <= 3, n = 1.
    check("D.odd.minus", 3**1 - 1 == 2)
    check("D.plus", 3**1 + 1 == 4 and 2**2 - 1 == 3)
    print(f"D: exact closure 3^n > 4n+1 for 3 <= n <= {NMAX} (even minus-case), "
          "odd/plus cases pinned at n = 1: done")


# ---------- E. shifted-target instance at c = 17 (q = -17) -------------------
def anchor_N(omega: int, bits: int) -> int:
    """N(omega) mod 2^bits for omega == 1 (mod 8), by digit-by-digit discrete
    log: the unique x mod 2^bits with 9^x == omega^(-1) (mod 2^(bits+3))."""
    assert omega % 8 == 1
    mod = 1 << (bits + 3)
    target = pow(omega, -1, mod)
    x = 0
    for i in range(bits):
        # decide bit i: test whether 9^(x + 2^i) matches target mod 2^(i+4)
        m = 1 << (i + 4)
        if pow(9, x, m) != target % m:
            x |= 1 << i
            assert pow(9, x, m) == target % m, (omega, i)
    return x


def check_E(JMAX: int = 2000, BITS: int = 64) -> None:
    # calibration against the published mod 2^8 values
    for omega, pub in ((17, 38), (25, 245), (33, 236)):
        check("E.calibration", anchor_N(omega, 8) % 256 == pub,
              f"N({omega}) mod 2^8 = {anchor_N(omega, 8) % 256}, published {pub}")
    N17 = anchor_N(17, BITS)
    guard = BITS - 8
    p9 = 1
    for j in range(1, JMAX + 1):
        p9 *= 9
        lhs = v2(p9 - 17)
        t = (j + N17) % (1 << BITS)
        rhs_v = v2(t) if t else BITS  # t == 0 cannot happen below the guard
        check("E.guard", rhs_v < guard, f"j={j}: valuation at precision limit")
        check("E.targetshift", lhs == 3 + rhs_v, f"j={j}: lhs={lhs} rhs=3+{rhs_v}")
    print(f"E: v2(9^j - 17) = 3 + v2(j + N(17)) for j <= {JMAX} "
          f"(N(17) mod 2^{BITS}, calibrated mod 2^8 against published values): done")


# ---------- F. gcd(q, 6) = 1 --------------------------------------------------
def check_F(BOUND: int = 60) -> None:
    for K in range(1, BOUND + 1):
        for n in range(1, BOUND + 1):
            q = 2**K - 3**n
            check("F.gcd", gcd(q, 6) == 1, f"(K,n)=({K},{n})")
    print(f"F: gcd(2^K - 3^n, 6) = 1 on the full grid K, n <= {BOUND}: done")


# ---------- G. bounded general-q texture (measurement) -----------------------
def check_G(NMAX: int = 4000) -> None:
    qs = [5, -5, 7, 23, -139]
    ceiling = 2 * log2(NMAX)  # soft: texture, not a law
    print(f"G: record matches max_(n <= {NMAX}) v2(3^n + q)  "
          f"[soft ceiling 2*log2({NMAX}) = {ceiling:.1f}]:")
    p = 1
    records = {q: (0, 0) for q in qs}
    for n in range(1, NMAX + 1):
        p *= 3
        for q in qs:
            val = v2(p + q)
            if val > records[q][0]:
                records[q] = (val, n)
    for q in qs:
        rec, at = records[q]
        print(f"     q = {q:5d}: record v2 = {rec} at n = {at}")
        check("G.texture", rec <= ceiling, f"q={q} record={rec}")


if __name__ == "__main__":
    check_A()
    check_B()
    check_C()
    check_D()
    check_E()
    check_F()
    check_G()
    total = len(FAILURES)
    print(f"\nRESULT: {'PASS - 0 failures' if total == 0 else f'{total} FAILURES'}")
    raise SystemExit(0 if total == 0 else 1)
