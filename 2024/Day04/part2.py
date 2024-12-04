def main() -> None:
    with open('input.txt') as file:
        word_search:list[str] = file.read().splitlines()
    
    searched_word: str = 'MAS'
    searched:list[str] = [searched_word, searched_word[::-1]]
    answer:int = 0

    for i in range(len(word_search)-len(searched_word)+1):
        for j in range(len(word_search[0])-len(searched_word)+1):
            if ''.join(word_search[i+k][j+k] for k in range(len(searched_word))) in searched:
                if ''.join(word_search[i+len(searched_word)-1-k][j+k] for k in range(len(searched_word))) in searched:
                    answer += 1
    
    print(answer)

if __name__ == '__main__':
    main()