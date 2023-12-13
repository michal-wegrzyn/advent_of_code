boards = [board.split() for board in open('input.txt').read().split('\n\n')]

ans = 0

for board in boards:
    for b, v in [[board, 100], [list(zip(*board)), 1]]:
        for i in range(len(b)-1):
            if all([b[i-j] == b[i+j+1] for j in range(min(i+1,len(b)-i-1))]):
                ans += v*(i+1)

print(ans)