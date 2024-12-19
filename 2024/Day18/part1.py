from itertools import islice
from collections import deque
from typing import Final, TypeAlias, Tuple, cast

Vertex: TypeAlias = Tuple[int, int]
Graph: TypeAlias = dict[Vertex, list[Vertex]]

DIRECTIONS: Final = ((-1, 0), (0, 1), (1, 0), (0, -1))


def move(vertex: Vertex, direction: Tuple[int, int]) -> Vertex:
    return vertex[0] + direction[0], vertex[1] + direction[1]


def create_graph(rows: int, columns: int, walls: set[tuple[int, ...]]) -> Graph:
    graph: Graph = {}
    vertex: Vertex
    neighbor: Vertex
    for r in range(rows + 1):
        for c in range(columns + 1):
            vertex = (c, r)
            if vertex in walls:
                continue
            graph[vertex] = []
            for direction in DIRECTIONS:
                neighbor = move(vertex, direction)
                if not 0 <= neighbor[0] <= rows:
                    continue
                if not 0 <= neighbor[1] <= columns:
                    continue
                if neighbor in walls:
                    continue
                graph[vertex].append(neighbor)
    return graph


def distance(graph: Graph, start: Vertex, end: Vertex) -> int:
    distances: dict[Vertex, int] = {vertex: -1 for vertex in graph}
    distances[start] = 0
    waiting: deque = deque([start])
    vertex: Vertex

    while waiting:
        vertex = waiting.popleft()
        for neighbor in graph[vertex]:
            if distances[neighbor] == -1:
                distances[neighbor] = distances[vertex] + 1
                waiting.append(neighbor)
                if neighbor == end:
                    return distances[end]

    return -1


def main() -> None:
    ROWS: Final = 70
    COLUMNS: Final = 70
    STEPS: Final = 1024
    with open("input.txt") as file:
        lines: islice[str] = islice(file, STEPS)
        coordinates: set[tuple[int, int]] = set(
            cast(Vertex, tuple(map(int, values)))
            for line in lines
            if len(values := line.split(",")) == 2
        )

    graph: Graph = create_graph(ROWS, COLUMNS, coordinates)
    start: Vertex = (0, 0)
    end: Vertex = (COLUMNS, ROWS)

    answer: int = distance(graph, start, end)
    if answer == -1:
        print("Exit not achievable")
    else:
        print(answer)


if __name__ == "__main__":
    main()
