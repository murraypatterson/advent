
import sys

def load_array(lines) :

    a = []
    line = lines.readline().strip()
    row = list(int(x) for x in line)
    m = len(row)
    a.append(row)

    for line in lines :
        line = line.strip()

        row = list(int(x) for x in line)
        assert len(row) == m
        a.append(row)

    n = len(a)

    return a, n, m

def v(i, j) :

    if i < 0 or i >= n or j < 0 or j >= m :
        return 9

    return a[i][j]

def neighbours(i, j) :

    return [(i-1,j), (i+1,j), (i,j-1), (i,j+1)]

def is_low(i, j) :

    val = v(i, j)
    for x, y in neighbours(i, j) :

        if v(x, y) <= val :
            return False

    return True

def extend(i, j) :

    s = set([(i,j)])
    for x, y in neighbours(i, j) :

        if v(x, y) < 9 :
            s.add((x,y))

    return s

def closure(i, j) :

    s = set([])
    t = set([(i,j)])

    while len(t) > len(s) :
        s = set(t)

        for x, y in s :
            t |= extend(x, y)

    return len(s)

a, n, m = load_array(open(sys.argv[1],'r'))

bs = []
for i in range(n) :
    for j in range(m) :
        if is_low(i, j) :
            bs.append((i,j))

print(sum(v(i,j) + 1 for i,j in bs))

# part 2
ss = []
for i, j in bs :
    ss.append(closure(i, j))

*_, x, y, z = sorted(ss)

print(x * y * z)
