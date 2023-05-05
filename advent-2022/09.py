import sys

# step hx,hy in direction d, determining direction dt for tx,ty
def s(hx, hy, tx, ty, d) :

    dt = None
    assert abs(hx - tx) <= 1, 'hx = {}, tx = {}'.format(hx,tx)
    assert abs(hy - ty) <= 1, 'hy = {}, ty = {}'.format(hy,ty)

    if d == 'R' :
        hx += 1

        if hx - tx > 1 :
            dt = 'R'

            if hy > ty :
                dt += 'U'
            if hy < ty :
                dt += 'D'

    elif d == 'L' :
        hx -= 1

        if tx - hx > 1 :
            dt = 'L'

            if hy > ty :
                dt += 'U'
            if hy < ty :
                dt += 'D'

    elif d == 'U' :
        hy += 1

        if hy - ty > 1 :
            dt = 'U'

            if hx > tx :
                dt = 'R' + dt
            if hx < tx :
                dt = 'L' + dt

    elif d == 'D' :
        hy -= 1

        if ty - hy > 1 :
            dt = 'D'

            if hx > tx :
                dt = 'R' + dt
            if hx < tx :
                dt = 'L' + dt

    elif d == 'RU' :
        hx += 1
        hy += 1

        if hx - tx > 1 or hy - ty > 1 :
            dt = d

    elif d == 'RD' :
        hx += 1
        hy -= 1

        if hx - tx > 1 or ty - hy > 1 :
            dt = d

    elif d == 'LU' :
        hx -= 1
        hy += 1

        if tx - hx > 1 or hy - ty > 1 :
            dt = d

    elif d == 'LD' :
        hx -= 1
        hy -= 1

        if tx - hx > 1 or ty - hy > 1 :
            dt = d

    else :
        assert not d, d

    return hx, hy, dt

# Main

# a
hx, hy = 0, 0
tx, ty = 0, 0
cs = set([(0, 0)])

# b
xs = 11 * [0]
ys = 11 * [0]
ds = set([(0, 0)])

#print('j\tx\ty\td')

for line in open(sys.argv[1],'r') :
    d, k = line.split()

    for i in range(int(k)) :
        dt = d

        # a
        hx, hy, dt = s(hx, hy, tx, ty, dt)
        tx, ty, dt = s(tx, ty, tx, ty, dt)
        cs.add((tx, ty))

        # b
        #print()
        #print(d)
        #print('----------------------------------------------------------------------')
        for j in range(10) :
            #print(j, xs[j], ys[j], xs[j+1], ys[j+1], dt, sep = '\t')
            xs[j], ys[j], dt = s(xs[j], ys[j], xs[j+1], ys[j+1], dt)
            #print(j, xs[j], ys[j], xs[j+1], ys[j+1], dt, sep = '\t')

        ds.add((xs[9], ys[9]))

print('09a:', len(cs))
print('09b:', len(ds))
