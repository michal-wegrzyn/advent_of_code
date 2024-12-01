from collections import Counter
pairs = [[int(value) for value in line.split()] for line in open('input').readlines()]
numbers1, numbers2 = zip(*pairs)
counter2 = Counter(numbers2)
print(sum(value*counter2[value] for value in numbers1))