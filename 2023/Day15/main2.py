def hash(text):
    res = 0
    for ch in text:
        res += ord(ch)
        res *= 17
        res %= 256
    return res

sequence = open('input.txt').read().strip().split(',')
boxes = [[] for _ in range(256)]

for step in sequence:
    label = step[:-1-(step[-2]=='=')]
    hsh = hash(label)
    pos = -1
    if label in [lens[0] for lens in boxes[hsh]]:
        pos = [lens[0] for lens in boxes[hsh]].index(label)

    if step[-1] == '-':
        if pos != -1:
            boxes[hsh].pop(pos)
    else:
        if pos == -1:
            boxes[hsh].append([label, int(step[-1])])
        else:
            boxes[hsh][pos][1] = int(step[-1])

ans = 0
for box_id, box in enumerate(boxes):
    for lens_id, lens in enumerate(box):
        ans += (box_id+1)*(lens_id+1)*lens[1]

print(ans)