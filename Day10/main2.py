directions = ((-1,0), (0,1), (1,0), (0,-1))
pipes = {'|': (0,2), '-':(1,3), 'L':(0,1), 'J':(0,3), '7':(2,3), 'F':(1,2), '.': ()}

lines = ['.'+line.strip()+'.' for line in open('input.txt').readlines()]
lines = ['.'*len(lines[0])] + lines + ['.'*len(lines[0])]

start = [-1,-1]
for row in range(len(lines)):
    if lines[row].find('S') != -1:
        start = [row, lines[row].index('S')]
        break

connected_neighbours = []
for i, d in enumerate(directions):
    coords = [start[0]+d[0], start[1]+d[1]]
    if (i+2)%4 in pipes[lines[coords[0]][coords[1]]]:
        connected_neighbours.append(i)

pipes['S'] = tuple(connected_neighbours)

curr_square = start
prev_square = [-1,-1]
prev_dir = -1

right_cnt = 0
if not connected_neighbours in [[0,2], [1,3]]:
    if connected_neighbours == [0,3]:
        right_cnt = -1
    else:
        right_cnt = 1

while True:
    for d in pipes[lines[curr_square[0]][curr_square[1]]]:
        if prev_square != [curr_square[0]+directions[d][0], curr_square[1]+directions[d][1]]:
            prev_square = curr_square
            curr_square = [curr_square[0]+directions[d][0], curr_square[1]+directions[d][1]]
            if prev_dir != -1:
                if (d - prev_dir)%4 == 1:
                    right_cnt += 1
                elif (d - prev_dir)%4 == 3:
                    right_cnt -= 1
            prev_dir = d
            break
    if curr_square == start:
        break

if right_cnt == -4:
    pipes['S'] = tuple(connected_neighbours[::-1])

cycle_info = []
for i in range(len(lines)):
    cycle_info.append([])
    for j in range(len(lines[i])):
        cycle_info[-1].append(0)

while True:
    for d in pipes[lines[curr_square[0]][curr_square[1]]]:
        if prev_square != [curr_square[0]+directions[d][0], curr_square[1]+directions[d][1]]:
            prev_square = curr_square
            curr_square = [curr_square[0]+directions[d][0], curr_square[1]+directions[d][1]]
            prev_dir = d
            cycle_info[curr_square[0]][curr_square[1]] = 2
            d2 = (d+1)%4
            if cycle_info[prev_square[0]+directions[d2][0]][prev_square[1]+directions[d2][1]] == 0:
                cycle_info[prev_square[0]+directions[d2][0]][prev_square[1]+directions[d2][1]] = 1
            if cycle_info[curr_square[0]+directions[d2][0]][curr_square[1]+directions[d2][1]] == 0:
                cycle_info[curr_square[0]+directions[d2][0]][curr_square[1]+directions[d2][1]] = 1
            break
    if curr_square == start:
        break

inside = []
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if cycle_info[i][j] == 1:
            inside.append([i,j])

id = 0
while id < len(inside):
    square = inside[id]
    for d in directions:
        if cycle_info[square[0]+d[0]][square[1]+d[1]] == 0:
            cycle_info[square[0]+d[0]][square[1]+d[1]] = 1
            inside.append([square[0]+d[0], square[1]+d[1]])
    id += 1

print(len(inside))