lines = open('input.txt').readlines()
for i in range(len(lines)):
    lines[i] = '.' + lines[i].strip() + '.'

lines.insert(0,'.'*len(lines[0]))
lines.append('.'*len(lines[0]))

numbers = [[-1 for _ in range(len(lines[0]))] for _ in range(len(lines))]

num = 0
st = -1

for r in range(1,len(lines)):
    for c in range(1, len(lines[0])):
        if '0'<=lines[r][c]<='9':
            num *= 10
            num += int(lines[r][c])
            if st == -1:
                st = c
        else:
            if st == -1:
                continue
            for i in range(st, c):
                numbers[r][i] = num
            num = 0
            st = -1

ans = 0

for r in range(1,len(lines)-1):
    for c in range(1, len(lines[0])-1):
        if lines[r][c] != '*':
            continue
        cnt = 0
        mult = 1

        for rr in range(r-1,r+2):
            for cc in range(c-1,c+2):
                if numbers[rr][cc] == -1:
                    continue
                if cc != c-1 and numbers[rr][cc-1] != -1:
                    continue
                cnt += 1
                mult *= numbers[rr][cc]
        
        if cnt != 2:
            continue
        ans += mult

print(ans)