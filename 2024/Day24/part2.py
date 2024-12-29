from collections import defaultdict


def main() -> None:
    with open("input.txt") as file:
        gates_text: str
        _, gates_text = file.read().split("\n\n")

    resolves: defaultdict[str, list[str]] = defaultdict(list)
    definitions: dict[str, tuple[str, str, str]] = {}
    gate_input: str
    gate_output: str
    name1: str
    operatation: str
    name2: str

    for gate in gates_text.splitlines():
        gate_input, gate_output = gate.split(" -> ")
        name1, operatation, name2 = gate_input.split(" ")
        definitions[gate_output] = (operatation, name1, name2)
        resolves[name1].append(gate_output)
        resolves[name2].append(gate_output)

    # Full adder scheme
    # x_i    a_i = x_i ^ y_i    z_i = a_i ^ c_i
    # y_i    b_i = a_i & c_i
    # c_i    d_i = x_i & y_i    c_i+1 = b_i | d_i

    name3: str
    last_z = max(name for name in definitions if name[0] == "z")
    wrong: set[str] = set()

    for name, (operatation, name1, name2) in definitions.items():
        if operatation == "XOR" and all(
            name3[0] not in "xyz" for name3 in (name, name1, name2)
        ):
            wrong.add(name)
        if name[0] == "z" and name != last_z and operatation != "XOR":
            wrong.add(name)
        if operatation == "XOR":
            for name3 in resolves[name]:
                if definitions[name3][0] == "OR":
                    wrong.add(name)
        if operatation == "AND" and {"x00", "y00"} != {name1, name2}:
            for name3 in resolves[name]:
                if definitions[name3][0] != "OR":
                    wrong.add(name)

    print(",".join(sorted(wrong)))


if __name__ == "__main__":
    main()
