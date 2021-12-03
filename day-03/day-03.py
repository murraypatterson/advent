
def list_rep(s) :
    return list(int(x) for x in s.strip())

def add_lists(a,b) :
    return list(x+y for x,y in zip(a,b))

def dec_rep(a) :

    if not a :
        return 0

    return a[-1] + 2 * dec_rep(a[:-1])

def counts(bs) :

    c, *bs = bs

    for b in bs :
        c = add_lists(c, b)

    return c

def rating(bs, mini = False) :

    i = 0
    cur = bs
    while True :

        c = counts(cur)
        m = 1 if 2 * c[i] >= len(cur) else 0

        if mini :
            m = 0 if 2 * c[i] >= len(cur) else 1

        n = []
        for a in cur :

            if a[i] == m :
                n.append(a)

        if len(n) == 1 :
            return n[0]

        cur = n
        i += 1

bs = list(list_rep(x) for x in open('input-03.txt','r').readlines())

# part 1

gamma = []
epsilon = []

c = counts(bs)
for x in c :

    g = 1
    e = 0

    if 2*x < len(bs) :
        g = 0
        e = 1

    gamma.append(g)
    epsilon.append(e)

print('part 1:', dec_rep(gamma) * dec_rep(epsilon))

# part 2

oxy = dec_rep(rating(bs))
co2 = dec_rep(rating(bs, mini = True))

print('part 2:', oxy * co2)
