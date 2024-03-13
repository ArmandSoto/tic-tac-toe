from board import Board
from player import Player
from opponent import Opponent

class Game:
    def __init__(self):
        self.board = Board()
        self.player = None
        self.opponent = None
        self.game_over = False
    
    def setup(self):
        while True:
            player_character = input("Choose X or O: ").upper()
            if player_character and (player_character == 'O' or player_character == 'X'):
                break
            else:
                print("Invalid Input")
        opponent_character = 'X' if player_character == 'O' else 'O'
        print("Rules ... \n Please select one of the following positions [0-8]\n--------------------")
        self.board.print()
        self.board.reset()
        self.board.print()

        while True:
            user_input = input("Would you like to go first?").upper()
            if user_input in ['Y', 'N']:
                is_player_first = user_input == 'Y'
                self.player = Player(player_character, is_player_first)
                self.opponent = Opponent(opponent_character, is_player_first)
                break
            else:
                print("Invalid Input")
        return [self.player, self.opponent, self.board]

    def check_win():
        print("Checks if there was a win")              