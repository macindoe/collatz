"""Williams (arXiv:2607.01718) skeleton coordinates against paper 1's reduced states.

Supports: briefs/ceiling-ccchallenge-sweep-findings.md, Item C (the Williams verdict).
It checks the dictionary between the record's reduced coordinates (paper 1 v3,
Definition 2.1 and Proposition 2.2 = the projection R(x) = (w, m + a) for an odd x
with x + 1 = 2^m 3^a w, 3 not dividing w, and the reduced map F) and the
coordinates of

  J. Williams, "A Coordinate System for Collatz Dynamics", arXiv:2607.01718v1
  (2 Jul 2026): n = lambda 2^a 3^b - 1 with gcd(lambda, 6) = 1, a >= 1, b >= 0;
  skeleton L_lambda; row k = a + b (Prop. 3.3); diagonal flow (a, b) -> (a-1, b+1)
  for a >= 2 under the full map C (Thm 3.6); boundary a = 1 exit with
  v2(3n + 1) = 1 + v2(lambda 3^(b+1) - 1) and next odd = odd part of
  lambda 3^(b+1) - 1 (Prop. 3.10).

Williams' formulas are transcribed from the held PDF (pp. 8-10); paper 1's from
paper/collatz-reduced-v3.tex lines 63-81. Fresh code; exact integer arithmetic.

Checks, over every odd n in [1, N]:
  1. (lambda, a + b) = R(n) = (w, d): Williams' skeleton index is the odd core and her
     row index is the depth.
  2. Williams' row k of L_lambda (b = 0..k-1, a = k-b) is exactly paper 1's
     representative list of (w, d) (x = 2^(d-a) 3^a w - 1, 0 <= a <= d-1).
  3. Diagonal flow: for a >= 2 the next odd iterate under C (= T odd-to-odd) is
     lambda 2^(a-1) 3^(b+1) - 1, i.e. Proposition 2.2(i).
  4. Boundary: at a = 1, v2(3n + 1) = 1 + s(w, d) and the next odd number is
     x_exit(w, d) (Definition 2.1 / Proposition 2.2(ii)).

Statement numbers are those of the published v3 PDF (Definition 2.1, Proposition 2.2
block structure, Theorem 2.3 convergence translation). The printed label of check 3
still reads "Prop 2.3(i)", kept so that the committed output stays byte-identical.
  5. Hence "the skeleton/row entered after the boundary exit" (Williams' open
     problem (1), the row-exit map) is F(w, d): R(next odd) = F(R(n)).

One command reproduces the committed output:
  python experiments/williams_coordinate_check.py > experiments/williams_coordinate_check_output.txt
"""
import sys

N = 200_001  # odd n up to N


def v2(x):
    c = 0
    while x % 2 == 0:
        x //= 2
        c += 1
    return c


def v3(x):
    c = 0
    while x % 3 == 0:
        x //= 3
        c += 1
    return c


def williams(n):
    """n odd -> (lambda, a, b) with n + 1 = lambda 2^a 3^b, gcd(lambda, 6) = 1."""
    a = v2(n + 1)
    r = (n + 1) >> a
    b = v3(r)
    lam = r // 3 ** b
    return lam, a, b


def R(x):
    """Paper 1's projection: x + 1 = 2^m 3^a w -> (w, m + a)."""
    m = v2(x + 1)
    u = (x + 1) >> m
    a = v3(u)
    return u // 3 ** a, m + a


def F(w, d):
    """Paper 1 Definition 2.1."""
    A = 3 ** d * w - 1
    s = v2(A)
    xe = A >> s
    C = A + 2 ** s
    sig = v2(C)
    ap = v3(C >> sig)
    wn = C // (2 ** sig * 3 ** ap)
    return (wn, (sig - s) + ap), s, xe


def T(x):
    """odd -> next odd under the full Collatz map C."""
    y = 3 * x + 1
    return y >> v2(y)


def main():
    counts = dict(states=0, rows=0, diag=0, boundary=0, rowexit=0)
    fails = []
    rows_seen = set()
    for n in range(1, N + 1, 2):
        lam, a, b = williams(n)
        w, d = R(n)
        counts['states'] += 1
        if (lam, a + b) != (w, d):
            fails.append(('1', n))
        if (w, d) not in rows_seen and d <= 40:
            rows_seen.add((w, d))
            row_w = sorted(lam * 2 ** (d - bb) * 3 ** bb - 1 for bb in range(d))
            row_p = sorted(2 ** (d - aa) * 3 ** aa * w - 1 for aa in range(d))
            counts['rows'] += 1
            if row_w != row_p or n not in row_w:
                fails.append(('2', n))
        nxt = T(n)
        if a >= 2:
            counts['diag'] += 1
            if nxt != lam * 2 ** (a - 1) * 3 ** (b + 1) - 1:
                fails.append(('3', n))
        else:
            counts['boundary'] += 1
            (Fw, s, xe) = F(w, d)
            if v2(3 * n + 1) != 1 + v2(lam * 3 ** (b + 1) - 1) or v2(3 * n + 1) != 1 + s:
                fails.append(('4v', n))
            odd_part = (lam * 3 ** (b + 1) - 1) >> v2(lam * 3 ** (b + 1) - 1)
            if nxt != odd_part or nxt != xe:
                fails.append(('4x', n))
            counts['rowexit'] += 1
            if R(nxt) != Fw:
                fails.append(('5', n))
    print('Williams (arXiv:2607.01718) coordinates vs paper 1 reduced states, odd n <= %d' % N)
    print('  1. (lambda, a+b) == R(n) = (w, d):            %d odd n checked' % counts['states'])
    print('  2. row k of L_lambda == representatives of (w, d): %d distinct rows (d <= 40) checked' % counts['rows'])
    print('  3. diagonal flow (a >= 2) == Prop 2.3(i):     %d interior positions checked' % counts['diag'])
    print('  4. boundary (a = 1): v2 = 1 + s, next = x_exit: %d boundary positions checked' % counts['boundary'])
    print('  5. row-exit map == F (R(next) == F(R(n))):      %d boundary positions checked' % counts['rowexit'])
    print('failures: %d' % len(fails))
    if fails:
        print('first failures:', fails[:10])
    print('ALL CHECKS PASS' if not fails else 'CHECKS FAILED')
    return 0 if not fails else 1


if __name__ == '__main__':
    sys.exit(main())
