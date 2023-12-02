import sys

digits = [str(x) for x in range(1,10)]

s = 0
for line in open('01.txt','r') :
    a = line.strip()

    i = 0
    j = -1

    while a[i] not in digits : i += 1
    while a[j] not in digits : j -=1

    s += int(a[i] + a[j])

print('01a:', s)

nums = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
dons = digits + nums
digit = {x:y for x,y in zip(nums, digits)}

s = 0
for line in open('01.txt','r') :
    a = line.strip()
    n = len(a)

    i = n
    j = 0
    for x in dons :
        y = a.find(x)
        if y != -1 and y < i : i = y

        z = a.rfind(x)
        if z != -1 and z > j : j = z

    p = ''
    q = ''
    for x in dons :
        if a.find(x) == i :
            p = x if x in digits else digit[x]

        if a.rfind(x) == j :
            q = x if x in digits else digit[x]
            
    s += int(p + q)

print('01b:', s)
