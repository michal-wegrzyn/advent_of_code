from typing import Final


def extract_values(line: str) -> list[int]:
    position: str
    velocity: str
    position, velocity = line.split(" v=")
    pos_x: int = int(position[2 : position.index(",")])
    pos_y: int = int(position[position.index(",") + 1 :])
    v_x: int = int(velocity[: velocity.index(",")])
    v_y: int = int(velocity[velocity.index(",") + 1 :])
    return [pos_x, pos_y, v_x, v_y]


def check_and_display_robots(
    robots: list[list[int]], rows: int, cols: int, filename: str, header: str
) -> bool:
    count: list[list[int]] = [[0] * cols for _ in range(rows)]
    for robot in robots:
        count[robot[1]][robot[0]] = 1
    lines: list[str] = ["".join(str(value) for value in count[r]) for r in range(rows)]
    if all(line.find("1" * 15) == -1 for line in lines):
        return False
    with open(filename, "a") as file:
        file.write(header)
        file.write("\n".join(lines))
        file.write("\n\n")
    return True


def main() -> None:
    with open("input.txt") as file:
        lines: list[str] = file.readlines()
    COLS: Final = 101
    ROWS: Final = 103
    MOVES: Final = ROWS * COLS
    DISPLAY_FILENAME: Final = "display.txt"
    with open(DISPLAY_FILENAME, "w"):
        pass
    robots: list[list[int]] = [extract_values(line) for line in lines]
    is_displayed: bool
    displayed_moves: list[int] = []
    for move in range(1, MOVES + 1):
        for i in range(len(robots)):
            robots[i][0] += robots[i][2]
            robots[i][0] %= COLS
            robots[i][1] += robots[i][3]
            robots[i][1] %= ROWS
        is_displayed = check_and_display_robots(
            robots, ROWS, COLS, DISPLAY_FILENAME, f"Move {move}:\n"
        )
        if is_displayed:
            displayed_moves.append(move)

    if len(displayed_moves) == 0:
        print("No solutions found.")
    else:
        print("Found:", ", ".join(str(value) for value in displayed_moves))
        print(
            f"Check if the {DISPLAY_FILENAME} file shows a Christmas tree made of 1s."
        )


if __name__ == "__main__":
    main()
