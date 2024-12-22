def mix(secret: int, number: int) -> int:
    return secret ^ number


def prune(secret: int) -> int:
    return secret % 16777216


def next_secret(secret: int) -> int:
    secret = prune(mix(secret, secret * 64))
    secret = prune(mix(secret, secret // 32))
    secret = prune(mix(secret, secret * 2048))
    return secret


def main() -> None:
    with open("input.txt") as file:
        secrets: list[int] = [int(line) for line in file.read().splitlines()]

    answer: int = 0
    for secret in secrets:
        for _ in range(2000):
            secret = next_secret(secret)
        answer += secret
    print(answer)


if __name__ == "__main__":
    main()
