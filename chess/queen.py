from piece import Piece, Types

class Queen(Piece):
    def __init__(self, x, y, color):
        self._x = x
        self._y = y
        self._type = Types.QUEEN
        self._color = color