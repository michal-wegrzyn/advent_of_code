from collections import defaultdict

def main() -> None:
    with open('input.txt') as file:
        order_lines:list[str]
        update_lines:list[str]
        order_lines, update_lines = [group.split('\n') for group in file.read().split('\n\n')]

    order:list[list[int]] = [[int(number) for number in line.split('|')] for line in order_lines]
    updates:list[list[int]] = [[int(number) for number in line.split(',')] for line in update_lines]

    pages_after:defaultdict[int,set[int]] = defaultdict(set)
    for x, y in order:
        pages_after[x].add(y)
    
    answer:int = 0
    previous_pages:set

    for update in updates:
        previous_pages = set()
        for page in update:
            if previous_pages & pages_after[page]:
                break
            previous_pages.add(page)
        else:
            answer += update[len(update)//2]
    
    print(answer)


if __name__ == '__main__':
    main()