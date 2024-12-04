def main() -> None:
    with open('input.txt') as file:
        word_search:list[str] = file.read().splitlines()
    
    searched_word: str = 'XMAS'
    searched:list[str] = [searched_word, searched_word[::-1]]
    answer:int = 0

    expandable_right:bool
    expandable_down:bool

    for i in range(len(word_search)):
        expandable_down = i < len(word_search)-len(searched_word)+1
        for j in range(len(word_search[0])):
            expandable_right = j < len(word_search[0])-len(searched_word)+1
            if expandable_down and ''.join(word_search[i+k][j] for k in range(len(searched_word))) in searched:
                answer += 1
            if expandable_right and ''.join(word_search[i][j+k] for k in range(len(searched_word))) in searched:
                answer += 1
            if expandable_down and expandable_right and ''.join(word_search[i+k][j+k] for k in range(len(searched_word))) in searched:
                answer += 1
            if expandable_down and expandable_right and ''.join(word_search[i+len(searched_word)-1-k][j+k] for k in range(len(searched_word))) in searched:
                answer += 1
    
    print(answer)

if __name__ == '__main__':
    main()