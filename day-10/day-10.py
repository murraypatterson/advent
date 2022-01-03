
import sys

j = dict((y,x+1) for x,y in enumerate('([{<'))

def score(s) :

    t = 0
    while s :
        t *= 5
        t += j[s.pop()]

    return t

p = { ')':'(', ']':'[', '}':'{', '>':'<' }
d = { ')':3, ']':57, '}':1197, '>':25137 }

t = 0
v = []
for line in open(sys.argv[1],'r') :

    i = True
    s = []
    for c in line.strip() :

        if c in p.values() :
            s.append(c)

        elif p[c] != s.pop() :
            i = False

            t += d[c]
            break

    if i :
        v.append(score(s))
        
print(t)
print(sorted(v)[len(v)//2])
