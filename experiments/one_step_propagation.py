# One-step displacement propagation (stage4.md 11.8.7.6): window-only decision
# procedure for the NEXT exit valuation s_+ (hence next 3-gain).
# Window: w mod 2^(sigma+k+2), d mod 2^(sigma+k); stratum labels (s, sigma, a_+).
# Claims verified:
#   (1) decided cases give s_+ EXACTLY (zero errors)
#   (2) undecided  <=>  next state lifting AND eps_+ = 0 mod 2^k; then true s_+ >= k+2
#   (3) undecided rate ~ 2^-k along real orbits
import random
def v2(x): return (x & -x).bit_length() - 1
def v3(x):
    v = 0
    while x % 3 == 0: x //= 3; v += 1
    return v
def N_mod(u, k):
    n = 0
    for j in range(k):
        m = 1 << (j + 4)
        if pow(9, n, m) != pow(u % m, -1, m): n += 1 << j
    return n
def M_mod(w, k): return N_mod((w * w) % (1 << (k + 4)), k)

S1_CLASSES = {(1, 1), (5, 1), (7, 0), (3, 0)}   # (w mod 8, d mod 2) -> s = 1
def decide(rw, rd, s, sigma, ap, k):
    """window-only; returns ('s+', value) or ('deep', k+2 lower bound)"""
    Q = sigma + k + 2; MQ = 1 << Q
    Chat = (pow(3, rd, MQ) * rw - 1 + (1 << s)) % MQ
    r = k + 2; Mr = 1 << r
    wp_hat = ((Chat >> sigma) * pow(pow(3, ap % (1 << k), Mr), -1, Mr)) % Mr
    dp = sigma - s + ap                              # exact
    cls = (wp_hat % 8, dp % 2)
    lifting = cls in {(1, 0), (3, 1)}
    if not lifting:
        return ('s+', 1 if cls in S1_CLASSES else 2)
    eps = (dp - M_mod(wp_hat, k)) % (1 << k)
    if eps != 0: return ('s+', 2 + v2(eps))
    return ('deep', k + 2)

random.seed(17)
for k in (4, 8):
    dec = und = err = 0; deep_viol = 0
    for _ in range(400):
        w = random.randrange(1, 10**6, 2)
        if w % 3 == 0: continue
        d = random.randrange(1, 25)
        for _ in range(50):
            A = 3**d * w - 1; s = v2(A); C = A + (1 << s)
            sigma = v2(C); ap = v3(C)
            wp = (C >> sigma) // 3**ap; dp = sigma - s + ap
            true_sp = v2(3**dp * wp - 1)
            verdict, val = decide(w % (1 << (sigma+k+2)), d % (1 << (sigma+k)), s, sigma, ap, k)
            if verdict == 's+':
                dec += 1
                if val != true_sp: err += 1
            else:
                und += 1
                if true_sp < k + 2: deep_viol += 1
            w, d = wp, dp
            if (w, d) == (1, 1): break
    tot = dec + und
    print(f"k={k}: {tot} steps | decided {dec} with {err} errors | "
          f"undecided {und} ({und/tot:.4f}, heuristic ~{2**-k:.4f}) | "
          f"deep-bound violations {deep_viol}")
