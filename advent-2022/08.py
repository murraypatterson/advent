import sys

a = []
for line in open(sys.argv[1],'r') :
    a.append([int(x) for x in line.strip()])

n = len(a)
m = len(a[0])

cs = set([]) # set of (visible) coordinates to maintain

for i in range(n) :

    x = -1
    for j in range(m) : # from the left..
        
        if a[i][j] > x :
            cs.add((i,j))
            x = a[i][j]

    x = -1
    for j in reversed(range(m)) : # from the right..

        if a[i][j] > x :
            cs.add((i,j))
            x = a[i][j]

for j in range(m) :

    x = -1
    for i in range(n) : # from the top..

        if a[i][j] > x :
            cs.add((i,j))
            x = a[i][j]

    x = -1
    for i in reversed(range(n)) : # from the bottom..

        if a[i][j] > x :
            cs.add((i,j))
            x = a[i][j]

a = len(cs)
print('08a:', a)
