from re import finditer
from heapq import merge

def main() -> None:
    with open('input.txt') as file:
        text:str = file.read()
    
    pattern:str = r"mul\((\d{1,3}),(\d{1,3})\)"
    matches_mul:list[tuple[int,int]] = [(match_obj.start(), int(match_obj.group(1))*int(match_obj.group(2))) for match_obj in finditer(pattern, text)]
    matches_do_dont:list[tuple[int,str]] = [(match_obj.start(), match_obj.group()) for match_obj in finditer(r"do\(\)|don't\(\)", text)]

    answer:int = 0
    enabled:bool = True
    for _, value in merge(matches_mul, matches_do_dont):
        if value == "do()":
            enabled = True
        elif value == "don't()":
            enabled = False
        else:
            if enabled:
                answer += value
    print(answer)

if __name__ == '__main__':
    main()