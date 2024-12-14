from typing import Final


def extract_values(line: str) -> tuple[int, int, int, int]:
    position: str
    velocity: str
    position, velocity = line.split(" v=")
    pos_x: int = int(position[2 : position.index(",")])
    pos_y: int = int(position[position.index(",") + 1 :])
    v_x: int = int(velocity[: velocity.index(",")])
    v_y: int = int(velocity[velocity.index(",") + 1 :])
    return pos_x, pos_y, v_x, v_y


def main() -> None:
    with open("input.txt") as file:
        lines: list[str] = file.readlines()
    pos_x: int
    pos_y: int
    v_x: int
    v_y: int
    # COLS: Final = 11
    # ROWS: Final = 7
    COLS: Final = 101
    ROWS: Final = 103
    MOVES: Final = 100
    quadrants: list[int] = [0, 0, 0, 0]
    for line in lines:
        pos_x, pos_y, v_x, v_y = extract_values(line)
        pos_x = (pos_x + v_x * MOVES) % COLS
        pos_y = (pos_y + v_y * MOVES) % ROWS
        if pos_x * 2 + 1 == COLS or pos_y * 2 + 1 == ROWS:
            continue
        quadrants[(pos_x < COLS // 2) * 2 + (pos_y < ROWS // 2)] += 1
    answer: int = quadrants[0]
    answer *= quadrants[1]
    answer *= quadrants[2]
    answer *= quadrants[3]
    print(answer)


if __name__ == "__main__":
    main()
