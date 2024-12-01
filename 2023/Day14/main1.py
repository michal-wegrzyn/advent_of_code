board = [list(line) for line in open('input.txt').read().strip().split('\n')]
board = [['#']*len(board[0])] + board

ans = 0
rolling = True
while rolling:
    rolling = False
    for row in range(1, len(board)):
        for column in range(len(board[row])):
            if board[row][column] == 'O':
                if board[row-1][column] == '.':
                    board[row][column] = '.'
                    board[row-1][column] = 'O'
                    rolling = True
                else:
                    board[row][column] = '#'
                    ans += len(board) - row

print(ans)