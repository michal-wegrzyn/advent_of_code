import heapq

def vertex_id(row, column, count, prev_direction):
    if not (0<=row<len(board) and 0<=column<len(board[0]) and 0<=count<3 and 0<=prev_direction<4):
        return -1
    return row*len(board[0])*12+column*12+count*4+prev_direction

directions = [[-1,0],[0,1],[1,0],[0,-1]]
board = open('input.txt').read().strip().split()

graph = [[] for _ in range(len(board)*len(board[0])*12)]
for row in range(len(board)):
    for column in range(len(board[0])):
        for count in range(3):
            for prev_dir in range(4):
                curr_vertex = vertex_id(row, column, count, prev_dir)
                for dir_id, dir in enumerate(directions):
                    if abs(dir_id-prev_dir) == 2:
                        continue
                    adjacent = vertex_id(row+dir[0], column+dir[1], (count+1)*(prev_dir==dir_id), dir_id)
                    if adjacent == -1:
                        continue
                    graph[curr_vertex].append([int(board[row+dir[0]][column+dir[1]]),adjacent])

graph.append([]) # starting vertex
graph[-1].append([int(board[0][1]),vertex_id(0,1,0,1)])
graph[-1].append([int(board[1][0]),vertex_id(1,0,0,2)])

# Dijkstra's algorithm
distances = [10*len(board)*len(board[0])]*len(graph)
distances[-1] = 0
updated_vertices = [[0,-1]]
while len(updated_vertices):
    distance, vertex = updated_vertices[0]
    heapq.heappop(updated_vertices)
    if distance > distances[vertex]:
        continue
    for dist, adj in graph[vertex]:
        if distances[adj] <= distance + dist:
            continue
        distances[adj] = distance + dist
        heapq.heappush(updated_vertices, [distances[adj], adj])

ans = min(distances[-13:-1])
print(ans)