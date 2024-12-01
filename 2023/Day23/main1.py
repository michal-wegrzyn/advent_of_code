from collections import deque

directions = {'^':(-1,0),'>':(0,1),'v':(1,0),'<':(0,-1)}
maze = open('input.txt').read().strip().split('\n')
graph = [[[] for _ in range(len(maze[0]))] for _ in range(len(maze))]
graph_inv = [[[] for _ in range(len(maze[0]))] for _ in range(len(maze))]
edge_info = [[[0,0,0] for _ in range(len(maze[0]))] for _ in range(len(maze))] # in, out, any
end_square = ()
square_queue = deque()

def add_edge(start, end):
    if end in graph[start[0]][start[1]]:
        return
    if maze[start[0]][start[1]] == '#':
        return
    if maze[end[0]][end[1]] == '#':
        return
    graph[start[0]][start[1]].append(end)
    graph_inv[end[0]][end[1]].append(start)
    edge_info[start[0]][start[1]][1] += 1
    edge_info[start[0]][start[1]][2] -= 1
    edge_info[end[0]][end[1]][0] += 1
    edge_info[end[0]][end[1]][2] -= 1

for row in range(len(maze)):
    for column in range(len(maze[0])):
        if maze[row][column] == '#':
            edge_info[row][column] = [-1,-1,-1]
            continue
        if row == 0:
            edge_info[row][column][1] += 1
            graph[0][column].append((1, column))
            graph_inv[1][column].append((0, column))
            edge_info[1][column][0] += 1
            edge_info[1][column][2] -= 1
            continue
        if row == len(maze)-1:
            edge_info[row][column][0] += 1
            graph[len(maze)-2][column].append((len(maze)-1, column))
            graph_inv[len(maze)-1][column].append((len(maze)-2, column))
            edge_info[len(maze)-2][column][1] += 1
            edge_info[len(maze)-2][column][2] -= 1
            end_square = (row, column)
            continue
        edge_info[row][column][2] += sum(maze[row+d[0]][column+d[1]]!='#' for d in directions.values())
        if maze[row][column] == '.':
            continue
        out_dir = directions[maze[row][column]]
        add_edge((row,column), (row+out_dir[0], column+out_dir[1]))
        for d in directions.values():
            if d == out_dir:
                continue
            add_edge((row+d[0], column+d[1]), (row, column))

for row in range(len(maze)):
    for column in range(len(maze[0])):
        if edge_info[row][column][2] == 1:
            if edge_info[row][column][0] == 0 or edge_info[row][column][1] == 0:
                square_queue.append((row,column))

while len(square_queue):
    row, column = square_queue.popleft()
    if edge_info[row][column][2] != 1:
        continue
    if edge_info[row][column][0] != 0 and edge_info[row][column][1] != 0:
        continue
    for d in directions.values():
        if maze[row+d[0]][column+d[1]] != '.':
            continue
        if (row+d[0], column+d[1]) in graph[row][column]:
            continue
        if (row, column) in graph[row+d[0]][column+d[1]]:
            continue
        remaining = (row+d[0], column+d[1])
        break
    if edge_info[row][column][0] == 0:
        add_edge(remaining, (row,column))
    else:
        add_edge((row,column), remaining)
    
    if edge_info[remaining[0]][remaining[1]][2] != 1:
        continue
    if edge_info[remaining[0]][remaining[1]][0] == 0 or edge_info[remaining[0]][remaining[1]][1] == 0:
        square_queue.append(remaining)

toposort = []
max_path = [[0 for _ in range(len(maze[0]))] for _ in range(len(maze))]

for row in range(len(maze)):
    for column in range(len(maze[0])):
        if edge_info[row][column][0] == 0:
            square_queue.append((row, column))

while len(square_queue):
    row, column = square_queue.popleft()
    toposort.append((row, column))
    for r, c in graph[row][column]:
        edge_info[r][c][0] -= 1
        if edge_info[r][c][0] == 0:
            square_queue.append((r,c))

for row, column in toposort:
    mx = 0
    for r, c in graph_inv[row][column]:
        mx = max(mx, max_path[r][c] + 1)
    max_path[row][column] = mx

print(max_path[end_square[0]][end_square[1]])