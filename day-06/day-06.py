
g = list(int(x) for x in open('input-06.txt','r').readline().split(','))

d = {}
for i in range(9) :
    d[i] = 0

for x in g :
    d[x] += 1

for i in range(256) :

    c = d[0]
    for j in range(8) :
        d[j] = d[j+1]

    d[6] += c
    d[8] = c

    n = sum(d[j] for j in d)
    print(i+1, n)
