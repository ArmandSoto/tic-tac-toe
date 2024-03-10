
# init board state
rows = cols = 3
characters = ('O', 'X')
board_state = [[i * cols + j for j in range(cols)] for i in range(rows)]
# write the rules of the game
print("Each position is labeled as follows:")    

#print board state
for row in board_state:
    for elem in row:
        print(elem, end=' ')
    print('\n')

# now init board state to '-'




