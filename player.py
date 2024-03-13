class Player:
    def __init__(self, character, is_first):
        self.character = character
        self.is_first = is_first


    def go(self, board):
        while True:
            position_input = int(input("Please enter a valid position: "))
            if position_input and (position_input in range(0,9)):
                break
            else:
                print("Invalid Input")
        coordinate = (int(position_input / 3, int(position_input % 3)))
        self.make_move(board, coordinate)
        board.print()


    
    def make_move(self, board, coordinate):
        x, y = coordinate
        if board.state[x][y] == '-':
            board.state[x][y] = self.character
        else:
            print("Area invalid")


