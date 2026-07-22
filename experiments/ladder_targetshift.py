"""Independent verification for ladder.md section 15.5 (the ladder as a face of
the target-shift lemma).

Supports, and is cited by, ladder.md 15.5:
  - Lemma 15.5.1   (depth steps are target shifts):
        s(w, d+k) = v2(3^d w - 3^(-k))  for all k >= 1.
  - Proposition 15.5.2 (even steps are anchor translations): for w = 1 (mod 8),
        d = 2n, k = 2j: the target 9^(-j) lies in 1 + 8 Z_2 with N(9^(-j)) = j,
        and s(w, d+2j) = 3 + v2(n + j - N(w)); verbatim on the odd component
        (w = 3 (mod 8), d = 2n+1) with the companion anchor N(3w).
  - Theorem 15.5.3 (ultrametric reading of the dichotomy):
        v2(1 - 3^(-1)) = 1;
        s(w,d) >= 2  ==>  s(w,d+1) = 1;
        s(w,d) = 1   ==>  s(w,d+1) = 1 + v2(3e + 1) >= 2, where e = e(w,d).
    Integer-level cross-check (15.1's content, NOT claimed recovered by the
    valuation frame): e(w,d+1) = T(e) off-spike, e(w,d+1) = 3*2^(s-1)*e + 1
    at a spike.

Method: exact integer arithmetic for every exit quantity (s, e via 3^d*w - 1
computed as a Python integer); 2-adic quantities as residues at explicit
precision -- targets 3^(-k) mod 2^P with P = 512, anchors N(w) mod 2^B with
B = 64 (obtained by digit-by-digit discrete log base 9, checked against the
defining congruence and against the published values N(17), N(25), N(33)
mod 2^8 from stage1-synthesis.md 11.8.3.6.6). A nonzero residue mod 2^P has a
well-defined 2-adic valuation < P, so every pass/fail comparison below is
exact; a zero residue would be flagged as a precision failure, never scored
as a pass.

Independent of experiments/ladder.py (imports nothing from it; written fresh
from the statements). Deterministic: seed 20260723.

Run: python experiments/ladder_targetshift.py
"""

import random

P = 512          # 2-adic precision (bits) for shifted-target residues
B = 64           # 2-adic precision (bits) for anchors N(w)
MODP = 1 << P
SEED = 20260723

D_MAX = 60       # max base depth d
K_MAX = 40       # max ladder shift k in check A
N_MAX = 24       # max n in check B
J_MAX = 10       # max j in check B
W_MAX = 10**6    # cores sampled below this bound


def v2(n):
    """Exact 2-adic valuation of a nonzero integer."""
    assert n != 0
    return (n & -n).bit_length() - 1


def valid_core(w):
    return w % 2 == 1 and w % 3 != 0


def exit_data(w, d):
    """Exact (s, e) for the state (w, d): A = 3^d*w - 1 = 2^s * e, e odd."""
    A = 3**d * w - 1
    s = v2(A)
    return s, A >> s


def T(e):
    """The odd Collatz map."""
    t = 3 * e + 1
    return t >> v2(t)


def anchor_N(w_res, bits):
    """N mod 2^bits with 9^N = w_res^(-1) (mod 2^(bits+3)), for w_res = 1 (mod 8).

    Digit-by-digit discrete log base 9 in the cyclic group 1 + 8Z/2^(bits+3):
    bit t of N is fixed by the congruence at level 2^(t+4).
    """
    assert w_res % 8 == 1
    m_full = 1 << (bits + 3)
    target = pow(w_res, -1, m_full)
    N = 0
    for t in range(bits):
        m = 1 << (t + 4)
        if pow(9, N, m) != target % m:
            N += 1 << t
    assert pow(9, N, m_full) == target, "discrete log failed its defining congruence"
    return N


def random_state(rng):
    while True:
        w = rng.randrange(1, W_MAX, 2)
        if valid_core(w):
            return w, rng.randrange(1, D_MAX + 1)


def check_anchor_calibration():
    """Anchor routine vs the published values (stage1-synthesis.md 11.8.3.6.6)."""
    known = {17: 38, 25: 245, 33: 236}   # N(w) mod 2^8
    for w, nref in known.items():
        got = anchor_N(w, B) % 256
        assert got == nref, f"N({w}) mod 2^8 = {got}, published {nref}"
    return len(known)


def check_A(rng, n_states=4000, ks_per_state=3):
    """Lemma 15.5.1: s(w, d+k) = v2(3^d*w - 3^(-k)), residues mod 2^P."""
    tested = failures = precision_flags = 0
    for _ in range(n_states):
        w, d = random_state(rng)
        x_res = pow(3, d, MODP) * w % MODP
        for k in rng.sample(range(1, K_MAX + 1), ks_per_state):
            lhs, _ = exit_data(w, d + k)                     # exact integers
            inv3k = pow(pow(3, k, MODP), -1, MODP)
            t = (x_res - inv3k) % MODP
            tested += 1
            if t == 0:
                precision_flags += 1
                continue
            if v2(t) != lhs:
                failures += 1
    return tested, failures, precision_flags


def check_B(rng, n_cores=300):
    """Proposition 15.5.2, even component: w = 1 (mod 8), d = 2n, k = 2j.

    Exact side: s(w, 2n+2j) by integer arithmetic.
    Anchor side: 3 + v2(n + j - N(w)), N(w) mod 2^B.
    Also: 9^(-j) = 1 (mod 8) and N(9^(-j)) = j (mod 2^B) for 1 <= j <= J_MAX.
    """
    modb = 1 << B
    # target properties: 9^(-j) in 1 + 8 Z_2 and N(9^(-j)) = j
    target_checks = target_failures = 0
    m_full = 1 << (B + 3)
    for j in range(1, J_MAX + 1):
        c = pow(pow(9, j, m_full), -1, m_full)
        target_checks += 2
        if c % 8 != 1:
            target_failures += 1
        if anchor_N(c, B) != j % modb:
            target_failures += 1
    # translation law over sampled cores
    cores = set()
    while len(cores) < n_cores:
        w = rng.randrange(1, W_MAX, 8)                       # w = 1 (mod 8)
        if valid_core(w):
            cores.add(w)
    tested = failures = precision_flags = 0
    for w in sorted(cores):
        Nw = anchor_N(w, B)
        for n in range(1, N_MAX + 1):
            for j in range(1, J_MAX + 1):
                s_exact, _ = exit_data(w, 2 * n + 2 * j)     # exact integers
                r = (n + j - Nw) % modb
                tested += 1
                if r == 0:
                    precision_flags += 1
                    continue
                if s_exact != 3 + v2(r):
                    failures += 1
    return target_checks, target_failures, tested, failures, precision_flags


def check_B_odd(rng, n_cores=300):
    """Proposition 15.5.2, odd component: w = 3 (mod 8), d = 2n+1, companion 3w.

    s(w, 2(n+j)+1) = 3 + v2(n + j - N(3w)); uses 3^(2n+1)*w = 9^n*(3w)
    (stage1.md 11.8.1.6.2).
    """
    modb = 1 << B
    cores = set()
    while len(cores) < n_cores:
        w = rng.randrange(3, W_MAX, 8)                       # w = 3 (mod 8)
        if valid_core(w):
            cores.add(w)
    tested = failures = precision_flags = 0
    for w in sorted(cores):
        N3w = anchor_N(3 * w % (1 << (B + 3)), B)
        for n in range(1, N_MAX + 1):
            for j in range(1, J_MAX + 1):
                s_exact, _ = exit_data(w, 2 * (n + j) + 1)   # exact integers
                r = (n + j - N3w) % modb
                tested += 1
                if r == 0:
                    precision_flags += 1
                    continue
                if s_exact != 3 + v2(r):
                    failures += 1
    return tested, failures, precision_flags


def check_C(rng, n_states=5000):
    """Theorem 15.5.3 + integer-level cross-check.

    Valuation claims: v2(1 - 3^(-1)) = 1 (residue mod 2^P);
    s >= 2 ==> s' = 1;  s = 1 ==> s' = 1 + v2(3e+1) >= 2.
    Also s' = v2(3^d*w - 3^(-1)) directly (the k = 1 target shift).
    Integer level (15.1, cross-check only): e' = T(e) off-spike,
    e' = 3*2^(s-1)*e + 1 at a spike.
    """
    inv3 = pow(3, -1, MODP)
    assert v2((1 - inv3) % MODP) == 1, "v2(1 - 3^(-1)) != 1"
    spike = offspike = failures = 0
    for _ in range(n_states):
        w, d = random_state(rng)
        s, e = exit_data(w, d)
        s1, e1 = exit_data(w, d + 1)
        ok = True
        # k = 1 target shift, residue side
        t = (pow(3, d, MODP) * w - inv3) % MODP
        ok &= (t != 0 and v2(t) == s1)
        if s >= 2:
            spike += 1
            ok &= (s1 == 1)
            ok &= (e1 == 3 * 2**(s - 1) * e + 1)             # kick (integer level)
        else:
            offspike += 1
            ok &= (s1 == 1 + v2(3 * e + 1))
            ok &= (s1 >= 2)
            ok &= (e1 == T(e))                               # Collatz step (integer level)
        if not ok:
            failures += 1
    return spike, offspike, failures


def main():
    rng = random.Random(SEED)
    print(f"ladder_targetshift.py  seed={SEED}  P={P}  B={B}  "
          f"w<{W_MAX}  d<={D_MAX}  k<={K_MAX}  n<={N_MAX}  j<={J_MAX}")

    n_cal = check_anchor_calibration()
    print(f"[anchor calibration] {n_cal} published values matched (N(17),N(25),N(33) mod 2^8)")

    tested, fail, flags = check_A(rng)
    print(f"[A: Lemma 15.5.1]    {tested} (state,k) pairs, {fail} failures, {flags} precision flags")
    a_fail = fail + flags

    tc, tf, tested, fail, flags = check_B(rng)
    print(f"[B: Prop 15.5.2 even] targets: {tc} checks, {tf} failures; "
          f"law: {tested} (w,n,j) triples, {fail} failures, {flags} precision flags")
    b_fail = tf + fail + flags

    tested, fail, flags = check_B_odd(rng)
    print(f"[B: Prop 15.5.2 odd]  law: {tested} (w,n,j) triples, {fail} failures, {flags} precision flags")
    bo_fail = fail + flags

    spike, offspike, fail = check_C(rng)
    print(f"[C: Thm 15.5.3]      {spike + offspike} states ({spike} spike / {offspike} off-spike), "
          f"{fail} failures (valuation + integer-level cross-check)")
    c_fail = fail

    total = a_fail + b_fail + bo_fail + c_fail
    print(f"TOTAL failures: {total}")
    assert total == 0, "verification FAILED"
    print("ALL CHECKS PASSED")


if __name__ == "__main__":
    main()
