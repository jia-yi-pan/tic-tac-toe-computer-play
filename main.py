from game_board import GameBoard
from game_play import GamePlay

game_board = GameBoard()
game_play = GamePlay()


def game():
    print("Welcome to Tic Tac Toe!")
    game_board.print_board()
    while not (game_board.is_board_full()):
        if not (game_play.is_winner(game_board.board, "O")):
            game_play.player_move(game_board)
            game_board.print_board()
        else:
            print("Sorry, O\'s won this time!")
            break
        if not (game_play.is_winner(game_board.board, "X")):
            move = game_play.comp_move(game_board.board)
            if move == 0:
                print("Tie game!")
            else:
                game_board.insert_letter("O", move)
                print(f"Computer placed an \'O\' in position {move}: ")
                game_board.print_board()
        else:
            # if player wins, break out of loop
            print("X\'s won this time! Good job!")
            break


while True:
    game()
    game_board.reset_board()
    play_again = input("Would you like to play again? (Y/N) ").upper().strip()
    if play_again == "N":
        break

