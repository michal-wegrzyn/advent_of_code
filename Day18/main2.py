directions = {'0':[0,1], '1':[1,0], '2':[0,-1], '3':[-1,0],}
coords = [0,0]
ans = 0
lines = [line.split()[2][2:-1] for line in open('input.txt').read().strip().split('\n')]

for line in lines:
    dir, dist = directions[line[-1]], int(line[:-1], 16)
    new_coords = [coords[0]+dir[0]*dist, coords[1]+dir[1]*dist]
    ans += new_coords[0]*coords[1] - new_coords[1]*coords[0]
    coords = new_coords

ans = abs(ans // 2) + sum(int(line[:-1], 16) for line in lines)//2 + 1
print(ans)