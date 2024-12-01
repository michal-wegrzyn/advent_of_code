lines = open('input.txt').readlines()
for i in range(len(lines)):
    lines[i] = '..' + lines[i].strip() + '.'

lines.insert(0,'.'*len(lines[0]))
lines.insert(0,'.'*len(lines[0]))
lines.append('.'*len(lines[0]))

prefix_sum = [[0 for _ in range(len(lines[0]))] for _ in range(len(lines))]

for r in range(2,len(lines)):
    for c in range(2, len(lines[0])):
        prefix_sum[r][c] = prefix_sum[r-1][c] + prefix_sum[r][c-1] - prefix_sum[r-1][c-1]
        if (not '0'<=lines[r][c]<='9') and lines[r][c] != '.':
            prefix_sum[r][c] += 1

num = 0
st = -1
ans = 0

for r in range(2,len(lines)):
    for c in range(2, len(lines[0])):
        if '0'<=lines[r][c]<='9':
            num *= 10
            num += int(lines[r][c])
            if st == -1:
                st = c
        else:
            if st == -1:
                continue
            if prefix_sum[r+1][c] - prefix_sum[r+1][st-2] - prefix_sum[r-2][c] + prefix_sum[r-2][st-2] > 0:
                ans += num
            num = 0
            st = -1

print(ans)