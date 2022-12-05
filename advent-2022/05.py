import sys

n = 9
s = [[] for i in range(n)]
t = [[] for i in range(n)]
m = 1 # mode
for a in open(sys.argv[1],'r') :

    if m :
        if a == '\n' :
            m = 0
            continue

        if a[1] == '1' :
            a = a.split()
            assert len(a) == n
            assert a[-1] == str(n)
            continue

        for i in range(n) :
            x = a[4*i+1]

            if x != ' ' :
                s[i].insert(0, x)
                t[i].insert(0, x)

    else :
        assert a.startswith('move')
        _, x, _, u, _, v = a.split()
        x = int(x)
        u = int(u)
        v = int(v)

        t[v-1] += t[u-1][-(x):]
        for i in range(x) :
            s[v-1].append(s[u-1].pop())
            t[u-1].pop()
            
a = ''.join(x[-1] for x in s)
b = ''.join(x[-1] for x in t)

print('05a:', a)
print('05b:', b)
