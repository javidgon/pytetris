import models.board
import models.piece
from random import randint

class Main(object):
    VALID_MOVEMENTS = ['a', 'd', 's']
    def __init__(self):
        self.board = models.board.Board()
        self.pieces = []
        self.start()

    def start(self):
        self.board.draw()
        self.pieces.append(self.create_piece())
        while True:
            movement = raw_input("Please make a move: ")
            if movement in self.VALID_MOVEMENTS:
                if movement == 'a':
                    self.move('left')
                elif movement == 'd':
                    self.move('right')
                elif movement == 's':
                    self.rotate()                
                self.move('down')
                self.board.draw(self.pieces)
            else:
                print('Sorry that\'s not a valid movement')

    def move(self, type='down'):
        for position_y, y in enumerate(self.pieces[0].structure):
            for position_x, x in enumerate(y):
                if x[0] != 0:
                    if type == 'right':
                        x[0] += 1
                    elif type == 'left':
                        x[0] -= 1
                    elif type == 'down':
                        x[1] += 1

    def rotate(self, type='clockwise'):
        
        self.pieces[-1].put_in_the_board(10)

    def create_piece(self):
        piece_type = randint(1, 5)
        piece_position = randint(1, 16)
        
        piece = models.piece.Piece(piece_type,
                                   piece_position)
        return piece



if __name__ == '__main__':
    program = Main()
