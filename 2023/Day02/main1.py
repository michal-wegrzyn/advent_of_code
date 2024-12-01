res = 0

lines = open('input.txt').readlines()
id = 0

for line in lines:
    id += 1
    cubes = {'red':0, 'green':0, 'blue':0}
    line = line[line.find(':')+1:].strip() + ';'
    line = line.split()
    for i in range(0,len(line), 2):
        color = line[i+1][:-1]
        cubes[color] = max(cubes[color], int(line[i]))
    if cubes['red'] <= 12 and cubes['green'] <= 13 and cubes['blue'] <= 14:
        res += id

print(res)