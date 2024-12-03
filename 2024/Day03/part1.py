from re import findall

def main() -> None:
    pattern:str = r"mul\((\d{1,3}),(\d{1,3})\)"
    with open('input.txt') as file:
        text:str = file.read()
    matches:list[tuple[str,str]] = findall(pattern, text)
    answer:int = sum(int(i)*int(j) for i, j in matches)
    print(answer)

if __name__ == '__main__':
    main()