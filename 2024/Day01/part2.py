from collections import Counter

def main():
    with open('input') as f:
        pairs: list[list[int,int]] = [[int(value) for value in line.split()] for line in f.readlines()]
    numbers1:list[int] = [pair[0] for pair in pairs]
    numbers2:list[int] = [pair[1] for pair in pairs]
    counter2:Counter = Counter(numbers2)
    answer:int = sum(value*counter2[value] for value in numbers1)
    print(answer)

if __name__ == '__main__':
    main()