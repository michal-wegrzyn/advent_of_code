def main():
    with open('input') as file:
        number_lists:list[list[int]] = [[int(value) for value in line.split()] for line in file.readlines()]

    answer:int = 0
    ok:bool
    for numbers in number_lists:
        if len(numbers) <= 2:
            answer += 1
            continue

        candidates_for_removal:list[int] = []
        for i in range(len(numbers)-1):
            if numbers[i] == numbers[i+1]:
                candidates_for_removal = [i]
                break
        else:
            for i in range(1,len(numbers)-1):
                if (numbers[i-1] < numbers[i]) != (numbers[i] < numbers[i+1]):
                    candidates_for_removal = [i, i+1]
                    if i == 1:
                        candidates_for_removal.append(0)
                    break
            else:
                candidates_for_removal = [0, len(numbers)-1]
        
        ok = False
        for i in candidates_for_removal:
            nums:list[int] = numbers.copy()
            nums.pop(i)
            if not all((nums[0]-nums[1])*(i-j)>0 for i, j in zip(nums, nums[1:])):
                continue
            if all(abs(i-j)<=3 for i, j in zip(nums, nums[1:])):
                ok = True
                break
        answer += ok

    print(answer)

if __name__ == '__main__':
    main()