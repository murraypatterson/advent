
import sys

def load_data(lines) :

    cs = []
    fs = []
    for line in lines :
        line = line.strip()

        if not line :
            continue

        if line.startswith('fold') :
            line = line[11:]

            a,b = line.split('=')
            fs.append((a, int(b)))

            continue

        x,y = line.split(',')
        cs.append((int(x), int(y)))

    return cs, fs

def fold(cs, a, b) :

    for i in range(len(cs)) :
        x, y = cs[i]

        if a == 'x' :
            assert x != b

            if x > b :
                x = b - (x - b)

        elif a == 'y' :
            assert y != b

            if y > b :
                y = b - (y - b)

        else :
            assert False

        cs[i] = x, y

    return cs

def display(cs) :

    cs = set(cs)

    m = 0
    n = 0
    for x, y in cs :

        if x > m :
            m = x

        if y > n :
            n = y

    a = []
    for y in range(n+1) :
        a.append(list((m+1) * '.'))

    for x, y in cs :
        a[y][x] = '#'

    for row in a :
        print(*row)

cs, fs = load_data(open(sys.argv[1],'r'))

for a, b in fs :
    cs = fold(cs, a, b)
    print(len(set(cs)))

display(cs)
