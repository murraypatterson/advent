
import sys

def ucheck(u, bs = set([])) :

    if u.isupper() :
        u = 'u{}'.format(u)
        bs.add(u)

    return u, bs

print()
U = set([])
bs = set([])
for line in open(sys.argv[1],'r') :
    line = line.strip()

    u, v = line.split('-')

    u, bs = ucheck(u, bs)
    v, bs = ucheck(v, bs)

    U.add(u)
    U.add(v)
    
    print('edge({},{}).'.format(u, v))
    print('edge({},{}).'.format(v, u))

print()
for b in bs :
    print('is_big({}).'.format(b))

print()

# part 2

ss = U - bs - set(['start','end'])
for s in ss : # a graph for each small cave

    h = open('run_{}.pl'.format(s),'w')
    print(file = h)
    for line in open(sys.argv[1],'r') :
        line = line.strip()

        u, v = line.split('-')

        u, _ = ucheck(u)
        v, _ = ucheck(v)

        print('edge({},{}).'.format(u, v), file = h)
        print('edge({},{}).'.format(v, u), file = h)

        # create a parallel node u' with N(u') = N(u)
        if u == s :
            print('edge({}prime,{}).'.format(s, v), file = h)
            print('edge({},{}prime).'.format(v, s), file = h)

        if v == s :
            print('edge({},{}prime).'.format(u, s), file = h)
            print('edge({}prime,{}).'.format(s, u), file = h)

    print(file = h)
    for b in bs :
        print('is_big({}).'.format(b), file = h)

    print(file = h)
            
    h.close()
