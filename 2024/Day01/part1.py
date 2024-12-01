def main():
    with open('input') as f:
        pairs: list[list[int,int]] = [[int(value) for value in line.split()] for line in f.readlines()]
    sorted_pairs:zip[tuple[int,int]] = zip(sorted(pair[0] for pair in pairs), sorted(pair[1] for pair in pairs))
    answer:int = sum(abs(pair[0] - pair[1]) for pair in sorted_pairs)
    print(answer)

if __name__ == '__main__':
    main()