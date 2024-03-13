import random

class Opponent:
    def __init__(self, character, is_first):
        self.character = character
        self.is_first = not is_first

    def go(self, board):
        # simplify the corner taking
        corners = [(0,0), (0,2), (2,0), (2,2)]
        if board.turn < 1:
            if self.is_first:
                random_corner = random.choice(corners)
                self.make_move(board, random_corner)
            else:
                print("Pick something else, perhaps center")
        board.print()

    def make_move(self, board, coordinate):
        x, y = coordinate
        if board.state[x][y] == '-':
            board.state[x][y] = self.character
        else:
            print("Area invalid")
        
    
        

            
        
