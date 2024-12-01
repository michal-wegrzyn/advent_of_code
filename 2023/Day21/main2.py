from collections import deque

MAX_DISTANCE = 26501365
# MAX_DISTANCE = 15

directions = [[-1,0], [0,1], [1,0], [0,-1]]
board = open('input.txt').read().strip().split('\n')

assert all(board[0][i]=='.' for i in range(len(board[0])))
assert all(board[-1][i]=='.' for i in range(len(board[-1])))
assert all(board[i][0]=='.' for i in range(len(board)))
assert all(board[i][-1]=='.' for i in range(len(board)))

S = (0, 0)

for ind, row in enumerate(board):
    if 'S' in row:
        S = (ind, row.find('S'))
        board[ind] = board[ind].replace('S', '.')
        break

assert all(board[S[0]][i]=='.' for i in range(len(board[S[0]])))
assert all(board[i][S[1]]=='.' for i in range(len(board)))
assert len(board) == len(board[0])
assert len(board) % 2 == 1
assert S[0] == S[1] == len(board) // 2

def bfs(start):
    res = [[-1]*len(board[0]) for _ in board]
    res[start[0]][start[1]] = 0
    visit = deque()
    visit.append(start)

    while len(visit):
        garden_plot = visit.popleft()
        for d in directions:
            new_garden_plot = (garden_plot[0]+d[0], garden_plot[1]+d[1])
            if not (0<=new_garden_plot[0]<len(board) and 0<=new_garden_plot[1]<len(board[0])):
                continue
            if board[new_garden_plot[0]][new_garden_plot[1]] == '#':
                continue
            if res[new_garden_plot[0]][new_garden_plot[1]] != -1:
                continue
            res[new_garden_plot[0]][new_garden_plot[1]] = res[garden_plot[0]][garden_plot[1]] + 1
            visit.append(tuple(new_garden_plot))
    
    return res

special_points = [(r, c) for r in (0, S[0], len(board)-1) for c in (0, S[1], len(board[0])-1)]
special_points = [special_points[i] for i in (0,1,2,5,8,7,6,3)]
distances = [bfs(point) for point in special_points]
distances_S = bfs(S)
ans = 0
# print(distances_S)
# print(distances)
for row in range(len(board)):
    for column in range(len(board[0])):
        if distances_S[row][column] == -1:
            continue
        if distances_S[row][column]%2 == MAX_DISTANCE % 2 and distances_S[row][column] <= MAX_DISTANCE:
            ans += 1
        for i in range(len(special_points)):
            if i % 2 == 0:
                distance_mult = len(board)
                single_distance = len(board) + 1
            else:
                distance_mult = len(board)
                single_distance = S[0] + 1
            single_distance += distances[i][row][column]
            
            cnt = (MAX_DISTANCE-single_distance) // distance_mult + 1
            # print(row, column, i, single_distance, distance_mult, cnt)
            if i%2 == 0:
                if distance_mult % 2 == 0:
                    if single_distance % 2 == MAX_DISTANCE % 2:
                        ans += cnt*(cnt+1)//2
                else:
                    if single_distance % 2 == MAX_DISTANCE % 2:
                        ans += ((cnt+1)//2)*((cnt+1)//2)
                    else:
                        ans += cnt*(cnt+1)//2 - ((cnt+1)//2)*((cnt+1)//2)
            else:
                if distance_mult % 2 == 0:
                    if single_distance % 2 == MAX_DISTANCE % 2:
                        ans += cnt
                else:
                    if single_distance % 2 == MAX_DISTANCE % 2:
                        ans += (cnt+1)//2
                    else:
                        ans += cnt//2
            # print(ans)

print(ans)