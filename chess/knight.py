from piece import Piece, Types

class Knight(Piece):
    def __init__(self, x, y, color):
        self._x = x
        self._y = y
        self._type = Types.KNIGHT
        self._color = color