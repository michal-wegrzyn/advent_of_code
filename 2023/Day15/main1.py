def hash(text):
    res = 0
    for ch in text:
        res += ord(ch)
        res *= 17
        res %= 256
    return res

sequence = open('input.txt').read().strip().split(',')

ans = sum(hash(step) for step in sequence)
print(ans)