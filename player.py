
class player:

    def __init__(self, piece):
        self.piece = piece

    def __str__(self):
        return f'piece: {self.piece}'

    def move(self, board):
        position = input(f"{self.piece}'s turn: ")
        board[position] = self.piece

        print(board)
        print()
