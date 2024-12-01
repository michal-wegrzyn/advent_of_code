lines = open('input.txt').readlines() + ['\n']

groups = [[int(i) for i in lines[0].split()[1:]]]*8

for num in range(len(groups[0])):
    line_id = 3
    for group_id in range(0,7):
        changed = False
        while lines[line_id] != '\n':
            if changed:
                line_id += 1
                continue
            start1, start2, length = [int(i) for i in lines[line_id].split()]
            if start2 <= groups[group_id][num] < start2 + length:
                groups[group_id+1][num] += start1 - start2
                changed = True
            line_id += 1
        line_id += 2

print(min(groups[-1]))