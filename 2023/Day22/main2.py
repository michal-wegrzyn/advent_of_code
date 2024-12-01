bricks = sorted([sorted([[int(num) for num in coords.split(',')] for coords in line.split('~')]) for line in open('input.txt').read().strip().split('\n')], key=lambda x: x[0][2])
supported_by = [set() for _ in bricks]
supporting = [set() for _ in bricks]
max_x = max(brick[1][0] for brick in bricks) + 1
max_y = max(brick[1][1] for brick in bricks) + 1
height = [[0]*max_y for _ in range(max_x)]
current_brick = [[-1]*max_y for _ in range(max_x)]


for ind, brick in enumerate(bricks):
    max_height = max(height[row][column] for row in range(brick[0][0], brick[1][0]+1) for column in range(brick[0][1], brick[1][1]+1))
    if max_height > 0:
        for row in range(brick[0][0], brick[1][0]+1):
            for column in range(brick[0][1], brick[1][1]+1):
                if height[row][column] == max_height:
                    supported_by[ind].add(current_brick[row][column])
                    supporting[current_brick[row][column]].add(ind)
    new_height = max_height + brick[1][2] - brick[0][2] + 1
    for row in range(brick[0][0], brick[1][0]+1):
        for column in range(brick[0][1], brick[1][1]+1):
            height[row][column] = new_height
            current_brick[row][column] = ind


ans = 0
for brick in range(len(bricks)):
    disintegrated = {brick}
    for b in range(brick+1, len(bricks)):
        if supported_by[b].issubset(disintegrated) and supported_by[b]!=set():
            disintegrated.add(b)
            ans += 1

print(ans)