from itertools import combinations

lines = [[line.split()[0], [int(num) for num in line.split()[1].split(',')]] for line in open('input.txt').read().strip().split('\n')]

ans = 0

for line in lines:
    line[0] = ['.']+list(line[0])
    indicies = tuple([i for i in range(len(line[0])) if line[0][i]=='?'])
    if len(indicies) < sum(line[1])-line[0].count('#'):
        continue
    for subset in combinations(indicies, sum(line[1])-line[0].count('#')):
        row = line[0].copy()
        for i in subset:
            row[i] = '#'
        groups = []
        for i, v in enumerate(row):
            if v != '#':
                continue
            if row[i-1] != '#':
                groups.append(1)
            else:
                groups[-1] += 1
        
        if groups == line[1]:
            ans += 1

print(ans)