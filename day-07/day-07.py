
def run_part(part) :

    cost_of = {}
    for x in range(a,b+1) :

        cost_of[x] = sum(abs(x-p) for p in ps)
        if part == 2 :
            cost_of[x] = sum(sum(range(abs(x-p)+1)) for p in ps)

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
