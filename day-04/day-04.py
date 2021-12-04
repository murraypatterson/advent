
def list_rep(s) :
    return list(int(x) for x in s)

def init_masks(boards) :

    masks = []
    for board in boards :

        k = len(board)
        mask = [[0 for i in range(k)] for j in range(k)]
        masks.append(mask)

    return masks

def apply_num(num, mask, board) :

    k = len(board)
    for i in range(k) :
        for j in range(k) :

            if board[i][j] == num :
                mask[i][j] = 1

    return mask

def is_winner(mask) :

    k = len(mask)
    for i in range(k) :

        if sum(mask[i]) == k :
            return True

    for j in range(k) :

        if sum(row[j] for row in mask) == k :
            return True

    return False

def sum_unmarked(board, mask) :

    k = len(board)
    s = 0
    for i in range(k) :
        for j in range(k) :
            s += 0 if mask[i][j] else board[i][j]

    return s

lines = open('input-04.txt','r')

draw = None
boards = []
buf = []
for line in lines :
    line = line.strip()

    if not line :

        if buf :
            assert len(buf) == len(buf[0])
            boards.append(buf)

        buf = []

    else :

        if draw :
            buf.append(list_rep(line.split()))

        else :
            draw = list_rep(line.split(','))

if buf :
    assert len(buf) == len(buf[0])
    boards.append(buf)
    
masks = init_masks(boards)

winners = []
win_num = {}
for num in draw :

    for i in range(len(boards)) :
        masks[i] = apply_num(num, masks[i], boards[i])

        if is_winner(masks[i]) :
            if i not in winners :
                winners.append(i)
                win_num[i] = num

masks = init_masks(boards)

for num in draw :

    for i in range(len(boards)) :
        masks[i] = apply_num(num, masks[i], boards[i])

        if is_winner(masks[i]) :

            if i == winners[0] and num == win_num[i] :
                print('part 1:', num * sum_unmarked(boards[i], masks[i]))            
            
            if i == winners[-1] and num == win_num[i] :
                print('part 2:', num * sum_unmarked(boards[i], masks[i]))
