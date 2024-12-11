from collections import Counter, defaultdict


def main() -> None:
    with open("input.txt") as file:
        stones: defaultdict[str, int] = defaultdict(
            lambda: 0, Counter(file.read().split())
        )

    stones2: defaultdict[str, int]
    for _ in range(75):
        stones2 = defaultdict(lambda: 0)
        for stone, count in stones.items():
            if stone == "0":
                stones2["1"] += count
            elif len(stone) % 2 == 0:
                stones2[stone[: len(stone) // 2]] += count
                stones2[stone[len(stone) // 2 :].lstrip("0") or "0"] += count
            else:
                stones2[str(int(stone) * 2024)] += count

        stones = stones2.copy()

    print(sum(stones.values()))


if __name__ == "__main__":
    main()
