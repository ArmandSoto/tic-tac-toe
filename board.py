class Board:
    def __init__(self):
        self.rows = self.cols = 3
        self.state = [[i * self.cols + j for j in range(self.cols)] for i in range(self.rows)]
        self.characters = ('O', 'X')

def print_board(board):
    for row in board:
        for elem in row:
            print(elem, end=' ')
        print('\n')        