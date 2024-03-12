class Player:
    def __init__(self, character, is_first):
        self.character = character
        self.is_first = is_first

    def make_move(self, board):
        while True:
            position_input = int(input("Please enter a valid position: "))
            if position_input and (position_input in range(0,9)):
                break
            else:
                print("Invalid Input")
        
        row_index = int(position_input / 3) # 0, 1, 2
        col_index = int(position_input % 3)
        if board.state[row_index][col_index] == '-':
            board.state[row_index][col_index] = self.character
        else:
            print("Area invalid")
