from collections import defaultdict
from typing import Callable


def main() -> None:
    with open("input.txt") as file:
        connections: list[list[str]] = [
            line.split("-") for line in file.read().splitlines()
        ]

    name_key: Callable[[str], tuple[bool, str]] = lambda name: (name[0] != "t", name)
    graph: defaultdict[str, set[str]] = defaultdict(set)
    for connection in connections:
        connection = sorted(connection, key=name_key)
        graph[connection[0]].add(connection[1])

    answer: int = 0

    for name1 in sorted(graph.keys(), key=name_key):
        if name1[0] != "t":
            break
        for name2 in graph[name1]:
            answer += len(graph[name1] & graph[name2])

    print(answer)


if __name__ == "__main__":
    main()
