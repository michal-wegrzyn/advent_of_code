lines = open('input.txt').readlines()

cnt_cards = [1]*len(lines)

for id, line in enumerate(lines):
    words = line.strip().split()[2:]
    winning = words[:words.index('|')]
    cnt = 0
    for i in range(words.index('|')+1, len(words)):
        if words[i] in winning:
            cnt += 1
    
    for i in range(1,cnt+1):
        cnt_cards[id+i] += cnt_cards[id]

print(sum(cnt_cards))