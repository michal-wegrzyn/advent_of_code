MIN_VALUE = 200000000000000
MAX_VALUE = 400000000000000

def coord_in_range(coord):
    if coord < MIN_VALUE:
        return -1
    if coord > MAX_VALUE:
        return 1
    return 0

def linear_function(f, x):
    return f[0]*x+f[1]

hailstones = [[[int(num) for num in part.split(', ')] for part in line.split(' @ ')] for line in open('input.txt').read().strip().split('\n')]
lines = []
for (x, y, _), (vx, vy, _) in hailstones:
    assert x != 0
    assert vx != 0
    a = vy/vx
    b = y - a*x
    lines.append([a,b, [x,[-1,1][vx>0]]])

ans = 0
for ind1, l1 in enumerate(lines):
    for l2 in lines[ind1+1:]:
        if l1 == l2:
            if coord_in_range(l1, MIN_VALUE) * coord_in_range(l1, MAX_VALUE) <= 0:
                ans += 1
            continue
        if l1[0] == l2[0]:
            continue
        x = (l2[1]-l1[1])/(l1[0]-l2[0])
        y = l1[0]*x+l1[1]
        if not (MIN_VALUE <= x <= MAX_VALUE):
            continue
        if not (MIN_VALUE <= y <= MAX_VALUE):
            continue
        if (x-l1[2][0])*l1[2][1] < 0:
            continue
        if (x-l2[2][0])*l2[2][1] < 0:
            continue
        ans += 1

print(ans)