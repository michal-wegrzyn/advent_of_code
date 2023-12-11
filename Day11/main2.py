board = open('input.txt').read().strip().split('\n')

ans = 0

for b in [board, zip(*board)]:
    dist_sum = 0
    galaxies_count = []
    galaxies_cnt = 0
    pos = 0
    for group in b:
        cnt = group.count('#')
        dist_sum += pos*cnt
        galaxies_count.append([pos, cnt])
        galaxies_cnt += cnt
        if cnt != 0:
            pos += 1
        else:
            pos += 1000000

    for i, v in galaxies_count:
        dist_sum -= i*v
        galaxies_cnt -= v
        ans += (dist_sum - i*galaxies_cnt)*v

print(ans)