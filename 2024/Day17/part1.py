from typing import Callable, Self


class Registers:
    def __init__(self: Self, values: list[int]) -> None:
        assert len(values) == 3
        self.a: int = values[0]
        self.b: int = values[1]
        self.c: int = values[2]

    def combo(self: Self, number: int) -> int:
        assert 0 <= number <= 6
        if number < 4:
            return number
        elif number == 4:
            return self.a
        elif number == 5:
            return self.b
        else:
            return self.c

    def adv(self: Self, number: int) -> None:
        self.a //= pow(2, self.combo(number))

    def bxl(self: Self, number: int) -> None:
        self.b ^= number

    def bst(self: Self, number: int) -> None:
        self.b = self.combo(number) % 8

    def bxc(self: Self, number: int) -> None:
        self.b ^= self.c

    def bdv(self: Self, number: int) -> None:
        self.b = self.a // pow(2, self.combo(number))

    def cdv(self: Self, number: int) -> None:
        self.c = self.a // pow(2, self.combo(number))

    def execute(self: Self, program: list[tuple[int, int]]) -> list[int]:
        pointer: int = 0
        opcode: int
        value: int
        answer: list[int] = []

        def jnz(number: int) -> None:
            if self.a == 0:
                return
            nonlocal pointer
            pointer = number - 1

        def out(number: int) -> int:
            return self.combo(number) % 8

        operations: dict[int, Callable[[int], None | int]] = {
            0: self.adv,
            1: self.bxl,
            2: self.bst,
            3: jnz,
            4: self.bxc,
            5: out,
            6: self.bdv,
            7: self.cdv,
        }

        while pointer < len(program):
            opcode, value = program[pointer]
            returned_value = operations[opcode](value)
            pointer += 1
            if returned_value is not None:
                answer.append(returned_value)

        return answer


def main() -> None:
    with open("input.txt") as file:
        registers_text: str
        program_text: str
        registers_text, program_text = file.read().split("\n\n")

    registers: Registers = Registers(
        [int(line[line.find(":") + 2 :]) for line in registers_text.splitlines()]
    )
    program_text = program_text[program_text.find(":") + 1 :]
    program_numbers: list[int] = [int(value) for value in program_text.split(",")]
    program: list[tuple[int, int]] = [
        (program_numbers[i], program_numbers[i + 1])
        for i in range(0, len(program_numbers), 2)
    ]

    answer: list[int] = registers.execute(program)
    print(",".join(str(value) for value in answer))


if __name__ == "__main__":
    main()
