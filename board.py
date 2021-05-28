from pretty_board import pretty_board
from copy import deepcopy
from collections import Counter


POSITIONS = {
    'tl': (0, 0), 'tm': (0, 1), 'tr': (0, 2),
    'ml': (1, 0), 'mm': (1, 1), 'mr': (1, 2),
    'bl': (2, 0), 'bm': (2, 1), 'br': (2, 2),
}

ROWS =    {'t': 0, 'm': 1, 'b': 2}
COLUMNS = {'l': 0, 'm': 1, 'r': 2}

DIAGONALS = {
    # top left to bottom right
    'TL_TO_BR': (
        POSITIONS['tl'], POSITIONS['mm'], POSITIONS['br']
    ),
    # top right to bottom left
    'TR_TO_BL': (
        POSITIONS['tr'], POSITIONS['mm'], POSITIONS['bl']
    ),
}

class PositionFull(Exception):
    pass

class InvalidMove(Exception):
    pass


class gameBoard:

    def __init__(self, test=False, board=None):
        """
        Note: index scheme goes from top left to bottom right
        in increasing order
        ie: (0,0), (0,1) ...
            (1,0), (1,1) ...
        """

        self.test = test
        # this var passed in during clone function
        if board:
            self.board = board
        elif test:
            self.board = [
                self.top(), self.middle(), self.bottom()
            ]
        else:
            # default initialization of board
            self.board = [
                [None for _ in range(3)]
                for _ in range(3)
            ]

    def __str__(self):
        return str(pretty_board(self))

    def __iter__(self):
        yield from self.board

    def __getitem__(self, index):
        if index not in POSITIONS:
            raise InvalidMove

        row, col = POSITIONS[index]
        return self.board[row][col]

    def __setitem__(self, index, value):
        if index not in POSITIONS:
            raise InvalidMove

        row, col = POSITIONS[index]
        if self.board[row][col]:
            raise PositionFull
        self.board[row][col] = value


    def get_row(self, row):
        yield from self.board[ROWS[row]]

    def get_column(self, column):
        for row in self.board:
            yield row[COLUMNS[column]]

    def get_diagonal(self, diagonal):
        for row, col in DIAGONALS[diagonal]:
            yield self.board[row][col]

    def stats(self, line_type, which_row):
        if line_type == 'row':
            return Counter(self.get_row(which_row))
        elif line_type == 'column':
            return Counter(self.get_column(which_row))
        elif line_type == 'diagonal':
            return Counter(self.get_diagonal(which_row))


    def all_lines(self):
         return (
            (self.stats('row', row) for row in ROWS),
            (self.stats('column', column) for column in COLUMNS),
            (self.stats('diagonal', diagonal) for diagonal in DIAGONALS),
        )


    def game_over(self):
        line_types = self.all_lines()
        return any(
            piece and count == 3
            for line_type in line_types      # line_type = row, column, diagonal
            for line in line_type            # loop over all of 1 type of line
            for piece, count in line.items() # get values from Counter object
        )

    def tie_game(self):
        # tie if no None objects left
        return all(
            self.board[row][col]
            for row, col in POSITIONS.values()
        )


    def clone(self):
        return gameBoard(board=deepcopy(self.board))



    # these are for testing -- initializes board to this config
    def top(self):
        return ['o', None, 'o']
    def middle(self):
        return [None, None, None]
    def bottom(self):
        return ['x', 'o', 'x']




if __name__ == '__main__':
    x = gameBoard()
    print(x)
    print(x['sr'])
