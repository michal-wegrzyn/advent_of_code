from typing import Tuple, List

Equation = Tuple[int, List[int]]

def isSolvable(equation:Equation) -> bool:
    if len(equation[1]) == 1:
        return equation[0] == equation[1][0]
    if equation[0] < equation[1][0]:
        return False
    multiply:Equation = (equation[0], [equation[1][0] * equation[1][1]] + equation[1][2:])
    add:Equation = (equation[0], [equation[1][0] + equation[1][1]] + equation[1][2:])
    concatenate:Equation = (equation[0], [int(str(equation[1][0]) + str(equation[1][1]))] + equation[1][2:])
    return isSolvable(multiply) or isSolvable(add) or isSolvable(concatenate)

def main() -> None:
    with open('input.txt') as file:
        splitted_lines:list[list[str]] = [line.split(':') for line in file.readlines()]
    equations:list[Equation] = [(int(line[0]), [int(number) for number in line[1].split()]) for line in splitted_lines]
    assert all(value > 0 for equation in equations for value in equation[1])
    print(sum(equation[0] for equation in equations if isSolvable(equation)))

if __name__ == '__main__':
    main()