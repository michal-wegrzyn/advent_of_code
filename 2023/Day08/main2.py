from math import lcm

lines = open('input.txt').readlines()

instructions = lines[0].strip()
graph = {}
poses = []
for line in lines[2:]:
    name = line[:line.index('=')-1]
    if name[-1] == 'A':
        poses.append(name)
    left = line[line.index('=')+3:line.index(',')]
    right = line[line.index(',')+2:-2]
    graph[name] = (left, right)

cycles = []

for pos in poses:
    path = {}
    steps = 0
    curr_pos = pos
    while not (curr_pos, steps%len(instructions)) in path.keys():
        for i in instructions:
            path[(curr_pos, steps%len(instructions))] = steps
            steps += 1
            curr_pos = graph[curr_pos][i=='R']
            if (curr_pos, steps%len(instructions)) in path.keys():
                break
    cycle_start = path[(curr_pos, steps%len(instructions))]
    cycle_size = len(path) - cycle_start
    cycles.append([[], cycle_size])
    for k, v in path.items():
        if v >= cycle_start and k[0][-1]=='Z':
            cycles[-1][0].append(v%cycle_size)

res = cycles[0][1]
for i in cycles:
    # this assertion holds for my data
    assert i[0] == [0]
    res = lcm(res, i[1])
print(res)