# Mirror-queue verification suite (reverse.md, sections 14.7-14.10):
# dualizing the forward per-step machinery (paper sec:anchor) to the 3-adic
# backward direction. Independent of experiments/reverse_tree.py (fresh
# implementations of M3, predecessor(), etc., per AGENTS.md house norms).
#
#   14.7  digit-determinacy facts (a'),(b'),(c') + combined window theorem
import random


def v3(x):
    v = 0
    while x % 3 == 0:
        x //= 3
        v += 1
    return v


def M3_full(y, k):
    """t in [0, 2*3^k) with 2^t = -1/y (mod 3^(k+1)); Z/2 x Z_3 CRT rep."""
    t = None
    for tt in (0, 1):
        if pow(2, tt, 3) == (-pow(y, -1, 3)) % 3:
            t = tt
    for j in range(1, k + 1):
        m = 3 ** (j + 1)
        tgt = (-pow(y, -1, m)) % m
        stride = 2 * 3 ** (j - 1)
        for c in range(3):
            if pow(2, t + c * stride, m) == tgt:
                t = t + c * stride
                break
    return t


def predecessor(y, s):
    """(omega, d, N) for door y, branch s (14.1.1 / 14.2.4)."""
    N = (1 << s) * y + 1
    d = v3(N)
    w = N // 3 ** d
    return w, d, N


def reconstruct_exp(s_trunc_mod, modpow, parity):
    """odd modpow; smallest-style rep with given residue mod modpow, parity mod 2."""
    if s_trunc_mod % 2 == parity:
        return s_trunc_mod
    return s_trunc_mod + modpow


# ---------------------------------------------------------------------------
# 14.7  digit-determinacy facts
# ---------------------------------------------------------------------------

def fact_a(trials=3000, seed=1):
    """M3(y) mod 3^k depends only on y mod 3^(k+1)."""
    random.seed(seed)
    bad = checked = 0
    for _ in range(trials):
        k = random.randrange(1, 7)
        mod = 3 ** (k + 1)
        y1 = random.randrange(1, 10 ** 6, 2)
        while y1 % 3 == 0:
            y1 = random.randrange(1, 10 ** 6, 2)
        y2 = y1 + random.randrange(1, 50) * mod
        if y2 % 3 == 0:
            continue
        checked += 1
        if M3_full(y1, k) != M3_full(y2, k):
            bad += 1
    return checked, bad


def fact_b(trials=3000, seed=2):
    """N=2^s y+1 mod 3^q depends on y mod 3^q and s mod 3^(q-1) (parity fixed)."""
    random.seed(seed)
    bad = checked = 0
    for _ in range(trials):
        q = random.randrange(2, 8)
        modq, modq1 = 3 ** q, 3 ** (q - 1)
        y1 = random.randrange(1, 10 ** 6, 2)
        while y1 % 3 == 0:
            y1 = random.randrange(1, 10 ** 6, 2)
        y2 = y1 + random.randrange(1, 50) * modq
        if y2 % 3 == 0:
            continue
        parity = 1 if y1 % 3 == 1 else 0
        s1 = random.randrange(1, 400)
        if s1 % 2 != parity:
            s1 += 1
        s2 = s1 + random.randrange(1, 50) * modq1 * 2
        checked += 1
        N1 = (1 << s1) * y1 + 1
        N2 = (1 << s2) * y2 + 1
        if (N1 - N2) % modq != 0:
            bad += 1
    return checked, bad


def fact_c(trials=3000, seed=3):
    """omega = N/3^d mod 3^r depends on N mod 3^(d+r) and d (exact division)."""
    random.seed(seed)
    bad = checked = 0
    for _ in range(trials):
        d = random.randrange(1, 15)
        r = random.randrange(1, 8)
        base = random.randrange(1, 10 ** 5)
        if base % 3 == 0:
            base += 1
        N1 = base * 3 ** d
        N2 = N1 + random.randrange(1, 50) * 3 ** (d + r)
        checked += 1
        w1 = (N1 % 3 ** (d + r)) // 3 ** d
        w2 = (N2 % 3 ** (d + r)) // 3 ** d
        if (w1 - w2) % 3 ** r != 0:
            bad += 1
    return checked, bad


def combined_window_theorem(trials=4000, seed=4, r=3):
    """Window-only recovery of (d exact, omega mod 3^r) from y,s truncations,
    chaining (a'),(b'),(c') exactly as thm:deltaM chains (a),(b),(c)."""
    random.seed(seed)
    bad = checked = deep = 0
    for _ in range(trials):
        y = random.randrange(1, 10 ** 7, 2)
        if y % 3 == 0:
            continue
        parity = 1 if y % 3 == 1 else 0
        s = random.randrange(1, 200)
        if s % 2 != parity:
            s += 1
        w_true, d_true, _ = predecessor(y, s)
        W = d_true + r + 2
        y_trunc_W = y % (3 ** (W + 1))
        s_trunc_W = s % (3 ** W)
        m3 = M3_full(y_trunc_W, W) % (3 ** W)
        eps = (s_trunc_W - m3) % (3 ** W)
        checked += 1
        if eps == 0:
            deep += 1
            continue
        d_rec = 1 + v3(eps)
        if d_rec != d_true:
            bad += 1
            continue
        Q = d_true + r
        modQ = 3 ** Q
        y_trunc_Q = y % modQ
        s_trunc_Qm1 = s % (3 ** (Q - 1))
        exp_c = reconstruct_exp(s_trunc_Qm1, 3 ** (Q - 1), parity)
        N_approx = (pow(2, exp_c, modQ) * y_trunc_Q + 1) % modQ
        w_approx = (N_approx // 3 ** d_true) % (3 ** r)
        if (w_approx - w_true % (3 ** r)) % (3 ** r) != 0:
            bad += 1
    return checked, deep, bad


if __name__ == "__main__":
    print("== 14.7 digit-determinacy facts ==")
    print("fact (a'):", fact_a())
    print("fact (b'):", fact_b())
    print("fact (c'):", fact_c())
    for r in (1, 3, 6):
        print(f"combined window theorem r={r}:", combined_window_theorem(r=r, seed=10 + r))
