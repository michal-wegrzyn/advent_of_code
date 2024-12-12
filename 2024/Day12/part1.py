def find_area_and_perimeter(
    garden: list[str], visited: list[list[bool]], start_x: int, start_y: int
) -> tuple[int, int]:
    if visited[start_x][start_y]:
        return 0, 0
    visited[start_x][start_y] = True

    area: int = 1
    perimeter: int = 0
    adjacent_x: int
    adjacent_y: int
    adjacent_area: int
    adjacent_perimeter: int

    for direction_x, direction_y in ((-1, 0), (0, 1), (1, 0), (0, -1)):
        adjacent_x = start_x + direction_x
        adjacent_y = start_y + direction_y
        if garden[adjacent_x][adjacent_y] != garden[start_x][start_y]:
            perimeter += 1
            continue
        if visited[adjacent_x][adjacent_y]:
            continue
        adjacent_area, adjacent_perimeter = find_area_and_perimeter(
            garden, visited, adjacent_x, adjacent_y
        )
        area += adjacent_area
        perimeter += adjacent_perimeter

    return area, perimeter


def main() -> None:
    with open("input.txt") as file:
        garden: list[str] = ["/" + line + "/" for line in file.read().splitlines()]
    garden = ["/" * len(garden[0])] + garden + ["/" * len(garden[0])]
    visited: list[list[bool]] = [[False] * len(garden[i]) for i in range(len(garden))]

    area: int
    perimeter = 0
    answer: int = 0

    for x in range(1, len(garden) - 1):
        for y in range(1, len(garden[0]) - 1):
            if visited[x][y]:
                continue
            area, perimeter = find_area_and_perimeter(garden, visited, x, y)
            answer += area * perimeter

    print(answer)


if __name__ == "__main__":
    main()
