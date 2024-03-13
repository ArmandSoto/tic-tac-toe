from game import Game

    
tic_tac_toe = Game()
player, opponent, board = tic_tac_toe.setup()

while (not tic_tac_toe.game_over):
    if player.is_first:
        player.go(board)
        opponent.go(board)
    else:
        opponent.go(board)
        player.go(board)


       





