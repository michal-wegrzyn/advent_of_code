from collections import defaultdict
from typing import Final, TypeAlias, Tuple, Generator

Vertex: TypeAlias = Tuple[int, int]
DIRECTIONS: Final = ((-1, 0), (0, 1), (1, 0), (0, -1))


def move(vertex: Vertex, direction: Tuple[int, int]) -> Vertex:
    return vertex[0] + direction[0], vertex[1] + direction[1]


def neighbors(vertex: Vertex, board: list[str]) -> Generator[Vertex, None, None]:
    neighbor: Vertex
    for d in DIRECTIONS:
        neighbor = move(vertex, d)
        if board[neighbor[0]][neighbor[1]] != "#":
            yield neighbor


def hacked_neighbors(vertex: Vertex, board: list[str]) -> Generator[Vertex, None, None]:
    neighbor: Vertex
    for i, d in enumerate(DIRECTIONS):
        for d2 in (DIRECTIONS[i], DIRECTIONS[i - 1]):
            neighbor = move(move(vertex, d), d2)
            if not 0 <= neighbor[0] < len(board):
                continue
            if not 0 <= neighbor[1] < len(board[neighbor[0]]):
                continue
            if board[neighbor[0]][neighbor[1]] != "#":
                yield neighbor


def distance_from_start(
    start: Vertex, end: Vertex, board: list[str]
) -> defaultdict[Vertex, int]:
    vertex: Vertex = start
    previous: Vertex = (-1, -1)
    distances: defaultdict[Vertex, int] = defaultdict(lambda: -1)
    distance: int = 0
    distances[start] = distance
    distance += 1
    while vertex != end:
        for neighbor in neighbors(vertex, board):
            if neighbor == previous:
                continue
            previous = vertex
            vertex = neighbor
            distances[vertex] = distance
            distance += 1
            break
    return distances


def main() -> None:
    with open("input.txt") as file:
        board: list[str] = file.read().splitlines()

    start: Vertex = (-1, -1)
    end: Vertex = (-1, -1)
    for r, line in enumerate(board):
        if (c := line.find("S")) != -1:
            start = (r, c)
        if (c := line.find("E")) != -1:
            end = (r, c)

    answer: int = 0
    distances: defaultdict[Vertex, int] = distance_from_start(start, end, board)
    for vertex, distance in distances.items():
        for hacked_neighbor in hacked_neighbors(vertex, board):
            if distances[hacked_neighbor] >= distance + 2 + 100:
                answer += 1

    print(answer)


if __name__ == "__main__":
    main()
