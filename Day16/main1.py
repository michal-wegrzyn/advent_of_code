directions = [[-1,0,[1,3]], [0,1,[0,2]], [1,0,[3,1]], [0,-1,[2,0]]] # r c / \
board = open('input.txt').read().strip().split()

beams = [[0,-1,1]]
history = set()
energized = set()

while beams:
    moved_beams = []
    for beam in beams:
        beam[0] += directions[beam[2]][0]
        beam[1] += directions[beam[2]][1]
        if not (0<=beam[0]<len(board) and 0<=beam[1]<len(board[0])):
            continue
        square_type = board[beam[0]][beam[1]]
        if square_type in ['/','\\']:
            beam[2] = directions[beam[2]][2][square_type=='\\']
        if square_type == ['-','|'][beam[2]%2]:
            beam[2] = (beam[2]+1)%4
            if not tuple(beam) in history:
                moved_beams.append(beam)
                history.add(tuple(beam))
                energized.add(tuple(beam[:2]))
            new_beam = beam.copy()
            new_beam[2] = (new_beam[2]+2)%4
            if not tuple(new_beam) in history:
                moved_beams.append(new_beam)
                history.add(tuple(new_beam))
                energized.add(tuple(new_beam[:2]))
        else:
            if not tuple(beam) in history:
                moved_beams.append(beam)
                history.add(tuple(beam))
                energized.add(tuple(beam[:2]))           
    
    beams = moved_beams

print(len(energized))