import re

def p(line) : # process a line
    a1,a2,b1,b2 = (int(x) for x in re.split(',|-', line))
    assert a1 <= a2, line
    assert b1 <= b2, line

    return a1,a2,b1,b2

def c(a1,a2,b1,b2) : # 1 if a \in b or vice versa, 0 otherwise

    if a1 <= b1 and a2 >= b2 :
        return 1
    if b1 <= a1 and b2 >= a2 :
        return 1

    return 0

def o(a1,a2,b1,b2) : # 1 if a overlaps b or vice versa, o.w. 0

    if a1 <= b2 and a2 >= b1 :
        return 1
    if b1 <= a2 and b2 >= a1 :
        return 1

    return 0

cs = 0
os = 0
for line in open('04.txt','r') :
    line = line.strip()

    a1,a2,b1,b2 = p(line)
    cs += c(a1,a2,b1,b2)
    os += o(a1,a2,b1,b2)

print('04a:', cs)
print('04b:', os)
