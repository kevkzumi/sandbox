# Chess board
from piece import COLOR, Types
from pawn import Pawn
from bishop import Bishop
from knight import Knight
from king import King
from queen import Queen
from rook import Rook

COLUMNS = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', ]
ROWS = ['1', '2', '3', '4', '5,' '6', '7', '8']

class GameBoard():
    def __init__(self):
        self.board = [[None for j in range(8)] for i in range(8)]
        self.pieces = []
        
        # set white board
        pieces = []
        for i in range(8):
            pieces.append(Pawn(i, 1, COLOR.WHITE))
        pieces.append(Rook(0, 0, COLOR.WHITE))
        pieces.append(Rook(7 ,0, COLOR.WHITE))
        pieces.append(Knight(1, 0, COLOR.WHITE))
        pieces.append(Knight(6, 0, COLOR.WHITE))
        pieces.append(Bishop(2, 0, COLOR.WHITE))
        pieces.append(Bishop(5, 0, COLOR.WHITE))
        pieces.append(King(3, 0, COLOR.WHITE))
        pieces.append(Queen(4, 0, COLOR.WHITE))

        #set black peices
        for i in range(8):
            pieces.append(Pawn(i, 6, COLOR.BLACK))
        pieces.append(Rook(0, 7, COLOR.BLACK))
        pieces.append(Rook(7 ,7, COLOR.BLACK))
        pieces.append(Knight(1, 7, COLOR.BLACK))
        pieces.append(Knight(6, 7, COLOR.BLACK))
        pieces.append(Bishop(2, 7, COLOR.BLACK))
        pieces.append(Bishop(5, 7, COLOR.BLACK))
        pieces.append(King(3, 7, COLOR.BLACK))
        pieces.append(Queen(4, 7, COLOR.BLACK))

        for _piece in pieces:
            self.pieces.append(_piece)
            self.board[_piece._x][_piece._y] = _piece

    def is_valid_move(self, x, y):
        within_bounds = x >= 0 and y >=0 and x < 8 and y < 8
        is_king = self.board[x, y] and self.board[x, y]._type == Types.KING
        return within_bounds and not is_king
    
    def move_peice(self, init_x, init_y, new_x, new_y):
        peice_to_move = self.board[init_x, init_y]
        if convert_coords(new_x, new_y) in peice_to_move._possible_moves:
            if self.board[new_x, new_y]:
                self.board[new_x, new_y]._taken = True
            self.board[init_x, init_x] = None
            self.board[new_x, new_y] = peice_to_move
            peice_to_move.move(new_x, new_y)
        for other_peice in self.pieces:
            other_peice.get_moves(self)
    
    def print(self):
        for y in range(8):
            row = ''
            for x in range(8):
                if self.board[x][y]:
                    row += self.board[x][y]._type
                else:
                    row += ' - '
            print(row)

def convert_coords(x, y):
    return '{}{}'.format(COLUMNS[x], ROWS[y])