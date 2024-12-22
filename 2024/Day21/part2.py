from collections import defaultdict
from enum import Enum


class KeypadType(Enum):
    NUMERIC = "NUMERIC"
    DIRECTIONAL = "DIRECTIONAL"


def difference(
    position1: tuple[int, int], position2: tuple[int, int]
) -> tuple[int, int]:
    return position1[0] - position2[0], position1[1] - position2[1]


def code_to_pairs_count(code: str, start: str = "A") -> defaultdict[str, int]:
    answer: defaultdict[str, int] = defaultdict(int)
    for operation in code:
        answer[start + operation] += 1
        start = operation
    return answer


def preferenced_order(
    operations: str, chain_length: int, memo: list[list[str]] = [["^<", "v>", "v<"]]
) -> str:
    assert operations in ["^>", "^<", "v>", "v<"]
    if len(memo) <= chain_length:
        for chain_len in range(len(memo) - 1, chain_length):
            memo.append([])
            for s in ["^>", "^<", "v>", "v<"]:
                if operate_keypad_length(
                    KeypadType.DIRECTIONAL, s + "A", chain_len
                ) <= operate_keypad_length(
                    KeypadType.DIRECTIONAL,
                    s[::-1] + "A",
                    chain_len,
                ):
                    memo[-1].append(s)

    return operations if operations in memo[chain_length] else operations[::-1]


def operate_keypad_length(
    keypad_type: KeypadType, code: str | defaultdict[str, int], chain_length: int
) -> int:
    previous: str = "A"
    new_code: str
    distance: tuple[int, int]
    operations: str
    result: defaultdict[str, int]
    answer: defaultdict[str, int] = defaultdict(int)
    button_position: dict[str, tuple[int, int]]
    if keypad_type == KeypadType.NUMERIC:
        button_position = {
            "7": (0, 0),
            "8": (0, 1),
            "9": (0, 2),
            "4": (1, 0),
            "5": (1, 1),
            "6": (1, 2),
            "1": (2, 0),
            "2": (2, 1),
            "3": (2, 2),
            "0": (3, 1),
            "A": (3, 2),
        }
    else:
        button_position = {
            "^": (0, 1),
            "A": (0, 2),
            "<": (1, 0),
            "v": (1, 1),
            ">": (1, 2),
        }
    pairs_count: defaultdict[str, int]
    if isinstance(code, str):
        pairs_count = code_to_pairs_count(code)
    else:
        pairs_count = code
    pair: str
    for pair, count in pairs_count.items():
        previous, button = pair[0], pair[1]
        new_code = ""
        if button == previous:
            answer["AA"] += count
            continue
        distance = difference(button_position[button], button_position[previous])
        if distance[1] == 0:
            if distance[0] > 0:
                new_code += "v" * distance[0]
            else:
                new_code += "^" * (-distance[0])
        elif distance[0] == 0:
            if distance[1] > 0:
                new_code += ">" * distance[1]
            else:
                new_code += "<" * (-distance[1])
        else:
            operations = ""
            if (
                keypad_type == KeypadType.NUMERIC
                and button in "0A"
                and previous in "741"
            ):
                operations = ">v"
            elif (
                keypad_type == KeypadType.NUMERIC
                and button in "741"
                and previous in "0A"
            ):
                operations = "v<"
            elif (
                keypad_type == KeypadType.DIRECTIONAL
                and button in "^A"
                and previous == "<"
            ):
                operations = ">^"
            elif (
                keypad_type == KeypadType.DIRECTIONAL
                and button == "<"
                and previous in "^A"
            ):
                operations = "v<"
            else:
                if distance[0] > 0:
                    operations += "^"
                else:
                    operations += "v"

                if distance[1] > 0:
                    operations += ">"
                else:
                    operations += "<"
                operations = preferenced_order(operations, chain_length)
            if operations[0] in "v^":
                if distance[0] > 0:
                    new_code += "v" * distance[0]
                else:
                    new_code += "^" * (-distance[0])
                if distance[1] > 0:
                    new_code += ">" * distance[1]
                else:
                    new_code += "<" * (-distance[1])
            else:
                if distance[1] > 0:
                    new_code += ">" * distance[1]
                else:
                    new_code += "<" * (-distance[1])
                if distance[0] > 0:
                    new_code += "v" * distance[0]
                else:
                    new_code += "^" * (-distance[0])

        new_code += "A"
        result = code_to_pairs_count(new_code)
        for key, value in result.items():
            answer[key] += value * count

    if chain_length == 0:
        return sum(answer.values())
    return operate_keypad_length(KeypadType.DIRECTIONAL, answer, chain_length - 1)


def main() -> None:
    with open("input.txt") as file:
        codes: list[str] = file.read().splitlines()

    numeric_part: int
    answer: int = 0

    for code in codes:
        numeric_part = int(code[:-1])
        answer += operate_keypad_length(KeypadType.NUMERIC, code, 25) * numeric_part

    print(answer)


if __name__ == "__main__":
    main()
