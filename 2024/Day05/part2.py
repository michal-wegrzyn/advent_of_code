def topological_sort(values:list[int], pairs:list[list[int]]) -> list[int] | None:
    values_after:dict[int,set[int]] = {value:set() for value in values}
    values_before_count:dict[int,int] = {value:0 for value in values}
    for x, y in pairs:
        if x not in values or y not in values:
            continue
        values_after[x].add(y)
        values_before_count[y] += 1
    
    previous_values:set = set()
    for page in values:
        if previous_values & values_after[page]:
            break
        previous_values.add(page)
    else:
        return values
    
    sorted_values:list[int] = [value for value in values if values_before_count[value] == 0]
    it:int = 0
    while it < len(sorted_values):
        for page in values_after[sorted_values[it]]:
            values_before_count[page] -= 1
            if values_before_count[page] == 0:
                sorted_values.append(page)
        it += 1
    
    if len(sorted_values) != len(values):
        return None
    
    return sorted_values

def main() -> None:
    with open('input.txt') as file:
        order_lines:list[str]
        update_lines:list[str]
        order_lines, update_lines = [group.split('\n') for group in file.read().split('\n\n')]

    order:list[list[int]] = [[int(number) for number in line.split('|')] for line in order_lines]
    updates:list[list[int]] = [[int(number) for number in line.split(',')] for line in update_lines]
    answer:int = 0

    for update in updates:
        sorted_pages:list[int]|None = topological_sort(update, order)
        if sorted_pages is None:
            continue
        if sorted_pages == update:
            continue
        answer += sorted_pages[len(sorted_pages)//2]
    
    print(answer)


if __name__ == '__main__':
    main()