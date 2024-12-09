from typing import cast


def main() -> None:
    with open("input.txt") as file:
        disk_map: str = file.read()
    id_number: int = 0
    blocks: list[int | None] = []
    position: int = 0
    for i, character in enumerate(disk_map):
        if i % 2:
            blocks += [None] * int(character)
        else:
            blocks += [id_number] * int(character)
            id_number += 1

    while position < len(blocks):
        if blocks[-1] is None:
            blocks.pop(-1)
            continue
        if blocks[position] is not None:
            position += 1
            continue
        blocks[position] = blocks[-1]
        blocks.pop(-1)
        position += 1

    print(sum(i * value for i, value in enumerate(cast(list[int], blocks))))


if __name__ == "__main__":
    main()
