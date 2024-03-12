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
        player = Player(user_input, True)
        # also create the opponenet
        break
    elif user_input == 'N':
        player = Player(user_input, False)
        # also Create the opponent
        break
    else:
        print("Invalid Input")


if not player.is_first:
    # opponent goes
    print("Opponent goes first")
else:
    player.make_move(board)


        
board.print()




# now init board state to '-'




