lines = [[i.split()[0], int(i.split()[1])] for i in open('input.txt').readlines()]

for i in range(len(lines)):
    cnt = []
    for card in lines[i][0]:
        cnt.append(lines[i][0].count(card))
    cnt = sorted(cnt)
    if cnt == [5,5,5,5,5]:
        lines[i][0] = '6' + lines[i][0]
    elif cnt == [1,4,4,4,4]:
        lines[i][0] = '5' + lines[i][0]
    elif cnt == [2,2,3,3,3]:
        lines[i][0] = '4' + lines[i][0]
    elif cnt == [1,1,3,3,3]:
        lines[i][0] = '3' + lines[i][0]
    elif cnt == [1,2,2,2,2]:
        lines[i][0] = '2' + lines[i][0]
    elif cnt == [1,1,1,2,2]:
        lines[i][0] = '1' + lines[i][0]
    else:
        lines[i][0] = '0' + lines[i][0]
    lines[i][0] = lines[i][0].replace('T','a')
    lines[i][0] = lines[i][0].replace('J','b')
    lines[i][0] = lines[i][0].replace('Q','c')
    lines[i][0] = lines[i][0].replace('K','d')
    lines[i][0] = lines[i][0].replace('A','e')

lines = sorted(lines)

ans = 0
for i in range(len(lines)):
    ans += (i+1)*lines[i][1]

print(ans)