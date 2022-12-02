import sys

s = ':'
for line in open('01.txt','r') :
    s += line.strip() + ':'

s = s.split('::')
s = [x.strip(':').split(':') for x in s]
s = [sum(int(x) for x in y) for y in s]

print('01a:', max(s))
print('01b:', sum(sorted(s)[-3:]))
