from itertools import cycle
from typing import Callable, Tuple

pair = Tuple[int,int]

def main() -> None:
    with open('input.txt') as file:
        board:list[str] = ['/'+line+'/' for line in file.read().splitlines()]
        board = ['/'*len(board[0])] + board + ['/'*len(board[0])]
    
    position:pair = (-1,-1)
    for i, line in enumerate(board):
        if (j := line.find('^')) != -1:
            position = (i,j)
            break
    
    directions:cycle[pair] = cycle(((-1,0),(0,1),(1,0),(0,-1)))
    current_direction:pair = next(directions)
    next_position:pair

    boardValue:Callable[[pair],str] = lambda indices: board[indices[0]][indices[1]]
    visited:set[pair] = set()
    visited_with_direction:set[tuple[pair,pair]] = set()
    position_with_direction:tuple[pair,pair]

    while boardValue(position) != '/':
        position_with_direction = (position,current_direction)
        if position_with_direction in visited_with_direction:
            break
        visited_with_direction.add(position_with_direction)
        visited.add(position)
        next_position = position[0] + current_direction[0], position[1] + current_direction[1]
        if boardValue(next_position) == '#':
            current_direction = next(directions)
        else:
            position = next_position
    
    print(len(visited))

if __name__ == '__main__':
    main()