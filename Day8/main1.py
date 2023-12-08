lines = open('input.txt').readlines()

instructions = lines[0].strip()
graph = {}
for line in lines[2:]:
    name = line[:line.index('=')-1]
    left = line[line.index('=')+3:line.index(',')]
    right = line[line.index(',')+2:-2]
    graph[name] = (left, right)

ans = 0
pos = 'AAA'
while pos != 'ZZZ':
    for i in instructions:
        pos = graph[pos][i=='R']
        ans += 1
        if pos == 'ZZZ':
            break

print(ans)