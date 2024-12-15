def main() -> None:
    with open("input.txt") as file:
        board_text: str
        instructions_text: str
        board_text, instructions_text = file.read().split("\n\n")
    board_lines: list[str] = board_text.split("\n")
    instructions: str = "".join(instructions_text.splitlines())
    item_value: dict[str, int] = {".": 0, "O": 1, "#": 2, "@": 0}
    board: list[list[int]] = [
        [item_value[item] for item in line] for line in board_lines
    ]
    position: list[int] = [-1, -1]
    for r, line in enumerate(board_lines):
        if (c := line.find("@")) != -1:
            position = [r, c]
            break

    directions: dict[str, tuple[int, int]] = {
        "^": (-1, 0),
        ">": (0, 1),
        "v": (1, 0),
        "<": (0, -1),
    }
    direction: tuple[int, int]
    check_position: list[int]
    value: int

    for instruction in instructions:
        direction = directions[instruction]
        check_position = position.copy()
        check_position[0] += direction[0]
        check_position[1] += direction[1]
        while True:
            value = board[check_position[0]][check_position[1]]
            if value == 2:
                break
            if value == 0:
                board[check_position[0]][check_position[1]] = 1
                position[0] += direction[0]
                position[1] += direction[1]
                board[position[0]][position[1]] = 0
                break
            check_position[0] += direction[0]
            check_position[1] += direction[1]

    answer: int = 0
    for r, row in enumerate(board):
        for c, value in enumerate(row):
            if value == 1:
                answer += r * 100 + c

    print(answer)


if __name__ == "__main__":
    main()
