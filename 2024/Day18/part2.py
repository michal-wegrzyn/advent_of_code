from collections import deque
from typing import Final, TypeAlias, Tuple, cast

Vertex: TypeAlias = Tuple[int, int]
Graph: TypeAlias = dict[Vertex, list[Vertex]]
Achievable: TypeAlias = dict[Vertex, bool]

DIRECTIONS: Final = ((-1, 0), (0, 1), (1, 0), (0, -1))


def move(vertex: Vertex, direction: Tuple[int, int]) -> Vertex:
    return vertex[0] + direction[0], vertex[1] + direction[1]


def is_within_boundaries(vertex: Vertex, rows: int, columns: int):
    return 0 <= vertex[0] <= columns and 0 <= vertex[1] <= rows


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
                if not is_within_boundaries(neighbor, rows, columns):
                    continue
                if neighbor in walls:
                    continue
                graph[vertex].append(neighbor)
    return graph


def achievable_vertices(graph: Graph, start: Vertex) -> Achievable:
    achievable: Achievable = {vertex: False for vertex in graph}
    achievable[start] = True
    update_achievable(start, graph, achievable)

    return achievable


def add_vertex(vertex: Vertex, graph: Graph, achievable: Achievable) -> None:
    neighbor: Vertex
    is_achievable: bool = False
    graph[vertex] = []
    achievable[vertex] = False

    for direction in DIRECTIONS:
        neighbor = move(vertex, direction)
        if not neighbor in graph:
            continue
        graph[vertex].append(neighbor)
        graph[neighbor].append(vertex)
        if achievable[neighbor]:
            is_achievable = True

    if is_achievable:
        update_achievable(vertex, graph, achievable)


def update_achievable(vertex: Vertex, graph: Graph, achievable: Achievable) -> None:
    achievable[vertex] = True
    waiting: deque = deque([vertex])

    while waiting:
        vertex = waiting.popleft()
        for neighbor in graph[vertex]:
            if not achievable[neighbor]:
                achievable[neighbor] = True
                waiting.append(neighbor)


def main() -> None:
    ROWS: Final = 70
    COLUMNS: Final = 70
    with open("input.txt") as file:
        lines: list[str] = file.readlines()
        coordinates: list[tuple[int, int]] = [
            cast(Vertex, tuple(map(int, values)))
            for line in lines
            if len(values := line.split(",")) == 2
        ]

    start: Vertex = (0, 0)
    end: Vertex = (COLUMNS, ROWS)
    index: int = len(coordinates)
    graph: Graph = create_graph(ROWS, COLUMNS, set(coordinates))
    achievable: Achievable = achievable_vertices(graph, start)
    vertex: Vertex = (-1, -1)

    while index and achievable[end] == False:
        index -= 1
        vertex = coordinates[index]
        add_vertex(vertex, graph, achievable)

    if vertex == (-1, -1):
        print("Exit achievable until the end")
    else:
        print(f"{vertex[0]},{vertex[1]}")


if __name__ == "__main__":
    main()
