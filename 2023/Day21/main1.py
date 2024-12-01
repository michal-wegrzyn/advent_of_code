from collections import deque

directions = [[-1,0], [0,1], [1,0], [0,-1]]
board = ['#'+line+'#' for line in open('input.txt').read().strip().split('\n')]
board = ['#'*len(board[0])] + board + ['#'*len(board[0])]

ans = 0
visited = set()
visit = deque()

for ind, row in enumerate(board):
    if 'S' in row:
        visit.append((ind, row.find('S'), 0))
        visited.add((ind, row.find('S')))
        break

while len(visit):
    garden_plot = visit.popleft()
    if garden_plot[2] % 2 == 0:
        ans += 1
    if garden_plot[2] == 64:
        continue
    for d in directions:
        new_garden_plot = (garden_plot[0]+d[0], garden_plot[1]+d[1], garden_plot[2]+1)
        if board[new_garden_plot[0]][new_garden_plot[1]] == '#':
            continue
        if new_garden_plot[:2] in visited:
            continue
        visit.append(tuple(new_garden_plot))
        visited.add(new_garden_plot[:2])

print(ans)