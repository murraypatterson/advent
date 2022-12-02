import sys

# there is probably a more compact representation
d = {
    ('A','X') : 3, ('A','Y') : 6, ('A','Z') : 0,
    ('B','X') : 0, ('B','Y') : 3, ('B','Z') : 6,
    ('C','X') : 6, ('C','Y') : 0, ('C','Z') : 3,
    }

s = {'X' : 1, 'Y' : 2, 'Z' : 3}

m = {
    ('A','X') : 'Z', ('A','Y') : 'X', ('A','Z') : 'Y',
    ('B','X') : 'X', ('B','Y') : 'Y', ('B','Z') : 'Z',
    ('C','X') : 'Y', ('C','Y') : 'Z', ('C','Z') : 'X',
    }

a,b = 0,0
for line in open('02.txt','r') :
    x, y = line.split()

    a += d[x,y] + s[y]
    b += d[x, m[x,y]] + s[m[x,y]]

print('02a:', a)
print('02b:', b)
