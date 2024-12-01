lines = [['.'+'?'.join([line.split()[0]]*5)+'.', [int(num) for num in line.split()[1].split(',')]*5] for line in open('input.txt').read().strip().split('\n')]

ans = 0

for line in lines:
    pattern = [0]
    for num in line[1]:
        pattern += [1]*num + [0]
    
    dp = [[1]+[0]*(len(pattern)-1)]
    for char in line[0]:
        dp.append([0]*len(pattern))
        if char == '#':
            dp[-1][0] = 0
        else:
            dp[-1][0] = dp[-2][0]
        
        for i in range(1, len(pattern)):
            if pattern[i] == 0 and char in ['.', '?']:
                dp[-1][i] += dp[-2][i-1]
                dp[-1][i] += dp[-2][i]
            if pattern[i] == 1 and char in ['#', '?']:
                dp[-1][i] += dp[-2][i-1]        
    
    ans += dp[-1][-1]

print(ans)