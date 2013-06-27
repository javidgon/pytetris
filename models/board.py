import sys

class Board(object):
    HEIGHT = 20
    WIDTH = 20
    def __init__(self):
        self.status = None

    def draw(self, pieces = []):
        for y in range(self.HEIGHT):
            for x in range(self.WIDTH):
                for piece in pieces:
                    if x == 0 or x == 19:
                        sys.stdout.write('*')
                    elif self.is_there_a_piece(piece, y, x):
                        sys.stdout.write('*')
                    else:
                        sys.stdout.write(' ') 
            sys.stdout.write('\n')
            if y == 19:
                sys.stdout.write('*' * 20)
        sys.stdout.write('\n')

    def is_there_a_piece(self, piece, board_y, board_x):
        decision = False
        for position_y, y in enumerate(piece.structure):
            for position_x, x in enumerate(y):
                if x[1] == board_y and x[0] == board_x:
                    decision = True
        return decision


