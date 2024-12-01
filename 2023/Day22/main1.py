bricks = sorted([sorted([[int(num) for num in coords.split(',')] for coords in line.split('~')]) for line in open('input.txt').read().strip().split('\n')], key=lambda x: x[0][2])
disintegratable = [1]*len(bricks)
max_x = max(brick[1][0] for brick in bricks) + 1
max_y = max(brick[1][1] for brick in bricks) + 1
height = [[0]*max_y for _ in range(max_x)]
current_brick = [[-1]*max_y for _ in range(max_x)]

for ind, brick in enumerate(bricks):
    heights = [height[row][column] for row in range(brick[0][0], brick[1][0]+1) for column in range(brick[0][1], brick[1][1]+1)]
    max_height = max(heights)
    if max_height > 0:
        supporting_bricks = set()
        for row in range(brick[0][0], brick[1][0]+1):
            for column in range(brick[0][1], brick[1][1]+1):
                if height[row][column] == max_height:
                    supporting_bricks.add(current_brick[row][column])
        if len(supporting_bricks) == 1:
            disintegratable[min(supporting_bricks)] = 0
    new_height = max_height + brick[1][2] - brick[0][2] + 1
    for row in range(brick[0][0], brick[1][0]+1):
        for column in range(brick[0][1], brick[1][1]+1):
            height[row][column] = new_height
            current_brick[row][column] = ind

# print(only_supporting)
print(disintegratable.count(1))