class GamePlay:
    def __init__(self):
        self.win_conditions = [
            [1, 5, 9],
            [1, 4, 7],
            [1, 2, 3],
            [2, 5, 8],
            [3, 5, 7],
            [3, 6, 9],
            [4, 5, 6],
            [7, 8, 9]
        ]

    def is_winner(self, board, letter):
        for win_condition in self.win_conditions:
            matching_count = 0
            for move in win_condition:
                if board[move] == letter:
                    matching_count += 1
            if matching_count == 3:
                return True
        return False

    def player_move(self, board):
        run = True
        while run:
            move = input("Please select a position to place an \'X\' (1-9): ")
            try:
                move = int(move)
                if 0 < move < 10:
                    if board.space_is_free(move):
                        run = False
                        board.insert_letter("X", move)
                    else:
                        print("Sorry, this space is occupied!")
                else:
                    print("Please type a number within the range!")
            except:
                print("Please type a number!")

    def comp_move(self, board):
        possible_moves = [x for x, letter in enumerate(board) if letter == " " and x != 0]
        move = 0

        for letter in ["O", "X"]:
            for i in possible_moves:
                board_copy = board[:]
                board_copy[i] = letter
                if self.is_winner(board_copy, letter):
                    move = i
                    return move

        corners_open = []
        for i in possible_moves:
            if i in [1, 3, 7, 9]:
                corners_open.append(i)

        if len(corners_open) > 0:
            move = self.select_random(corners_open)
            return move

        if 5 in possible_moves:
            move = 5
            return move

        edges_open = []
        for i in possible_moves:
            if i in [2, 4, 6, 8]:
                edges_open.append(i)

        if len(edges_open) > 0:
            move = self.select_random(edges_open)
            return move

        return move

    def select_random(self, li):
        import random
        list_length = len(li)
        r = random.randrange(0, list_length)
        return li[r]
    