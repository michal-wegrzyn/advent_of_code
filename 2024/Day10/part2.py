def trailhead_score(heights: list[list[int]], position: tuple[int, int]) -> int:
    if heights[position[0]][position[1]] == 9:
        return 1
    answer: int = 0
    new_position: tuple[int, int]
    for direction in ((-1, 0), (0, 1), (1, 0), (0, -1)):
        new_position = position[0] + direction[0], position[1] + direction[1]
        if (
            heights[position[0]][position[1]] + 1
            == heights[new_position[0]][new_position[1]]
        ):
            answer += trailhead_score(heights, new_position)

    return answer


def main() -> None:
    with open("input.txt") as file:
        topographic_map: list[str] = file.read().splitlines()

    heights: list[list[int]] = [[-2] * (len(topographic_map[0]) + 2)]
    for row in topographic_map:
        heights.append([-2] + [int(value) for value in row] + [-2])
    heights.append([-2] * (len(topographic_map[0]) + 2))

    print(
        sum(
            trailhead_score(heights, (r, c))
            for r in range(1, len(heights) - 1)
            for c in range(1, len(heights[0]) - 1)
            if heights[r][c] == 0
        )
    )


if __name__ == "__main__":
    main()
