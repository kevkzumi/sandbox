from piece import Piece, Types

class King(Piece):
    def __init__(self, x, y, color):
        self._x = x
        self._y = y
        self._type = Types.KING
        self._color = color