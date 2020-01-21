from piece import Piece, Types, COLOR
import board

COLOR_MOVE_MODIFYERS = {
    COLOR.WHITE: 1,
    COLOR.BLACK: -1
}

class Pawn(Piece):
    def __init__(self, x, y, color):
        self._x = x
        self._y = y
        self._type = Types.PAWN
        self._color = color
        self._taken = False
        self._first_move = True
        self._possible_moves = None
    
    def get_moves(self, game_board):
        possible_moves = set()
        # move forward 1 space
        x = self._x
        y = self._y + 1 * (COLOR_MOVE_MODIFYERS[self._color])
        if game_board.is_valid_move(x, y):
            if not game_board[x, y]:
                possible_moves.add(board.convert_coords(x, y))
        # take opposing peice in the diagnal
        x = self._x + 1
        y = self._y + 1 * (COLOR_MOVE_MODIFYERS[self._color])
        if game_board.is_valid_move(x, y):
            if game_board[x, y] and game_board[x, y]._color != self._color:
                possible_moves.add(board.convert_coords(x, y))
        x = self._x - 1
        y = self._y + 1 * (COLOR_MOVE_MODIFYERS[self._color])
        if game_board.is_valid_move(x, y):
            if game_board[x, y] and game_board[x, y]._color != self._color:
                possible_moves.add(board.convert_coords(x, y))
        # first pawn move
        x = self._x
        y = self._y + 2 * (COLOR_MOVE_MODIFYERS[self._color])
        if self._first_move:
            if not game_board[x, y]:
                possible_moves.add(board.convert_coords(x, y))

        self._possible_moves = possible_moves

        if self._taken:
            possible_moves = set()
    