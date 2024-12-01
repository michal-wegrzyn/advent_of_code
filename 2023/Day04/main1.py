lines = open('input.txt').readlines()

ans = 0

for line in lines:
    words = line.strip().split()[2:]
    winning = words[:words.index('|')]
    cnt = 0
    for i in range(words.index('|')+1, len(words)):
        if words[i] in winning:
            cnt += 1
    
    if cnt > 0:
        ans += pow(2,cnt-1)

print(ans)