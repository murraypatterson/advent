
def disp_grid(grid) :

    print()
    for y in grid :
        for x in y :
            print(x if x else '.', end = '')
        print()
    print()

def count(vents) :

    grid = [[0 for i in range(n+1)] for j in range(n+1)]

    for vent in vents :
        for x,y in vent :
            grid[y][x] += 1

    #disp_grid(grid)

    c = 0
    for y in grid :
        for x in y :
            if x > 1 :
                c += 1

    return c

lines = open('input-05.txt','r')

n = 0
v1s = []
v2s = []
for line in lines :

    p1,p2 = line.split('->')
    x1,y1 = p1.split(',')
    x2,y2 = p2.split(',')
    x1,y1,x2,y2 = [int(x) for x in [x1,y1,x2,y2]]

    m = max(x1,y1,x2,y2)
    if m > n :
        n = m

    if x1 == x2 or y1 == y2 :
        
        if x1 == x2 :
            ya = min(y1,y2)
            yb = max(y1,y2)

            vent = [(x1,y) for y in range(ya,yb+1)]

        else :
            xa = min(x1,x2)
            xb = max(x1,x2)

            vent = [(x,y1) for x in range(xa,xb+1)]

        v1s.append(vent)
        v2s.append(vent)

    else :
        xa = min(x1,x2)
        xb = max(x1,x2)
        ya = min(y1,y2)
        yb = max(y1,y2)

        assert (xb - xa) == (yb - ya)
        k = xb - xa
        
        if x1 <= x2 :
            if y1 <= y2 :
                vent = [(x1+o,y1+o) for o in range(k+1)]
            else :
                vent = [(x1+o,y1-o) for o in range(k+1)]

        else :
            if y1 <= y2 :
                vent = [(x2+o,y2-o) for o in range(k+1)]
            else :
                vent = [(x2+o,y2+o) for o in range(k+1)]

        v2s.append(vent)

print('part 1:', count(v1s))
print('part 2:', count(v2s))
