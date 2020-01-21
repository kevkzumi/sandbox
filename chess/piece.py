# parent class
class Types:
    PAWN = 'PAWN'
    KNIGHT = 'KNIGHT'
    KING = 'KING'
    QUEEN = 'QUEEN'
    ROOK = 'ROOK'
    BISHOP = 'BISHOP'

class COLOR:
    WHITE = 'WHITE'
    BLACK = 'BLACK'

class Piece:
    _x = None
    _y = None
    _type = None
    _taken = None
    _color = None
    _possible_moves = None

    def get_moves(self):
        pass

    def move(x, y):
        move = board.convert_coords(x, y)
        if move in _possible_moves():
            self._x = x
            self._y = y
        else:
            print('Invalid Move')
