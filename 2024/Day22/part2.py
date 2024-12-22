def mix(secret: int, number: int) -> int:
    return secret ^ number


def prune(secret: int) -> int:
    return secret % 16777216


def next_secret(secret: int) -> int:
    secret = prune(mix(secret, secret * 64))
    secret = prune(mix(secret, secret // 32))
    secret = prune(mix(secret, secret * 2048))
    return secret


def get_prices_sequence(secret: int, length: int) -> list[int]:
    return [value % 10 for value in get_sequence(secret, length)]


def get_sequence(secret: int, length: int) -> list[int]:
    return [secret] + [secret := next_secret(secret) for _ in range(length - 1)]


def get_differences(sequence: list[int]) -> list[int]:
    return [sequence[i + 1] - sequence[i] for i in range(len(sequence) - 1)]


def differences_to_price(secret: int, length: int) -> dict[tuple[int, ...], int]:
    sequence: list[int] = get_prices_sequence(secret, length)
    differences: list[int] = get_differences(sequence)
    answer: dict[tuple[int, ...], int] = {}
    diffs: tuple[int, ...]
    for i in range(4, len(sequence)):
        diffs = tuple(differences[i - 4 : i])
        if not diffs in answer:
            answer[diffs] = sequence[i]
    return answer


def main() -> None:
    with open("input.txt") as file:
        secrets: list[int] = [int(line) for line in file.read().splitlines()]

    prices: dict[tuple[int, ...], int]
    total: dict[tuple[int, ...], int] = {}
    for secret in secrets:
        prices = differences_to_price(secret, 2000)
        for key, value in prices.items():
            total[key] = total.get(key, 0) + value

    print(max(total.values()))


if __name__ == "__main__":
    main()
