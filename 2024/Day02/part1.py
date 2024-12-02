def main():
    with open('input') as file:
        number_lists:list[list[int]] = [[int(value) for value in line.split()] for line in file.readlines()]
    answer:int = 0
    for numbers in number_lists:
        if not all((numbers[0]-numbers[1])*(i-j)>0 for i, j in zip(numbers, numbers[1:])):
            continue
        if all(abs(i-j)<=3 for i, j in zip(numbers, numbers[1:])):
            answer += 1

    print(answer)

if __name__ == '__main__':
    main()