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

    possible: set[str] = set([""])
    for subpattern in subpatterns:
        if any(subpattern.removesuffix(towel) in possible for towel in towels):
            possible.add(subpattern)

    print(sum(pattern in possible for pattern in patterns))


if __name__ == "__main__":
    main()
