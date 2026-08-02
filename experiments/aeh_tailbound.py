"""Verification for aeh.md 13.6.3(iv): the exceptional tail P(a >= j) under B-hat.

Supports: aeh.md 13.6.3(iii)-(iv), 13.6.5, 13.2.4(e), 13.6.4.
Fresh code -- imports nothing from aeh_symbolic.py, aeh_calibration.py,
aeh_basecase.py, aeh_anomaly.py or itinerary_coding.py.  Everything is
re-derived from the seam formulas as printed in reverse.md 14.14.4.1 /
14.14.8.2 and itinerary.md 14.15.3.3.

Objects
-------
letter      (m, r), m = v2(y+1), r = v2(3^m q - 1), q = (y+1)/2^m; P = 2^-(m+r)
door map    G(y) = (3^m (y+1)/2^m - 1)/2^r = 3^m 2^-(m+r) y + (3^m - 2^m) 2^-(m+r)
past limit  y3 = lim_n B_n, B_n the composed affine offset of the last n letters
absorption  a = v3(y3 + 1)

The law is computed from the *backward* (prepend) form, which is independent of
the forward kernel used in aeh_symbolic.nu_exact:

    W := y3 + 1     satisfies     W = (1 - 2^-r) + 3^m 2^-(m+r) W' ,

with (m, r) the letter of the preceding door and W' that door's own y3 + 1,
independent of (m, r) under B-hat and equal to W in law by stationarity.

Checks
------
 1. exact rational law of W mod 3^J, J <= 5     -> P(a >= j) against 13.6.5
 2. float law of W mod 3^J, J = 11              -> tail table against both bounds
 3. max atom Q_t = max_z P(W = z mod 3^t)       -> against Q_t <= (5/6)^t
 4. Monte Carlo on the composed-affine offsets  -> independent code path
 5. real integer orbits                         -> P(v3(y_n + 1) >= j) along orbits
 6. finite-past reconstruction of the capped window at several past-windows W

Run: python experiments/aeh_tailbound.py     (date: 2026-08-02)
"""

import random
from collections import defaultdict
from fractions import Fraction

import numpy as np

FAILS = []


def check(name, ok, detail=""):
    if not ok:
        FAILS.append(name)
    print(f"  [{'ok  ' if ok else 'FAIL'}] {name}" + (f"   ({detail})" if detail else ""))


# ---- elementary valuations, the stratum and the door map --------------------

def v2(n):
    k = 0
    while n % 2 == 0:
        n //= 2
        k += 1
    return k


def v3(n):
    k = 0
    while n % 3 == 0:
        n //= 3
        k += 1
    return k


def stratum(y):
    m = v2(y + 1)
    q = (y + 1) >> m
    return m, v2(3 ** m * q - 1)


def G(y):
    m = v2(y + 1)
    q = (y + 1) >> m
    z = 3 ** m * q - 1
    return z >> v2(z)


def state_of_door(y):
    """(omega, d) with y + 1 = 2^m 3^a omega and d = m + a  (reverse.md 14.14.7)."""
    m = v2(y + 1)
    rest = (y + 1) >> m
    a = v3(rest)
    return rest // 3 ** a, m + a


# ---- 1. exact law of W = y3 + 1 mod 3^J ------------------------------------

def mu_exact(J):
    """Exact law of W mod 3^J, {residue: Fraction}.

    r is lumped by residue class mod ord(2 mod 3^J) = 2*3^(J-1) with the exact
    geometric mass 2^-c/(1 - 2^-P) of {r >= 1 : r == c mod P}; m is enumerated
    1..J-1 with m >= J lumped (3^m == 0 mod 3^J there).  After J applications of
    the kernel the answer is independent of the start, the accumulated
    multiplier having 3-adic valuation sum(m_i) >= J.
    """
    mod = 3 ** J
    P = 2 * 3 ** (J - 1)
    inv2 = pow(2, -1, mod)
    wr = {c: Fraction(1, 2 ** c) / (1 - Fraction(1, 2 ** P)) for c in range(1, P + 1)}
    i2 = [1] * (P + 1)
    for c in range(1, P + 1):
        i2[c] = (i2[c - 1] * inv2) % mod

    dist = {0: Fraction(1)}
    for _ in range(J):
        nxt = defaultdict(Fraction)
        for m in range(1, J):
            sub = 3 ** (J - m)
            fold = defaultdict(Fraction)
            for u, p in dist.items():
                fold[u % sub] += p
            pm, p3, invm = Fraction(1, 2 ** m), 3 ** m, pow(inv2, m, mod)
            for c, wc in wr.items():
                B = (1 - i2[c]) % mod
                unit = (invm * i2[c]) % sub
                w = pm * wc
                for u, p in fold.items():
                    nxt[(B + p3 * ((unit * u) % sub)) % mod] += p * w
        pm = Fraction(1, 2 ** (J - 1))                       # P(m >= J)
        for c, wc in wr.items():
            nxt[(1 - i2[c]) % mod] += pm * wc
        dist = dict(nxt)
    assert sum(dist.values()) == 1
    return dist


def mu_float(J, RCAP=90):
    """The same law in floating point, r truncated at RCAP (tail mass < 2^-RCAP)."""
    mod = 3 ** J
    inv2 = pow(2, -1, mod)
    i2 = [1] * (RCAP + 1)
    for c in range(1, RCAP + 1):
        i2[c] = (i2[c - 1] * inv2) % mod

    dist = np.zeros(mod)
    dist[0] = 1.0
    for _ in range(J):
        nxt = np.zeros(mod)
        for m in range(1, J):
            sub = 3 ** (J - m)
            fold = dist.reshape(-1, sub).sum(axis=0)          # u -> u % sub
            idx = np.arange(sub)
            pm, p3, invm = 2.0 ** -m, 3 ** m, pow(inv2, m, mod)
            for c in range(1, RCAP + 1):
                B = (1 - i2[c]) % mod
                unit = (invm * i2[c]) % sub
                np.add.at(nxt, (B + p3 * ((unit * idx) % sub)) % mod,
                          fold * (pm * 2.0 ** -c))
        pm = 2.0 ** -(J - 1)
        for c in range(1, RCAP + 1):
            nxt[(1 - i2[c]) % mod] += pm * 2.0 ** -c
        dist = nxt
    return dist


# ---- 4. Monte Carlo on the composed-affine offset recursion ----------------

def mc_tail(J, N, seed):
    """Draw J iid letters, build the offset by 14.14.8.2, read a = v3(B_J + 1)."""
    rng = random.Random(seed)
    mod = 3 ** J
    cnt = [0] * (J + 1)

    def geo():
        k = 1
        while rng.random() < 0.5:
            k += 1
        return k

    for _ in range(N):
        A, B = 1, 0
        for _ in range(J):
            m, r = geo(), geo()
            inv = pow(pow(2, m + r, mod), -1, mod)
            al = (pow(3, m, mod) * inv) % mod
            be = ((pow(3, m, mod) - pow(2, m, mod)) * inv) % mod
            A, B = (al * A) % mod, (al * B + be) % mod
        w = (B + 1) % mod
        a = J if w == 0 else v3(w)
        for j in range(min(a, J) + 1):
            cnt[j] += 1
    return [c / N for c in cnt]


# ---- 5/6. real orbits: the absorption law and the finite-past reconstruction

def offset_from_letters(letters, mod):
    """B_n mod `mod` for `letters` in forward order (14.14.8.2)."""
    A, B = 1, 0
    for (m, r) in letters:
        inv = pow(pow(2, m + r, mod), -1, mod)
        al = (pow(3, m, mod) * inv) % mod
        be = ((pow(3, m, mod) - pow(2, m, mod)) * inv) % mod
        A, B = (al * A) % mod, (al * B + be) % mod
    return B


def orbit_run(seed, NORB, L, BITS, Ws, k, D):
    rng = random.Random(seed)
    tail = defaultdict(int)
    nvis = 0
    stat = {W: dict(n=0, exc=0, bad_sync=0, bad_state=0, bad_capped=0) for W in Ws}
    Wmax = max(Ws)
    for _ in range(NORB):
        y = rng.randrange(1 << (BITS - 1), 1 << BITS) | 1
        while y % 3 == 0:
            y = rng.randrange(1 << (BITS - 1), 1 << BITS) | 1
        doors = [y]
        for _ in range(L):
            doors.append(G(doors[-1]))
        letters = [stratum(t) for t in doors]
        for n in range(Wmax, L - 6):
            a = v3(doors[n] + 1)
            nvis += 1
            for j in range(min(a, 12) + 1):
                tail[j] += 1
        for W in Ws:
            mod3 = 3 ** W
            st = stat[W]
            for n in range(Wmax, L - 6):
                st["n"] += 1
                B = offset_from_letters(letters[n - W:n], mod3)
                if doors[n] % mod3 != B % mod3:
                    st["bad_sync"] += 1
                    continue
                w = (B + 1) % mod3
                a_rec = W if w == 0 else v3(w)
                true_om, true_d = state_of_door(doors[n])
                true_state = (true_om % (1 << (k + 2)), min(true_d, D))
                if a_rec >= W:
                    st["exc"] += 1
                    if min(true_d, D) != D:        # W >= D forces the cap to saturate
                        st["bad_capped"] += 1
                    continue
                m_n = letters[n][0]
                mk = 1 << (k + 2)
                q = ((doors[n] + 1) >> m_n) % mk
                om_rec = (q * pow(pow(3, a_rec, mk), -1, mk)) % mk
                if (om_rec, min(m_n + a_rec, D)) != true_state:
                    st["bad_state"] += 1
    return tail, nvis, stat


# ---------------------------------------------------------------------------

def main():
    print("== 1. exact law of W = y3 + 1 mod 3^J (backward recursion, rationals) ==")
    d5 = mu_exact(5)
    t5 = [sum(p for u, p in d5.items() if u % 3 ** j == 0) for j in range(6)]
    for j in range(1, 6):
        print(f"    P(a >= {j}) = {t5[j]} = {float(t5[j]):.8f}")
    check("P(a >= 1) = 1/3 exactly (13.6.5)", t5[1] == Fraction(1, 3))
    check("P(a >= 2) = 2/63 exactly (13.6.5)", t5[2] == Fraction(2, 63))
    check("P(a = 1) = 19/63 exactly (13.6.5)", t5[1] - t5[2] == Fraction(19, 63))
    check("P(a = 0) = 2/3 exactly (13.6.5)", 1 - t5[1] == Fraction(2, 3))
    check("P(a >= 3) ~ 0.0061 (13.6.5)", abs(float(t5[3]) - 0.0061) < 5e-5,
          f"{t5[3]}")

    print("\n== 2. tail to J = 11 (float, r truncated at 90) vs the bounds ==")
    J = 11
    df = mu_float(J)
    tf = [float(df[::3 ** j].sum()) for j in range(J + 1)]
    print(f"  {'j':>3} {'P(a>=j)':>12} {'(1/3)(5/6)^(j-1)':>18} {'2(0.93)^j':>12}"
          f" {'P(a>=j)*3^j':>13}")
    ok_new = ok_old = True
    for j in range(1, J + 1):
        bn, bo = float(Fraction(1, 3) * Fraction(5, 6) ** (j - 1)), 2 * 0.93 ** j
        ok_new &= tf[j] <= bn
        ok_old &= tf[j] <= bo
        print(f"  {j:>3} {tf[j]:>12.4e} {bn:>18.4e} {bo:>12.4e} {tf[j]*3.0**j:>13.4f}")
    check("P(a >= j) <= (1/3)(5/6)^(j-1) at every j <= 11", ok_new)
    check("P(a >= j) <= 2*(0.93)^j at every j <= 11", ok_old)
    check("float tail matches the exact tail for j <= 5",
          max(abs(tf[j] - float(t5[j])) for j in range(6)) < 1e-12,
          f"max |diff| = {max(abs(tf[j]-float(t5[j])) for j in range(6)):.1e}")

    print("\n== 3. max atom Q_t = max_z P(W = z mod 3^t) vs (5/6)^t ==")
    okQ = True
    for t in range(J + 1):
        Q = 1.0 if t == 0 else float(df.reshape(-1, 3 ** t).sum(axis=0).max())
        b = (5 / 6) ** t
        okQ &= Q <= b + 1e-15
        print(f"    t = {t:>2}:  Q_t = {Q:.10f}   (5/6)^t = {b:.10f}   ratio {Q/b:.5f}")
    check("Q_t <= (5/6)^t at every t <= 11", okQ)

    print("\n== 4. Monte Carlo on the composed-affine offsets (independent path) ==")
    for (Jm, N, sd) in ((6, 400000, 51001), (8, 400000, 51002)):
        mc = mc_tail(Jm, N, sd)
        worst = max(abs(mc[j] - tf[j]) / max((tf[j] / N) ** 0.5, 1e-12)
                    for j in range(1, Jm + 1))
        for j in range(1, Jm + 1):
            print(f"    j = {j}:  MC {mc[j]:.6f}   computed {tf[j]:.6f}")
        check(f"MC tail agrees with the computed tail, J = {Jm}, N = {N}, seed {sd}",
              worst < 4.0, f"worst z = {worst:.2f}")

    print("\n== 5/6. real integer orbits ==")
    Ws, k, D = [2, 3, 4, 6, 8], 3, 2
    tail, nvis, stat = orbit_run(52001, 260, 90, 220, Ws, k, D)
    print(f"  {nvis} tallied visits (260 orbits, 220-bit starts, 90 blocks, first 8 dropped)")
    okorb = True
    for j in range(1, 7):
        emp = tail[j] / nvis
        z = abs(emp - tf[j]) / max((tf[j] * (1 - tf[j]) / nvis) ** 0.5, 1e-12)
        okorb &= z < 4.5
        print(f"    j = {j}:  orbit {emp:.6f}   B-hat {tf[j]:.6f}   z = {z:.2f}")
    check("orbit absorption law matches the B-hat tail (j <= 6)", okorb)

    print(f"\n  finite-past reconstruction of (omega mod 2^{k+2}, min(d,{D})):")
    print(f"  {'W':>3} {'visits':>8} {'exc':>6} {'rate':>11} {'P(a>=W)':>11}"
          f" {'sync':>6} {'state':>6} {'capped':>7}")
    ok_rec = ok_rate = True
    for W in Ws:
        s = stat[W]
        rate = s["exc"] / s["n"]
        ok_rec &= (s["bad_sync"] == 0 and s["bad_state"] == 0 and s["bad_capped"] == 0)
        ok_rate &= abs(rate - tf[W]) < 4.5 * (tf[W] / s["n"]) ** 0.5 + 1e-9
        print(f"  {W:>3} {s['n']:>8} {s['exc']:>6} {rate:>11.3e} {tf[W]:>11.3e}"
              f" {s['bad_sync']:>6} {s['bad_state']:>6} {s['bad_capped']:>7}")
    check("reconstruction exact off {a >= W}: 0 sync, 0 state, 0 capped failures", ok_rec)
    check("measured failure rate = P_B-hat(a >= W) at every tested W", ok_rate)

    print("\nFAILURES:", FAILS if FAILS else "none")


if __name__ == "__main__":
    main()
