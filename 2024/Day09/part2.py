import heapq


def sum_on_range(start: int, end: int) -> int:
    return end * (end - 1) // 2 - start * (start - 1) // 2


def main() -> None:
    with open("input.txt") as file:
        disk_map: str = file.read()

    disk: list[int] = [int(character) for character in disk_map]
    if len(disk) % 2 == 0:
        disk.pop(-1)
    positions: list[int] = [0]
    for i in disk[:-1]:
        positions.append(positions[-1] + i)

    free_spaces_postions: list[list[int]] = [[] for _ in range(10)]
    for i in range(1, len(disk), 2):
        free_spaces_postions[disk[i]].append(positions[i])

    disk = disk[::-2]
    positions = positions[::-2]
    file_id: int
    found: tuple[int, int] | None
    answer: int = 0

    for i, (position, length) in enumerate(zip(positions, disk)):
        file_id = len(disk) - 1 - i
        found = None
        for l in range(length, 10):
            if not free_spaces_postions[l]:
                continue
            if not free_spaces_postions[l][0] < position:
                continue
            if found is None or found[0] > free_spaces_postions[l][0]:
                found = (free_spaces_postions[l][0], l)
        if found is None:
            answer += sum_on_range(position, position + length) * file_id
            continue
        heapq.heappop(free_spaces_postions[found[1]])
        heapq.heappush(free_spaces_postions[found[1] - length], found[0] + length)
        answer += sum_on_range(found[0], found[0] + length) * file_id

    print(answer)


if __name__ == "__main__":
    main()
