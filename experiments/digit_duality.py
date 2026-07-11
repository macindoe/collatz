# Forward/reverse digit-consumption duality (probe for the anchor question).
#
# Claim under test: the per-step "digit budget" that makes bounded-window
# determinism impossible FORWARD (stage4.md 11.8.7.7) and the per-step
# "precision loss" that obstructs a stationary residue LP in REVERSE
# (reverse.md 14.13) are the SAME phenomenon, dual under 2<->3.
#
# Both directions form a raw combination, then extract a coprime core by
# dividing out a power of the anchor's own prime:
#   FORWARD: C = 3^d*w - 1 + 2^s ;  w_+ = (C / 2^sigma) / 3^a_+ ;  anchor 2-adic
#            -> to know w_+ mod 2^r you need w mod 2^(sigma + r): sigma digits lost.
#   REVERSE: N = 2^s*y + 1 ;        w' = N / 3^d ;                 anchor 3-adic
#            -> to know w' mod 3^r you need y mod 3^(d + r):       d digits lost.
#
# So loss-per-step = valuation of the raw quantity in the stripped prime:
#   forward  sigma = v2(C) >= 1 always;  reverse  d = v3(N) >= 1 always.
# Fresh implementations; imports nothing from the repo (AGENTS.md house norm).
import random

def v2(x):
    v = 0
    while x % 2 == 0:
        x //= 2; v += 1
    return v

def v3(x):
    v = 0
    while x % 3 == 0:
        x //= 3; v += 1
    return v

# ---------------------------------------------------------------------------
# FORWARD reduced step:  (w, d) -> (w_+, d_+),  and its 2-adic precision law.
# ---------------------------------------------------------------------------
def forward_step(w, d):
    A = 3**d * w - 1
    s = v2(A)
    C = A + (1 << s)
    sigma = v2(C)
    a_plus = v3(C)
    w_plus = (C >> sigma) // 3**a_plus
    d_plus = (sigma - s) + a_plus
    return dict(s=s, sigma=sigma, a_plus=a_plus, w_plus=w_plus, d_plus=d_plus)

def test_forward_precision(trials=6000, r=3, seed=101, d_fixed=7):
    """With the depth coordinate d held FIXED (the forward state is 2-D, unlike
       the reverse door y which is 1-D), w mod 2^(sigma+r) should pin w_+ mod 2^r
       (sigma digits of w lost), and w mod 2^(sigma+r-1) should NOT."""
    random.seed(seed)
    tight = {}      # key at precision sigma+r   -> set of (w_+ mod 2^r)
    loose = {}      # key at precision sigma+r-1 -> set of (w_+ mod 2^r)
    sigmas = []
    for _ in range(trials):
        w = random.randrange(1, 10**7) | 1          # odd
        if w % 3 == 0:
            continue
        d = d_fixed
        st = forward_step(w, d)
        sg, R = st["sigma"], 1 << r
        sigmas.append(sg)
        wp_r = st["w_plus"] % R
        lab = (st["s"], sg, st["a_plus"])
        k_tight = lab + (w % (1 << (sg + r)),)
        k_loose = lab + (w % (1 << (sg + r - 1)),)
        tight.setdefault(k_tight, set()).add(wp_r)
        loose.setdefault(k_loose, set()).add(wp_r)
    tight_conflicts = sum(1 for v in tight.values() if len(v) > 1)
    loose_conflicts = sum(1 for v in loose.values() if len(v) > 1)
    return dict(groups=len(tight), tight_conflicts=tight_conflicts,
                loose_groups=len(loose), loose_conflicts=loose_conflicts,
                sigma_min=min(sigmas), mean_sigma=round(sum(sigmas)/len(sigmas), 3))

# ---------------------------------------------------------------------------
# REVERSE step:  door y, admissible branch s -> predecessor core w', depth d.
# ---------------------------------------------------------------------------
def reverse_step(y, s):
    N = (1 << s) * y + 1
    d = v3(N)
    w = N // 3**d
    return dict(d=d, w=w, N=N)

def admissible_s0(y):
    # branch parity: s odd iff y == 1 mod 3 (so that 3 | N)
    return 1 if y % 3 == 1 else 2

def test_reverse_precision(trials=6000, r=3, seed=202):
    """y mod 3^(d+r) should pin w' mod 3^r (d digits lost), and
       y mod 3^(d+r-1) should NOT (loss is exactly d)."""
    random.seed(seed)
    tight = {}
    loose = {}
    ds = []
    for _ in range(trials):
        y = random.randrange(1, 10**7)
        if y % 3 == 0:
            continue
        s0 = admissible_s0(y)
        s = s0 + 2 * random.randrange(0, 4)       # admissible branch
        st = reverse_step(y, s)
        d, R = st["d"], 3**r
        if d == 0:
            return dict(error="d=0 encountered (should be impossible for admissible s)")
        ds.append(d)
        wp_r = st["w"] % R
        lab = (s, d)
        k_tight = lab + (y % 3**(d + r),)
        k_loose = lab + (y % 3**(d + r - 1),)
        tight.setdefault(k_tight, set()).add(wp_r)
        loose.setdefault(k_loose, set()).add(wp_r)
    tight_conflicts = sum(1 for v in tight.values() if len(v) > 1)
    loose_conflicts = sum(1 for v in loose.values() if len(v) > 1)
    return dict(groups=len(tight), tight_conflicts=tight_conflicts,
                loose_groups=len(loose), loose_conflicts=loose_conflicts,
                d_min=min(ds), mean_d=round(sum(ds)/len(ds), 3))

if __name__ == "__main__":
    print("FORWARD 2-adic precision law  (loss per step = sigma = v2(C), d held fixed):")
    f = None
    for dfx in (5, 7, 12):
        f = test_forward_precision(d_fixed=dfx)
        print(f"   d={dfx:2d}:", f)
    print("   -> w mod 2^(sigma+r) pins w_+ mod 2^r:", f["tight_conflicts"] == 0,
          "| dropping one digit breaks it:", f["loose_conflicts"] > 0)

    print("REVERSE 3-adic precision law  (loss per step = d = v3(N)):")
    g = test_reverse_precision()
    print("  ", g)
    print("   -> y mod 3^(d+r) pins w' mod 3^r:", g["tight_conflicts"] == 0,
          "| dropping one digit breaks it:", g["loose_conflicts"] > 0)

    print("\nDuality: both strip a power of the anchor's own prime each step;")
    print("loss = that exponent, always >= 1 -> no bounded-precision iterate either way.")
    print(f"  forward mean sigma (2-adic digits/step) = {f['mean_sigma']}, min = {f['sigma_min']}")
    print(f"  reverse mean d     (3-adic digits/step) = {g['mean_d']}, min = {g['d_min']}")
