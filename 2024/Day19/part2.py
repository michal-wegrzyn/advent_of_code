def main() -> None:
    with open("input.txt") as file:
        towels_text: str
        patterns_text: str
        towels_text, patterns_text = file.read().split("\n\n")

    towels: list[str] = towels_text.split(", ")
    patterns: list[str] = patterns_text.splitlines()
    subpatterns: list[str] = sorted(
        set(pattern[: i + 1] for pattern in patterns for i in range(len(pattern))),
        key=len,
    )

    ways_to_achieve: dict[str, int] = {"": 1}
    for subpattern in subpatterns:
        ways_to_achieve[subpattern] = sum(
            ways_to_achieve[subpattern.removesuffix(towel)]
            for towel in towels
            if subpattern.endswith(towel)
        )

    print(sum(ways_to_achieve[pattern] for pattern in patterns))


if __name__ == "__main__":
    main()
