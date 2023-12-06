from math import pow, sqrt, ceil, floor

numbers = [int(''.join(line.split()[1:])) for line in open('input.txt').readlines()]

delta = pow(numbers[0],2)-4*numbers[1]

v1 = max(ceil((numbers[0]-sqrt(delta))/2),0)
v2 = min(floor((numbers[0]+sqrt(delta))/2), numbers[0])
print(v2-v1+1)