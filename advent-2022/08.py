import sys
from math import prod

# step onto a[i,j] wrt x and u
def step(i, j, x, a, u, cs) :

    if a[i][j] > x :
        cs.add((i,j))
        x = a[i][j]

    if u : # for part b
        if x < u :
            if a[i][j] <= u : # make an exception
                cs.add((i,j))

        else : # x >= u, make it stop
            x = 9

    return cs, x

# coords visible in a from origin o in direction d with upper bound u
def coords(a, o, d, u = None) :
    cs = set([])

    n = len(a)
    m = len(a[0])
    
    r, c = o
    assert d in ['n','e','s','w']
    x = -1

    xs = a, u, cs
    if d == 'n' :
        for i in reversed(range(r)) :
            cs, x = step(i, c, x, *xs)
            
    elif d == 'e' :
        for j in range(c+1, m) :
            cs, x = step(r, j, x, *xs)
            
    elif d == 's' :
        for i in range(r+1, n) :
            cs, x = step(i, c, x, *xs)
            
    elif d == 'w' :
        for j in reversed(range(c)) :
            cs, x = step(r, j, x, *xs)
            
    else :
        assert False, d

    return cs

# Main

a = []
for line in open(sys.argv[1],'r') :
    a.append([int(x) for x in line.strip()])

n = len(a)
m = len(a[0])

# a
cs = set([]) # set of (visible) coordinates to maintain

for i in range(n) :
    cs.update(coords(a, (i,-1), 'e')) # from the left..
    cs.update(coords(a, (i,m), 'w')) # from the right..

for j in range(m) :
    cs.update(coords(a, (-1,j), 's')) # from the top..
    cs.update(coords(a, (m,j), 'n')) # from the bottom..

# b
b = 0
for i in range(n) :
    for j in range(m) :

        s = []
        for d in ['n','e','s','w'] :
            s.append(len(coords(a, (i,j), d, a[i][j])))

        b = max(b, prod(s))
        
print('08a:', len(cs))
print('08b:', b)
