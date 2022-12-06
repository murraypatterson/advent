import sys

def p(a, k) :

    for i in range(k-1, len(a)) :
        if len(set(a[i-k+1:i+1])) == k :
            return i+1

for line in open(sys.argv[1],'r') :
    line = line.strip()

    a = p(line, 4)
    b = p(line, 14)
    
print('06a:', a)
print('06b:', b)
