res = 0

lines = open('input.txt').readlines()
for line in lines:
    cubes = {'red':0, 'green':0, 'blue':0}
    line = line[line.find(':')+1:].strip() + ';'
    line = line.split()
    for i in range(0,len(line), 2):
        color = line[i+1][:-1]
        cubes[color] = max(cubes[color], int(line[i]))
    mult = 1
    for i in cubes.values():
        mult *= i
    res += mult

print(res)