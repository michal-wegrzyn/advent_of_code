from typing import Self, Generator, Callable


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

    def execute(self: Self, program: list[int]) -> Generator[int, None, None]:
        pairs: list[tuple[int, int]] = [
            (program[i], program[i + 1]) for i in range(0, len(program), 2)
        ]
        pointer: int = 0
        opcode: int
        value: int
        returned_value: int | None

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

        while pointer < len(pairs):
            opcode, value = pairs[pointer]
            returned_value = operations[opcode](value)
            pointer += 1
            if returned_value is not None:
                yield returned_value


def main() -> None:
    with open("input.txt") as file:
        registers_text: str
        program_text: str
        registers_text, program_text = file.read().split("\n\n")

    values: list[int] = [
        int(line[line.find(":") + 2 :]) for line in registers_text.splitlines()
    ]

    program_text = program_text[program_text.find(":") + 2 :]
    program: list[int] = [int(value) for value in program_text.split(",")]

    opcodes: list[int] = program[::2]
    assert len(program) % 2 == 0
    assert opcodes.count(3) == 1
    assert opcodes.count(0) == 1
    assert opcodes.count(5) == 1
    assert opcodes.index(5) < opcodes.index(3)
    assert opcodes.index(0) < opcodes.index(3)
    op0_value: int = program[opcodes.index(0) * 2 + 1]
    assert op0_value <= 3

    registers: Registers
    max_bits_set: int = op0_value * len(program)
    bits_set: int = min(10 - op0_value, max_bits_set)
    candidates: list[int] = list(range(pow(2, bits_set)))
    new_candidates: list[int]
    extensions: list[int]
    extension_size: int

    for iteration in range(len(program)):
        extension_size = min(op0_value, max_bits_set - bits_set)
        extensions = list(range(pow(2, extension_size)))
        candidates = [
            candidate + pow(2, bits_set) * extension
            for extension in extensions
            for candidate in candidates
        ]
        bits_set += extension_size

        new_candidates = []
        for candidate in candidates:
            values[0] = candidate
            registers = Registers(values)
            execute = registers.execute(program)
            for value in program[: iteration + 1]:
                try:
                    if value != next(execute):
                        break
                except StopIteration:
                    break
            else:
                if iteration != len(program) - 1:
                    new_candidates.append(candidate)
                    continue

                try:
                    next(execute)
                except StopIteration:
                    new_candidates.append(candidate)
                    print(candidate)
                    break
        candidates = new_candidates.copy()


if __name__ == "__main__":
    main()
