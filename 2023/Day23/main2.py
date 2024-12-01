directions = ((-1,0),(0,1),(1,0),(0,-1))
maze = open('input.txt').read().strip().split('\n')
start, end = (), ()

def find_next(v, p):
    if v[0] in [0, len(maze)-1]:
        return v, 0
    # print(v, p)
    cnt = sum(maze[v[0]+d[0]][v[1]+d[1]]!='#' for d in directions)
    if cnt > 2:
        return v, 0
    if cnt < 2:
        return None
    for d in directions:
        n = v[0]+d[0], v[1]+d[1]
        if maze[n[0]][n[1]] == '#':
            continue
        if n != p:
            res = find_next(n, v)
            if res is None:
                return None
            return res[0], res[1]+1

def longest_path(visited):
    curr = visited[-1]
    if curr == end:
        # print(visited)
        return 0
    res = -len(maze)*len(maze[0])
    for i in graph[curr]:
        if i[0] in visited:
            continue
        res = max(res, i[1]+longest_path(visited+[i[0]]))
    return res

graph = {}
# print(len(maze))

for row in range(len(maze)):
    for column in range(len(maze[0])):
        if maze[row][column] == '#':
            continue
        if row in [0, len(maze)-1]:
            graph[(row,column)] = []
            if row == 0:
                start = (row, column)
            else:
                end = (row, column)
            continue
        if sum(maze[row+d[0]][column+d[1]]!='#' for d in directions) > 2:
            graph[(row,column)] = []

for row, column in graph:
    for dir in directions:
        r = row+dir[0]
        c = column+dir[1]
        if r in [-1, len(maze)]:
            continue
        if maze[r][c] == '#':
            continue
        adj = find_next((r,c), (row, column))
        if adj is None:
            continue
        graph[(row,column)].append((adj[0], adj[1]+1))

# print(graph)
print(longest_path([start]))