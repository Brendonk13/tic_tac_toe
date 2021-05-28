from board import gameBoard, PositionFull, InvalidMove
from player import player
from random import choice



def initial_state():
    # board = gameBoard(test=True)
    board = gameBoard()
    x = player('x')
    o = player('o')
    print(board)
    print()
    return board, x, o


def play_game(board, x, o, tie_game=False):
    curr_player = choice((x, o))
    retry_move = False
    while not board.game_over() and not (tie_game := board.tie_game()):
        try:
            curr_player.move(board)
            # only switch players if no exception raised during move
            curr_player = o if curr_player.piece == 'x' else x

        except PositionFull:
            print('Position taken, please try again.')
        except InvalidMove:
            print('Invalid Move, please try again.')

    last_player = o if curr_player.piece == 'x' else x
    return tie_game, last_player.piece



def decide_winner(tie_game, winner):
    if tie_game:
        print("It's a tie! Thanks for playing!")
    else:
        print(f'Congratulations to: {winner}')


if __name__ == "__main__":
    decide_winner(*play_game(*initial_state()))

