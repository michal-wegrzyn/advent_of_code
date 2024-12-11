def main() -> None:
    with open("input.txt") as file:
        stones: list[str] = file.read().split()

    stones2: list[str]
    for _ in range(25):
        stones2 = []
        for stone in stones:
            if stone == "0":
                stones2.append("1")
            elif len(stone) % 2 == 0:
                stones2.append(stone[: len(stone) // 2])
                stones2.append(stone[len(stone) // 2 :].lstrip("0") or "0")
            else:
                stones2.append(str(int(stone) * 2024))

        stones = stones2.copy()

    print(len(stones))


if __name__ == "__main__":
    main()
