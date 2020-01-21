
from peice import Piece, Types

class Rook(Piece):
    def __init__(self, x, y, color):
        self._x = x
        self._y = y
        self._type = Types.ROOK
        self._color = color