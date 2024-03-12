class Opponent:
    def __init__(self, player_symbol, is_first):
        self.player_symbol = player_symbol
        self.is_first = not is_first

    def make_move(self, board):
        print("Now we are going to have a bunch of switch statements")
