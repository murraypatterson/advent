
import sys
from collections import defaultdict

def get_pairs(t) :

    ps = defaultdict(int)
    for i in range(len(t)-1) :
        p = t[i:i+2]
        ps[p] += 1

    return ps, t[0], t[-1]

def load_rules(lines) :

    rs = {}
    for line in lines :
        line = line.strip()

        if not line :
            continue

        a, _, b = line.split()
        rs[a] = b

    return rs

def apply_rules(rs, ps) :

    qs = defaultdict(int)
    for p in ps :

        if p in rs :
            m = ps[p]
            r = rs[p]

            a = p[0] + r
            b = r + p[1]

            qs[a] += m
            qs[b] += m

    return qs

def get_counts(ps, s, t) :

    cs = defaultdict(int)
    for p in ps :
        m = ps[p]

        a = p[0]
        b = p[1]

        cs[a] += m
        cs[b] += m

    for c in cs :
        cs[c] = cs[c] // 2

    cs[s] += 1
    cs[t] += 1

    return cs

def score(cs) :

    cs = sorted(cs.values())

    a = cs[0]
    b = cs[-1]

    return b - a

lines = open(sys.argv[1],'r')
n = int(sys.argv[2])

ps, s, t = get_pairs(lines.readline().strip())
rs = load_rules(lines)

for i in range(n) :
    ps = apply_rules(rs, ps)

cs = get_counts(ps, s, t)

print(score(cs))
