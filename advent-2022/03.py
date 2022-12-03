
def p(x) :
    x = ord(x)

    if x >= 97 and x <= 122 : # lowercase
        return x - 96
    if x >= 65 and x <= 90 : # uppercase
        return x - 38

    assert False

s = []
t = []
q = []
i = 0
for line in open('03.txt','r') :
    line = line.strip()

    m = len(line) // 2
    a, b = set(line[:m]), set(line[m:])
    c = a & b
    s += list(c)

    if i % 3 :
        q.append(set(line))
    else :
        if q : t += list(q[0] & q[1] & q[2]) # first case
        q = [set(line)]

    i += 1

t += list(q[0] & q[1] & q[2]) # last case

a = sum(p(x) for x in s)
b = sum(p(x) for x in t)

print('03a:', a)
print('03b:', b)
