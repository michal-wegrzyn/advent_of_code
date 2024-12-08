from collections import defaultdict
from typing import Tuple, Callable
from itertools import combinations
from math import gcd
from functools import partial

Pair = Tuple[int, int]


def is_nonnegative_index(index: Pair, liststr: list[str]) -> bool:
    row, col = index
    return 0 <= row < len(liststr) and 0 <= col < len(liststr[row])


def main() -> None:
    with open("input.txt") as file:
        board: list[str] = file.read().splitlines()

    antennas: defaultdict[str, set[Pair]] = defaultdict(set)
    for i, line in enumerate(board):
        for j, value in enumerate(line):
            if value != ".":
                antennas[value].add((i, j))

    isOnBoard: Callable[[Pair], bool] = partial(is_nonnegative_index, liststr=board)

    antinodes: set[Pair] = set()
    d: int
    difference: Pair
    step: Pair
    point: Pair

    for points in antennas.values():
        for point1, point2 in combinations(points, 2):
            difference = point1[0] - point2[0], point1[1] - point2[1]
            d = gcd(*difference)
            step = difference[0] // d, difference[1] // d
            point = point1
            while isOnBoard(point):
                antinodes.add(point)
                point = point[0] + step[0], point[1] + step[1]
            point = point1
            while isOnBoard(point):
                antinodes.add(point)
                point = point[0] - step[0], point[1] - step[1]

    print(len(antinodes))


if __name__ == "__main__":
    main()
