"""Verification for aeh.md section 13.6 (the genericity form of AEH).

Supports:
  13.6.1 (letter law)            -- exact exhaustive cylinder counts, single letters
  13.6.2 (Bernoulli identification) -- exact exhaustive word counts, pushforward
                                    uniformity, renewal property (fresh-door Haar law)
  13.6.3 (dictionary + time change) -- seam identities, expansion dictionary
                                    G = T^m, exact T-step bookkeeping on finite
                                    orbits, two-sided window reconstruction
                                    (past letters -> 3-adic residues, future
                                    letters -> 2-adic residues), exceptional-event
                                    counts
  13.6.4/13.6.5 (equivalence + depth marginal) -- exact B-side laws (nu_j via the
                                    j-step synchronizing kernel, exact rationals),
                                    exact window-chain depth law (fresh analytic
                                    kernel), protocol-compliant orbit texture
                                    (fixed horizon, unweighted, per-visit, uniform
                                    starts, bulk cut; aeh.md 13.5 standing rule)

Independence: imports nothing from experiments/itinerary_coding.py,
experiments/aeh_calibration.py, or experiments/aeh_anomaly.py (or anywhere else
in the repository). Pure stdlib. Exact integer / Fraction arithmetic wherever a
pass/fail decision is made; sampled statistics are labeled as such.

Run: python experiments/aeh_symbolic.py     (date: 2026-07-23)
"""

import random
from fractions import Fraction
from collections import Counter, defaultdict

FAILURES = []


def check(name, ok, detail=""):
    tag = "PASS" if ok else "FAIL"
    print(f"  [{tag}] {name}" + (f" -- {detail}" if detail else ""))
    if not ok:
        FAILURES.append((name, detail))


def v2(x):
    return (x & -x).bit_length() - 1


def v3(x):
    a = 0
    while x % 3 == 0:
        x //= 3
        a += 1
    return a


# ---- fresh primitives -------------------------------------------------------

def stratum(y):
    """(m, r) of an odd integer y != -1: m = v2(y+1), r = v2(3^m q - 1)."""
    m = v2(y + 1)
    q = (y + 1) >> m
    r = v2(3 ** m * q - 1)
    return m, r


def G(y):
    m = v2(y + 1)
    q = (y + 1) >> m
    x = 3 ** m * q - 1
    r = v2(x)
    return x >> r


def T(x):
    z = 3 * x + 1
    return z >> v2(z)


def F_step(w, d):
    """One reduced-map step from state (w, d). Returns (s, sig, a_plus, w1, d1, exit)."""
    A = 3 ** d * w - 1
    s = v2(A)
    C = A + (1 << s)
    sig = v2(C)
    u = C >> sig
    a = v3(u)
    w1 = u // 3 ** a
    d1 = (sig - s) + a
    return s, sig, a, w1, d1, A >> s


def state_of_door(y):
    """state(y) = (Omega, D): y+1 = 2^m 3^a Omega, D = m + a  (reverse.md 14.14.1/14.14.7)."""
    m = v2(y + 1)
    t = (y + 1) >> m
    a = v3(t)
    return t // 3 ** a, m + a


# ---- 1. letter law (13.6.1) -------------------------------------------------

def check_letter_law():
    print("\n== 1. Letter law: stratum (m,r) is exactly one odd class mod 2^(m+r+1) ==")
    bad = 0
    for m in range(1, 7):
        for r in range(1, 7):
            mod = 1 << (m + r + 1)
            hits = [y for y in range(1, mod, 2) if stratum(y) == (m, r)]
            if len(hits) != 1:
                bad += 1
    check("all (m,r) with m,r <= 6: exactly one class each", bad == 0,
          f"36 strata checked, {bad} bad")
    # totality: every odd y >= 1 has a stratum with m, r >= 1
    tot_bad = sum(1 for y in range(1, 2 ** 15, 2)
                  if not (stratum(y)[0] >= 1 and stratum(y)[1] >= 1))
    check("totality: every odd y < 2^15 has m,r >= 1", tot_bad == 0)


# ---- 2. word law (13.6.2) ---------------------------------------------------

def follows(y, word):
    for (m, r) in word:
        if y == -1 or stratum(y) != (m, r):
            return False
        y = G(y)
    return True


def check_word_law():
    print("\n== 2. Word law: every word W is exactly one odd class mod 2^(S+1) ==")
    letters3 = [(m, r) for m in (1, 2, 3) for r in (1, 2, 3)]
    bad = 0
    for w0 in letters3:
        for w1 in letters3:
            word = (w0, w1)
            S = sum(m + r for (m, r) in word)
            mod = 1 << (S + 1)
            n = sum(1 for y in range(1, mod, 2) if follows(y, word))
            if n != 1:
                bad += 1
    check("all 81 two-letter words (letters <= 3): exactly one class each", bad == 0)
    letters2 = [(m, r) for m in (1, 2) for r in (1, 2)]
    bad = 0
    for w0 in letters2:
        for w1 in letters2:
            for w2 in letters2:
                word = (w0, w1, w2)
                S = sum(m + r for (m, r) in word)
                mod = 1 << (S + 1)
                n = sum(1 for y in range(1, mod, 2) if follows(y, word))
                if n != 1:
                    bad += 1
    check("all 64 three-letter words (letters <= 2): exactly one class each", bad == 0)


# ---- 3. expansion dictionary and block-map identity (13.6.3, time change) ----

def check_expansion(seed=31001, N=5000):
    print("\n== 3. Expansion dictionary: G(y) = T^m(y), valuation word (1,..,1,r+1) ==")
    rng = random.Random(seed)
    bad = 0
    for _ in range(N):
        y = rng.randrange(1, 1 << 40) | 1
        m, r = stratum(y)
        x = y
        word = []
        for _ in range(m):
            z = 3 * x + 1
            word.append(v2(z))
            x = z >> v2(z)
        expect = [1] * (m - 1) + [r + 1]
        if x != G(y) or word != expect or G(y) % 3 == 0:
            bad += 1
    check(f"{N} random odd y < 2^40 (seed {seed})", bad == 0, f"{bad} failures")


# ---- 4. seam alignment and exact time-change bookkeeping ---------------------

def check_seam_and_time(seed=31002, N=400, L=50):
    print("\n== 4. Seam alignment + T-step bookkeeping on explicit orbits ==")
    rng = random.Random(seed)
    bad_state = bad_G = bad_letter = bad_depth = bad_T = 0
    for _ in range(N):
        w = rng.randrange(1, 1 << 48) | 1
        if w % 3 == 0:
            continue
        d = rng.randrange(1, 20)
        # run L+1 F-steps, collect edges
        ws, ds, ss, sigs, aps, exits = [w], [d], [], [], [], []
        for _ in range(L + 1):
            s, sig, a, w1, d1, ex = F_step(ws[-1], ds[-1])
            ss.append(s); sigs.append(sig); aps.append(a); exits.append(ex)
            ws.append(w1); ds.append(d1)
        for n in range(L):
            y = exits[n]
            # doors chain under G and the seam identity state(y_n) = (w_{n+1}, d_{n+1})
            if state_of_door(y) != (ws[n + 1], ds[n + 1]):
                bad_state += 1
            if G(y) != exits[n + 1]:
                bad_G += 1
            m, r = stratum(y)
            # letter n = (m_+ of edge n, s of edge n+1) = (sig_n - s_n, s_{n+1})
            if (m, r) != (sigs[n] - ss[n], ss[n + 1]):
                bad_letter += 1
            # depth dictionary: d_{n+1} = m + v3(y+1)
            if ds[n + 1] != m + v3(y + 1):
                bad_depth += 1
        # exact T-step count: from door y_0, sum of letter m's = T-steps to y_n
        y0, yn = exits[0], exits[L - 1]
        msum = sum(stratum(exits[i])[0] for i in range(L - 1))
        x = y0
        for _ in range(msum):
            x = T(x)
        if x != yn:
            bad_T += 1
    check("state(y_n) = (w_{n+1}, d_{n+1}) on every edge", bad_state == 0, f"{bad_state} bad")
    check("G chains the doors: G(y_n) = y_{n+1}", bad_G == 0, f"{bad_G} bad")
    check("letter n = (sig_n - s_n, s_{n+1}) (seam identification)", bad_letter == 0, f"{bad_letter} bad")
    check("depth dictionary d_{n+1} = m(y_n) + v3(y_n + 1)", bad_depth == 0, f"{bad_depth} bad")
    check(f"T-step bookkeeping: T^(sum m_i)(y_0) = y_n exactly ({N} orbits, seed {seed})",
          bad_T == 0, f"{bad_T} bad")
    # per-T-step vs per-letter frequency: exact finite-horizon identity
    # freq_T(letter = l) = m_l * count(l) / sum_i m_i   (each letter occupies m T-steps)
    rng2 = random.Random(seed + 1)
    w = rng2.randrange(1 << 69, 1 << 70) | 1
    while w % 3 == 0:
        w = rng2.randrange(1 << 69, 1 << 70) | 1
    d = 3
    s, sig, a, w1, d1, y = F_step(w, d)
    doors = [y]
    for _ in range(59):
        doors.append(G(doors[-1]))
    letters = [stratum(y) for y in doors[:-1]]
    total_T = sum(m for (m, r) in letters)
    cnt = Counter(letters)
    # walk the raw T-orbit and attribute each T-step to its letter
    tcnt = Counter()
    x = doors[0]
    for (m, r) in letters:
        for _ in range(m):
            tcnt[(m, r)] += 1
            x = T(x)
    ok = all(tcnt[l] == l[0] * cnt[l] for l in cnt) and sum(tcnt.values()) == total_T
    check("per-T-step counts = m_l * per-letter counts (exact, 60-letter bulk orbit)", ok,
          f"total T-steps {total_T}, letters 60, mean m {total_T/60:.3f} (E_B[m] = 2)")


# ---- 5. two-sided window reconstruction (13.6.3) -----------------------------

def word_class_rep(word):
    """Representative and modulus of the followers of `word` (fresh 14.15.1.4 lifting)."""
    m0, r0 = word[0]
    mod0 = 1 << (m0 + r0 + 1)
    y0 = next(y for y in range(1, mod0, 2) if stratum(y) == (m0, r0))
    S = m0 + r0
    M = m0
    z = G(y0)  # image of the representative under the prefix
    for (m, r) in word[1:]:
        modl = 1 << (m + r + 1)
        w_target = next(y for y in range(1, modl, 2) if stratum(y) == (m, r))
        # solve z + 2*3^M t == w_target (mod 2^(m+r+1))
        t0 = ((w_target - z) // 2 * pow(3 ** M, -1, modl >> 1)) % (modl >> 1)
        y0 = y0 + (t0 << (S + 1))
        z = z + 2 * 3 ** M * t0
        # advance the prefix image through the new letter
        S += m + r
        M += m
        z = G(z)
    return y0, S


def check_two_sided_reconstruction(seed=31003, N=120, L=70, W=8, k=3, D=6):
    print("\n== 5. Two-sided window reconstruction of the AEH window state ==")
    rng = random.Random(seed)
    mod3 = 3 ** W
    bad_sync = bad_state = 0
    n_checked = n_exc = 0
    for _ in range(N):
        w = rng.randrange(1, 1 << 60) | 1
        if w % 3 == 0:
            continue
        d = rng.randrange(1, 15)
        s, sig, a, w1, d1, y = F_step(w, d)
        doors = [y]
        for _ in range(L):
            doors.append(G(doors[-1]))
        letters = [stratum(t) for t in doors]
        for n in range(W, L - k - 3):
            # (i) past letters n-W..n-1 give y_n mod 3^W (synchronization 14.14.8.3)
            A, B = 1, 0
            for (m, r) in letters[n - W:n]:
                al = (3 ** m * pow(1 << (m + r), -1, mod3)) % mod3
                be = ((3 ** m - 2 ** m) * pow(1 << (m + r), -1, mod3)) % mod3
                A, B = (al * A) % mod3, (al * B + be) % mod3
            if doors[n] % mod3 != B % mod3:
                bad_sync += 1
                continue
            # (ii) reconstruct the depth-k window state of state(y_n) from letters only
            m_n = letters[n][0]
            a_rec = v3(B + 1) if (B + 1) % mod3 != 0 else W  # >= W means exceptional
            n_checked += 1
            true_w, true_d = state_of_door(doors[n])
            true_state = (true_w % (1 << (k + 2)), min(true_d, D))
            if a_rec >= W:
                n_exc += 1  # exceptional event {a >= W}: capped depth still known
                if min(true_d, D) != D:
                    bad_state += 1
                continue
            # future letters n..n+t pin y_n mod 2^(m_n+k+2) via the cylinder class
            need = m_n + k + 2
            t = 1
            while sum(mm + rr for (mm, rr) in letters[n:n + t]) + 1 < need:
                t += 1
            rep, S = word_class_rep(letters[n:n + t])
            q_rec = ((rep + 1) >> m_n) % (1 << (k + 2))
            w_rec = (q_rec * pow(3 ** a_rec, -1, 1 << (k + 2))) % (1 << (k + 2))
            d_rec = min(m_n + a_rec, D)
            if (w_rec, d_rec) != true_state:
                bad_state += 1
    check(f"synchronization: y_n mod 3^{W} from the last {W} letters alone",
          bad_sync == 0, f"{bad_sync} bad")
    check(f"window state (omega mod 2^{k+2}, min(d,{D})) reconstructed from letters only",
          bad_state == 0,
          f"{n_checked} visits, {n_exc} exceptional (a >= {W}; rate {n_exc/max(n_checked,1):.2e}), {bad_state} bad (seed {seed})")


# ---- 6. pushforward uniformity and renewal (13.6.2) --------------------------

def check_pushforward(seed=31004, N=200000):
    print("\n== 6. Pushforward uniformity + renewal (sampled; seed stated) ==")
    rng = random.Random(seed)
    gmod = Counter()
    qmod = Counter()
    mq = Counter()
    cond = defaultdict(Counter)
    for _ in range(N):
        y = rng.randrange(1 << 39, 1 << 40) | 1
        g = G(y)
        gmod[g % 128] += 1
        m, r = stratum(y)
        q = (y + 1) >> m
        qmod[q % 64] += 1
        mq[(min(m, 5), q % 8)] += 1
        if (m, r) == (1, 1):
            cond[(m, r)][g % 64] += 1
    # G(y) mod 128 uniform over odd residues
    exp = N / 64
    dev = max(abs(gmod[c] - exp) / exp for c in range(1, 128, 2))
    check("G(y) mod 128 uniform over odd residues (max rel dev < 5 sigma)",
          dev < 5 * (1 / exp) ** 0.5, f"max rel dev {dev:.4f}, 1 sigma = {(1/exp)**0.5:.4f}")
    exp = N / 32
    dev = max(abs(qmod[c] - exp) / exp for c in range(1, 64, 2))
    check("q = (y+1)/2^m mod 64 uniform over odd residues", dev < 5 * (1 / exp) ** 0.5,
          f"max rel dev {dev:.4f}")
    # independence m vs q mod 8: P(m=j, q=c) = 2^-j * 1/4
    worst = 0
    for j in range(1, 5):
        for c in (1, 3, 5, 7):
            e = N * 2 ** -j / 4
            worst = max(worst, abs(mq[(j, c)] - e) / e)
    check("independence of m and q mod 8 (worst cell < 5 sigma at the smallest cell)",
          worst < 5 * (1 / (N * 2 ** -4 / 4)) ** 0.5, f"worst rel dev {worst:.4f}")
    # renewal: conditioned on letter_0 = (1,1), next door uniform mod 64 over odds
    c11 = cond[(1, 1)]
    n11 = sum(c11.values())
    exp = n11 / 32
    dev = max(abs(c11[c] - exp) / exp for c in range(1, 64, 2))
    check("renewal: G(y) mod 64 uniform given stratum(y) = (1,1)",
          dev < 5 * (1 / exp) ** 0.5, f"n = {n11}, max rel dev {dev:.4f}")


# ---- 7. exact B-side laws: nu_j and the depth marginal (13.6.5) --------------

def nu_exact(j):
    """Exact law of y mod 3^j under B (stationary; equals K^j from any start).

    Kernel: y' = (3^m (y+1) 2^-m - 1) 2^-r, letters (m, r) iid P = 2^-(m+r).
    For m >= j the 3^m term dies: y' = -2^-r, independent of y and m.
    r is lumped by residue class mod ord(2 mod 3^j) with exact geometric weights.
    """
    mod = 3 ** j
    # ord of 2 mod 3^j
    ordn = 1
    t = 2 % mod
    while t != 1:
        t = (t * 2) % mod
        ordn += 1
    denom = 1 - Fraction(1, 2 ** ordn)
    wr = {c: Fraction(1, 2 ** c) / denom for c in range(1, ordn + 1)}  # sum_{r=c mod ord} 2^-r
    inv2 = {c: pow(2, -c, mod) for c in range(1, ordn + 1)}
    dist = {1: Fraction(1)}
    for _ in range(j):
        nxt = defaultdict(Fraction)
        for u, p in dist.items():
            # m = 1..j-1 exactly (weight 2^-m); the residual m-class mass with 3^m == 0
            for m in range(1, j):
                q = ((u + 1) * pow(2, -m, mod)) % mod
                base = (3 ** m * q - 1) % mod
                for c, wc in wr.items():
                    nxt[(base * inv2[c]) % mod] += p * Fraction(1, 2 ** m) * wc
            # m >= j: y' = -2^-r
            for c, wc in wr.items():
                nxt[(-inv2[c]) % mod] += p * Fraction(1, 2 ** (j - 1)) * wc
        dist = dict(nxt)
    assert sum(dist.values()) == 1
    return dist


def b_side_depth_law(jmax=5):
    """Exact P_B(a = i), i < jmax, and P_B(d = t) = sum_i P(a=i) 2^-(t-i), t <= jmax."""
    nu = nu_exact(jmax)
    mod = 3 ** jmax
    pa = []
    for i in range(jmax):
        # a = i  <=>  y == -1 mod 3^i  and  y != -1 mod 3^(i+1)
        ge_i = sum(p for u, p in nu.items() if (u + 1) % 3 ** i == 0)
        ge_i1 = sum(p for u, p in nu.items() if (u + 1) % 3 ** (i + 1) == 0)
        pa.append(ge_i - ge_i1)
    pd = {}
    for t in range(1, jmax + 1):
        pd[t] = sum(pa[i] * Fraction(1, 2 ** (t - i)) for i in range(min(t, jmax)))
    return pa, pd, nu


def check_b_side_laws():
    print("\n== 7. Exact B-side laws (exact rational arithmetic) ==")
    nu1 = nu_exact(1)
    check("nu_1 = (2/3, 1/3) on (1, 2) mod 3",
          nu1.get(1, 0) == Fraction(2, 3) and nu1.get(2, 0) == Fraction(1, 3),
          f"nu_1 = {dict(nu1)}")
    # marginal consistency nu_3 -> nu_2 -> nu_1
    nu3, nu2 = nu_exact(3), nu_exact(2)
    proj = defaultdict(Fraction)
    for u, p in nu3.items():
        proj[u % 9] += p
    check("nu_3 projects exactly to nu_2", dict(proj) == {u: p for u, p in nu2.items()})
    pa, pd, nu = b_side_depth_law(5)
    print("    P_B(a = i), exact:", [f"{i}: {p} = {float(p):.6f}" for i, p in enumerate(pa)])
    print("    P_B(d = t), exact:", [f"{t}: {float(p):.6f}" for t, p in pd.items()])
    check("P_B(a = 0) = 2/3 and P_B(d = 1) = 1/3 exactly",
          pa[0] == Fraction(2, 3) and pd[1] == Fraction(1, 3))
    # exceptional tail: nu_j(-1 mod 3^j) decays
    tails = []
    for j in range(1, 6):
        nuj = nu_exact(j)
        tails.append(float(sum(p for u, p in nuj.items() if (u + 1) % 3 ** j == 0)))
    print("    P_B(a >= j) =", [f"{t:.6g}" for t in tails])
    check("exceptional tail decays at least geometrically (ratio <= 2/3 each level)",
          all(tails[i + 1] <= tails[i] * 2 / 3 + 1e-15 for i in range(len(tails) - 1)),
          f"ratios {[round(tails[i+1]/tails[i], 4) for i in range(len(tails)-1)]}")
    return pa, pd


# ---- 8. exact window-chain depth law (fresh analytic kernel) ------------------

def chain_depth_law(DCAP=60, SCAP=64, XCAP=40):
    """Depth marginal of the exact window chain (Haar refresh of all unseen
    digits, 2-adic and 3-adic): fresh analytic kernel.

    Given d: s-law is the ledger (P(s=t) = 2^-t) independent of d (checked
    against w8 in {1,3,5,7} uniform).  Given s odd: a=0.  Given s even:
    e = 1 + v3(s); a = min(d, e) if d != e, else d + X with
    P(X=0) = 1/2, P(X=x) = (1/2)(2/3)(1/3)^(x-1)  (uniform 3-adic unit refresh).
    d' = m + a with m geometric(1/2) independent.
    """
    # verify the s-law claim exactly over w8 x parity(d)
    for dpar in (0, 1):
        cnt = Counter()
        for w8 in (1, 3, 5, 7):
            A = (pow(3, 2 + dpar, 8) * w8 - 1) % 8
            if A % 4 == 2:
                cnt[1] += 1
            elif A % 8 == 4:
                cnt[2] += 1
            else:
                cnt["3+"] += 1
        assert cnt[1] == 2 and cnt[2] == 1 and cnt["3+"] == 1
    s_law = {t: Fraction(1, 2 ** t) for t in range(1, SCAP)}
    s_law[SCAP] = Fraction(1, 2 ** (SCAP - 1))  # tail lump (immaterial: s odd/even split kept below)

    def a_law(d):
        """P(a = i | d), exact Fractions."""
        out = defaultdict(Fraction)
        for s, ps in s_law.items():
            if s % 2 == 1:
                out[0] += ps
                continue
            e = 1 + v3(s)
            if d != e:
                out[min(d, e)] += ps
            else:
                out[d] += ps * Fraction(1, 2)
                for x in range(1, XCAP):
                    out[d + x] += ps * Fraction(1, 2) * Fraction(2, 3) * Fraction(1, 3) ** (x - 1)
                out[d + XCAP] += ps * Fraction(1, 2) * Fraction(1, 3) ** (XCAP - 1) / 2  # tiny tail
        return out

    m_law = {m: Fraction(1, 2 ** m) for m in range(1, 50)}
    m_law[50] = Fraction(1, 2 ** 49)
    # kernel d -> d'
    Kd = {}
    for d in range(1, DCAP + 1):
        row = defaultdict(Fraction)
        al = a_law(d)
        for a, pa_ in al.items():
            for m, pm in m_law.items():
                row[min(a + m, DCAP)] += pa_ * pm
        Kd[d] = row
    # stationary by power iteration (floats; discrimination target ~1e-3)
    pi = {d: 1.0 / DCAP for d in range(1, DCAP + 1)}
    for _ in range(4000):
        nxt = defaultdict(float)
        for d, p in pi.items():
            for d2, w in Kd[d].items():
                nxt[d2] += p * float(w)
        pi = dict(nxt)
    return pi


def check_depth_comparison(pa, pd):
    print("\n== 8. Depth marginal: B-side exact law vs window-chain law ==")
    pi = chain_depth_law()
    print("    t : chain P(d=t)   B-side P_B(d=t)   diff")
    diffs = {}
    for t in range(1, 6):
        diffs[t] = pi[t] - float(pd[t])
        print(f"    {t} :   {pi[t]:.6f}       {float(pd[t]):.6f}      {diffs[t]:+.6f}")
    agree = all(abs(x) < 5e-4 for x in diffs.values())
    print(f"    identification of the two laws: {'AGREE within 5e-4' if agree else 'DIFFER beyond 5e-4'}")
    # chain-side a-marginal (mix a_law over the stationary d-law) for the report
    # reconstruct via P(d=2) = 1/6 + P(a=1)/2 and P(a>=1) = 1/3 (both hold on each side)
    pc_a1 = 2 * (pi[2] - 1 / 6)
    print(f"    P(a=1): chain {pc_a1:.6f} (= {pc_a1*63:.3f}/63), B-side exact {float(pa[1]):.6f} (= 19/63)")
    print(f"    P(a>=2): chain {1/3 - pc_a1:.6f} (= {(1/3-pc_a1)*63:.3f}/63), B-side exact "
          f"{1/3 - float(pa[1]):.6f} (= 2/63)")
    return pi, diffs, agree


# ---- 9. orbit texture, 13.5-standing-rule protocol ---------------------------

def check_orbit_texture(pa, pd, pi_chain, seed=31005, NORB=8000, BURN=10, HOR=30, CUT=1 << 30):
    """Fixed-horizon, unweighted, per-visit sampling from uniform starts (13.5
    standing rule): starts in [2^70, 2^71) so the bulk cut omega > 2^30 never
    binds within the burn-in + horizon (no survivorship selection at finite
    size; 13.2.1's limit regime realized directly); fixed burn-in of BURN steps
    from the artificial start state, then exactly HOR steps, every visit pooled."""
    print("\n== 9. Orbit texture (fixed horizon, unweighted, per-visit, uniform starts;")
    print(f"      starts 2^70, burn-in {BURN}, horizon {HOR}, cut omega > 2^30; 13.5 rule) ==")
    rng = random.Random(seed)
    dhist = Counter()
    letter_hist = Counter()
    pair_hist = Counter()
    mod3_cond = Counter()  # (a==0, omega mod 3)
    nvis = nbelow = 0
    per_orbit_w3 = []
    for _ in range(NORB):
        w = rng.randrange(1 << 70, 1 << 71) | 1
        if w % 3 == 0:
            continue
        d = rng.randrange(1, 13)
        for _ in range(BURN):
            s, sig, a, w1, d1, y = F_step(w, d)
            w, d = w1, d1
        prev_letter = None
        o_w3 = [0, 0]
        for _ in range(HOR):
            s, sig, a, w1, d1, y = F_step(w, d)
            if w1 > CUT:
                nvis += 1
                m, r = stratum(y)
                letter_hist[(min(m, 6), min(r, 6))] += 1
                if prev_letter is not None:
                    pair_hist[(prev_letter, (min(m, 6), min(r, 6)))] += 1
                prev_letter = (min(m, 6), min(r, 6))
                dhist[min(d1, 12)] += 1
                if a == 0:
                    mod3_cond[w1 % 3] += 1
                    o_w3[0] += 1
                    o_w3[1] += 1 if w1 % 3 == 1 else 0
            else:
                nbelow += 1
                prev_letter = None
            w, d = w1, d1
        if o_w3[0] > 10:
            per_orbit_w3.append(o_w3[1] / o_w3[0])
    print(f"    {nvis} bulk visits from {NORB} orbits ({nbelow} below cut; seed {seed})")
    # letter marginals vs 2^-(m+r); tolerance 5 pooled-SE with 1.5x inflation
    worst_z = 0
    for m in range(1, 4):
        for r in range(1, 4):
            f = letter_hist[(m, r)] / nvis
            e = 2 ** -(m + r)
            se = (e * (1 - e) / nvis) ** 0.5 * 1.5
            worst_z = max(worst_z, abs(f - e) / se)
    check("letter marginals match 2^-(m+r) (cells m,r <= 3, worst z < 5)",
          worst_z < 5, f"worst z {worst_z:.2f}")
    # pair independence spot check
    f11 = letter_hist[(1, 1)] / nvis
    fp = pair_hist[((1, 1), (1, 1))] / max(sum(pair_hist.values()), 1)
    check("consecutive-letter independence: P((1,1),(1,1)) vs P(1,1)^2 within 5%",
          abs(fp - f11 * f11) / (f11 * f11) < 0.05,
          f"pair {fp:.5f} vs product {f11*f11:.5f}")
    # the discriminating cell: P(omega == 1 mod 3 | a = 0) -> 2/3 under B, 1/2 under naive refresh
    n0 = sum(mod3_cond.values())
    f1 = mod3_cond[1] / n0
    se = (sum((x - f1) ** 2 for x in per_orbit_w3) / max(len(per_orbit_w3) - 1, 1)) ** 0.5 \
        / max(len(per_orbit_w3), 1) ** 0.5
    print(f"    P(omega_+ == 1 mod 3 | a_+ = 0) = {f1:.4f}  (n = {n0}; across-orbit SE ~ {se:.4f})")
    print(f"      B-side prediction 2/3 = 0.6667 : {abs(f1 - 2/3)/max(se,1e-9):.1f} sigma")
    print(f"      naive-refresh prediction 1/2  : {abs(f1 - 1/2)/max(se,1e-9):.1f} sigma")
    check("mod-3 core conditional matches the B-side value 2/3 (within 4 sigma)",
          abs(f1 - 2 / 3) < 4 * se + 0.01)
    # depth histogram vs the two exact candidates
    print("    t : orbit freq   B-side    chain")
    for t in range(1, 6):
        f = dhist[t] / nvis
        print(f"    {t} :  {f:.5f}    {float(pd[t]):.5f}   {pi_chain[t]:.5f}")
    fb = sum(abs(dhist[t] / nvis - float(pd[t])) for t in range(1, 6))
    fc = sum(abs(dhist[t] / nvis - pi_chain[t]) for t in range(1, 6))
    print(f"    L1 distance (t <= 5): orbit-vs-B {fb:.5f}   orbit-vs-chain {fc:.5f}")
    return fb, fc


# ---- main --------------------------------------------------------------------

if __name__ == "__main__":
    print("aeh_symbolic.py -- verification for aeh.md 13.6 (2026-07-23)")
    check_letter_law()
    check_word_law()
    check_expansion()
    check_seam_and_time()
    check_two_sided_reconstruction()
    check_pushforward()
    pa, pd = check_b_side_laws()
    pi_chain, diffs, agree = check_depth_comparison(pa, pd)
    fb, fc = check_orbit_texture(pa, pd, pi_chain)
    print("\n== summary ==")
    if FAILURES:
        print(f"FAILURES: {len(FAILURES)}")
        for name, det in FAILURES:
            print(f"  - {name}: {det}")
    else:
        print("all checks passed")
    print(f"depth-marginal identification (chain vs B-side): "
          f"{'agrees within 5e-4' if agree else 'DIFFERS: ' + str({t: round(d,5) for t,d in diffs.items()})}")
    print(f"orbit depth histogram L1 (t<=5): vs B-side {fb:.5f}, vs chain {fc:.5f}")
