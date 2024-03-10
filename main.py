
# init board state
rows = cols = 3
characters = ('O', 'X')
board_state = [['-' for _ in range(cols)] for _ in range(rows)]

#print board state
for row in board_state:
    for elem in row:
        print(elem, end=' ')
    print('\n')

# write the rules of the game

print("Each position is labeled as follows:")



