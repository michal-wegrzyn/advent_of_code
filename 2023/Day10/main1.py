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
cycle_len = 0

while True:
    for d in pipes[lines[curr_square[0]][curr_square[1]]]:
        if prev_square != [curr_square[0]+directions[d][0], curr_square[1]+directions[d][1]]:
            prev_square = curr_square
            curr_square = [curr_square[0]+directions[d][0], curr_square[1]+directions[d][1]]
            cycle_len += 1
            break
    if curr_square == start:
        break

print(cycle_len//2)