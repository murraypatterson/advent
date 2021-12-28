
import sys
from itertools import permutations

def decode(s) :
    s = ''.join(sorted(s))

    if s == 'abcefg' : return 0
    if s == 'cf' : return 1
    if s == 'acdeg' : return 2
    if s == 'acdfg' : return 3
    if s == 'bcdf' : return 4
    if s == 'abdfg' : return 5
    if s == 'abdefg' : return 6
    if s == 'acf' : return 7
    if s == 'abcdefg' : return 8
    if s == 'abcdfg' : return 9

    return 100

def mapp(s, i, p) :

    ps = []
    for x in s :
        ps.append(p[i[x]])

    return ps

alpha = 'abcdefg'
ind = dict((x, i) for i, x in enumerate(alpha))

agg = 0
for line in open(sys.argv[1],'r') :
    line = line.strip()

    a, b = line.split('|')
    a = a.split()
    b = b.split()

    for p in permutations(alpha) :

        if sum(decode(mapp(s,ind,p)) for s in a) < 100 :
            agg += int(''.join(str(decode(mapp(t,ind,p))) for t in b))

print(agg)
