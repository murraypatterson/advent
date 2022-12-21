import sys

# step hx,hy in direction d, possibly affecting tx,ty
def s(hx, hy, tx, ty, d) :

    assert abs(hx - tx) <= 1
    assert abs(hy - ty) <= 1

    if d == 'R' :
        hx += 1

        if hx - tx > 1 :
            tx += 1
            ty = hy

    elif d == 'L' :
        hx -= 1

        if tx - hx > 1 :
            tx -= 1
            ty = hy

    elif d == 'U' :
        hy += 1

        if hy - ty > 1 :
            ty += 1
            tx = hx

    elif d == 'D' :
        hy -= 1

        if ty - hy > 1 :
            ty -= 1
            tx = hx

    else :
        assert False, d

    return hx, hy, tx, ty

# Main

hx, hy = 0, 0
tx, ty = 0, 0
cs = set([(0, 0)])

for line in open(sys.argv[1],'r') :
    d, k = line.split()

    for i in range(int(k)) :

        hx, hy, tx, ty = s(hx, hy, tx, ty, d)
        cs.add((tx, ty))

print('09a:', len(cs))
