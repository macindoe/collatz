"""Williams' row-exit map (arXiv:2607.01718, open problem (1)) against paper 1's F and laws.

Supports: briefs/williams-letter-findings.md (Item A: what paper 1 gives toward
J. Williams' open problem (1), stated in their notation).

Williams' coordinates: odd n = lam 2^a 3^b - 1, gcd(lam, 6) = 1, a >= 1, b >= 0,
row k = a + b. Diagonal flow (a, b) -> (a-1, b+1) for a >= 2 (their Thm 3.6);
the row exits at the boundary position (1, k-1) (their Cor. 3.9) with
v2(3n + 1) = 1 + v2(lam 3^k - 1) and next odd = odd part of lam 3^k - 1 (their
Prop. 3.10). Open problem (1) (p. 18) asks which skeleton is entered.

Paper 1 (v3, paper/collatz-reduced-v3.tex): the state (w, d) is (lam, k); F is
Definition 2.1; the exit valuation, entry depth and 3-absorption obey the laws of
Section 3 (Thm 3.3 global valuation law, Thm 3.5 depth closure / entry-depth law,
Lemma 3.4 absorption law), all in terms of the 2-adic anchor M(w) = N(w^2),
N(u) = the t in Z_2 with 9^t = u^(-1).

Fresh code, written for this check. Nothing here imports the record's other
scripts. "Ground truth" is the literal full Collatz map C(n) = n/2 or 3n + 1,
iterated step by step on integers.

For every lam coprime to 6 with lam < LAM and every row 1 <= k <= K:
  T1. Diagonal flow from the row's top position (k, 0), n = lam 2^k - 1, under the
      literal C: every odd iterate before the exit sits in row k of L_lam at
      position (k-j, j); the exit position is (1, k-1). (Every row member lies on
      this diagonal, so every member exits identically: the entered skeleton
      depends on (lam, k) only.)
  T2. The literal exit (halvings after 3n+1 at (1, k-1), next odd n', and the
      Williams decomposition n' + 1 = lam' 2^a' 3^b') equals F's closed formula in
      their notation:
        s   = v2(lam 3^k - 1)           [their v2(3n+1) = 1 + s]
        a'  = v2(lam 3^k - 1 + 2^s) - s
        b'  = v3(lam 3^k - 1 + 2^s)
        lam'= (lam 3^k - 1 + 2^s) / (2^(s+a') 3^b')
        k'  = a' + b'
      i.e. (lam', k') = F(lam, k) and (a', b') = (m_+, a_+).
  T3. Exit valuation law (paper 1 Thm 3.3): s = 2 + v2(k - M(lam)) when
      lam 3^k = 1 mod 8; otherwise s in {1,2} from (lam mod 8, k mod 2).
  T4. Entry-position law a' = m_+ (paper 1 Thm 3.5, the entry-depth law).
  T5. Entry-position law b' = a_+ (paper 1 Lemma 3.4, the absorption law),
      including the boundary branch d = h(s).
  T6. How far the target skeleton lam' is a function of lam alone: the number of
      lam whose rows k = 1..K exit into more than one skeleton.
  T7. Negative control: the T3 law with the anchor deliberately shifted
      (M -> M + 2) must be rejected on every lifting state of a smaller range.

One command reproduces the committed output:
  python experiments/williams_transition_check.py > experiments/williams_transition_check_output.txt
"""
import sys

LAM = 2000      # lam < LAM, gcd(lam, 6) = 1
K = 80          # rows 1..K
P = 192         # 2-adic precision (bits) for the anchor computations


def v2(x):
    if x == 0:
        raise ValueError('v2(0)')
    c = 0
    while x % 2 == 0:
        x //= 2
        c += 1
    return c


def v3(x):
    if x == 0:
        raise ValueError('v3(0)')
    c = 0
    while x % 3 == 0:
        x //= 3
        c += 1
    return c


def decompose(n):
    """Williams' coordinates of odd n: n + 1 = lam 2^a 3^b, gcd(lam, 6) = 1."""
    a = v2(n + 1)
    r = (n + 1) >> a
    b = v3(r)
    return r // 3 ** b, a, b


def N2(u, bits=P):
    """t mod 2^bits with 9^t * u = 1 in Z_2, for u = 1 mod 8 (u may be negative)."""
    mod = 1 << (bits + 3)
    u %= mod
    assert u % 8 == 1
    t = 0
    for j in range(bits):
        if (pow(9, t, mod) * u) % (1 << (j + 4)) != 1:
            t += 1 << j
    return t


def v2_mod(x, bits=P):
    """v2 of a 2-adic number known mod 2^bits; fails loudly if precision runs out."""
    x %= 1 << bits
    if x == 0:
        raise ArithmeticError('2-adic precision exhausted')
    return v2(x)


def literal_exit(lam, k):
    """Walk the literal map C from the top of row k of L_lam to the exit.

    Returns (ok_diagonal, s_literal, next_odd)."""
    n = lam * 2 ** k - 1
    ok = True
    for j in range(k - 1):            # k-1 interior odd steps, positions (k-j, j)
        if decompose(n) != (lam, k - j, j):
            ok = False
        m = 3 * n + 1
        h = 0
        while m % 2 == 0:
            m //= 2
            h += 1
        if h != 1:                    # interior: exactly one halving (their Cor 3.7)
            ok = False
        n = m
    if decompose(n) != (lam, 1, k - 1):  # exit position (1, k-1)
        ok = False
    m = 3 * n + 1
    h = 0
    while m % 2 == 0:
        m //= 2
        h += 1
    return ok, h - 1, m               # their v2(3n+1) = 1 + s


def F_williams(lam, k):
    """F (paper 1 Def. 2.1) written in Williams' notation."""
    A = lam * 3 ** k - 1
    s = v2(A)
    C = A + 2 ** s
    ap = v2(C) - s
    bp = v3(C)
    lamp = C // (2 ** (s + ap) * 3 ** bp)
    return s, ap, bp, lamp, A >> s


def s_law(lam, k):
    """Paper 1 Thm 3.3 (global valuation law)."""
    if (lam * pow(3, k, 8)) % 8 == 1:                   # lifting
        M = N2(lam * lam)
        return 2 + v2_mod(k - M), True
    table = {(1, 1): 1, (5, 1): 1, (7, 0): 1, (3, 0): 1, (5, 0): 2, (7, 1): 2}
    return table[(lam % 8, k % 2)], False


def entry_depth_law(lam, k, s, lifting):
    """Paper 1 Thm 3.5 (entry-depth law): m_+ = a'."""
    if lifting:
        if k % 2 == 0:
            n = k // 2
            eps = n - N2(lam)
        else:
            n = (k - 1) // 2
            eps = n - N2(3 * lam)
        delta = N2(1 - 2 ** s)
        return 3 - s + v2_mod(eps + delta)
    M = N2(lam * lam)
    if s == 1:
        return 1 + v2_mod(k - M)
    if s == 2:
        return v2_mod((k - 1) - M)
    raise AssertionError('non-lifting s not in {1,2}')


def absorption_law(lam, k, s):
    """Paper 1 Lemma 3.4: a_+ = b'."""
    if s % 2 == 1:
        return 0, 'odd'
    h = 1 + v3(s)
    if k != h:
        return min(k, h), 'even'
    return k + v3(lam + (2 ** s - 1) // 3 ** k), 'boundary'


def main():
    c = dict(states=0, lifting=0, nonlifting=0, absorb_even=0, absorb_boundary=0,
             interior_steps=0)
    fails = []
    targets = {}
    max_s = (0, None)
    max_ap = (0, None)
    for lam in range(1, LAM):
        if lam % 2 == 0 or lam % 3 == 0:
            continue
        targets[lam] = set()
        for k in range(1, K + 1):
            c['states'] += 1
            c['interior_steps'] += k - 1
            ok, s_lit, nxt = literal_exit(lam, k)
            if not ok:
                fails.append(('T1', lam, k))
            s, ap, bp, lamp, xe = F_williams(lam, k)
            lam_lit, a_lit, b_lit = decompose(nxt)
            if (s_lit, nxt, lam_lit, a_lit, b_lit) != (s, xe, lamp, ap, bp):
                fails.append(('T2', lam, k))
            s_pred, lifting = s_law(lam, k)
            c['lifting' if lifting else 'nonlifting'] += 1
            if s_pred != s:
                fails.append(('T3', lam, k))
            if entry_depth_law(lam, k, s, lifting) != ap:
                fails.append(('T4', lam, k))
            bp_pred, branch = absorption_law(lam, k, s)
            if branch == 'even':
                c['absorb_even'] += 1
            elif branch == 'boundary':
                c['absorb_boundary'] += 1
            if bp_pred != bp:
                fails.append(('T5', lam, k))
            targets[lam].add(lamp)
            if s > max_s[0]:
                max_s = (s, (lam, k))
            if ap > max_ap[0]:
                max_ap = (ap, (lam, k))
    multi = sum(1 for t in targets.values() if len(t) > 1)
    # T7 negative control: T3 with the anchor shifted by 2 must fail on every
    # lifting state (lam >= 5 so that k - M - 2 is never exactly 0).
    ctrl_tot = ctrl_bad = 0
    for lam in range(5, 300):
        if lam % 2 == 0 or lam % 3 == 0:
            continue
        for k in range(1, 40):
            if (lam * pow(3, k, 8)) % 8 != 1:
                continue
            ctrl_tot += 1
            if 2 + v2_mod(k - N2(lam * lam) - 2) != F_williams(lam, k)[0]:
                ctrl_bad += 1
    if ctrl_bad != ctrl_tot:
        fails.append(('T7', ctrl_bad, ctrl_tot))
    print("Williams' row-exit map vs paper 1's F and Section 3 laws")
    print('  range: lam < %d coprime to 6 (%d skeletons), rows 1 <= k <= %d; %d (lam, k) states'
          % (LAM, len(targets), K, c['states']))
    print('  T1 literal diagonal flow to exit (1, k-1):      %d states, %d interior odd steps'
          % (c['states'], c['interior_steps']))
    print('  T2 literal exit == F in Williams notation:       %d states' % c['states'])
    print('  T3 s law (Thm 3.3): lifting %d, non-lifting %d; max s = %d at (lam, k) = %s'
          % (c['lifting'], c['nonlifting'], max_s[0], max_s[1]))
    print("  T4 a' = entry-depth law (Thm 3.5):               %d states; max a' = %d at %s"
          % (c['states'], max_ap[0], max_ap[1]))
    print("  T5 b' = absorption law (Lemma 3.4):              %d states; s even with k != h(s): %d, boundary k = h(s): %d"
          % (c['states'], c['absorb_even'], c['absorb_boundary']))
    print("  T6 skeletons whose rows exit into more than one skeleton: %d of %d"
          % (multi, len(targets)))
    print('  T7 control (anchor shifted by 2, 5 <= lam < 300, k < 40): %d of %d lifting states rejected'
          % (ctrl_bad, ctrl_tot))
    print('failures: %d' % len(fails))
    if fails:
        print('first failures:', fails[:10])
    print('ALL CHECKS PASS' if not fails else 'CHECKS FAILED')
    return 0 if not fails else 1


if __name__ == '__main__':
    sys.exit(main())
