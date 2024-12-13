from typing import Tuple, Callable, Final
from math import gcd

Pair = Tuple[int, int]


def values_of_x_and_y(line: str) -> Pair:
    x: int = int(line[line.index("X") + 2 : line.index(",")])
    y: int = int(line[line.index("Y") + 2 :])
    return (x, y)


def det(v1: Pair, v2: Pair) -> int:
    return v1[0] * v2[1] - v1[1] * v2[0]


def solve_diophantine_equation_max_x(a: int, b: int, c: int) -> Pair | None:
    """
    Solves the linear Diophantine equation `ax + by = c`.
    Finds nonnegative integer solutions `(x, y)` such that `x` is maximized.
    Returns found solution or None if it doesn't exist.
    """
    assert a > 0 and b > 0 and c >= 0
    if c == 0:
        return 0, 0
    d: int = gcd(a, b)
    if c % d:
        return None
    a //= d
    b //= d
    c //= d
    b %= a
    if b == 0:
        if c % a:
            return None
        return c // a, 0
    y = (pow(b, -1, a) * c) % a
    x = (c - y * b) // a
    if x < 0:
        return None
    return x, y


def minimal_cost(button_a: Pair, button_b: Pair, price: Pair) -> int:
    COST_A: Final = 3
    COST_B: Final = 1
    det_AB: int = det(button_a, button_b)
    det_PB: int = det(price, button_b)
    det_AP: int = det(button_a, price)
    if det_AB != 0:
        if det_PB % det_AB:
            return 0
        if det_AP % det_AB:
            return 0
        return COST_A * det_PB // det_AB + COST_B * det_AP // det_AB
    if det_AP != 0 or det_PB != 0:
        return 0

    solution: Pair | None
    if button_a[0] * COST_B >= button_b[0] * COST_A:
        solution = solve_diophantine_equation_max_x(button_a[0], button_b[0], price[0])
        if solution is None:
            return 0
        return COST_A * solution[0] + COST_B * solution[1]
    else:
        solution = solve_diophantine_equation_max_x(button_b[0], button_a[0], price[0])
        if solution is None:
            return 0
        return COST_A * solution[1] + COST_B * solution[0]


def main() -> None:
    with open("input.txt") as file:
        machine_describtions: list[list[str]] = [
            lines.splitlines() for lines in file.read().split("\n\n")
        ]
    button_a: Pair
    button_b: Pair
    price: Pair
    answer: int = 0
    ERROR: Final = int(1e13)
    add_error: Callable[[Pair], Pair] = lambda p: (p[0] + ERROR, p[1] + ERROR)
    for describtion in machine_describtions:
        button_a = values_of_x_and_y(describtion[0])
        button_b = values_of_x_and_y(describtion[1])
        price = add_error(values_of_x_and_y(describtion[2]))
        answer += minimal_cost(button_a, button_b, price)

    print(answer)


if __name__ == "__main__":
    main()
