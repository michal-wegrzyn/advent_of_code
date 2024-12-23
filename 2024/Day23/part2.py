import networkx as nx


def main() -> None:
    with open("input.txt") as file:
        connections: list[list[str]] = [
            line.split("-") for line in file.read().splitlines()
        ]

    graph: nx.Graph = nx.Graph()
    graph.add_edges_from(connections)
    largest_clique: list[str] = max(nx.find_cliques(graph), key=len)

    print(",".join(sorted(largest_clique)))


if __name__ == "__main__":
    main()
