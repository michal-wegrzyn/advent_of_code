res =0

numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

for line in open('input.txt', 'r').readlines():
    line += '/////'
    first, second = -1, -1
    for i in range(len(line)-5):
        if '0'<=line[i]<='9':
            if first == -1:
                first = int(line[i])
            second = int(line[i])
        for num in range(1,10):
            if line[i:i+len(numbers[num-1])] == numbers[num-1]:
                if first == -1:
                    first = num
                second = num
    res += first*10+second

print(res)