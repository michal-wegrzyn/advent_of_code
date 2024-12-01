from math import pow, sqrt, ceil, floor

numbers = [int(''.join(line.split()[1:])) for line in open('input.txt').readlines()]

delta = pow(numbers[0],2)-4*numbers[1]

v1 = ceil((numbers[0]-sqrt(delta))/2)
v2 = floor((numbers[0]+sqrt(delta))/2)
print(v2-v1+1)