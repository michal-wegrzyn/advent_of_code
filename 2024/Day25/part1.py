from typing import Final


def main() -> None:
    WIDTH: Final = 5
    HEIGHT: Final = 7

    with open("input.txt") as file:
        images: list[list[str]] = [
            image.splitlines() for image in file.read().split("\n\n")
        ]

    for image in images:
        assert len(image) == HEIGHT
        for row in image:
            assert len(row) == WIDTH

    locks: list[list[int]] = []
    keys: list[list[int]] = []

    for image in images:
        if image[0][0] == "#":
            locks.append([column.count("#") - 1 for column in list(zip(*image))])
        else:
            keys.append([column.count("#") - 1 for column in list(zip(*image))])

    answer: int = 0
    for lock in locks:
        for key in keys:
            if all(l + k <= HEIGHT - 2 for l, k in zip(lock, key)):
                answer += 1

    print(answer)


if __name__ == "__main__":
    main()
