# Steering laws (reverse.md 14.12 / paper 2 sec 7):
# (ii) 2-adic freeze: omega = 3^(-d) mod 2^min(s,k)
# (iii) placement: M(omega) = d mod 2^(s-2), sharp (M(3) = N(9) = -1)
import random
def v2(x):
    v=0
    while x%2==0: x//=2; v+=1
    return v
def v3(x):
    v=0
    while x%3==0: x//=3; v+=1
    return v
def N_mod(u,k):
    n=0
    for j in range(k):
        m=1<<(j+4)
        if pow(9,n,m)!=pow(u%m,-1,m): n+=1<<j
    return n
if __name__=="__main__":
    K=20
    assert N_mod(9,K)==2**K-1, "M(3)=N(9)=-1"
    random.seed(163); bad_f=bad_p=n=0; sharp=0
    for _ in range(3000):
        y=random.randrange(1,10**4,2)
        if y%3==0: continue
        s0=1 if y%3==1 else 2
        s=s0+2*random.randrange(2,40)
        if s<3: continue
        N=(1<<s)*y+1
        d=v3(N); w=N//3**d
        if w%3==0: continue
        n+=1
        k=min(s,16)
        if (w-pow(3,-d,1<<k))%(1<<k): bad_f+=1
        dep=min(s-2,K)
        Mw=N_mod((w*w)%(1<<(K+5)) if w>(1<<(K+5)) else w*w, K)
        diff=(Mw-d)%(1<<K)
        if diff%(1<<dep): bad_p+=1
        if dep<K and diff and v2(diff)==dep: sharp+=1
    print(f"freeze: {n} checks, {bad_f} failures; placement: {bad_p} failures; sharpness attained in {sharp} cases")
