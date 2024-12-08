from collections import defaultdict
from typing import Tuple, Callable
from functools import partial

Pair = Tuple[int, int]


def is_nonnegative_index(index: Pair, liststr: list[str]) -> bool:
    row, col = index
    return 0 <= row < len(liststr) and 0 <= col < len(liststr[row])


def reflectAboutPoint(center_point: Pair, point_to_reflect: Pair) -> Pair:
    return (
        center_point[0] * 2 - point_to_reflect[0],
        center_point[1] * 2 - point_to_reflect[1],
    )


def main() -> None:
    with open("input.txt") as file:
        board: list[str] = file.read().splitlines()

    antennas: defaultdict[str, set[Pair]] = defaultdict(set)
    for i, line in enumerate(board):
        for j, value in enumerate(line):
            if value != ".":
                antennas[value].add((i, j))

    isOnBoard: Callable[[Pair], bool] = partial(is_nonnegative_index, liststr=board)
    point: Pair
    antinodes: set[Pair] = set()

    for points in antennas.values():
        for point1 in points:
            for point2 in points:
                if point1 == point2:
                    continue
                point = reflectAboutPoint(point1, point2)
                if isOnBoard(point):
                    antinodes.add(point)

    print(len(antinodes))


if __name__ == "__main__":
    main()
