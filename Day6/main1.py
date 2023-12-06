numbers = [[int(num) for num in line.split()[1:]] for line in open('input.txt').readlines()]

ans = 1
for i in range(len(numbers[0])):
    cnt = 0
    for v in range(numbers[0][i]):
        if v*(numbers[0][i]-v) > numbers[1][i]:
            cnt += 1
    ans *= cnt

print(ans)