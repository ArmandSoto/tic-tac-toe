class Board:
    def __init__(self):
        self.rows = self.cols = 3
        self.state = [[i * self.cols + j for j in range(self.cols)] for i in range(self.rows)]
        self.available_moves = [[(i,j) for i in range(self.cols)] for j in range(self.rows)]
        self.characters = ('O', 'X')
        self.turn = 0
        

    def print(self):
        for row in self.state:
            for elem in row:
                print(elem, end=' ')
            print('\n')

    def reset(self):
        self.state = [['-' for _ in range(self.cols)] for _ in range(self.rows)]

    def nextTurn(self):
        self.turn += 1
