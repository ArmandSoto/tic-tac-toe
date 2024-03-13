from board import Board
from player import Player
from opponent import Opponent

    
board = Board()

while True:
    player_character = input("Choose X or O: ").upper()
    if player_character and (player_character == 'O' or player_character == 'X'):
        break
    else:
        print("Invalid Input")
opponent_character = 'X' if player_character == 'O' else 'O'
print("Rules ... \n Please select one of the following positions [0-8]\n--------------------")
board.print()
board.reset()
board.print()

while True:
    user_input = input("Would you like to go first?").upper()
    if user_input == 'Y':
        player = Player(player_character, True)
        opponent = Opponent(opponent_character, True)
        # also create the opponenet
        break
    elif user_input == 'N':
        player = Player(user_input, False)
        opponent = Opponent(opponent_character, False)
        break
    else:
        print("Invalid Input")


if player.is_first:
    player.make_move(board.state)
else:
    opponent.make_move(board.state)

       
board.print()





