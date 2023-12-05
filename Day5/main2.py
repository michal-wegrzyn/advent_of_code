groups = open('input.txt').read().strip().split('\n\n')

seeds = [int(i) for i in groups[0].split()[1:]]
groups.pop(0)

intervals = [[[seeds[i], seeds[i]+seeds[i+1]-1] for i in range(0,len(seeds),2)]]
split_points = []

for i in range(len(groups)):
    split_points.append([])
    groups[i] = groups[i].split('\n')[1:]
    for j in range(len(groups[i])):
        groups[i][j] = [int(k) for k in groups[i][j].split()]
        # print(groups[i][j])
        split_points[i].append(groups[i][j][1])
        split_points[i].append(groups[i][j][1] + groups[i][j][2])

    split_points[i] = sorted(list(set(split_points[i])))
    intervals.append([])

    for interval in intervals[-2]:
        for point in split_points[-1]:
            if interval[1] < point:
                break
            if interval[0] < point:
                intervals[-1].append([interval[0], point-1])
                interval[0] = point
        intervals[-1].append(interval)
    for ind in range(len(intervals[-1])):
        for j in range(len(groups[i])):
            if groups[i][j][1] <= intervals[-1][ind][0] < groups[i][j][1] + groups[i][j][2]:
                intervals[-1][ind][0] += groups[i][j][0] - groups[i][j][1]
                intervals[-1][ind][1] += groups[i][j][0] - groups[i][j][1]
                break

    # print(split_points[-1])
    # print(intervals[-1])

ans = intervals[-1][0][0]
for i in intervals[-1]:
    ans = min(ans, i[0])

print(ans)