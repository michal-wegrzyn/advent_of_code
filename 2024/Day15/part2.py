def is_pushable(
    board: list[list[int]], position: list[int], direction: tuple[int, int]
) -> bool:
    new_position: list[int] = position.copy()
    new_position[0] += direction[0]
    new_position[1] += direction[1]
    value: int = board[new_position[0]][new_position[1]]
    if value == 3:
        return False
    if value == 0:
        return True
    if direction[1] != 0:
        new_position[0] += direction[0]
        new_position[1] += direction[1]
        return is_pushable(board, new_position, direction)
    second_position: list[int] = new_position.copy()
    if value == 1:
        second_position[1] += 1
    else:
        second_position[1] -= 1
    return is_pushable(board, new_position, direction) and is_pushable(
        board, second_position, direction
    )


def push(
    board: list[list[int]], position: list[int], direction: tuple[int, int]
) -> None:
    new_position: list[int] = position.copy()
    new_position[0] += direction[0]
    new_position[1] += direction[1]
    value: int = board[new_position[0]][new_position[1]]
    if value == 3:
        return
    if value == 0:
        return
    second_position: list[int]
    if direction[1] != 0:
        second_position = new_position.copy()
        second_position[0] += direction[0]
        second_position[1] += direction[1]
        push(board, second_position, direction)
        board[new_position[0]][new_position[1]] = 0
        if direction[1] == 1:
            board[second_position[0]][second_position[1]] = 1
            second_position[0] += direction[0]
            second_position[1] += direction[1]
            board[second_position[0]][second_position[1]] = 2
        if direction[1] == -1:
            board[second_position[0]][second_position[1]] = 2
            second_position[0] += direction[0]
            second_position[1] += direction[1]
            board[second_position[0]][second_position[1]] = 1
        return
    second_position = new_position.copy()
    second_position[1] += 1 if value == 1 else -1
    push(board, new_position, direction)
    push(board, second_position, direction)
    board[new_position[0]][new_position[1]] = 0
    board[second_position[0]][second_position[1]] = 0
    new_position[0] += direction[0]
    new_position[1] += direction[1]
    second_position[0] += direction[0]
    second_position[1] += direction[1]
    board[new_position[0]][new_position[1]] = 1 if value == 1 else 2
    board[second_position[0]][second_position[1]] = 2 if value == 1 else 1


def main() -> None:
    with open("input.txt") as file:
        board_text: str
        instructions_text: str
        board_text, instructions_text = file.read().split("\n\n")
    board_text = (
        board_text.replace(".", "..")
        .replace("#", "##")
        .replace("O", "[]")
        .replace("@", "@.")
    )
    board_lines: list[str] = board_text.split("\n")
    instructions: str = "".join(instructions_text.splitlines())
    item_value: dict[str, int] = {".": 0, "[": 1, "]": 2, "#": 3, "@": 0}
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
    value: int

    for instruction in instructions:
        direction = directions[instruction]
        if not is_pushable(board, position, direction):
            continue
        push(board, position, direction)
        position[0] += direction[0]
        position[1] += direction[1]

    answer: int = 0
    for r, row in enumerate(board):
        for c, value in enumerate(row):
            if value == 1:
                answer += r * 100 + c

    print(answer)


if __name__ == "__main__":
    main()
