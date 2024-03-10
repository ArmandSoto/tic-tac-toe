from helper import print_board

# init board state
rows = cols = 3
characters = ('O', 'X')
board_state = [[i * cols + j for j in range(cols)] for i in range(rows)]

# write the rules of the game
print("Each position is labeled as follows: ")
print_board(board_state)
    
print("Then select either X or O")

board_state = [['-' for _ in range(cols)] for _ in range(rows)]

print_board(board_state)

#check for a valid position
while True:
    position_input = input("Please enter a valid position: ")
    if position_input and (position_input in range(0,9)):
        break
    else:
        print("Invalid Input")

#check if user entered "O" or "X"
while True:
    user_input = input("Choose X or O ").upper()
    if user_input and (user_input == 'O' or user_input == 'X'):
        break
    else:
        print("Invalid Input")

#check if something is already there or if it is empty
    for element in board_state:
        if element == '-':
            #make a move
            
        









# now init board state to '-'




