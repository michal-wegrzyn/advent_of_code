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
    adjacent_perpendicularly: tuple[tuple[int, int], tuple[int, int]]
    adjacent_area: int
    adjacent_perimeter: int
    border_count: int
    current_plant: str = garden[start_x][start_y]

    for direction_x, direction_y in ((-1, 0), (0, 1), (1, 0), (0, -1)):
        adjacent_x = start_x + direction_x
        adjacent_y = start_y + direction_y
        if garden[adjacent_x][adjacent_y] == current_plant:
            continue

        border_count = 1
        adjacent_perpendicularly = (
            (start_x + direction_y, start_y - direction_x),
            (start_x - direction_y, start_y + direction_x),
        )

        for adjacent_x2, adjacent_y2 in adjacent_perpendicularly:
            if (
                visited[adjacent_x2][adjacent_y2]
                and garden[adjacent_x2][adjacent_y2] == current_plant
                and garden[adjacent_x2 + direction_x][adjacent_y2 + direction_y]
                != current_plant
            ):
                border_count -= 1

        perimeter += border_count

    for direction_x, direction_y in ((-1, 0), (0, 1), (1, 0), (0, -1)):
        adjacent_x = start_x + direction_x
        adjacent_y = start_y + direction_y
        if garden[adjacent_x][adjacent_y] != current_plant:
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
    perimeter: int
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
