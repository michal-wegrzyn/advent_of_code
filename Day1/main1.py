res =0

for line in open('input.txt', 'r').readlines():
    first, second = -1, -1
    for i in line:
        if '0'<=i<='9':
            if first == -1:
                first = int(i)
            second = int(i)
    res += first*10+second

print(res)