import sys

d = {}

def f(s,b) :
    c = 0

    while True :
        a = b.readline().strip()

        if not a :
            return c

        if a == '$ ls' :
            continue

        if a.startswith('$ cd') :
            _, _, a = a.split()

            if a == '..' :
                return c

            else :
                a = s + '/' + a
                d[a] += f(a,b)
                c += d[a]

            continue

        # o.w. it is not a command
        x, y = a.split()

        if x == 'dir' :
            y = s + '/' + y
            d[y] = 0

        else :
            c += int(x)

b = open(sys.argv[1],'r')
a = b.readline().strip()
assert a == '$ cd /'

d['/'] = f('/',b) # start it off

b.close()

a = 0
for x in d :
    if d[x] <= 100000 :
        a += d[x]

b = 0
m = max(0, d['/'] - 40000000)
d = dict(sorted(d.items(), key = lambda item : item[1]))
for x in d :

    if d[x] >= m :
        b = d[x]
        break

print('07a:', a)
print('07b:', b)
