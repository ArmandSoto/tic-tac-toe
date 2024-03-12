class Opponent:
    def __init__(self, symbol, is_first):
        self.symbol = symbol
        self.is_first = not is_first

    def make_move(self, board):
        if self.is_first:
            #exhaust the corners
            for i in range(0,2,2):
                for j in range(0,2,2):
                    board[i][j] = self.symbol
            
        
