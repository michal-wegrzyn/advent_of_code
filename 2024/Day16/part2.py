from typing import Tuple, Final, TypeAlias
from collections import defaultdict
import heapq

DIRECTIONS: Final = ((-1, 0), (0, 1), (1, 0), (0, -1))
Position: TypeAlias = Tuple[int, int]  # row, column
State: TypeAlias = Tuple[Position, int]  # position, direction index
Graph: TypeAlias = defaultdict[
    State, list[Tuple[int, State]]
]  # vertices: states, edges: Tuple[weight, neighbor state]


def move_straight(state: State) -> State:
    direction: Tuple[int, int] = DIRECTIONS[state[1]]
    return ((state[0][0] + direction[0], state[0][1] + direction[1]), state[1])


def rotate_clockwise(state: State) -> State:
    return state[0], (state[1] + 1) % 4


def rotate_counterclockwise(state: State) -> State:
    return state[0], (state[1] - 1) % 4


def create_graph(board: list[str]) -> Graph:
    graph: Graph = defaultdict(list)
    state: State
    new_state: State
    for r, row in enumerate(board):
        for c, value in enumerate(row):
            if value == "#":
                continue
            for d in range(4):
                state = ((r, c), d)
                graph[state].append((1000, rotate_clockwise(state)))
                graph[state].append((1000, rotate_counterclockwise(state)))
                new_state = move_straight(state)
                if board[new_state[0][0]][new_state[0][1]] != "#":
                    graph[state].append((1, new_state))

    return graph


def transpose_graph(graph: Graph) -> Graph:
    transposed_graph: Graph = defaultdict(list)
    for vertex, edges in graph.items():
        for weight, neighbor in edges:
            transposed_graph[neighbor].append((weight, vertex))
    return transposed_graph


def min_distances(graph: Graph, start: State) -> defaultdict[State, int]:
    assert all(distance >= 0 for values in graph.values() for distance, _ in values)

    min_distance: defaultdict[State, int] = defaultdict(lambda: -1)
    min_distance[start] = 0
    heap: list[tuple[int, State]] = [(0, start)]
    distance: int
    neighbor_distance: int
    while len(heap):
        state = heap[0][1]
        distance = heap[0][0]
        heapq.heappop(heap)
        if distance > min_distance[state]:
            continue
        for weight, neighbor in graph[state]:
            neighbor_distance = distance + weight
            if (
                min_distance[neighbor] == -1
                or min_distance[neighbor] > neighbor_distance
            ):
                min_distance[neighbor] = neighbor_distance
                heapq.heappush(heap, (neighbor_distance, neighbor))

    return min_distance


def states_on_any_shortest_path(
    graph: Graph, start: State, end: Position
) -> set[State]:
    min_distance: defaultdict[State, int] = min_distances(graph, start)
    transposed_graph: Graph = transpose_graph(graph)
    answer: set[State] = set()
    min_end_distance: int = min(min_distance[(end, d)] for d in range(4))
    if min_end_distance == -1:
        return set()
    waiting: list[State] = [
        (end, d) for d in range(4) if min_distance[(end, d)] == min_end_distance
    ]

    state: State
    distance: int

    while len(waiting):
        state = waiting[-1]
        waiting.pop(-1)
        if state in answer:
            continue
        answer.add(state)
        distance = min_distance[state]
        for weight, neighbor in transposed_graph[state]:
            if min_distance[neighbor] + weight == distance:
                waiting.append(neighbor)

    return answer


def positions_on_any_shortest_path(
    graph: Graph, start: State, end: Position
) -> set[Position]:
    states: set[State] = states_on_any_shortest_path(graph, start, end)
    return set(state[0] for state in states)


def main() -> None:
    with open("input.txt") as file:
        board: list[str] = file.read().splitlines()
    start: State = ((-1, -1), -1)
    end: Position = (-1, -1)
    for r, row in enumerate(board):
        for c, value in enumerate(row):
            if value == "S":
                start = ((r, c), 1)
            if value == "E":
                end = (r, c)

    assert start != ((-1, -1), -1)
    assert end != (-1, -1)

    graph: Graph = create_graph(board)
    answer: int = len(positions_on_any_shortest_path(graph, start, end))

    print(answer)


if __name__ == "__main__":
    main()
