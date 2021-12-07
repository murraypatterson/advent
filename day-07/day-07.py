
def abs(x) :
    if x < 0 :
        return -x
    return x

def cost(x, ps, part = 1) :

    if part == 2 :
        return sum(sum(range(abs(x-p)+1)) for p in ps)

    return sum(abs(x-p) for p in ps)

def run_part(part) :

    cost_of = {}
    for x in range(a,b+1) :
        cost_of[x] = cost(x,ps,part)

        m = min(cost_of.values())

    print('part {}:'.format(part))
    for x in cost_of :
        if cost_of[x] == m :
            print(x, cost_of[x])

ps = list(int(x) for x in open('input-07.txt','r').readline().split(','))

a = min(ps)
b = max(ps)

run_part(1)
run_part(2)
