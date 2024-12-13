from typing import Tuple, Final

Pair = Tuple[int, int]


def values_of_x_and_y(line: str) -> Pair:
    x: int = int(line[line.index("X") + 2 : line.index(",")])
    y: int = int(line[line.index("Y") + 2 :])
    return (x, y)


def minimal_cost(button_a: Pair, button_b: Pair, price: Pair) -> int:
    COST_A: Final = 3
    COST_B: Final = 1

    min_score: int = 0
    score: int
    for cnt_a in range(100):
        if cnt_a * button_a[0] > price[0]:
            continue
        if (price[0] - cnt_a * button_a[0]) % button_b[0] == 0:
            cnt_b = (price[0] - cnt_a * button_a[0]) // button_b[0]
            if button_a[1] * cnt_a + button_b[1] * cnt_b != price[1]:
                continue
            score = COST_A * cnt_a + COST_B * cnt_b
            if min_score == 0 or score < min_score:
                min_score = score

    return min_score


def main() -> None:
    with open("input.txt") as file:
        machine_describtions: list[list[str]] = [
            lines.splitlines() for lines in file.read().split("\n\n")
        ]
    button_a: Pair
    button_b: Pair
    price: Pair
    answer: int = 0
    for describtion in machine_describtions:
        button_a = values_of_x_and_y(describtion[0])
        button_b = values_of_x_and_y(describtion[1])
        price = values_of_x_and_y(describtion[2])
        answer += minimal_cost(button_a, button_b, price)

    print(answer)


if __name__ == "__main__":
    main()
