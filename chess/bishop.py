from peice import Peice, Types

class Bishop(Peice):
    def __init__(self, x, y, color):
        self._x = x
        self._y = y
        self._type = Types.BISHOP
        self._color = color