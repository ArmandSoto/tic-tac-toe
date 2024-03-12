from board import Board
from player import Player

    
board = Board()

while True:
    user_input = input("Choose X or O: ").upper()
    if user_input and (user_input == 'O' or user_input == 'X'):
        break
    else:
        print("Invalid Input")
print("Rules ... \n Please select one of the following positions [0-8]\n--------------------")
board.print()
board.reset()
board.print()

while True:
    user_input = input("Would you like to go first?").upper()
    if user_input == 'Y':
        player_go_first = True
        break
    elif user_input == 'N':
        # continue check
        player_go_first = False
        break
    else:
        print("Invalid Input")

player = Player(user_input)
if not player_go_first:
    # opponent goes
    print("Opponent goes first")
else:
    player.make_move(board)


        
board.print()




# now init board state to '-'




