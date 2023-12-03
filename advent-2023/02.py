import sys

d = {'red':12, 'green':13, 'blue':14}

t = 0
t2 = 0
for line in open('02.txt','r') :
    line = line.strip()

    a,b = line.split(':')
    i = int(a.lstrip('Game').strip())
    sss = [ss.split(',') for ss in b.split(';')]

    j = i
    c = {'red':0, 'green':0, 'blue':0}
    for ss in sss :
        for s in ss :
            x,y = s.split()

            if int(x) > d[y] : j = 0

            c[y] = max(int(x), c[y])
            
    t += j
    p = 1
    for k in c :
        p *= c[k]

    t2 += p
    
print('02a:',t)
print('02b:',t2)
