from helper import print_board
from board import Board

# init board state
board = Board()



while True:
    user_input = input("Choose X or O: ").upper()
    if user_input and (user_input == 'O' or user_input == 'X'):
        break
    else:
        print("Invalid Input")
print("Rules ... \n Please select one of the following positions [0-8]")
print_board(board_state)

# init board state
board_state = [['-' for _ in range(board.cols)] for _ in range(board.rows)]

print_board(board_state)

#check for a valid position
while True:
    position_input = int(input("Please enter a valid position: "))
    if position_input and (position_input in range(0,9)):
        break
    else:
        print("Invalid Input")

#check if user entered "O" or "X"

#check if something is already there or if it is empty
row_index = int(position_input / 3) # 0, 1, 2
col_index = int(position_input % 3)
if board_state[row_index][col_index] == '-':
    board_state[row_index][col_index] = user_input
else:
    print("Area invalid")
        
print_board(board_state)


            
        









# now init board state to '-'




