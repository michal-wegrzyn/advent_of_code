board = [['#']+list(line)+['#'] for line in open('input.txt').read().strip().split('\n')]
board = [['#']*len(board[0])] + board + [['#']*len(board[0])]
directions = [[-1,0], [0,-1], [1,0], [0,1]]

history = {}
history2 = []
cycles_cnt = 1000000000

for cycle in range(cycles_cnt):
    board_tuple = tuple([tuple(row) for row in board])
    if board_tuple in history:
        pos = history[board_tuple]
        board = history2[pos+(cycles_cnt - pos)%(cycle - pos)]
        break
    
    history[board_tuple] = cycle
    history2.append(board_tuple)
    for i, dir in enumerate(directions):
        rolling = True
        while rolling:
            rolling = False
            step = 1
            if i in [2,3]:
                step = -1
            for row in list(range(len(board)))[::step]:
                for column in list(range(len(board[row])))[::step]:
                    if board[row][column] == 'O' and board[row+dir[0]][column+dir[1]] == '.':
                        board[row][column] = '.'
                        board[row+dir[0]][column+dir[1]] = 'O'
                        rolling = True

ans = 0
for row in range(len(board)):
    for column in range(len(board[row])):
        if board[row][column] == 'O':
            ans += len(board) - row - 1
print(ans)