class GameBoard:
    def __init__(self):
        self.board = [" " for x in range(10)]

    def print_board(self):
        print(f"        [ {self.board[1]} ] [ {self.board[2]} ] [ {self.board[3]} ]\n"
              f"        [ {self.board[4]} ] [ {self.board[5]} ] [ {self.board[6]} ]\n"
              f"        [ {self.board[7]} ] [ {self.board[8]} ] [ {self.board[9]} ]\n")

    def insert_letter(self, letter, pos):
        self.board[pos] = letter

    def is_board_full(self):
        if self.board.count(" ") > 1:
            return False
        else:
            return True

    def space_is_free(self, pos):
        return self.board[pos] == " "

    def reset_board(self):
        self.board = [" " for x in range(10)]
