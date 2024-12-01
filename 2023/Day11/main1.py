board = open('input.txt').read().strip().split('\n')

ans = 0

for b in [board, zip(*board)]:
    dist_sum = 0
    galaxies_count = []
    galaxies_cnt = 0
    for group in b:
        cnt = group.count('#')
        dist_sum += len(galaxies_count)*cnt
        galaxies_count.append(cnt)
        galaxies_cnt += cnt
        if cnt == 0:
            galaxies_count.append(0)

    for i, v in enumerate(galaxies_count):
        dist_sum -= i*v
        galaxies_cnt -= v
        ans += (dist_sum - i*galaxies_cnt)*v

print(ans)