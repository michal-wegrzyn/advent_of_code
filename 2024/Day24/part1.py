from collections import defaultdict


def main() -> None:
    with open("input.txt") as file:
        values_text: str
        gates_text: str
        values_text, gates_text = file.read().split("\n\n")

    values: dict[str, int] = {}
    deg_in: dict[str, int] = {}
    resolves: defaultdict[str, list[str]] = defaultdict(list)
    definitions: dict[str, tuple[str, str, str] | int] = {}
    gate_input: str
    gate_output: str
    name1: str
    operatation: str
    name2: str
    for gate in gates_text.splitlines():
        gate_input, gate_output = gate.split(" -> ")
        name1, operatation, name2 = gate_input.split(" ")
        definitions[gate_output] = (operatation, name1, name2)
        deg_in[gate_output] = 2
        resolves[name1].append(gate_output)
        resolves[name2].append(gate_output)

    name: str
    value_str: str
    for value_line in values_text.splitlines():
        name, value_str = value_line.split(": ")
        definitions[name] = int(value_str)
        deg_in[name] = 0

    waiting: list[str] = [name for name, value in deg_in.items() if value == 0]
    toposort: list[str] = []
    while len(waiting):
        name = waiting[-1]
        waiting.pop(-1)
        toposort.append(name)
        for name2 in resolves[name]:
            deg_in[name2] -= 1
            if deg_in[name2] == 0:
                waiting.append(name2)

    definition: tuple[str, str, str] | int
    for name in toposort:
        definition = definitions[name]
        if isinstance(definition, int):
            values[name] = definition
        elif definition[0] == "AND":
            name1, name2 = definition[1:]
            values[name] = values[name1] & values[name2]
        elif definition[0] == "OR":
            name1, name2 = definition[1:]
            values[name] = values[name1] | values[name2]
        elif definition[0] == "XOR":
            name1, name2 = definition[1:]
            values[name] = values[name1] ^ values[name2]

    answer: int = 0
    pow2 = 1
    for name, value in sorted(
        (name, value) for name, value in values.items() if name[0] == "z"
    ):
        answer += value * pow2
        pow2 *= 2

    print(answer)


if __name__ == "__main__":
    main()
