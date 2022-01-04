
import sys

def load_array(lines) :

    a = []
    for line in lines :
        a.append(list(int(x) for x in line.strip()))

    return a, len(a)

def incr(a) :

    for i in range(n) :
        for j in range(n) :
            a[i][j] += 1

def neighbours(x,y) :

    return [(x+i, y+j) for i in [-1,0,1] for j in [-1,0,1]]

def flash(x,y) :

    if a[x][y] < 10 :
        return 0

    for i,j in neighbours(x,y) :
        if i in range(n) and j in range(n) and a[i][j] > 0 :
            a[i][j] += 1

    a[x][y] = 0

    return 1

def update(a) :

    f = 0
    for i in range(n) :
        for j in range(n) :
            f += flash(i,j)

    return f

def step(a) :

    incr(a)

    f = 0
    g = update(a)
    while g > f :
        f = g
        g += update(a)

    return f

a, n = load_array(open(sys.argv[1],'r'))

# part 1
if len(sys.argv) > 2 :

    c = 0
    for i in range(int(sys.argv[2])) :
        c += step(a)

    print(c)

# part 2
else :

    i = 1
    while True :

        if step(a) == n * n :
            print(i)
            break

        i += 1
