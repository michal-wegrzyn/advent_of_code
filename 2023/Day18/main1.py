directions = {'U':[-1,0], 'R':[0,1], 'D':[1,0], 'L':[0,-1]}
coords = [0,0]
ans = 0
lines = [line.split()[:2] for line in open('input.txt').read().strip().split('\n')]

for line in lines:
    dir, dist = directions[line[0]], int(line[1])
    new_coords = [coords[0]+dir[0]*dist, coords[1]+dir[1]*dist]
    ans += new_coords[0]*coords[1] - new_coords[1]*coords[0]
    coords = new_coords

ans = abs(ans // 2) + sum(int(line[1]) for line in lines)//2 + 1
print(ans)