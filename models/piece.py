

class Piece(object):
    def __init__(self, type = None, position = None):
        self.structure = [[[0,0],[0,0],[0,0],[0,0]],
                          [[0,0],[0,0],[0,0],[0,0]],
                          [[0,0],[0,0],[0,0],[0,0]],
                          [[0,0],[0,0],[0,0],[0,0]]]
        self.position = position
        if type == 1:
            self.structure = [[[1,1],[1,1],[1,1],[1,1]],
                          [[0,0],[0,0],[0,0],[0,0]],
                          [[0,0],[0,0],[0,0],[0,0]],
                          [[0,0],[0,0],[0,0],[0,0]]]
        elif type == 2:
            self.structure = [[[1,1],[0,0],[0,0],[0,0]],
                          [[1,1],[0,0],[0,0],[0,0]],
                          [[1,1],[1,1],[0,0],[0,0]],
                          [[0,0],[0,0],[0,0],[0,0]]]
        elif type == 3:
            self.structure = [[[0,0],[1,1],[0,0],[0,0]],
                          [[0,0],[1,1],[0,0],[0,0]],
                          [[1,1],[1,1],[0,0],[0,0]],
                          [[0,0],[0,0],[0,0],[0,0]]]
        elif type == 4:
            self.structure = [[[0,0],[1,1],[0,0],[0,0]],
                           [[1,1],[1,1],[0,0],[0,0]],
                           [[1,1],[0,0],[0,0],[0,0]],
                          [[0,0],[0,0],[0,0],[0,0]]]
        elif type == 5:
            self.structure = [[[1,1],[1,1],[0,0],[0,0]],
                           [[1,1],[1,1],[0,0],[0,0]],
                           [[0,0],[0,0],[0,0],[0,0]],
                          [[0,0],[0,0],[0,0],[0,0]]]

        self.put_in_the_board(self.position)      
    def put_in_the_board(self, position): 
        for position_y, dim1 in enumerate(self.structure):
            for position_x, dim2 in enumerate(dim1):
                dim2[0] = (position + position_x) * dim2[0]
                dim2[1] = position_y * dim2[1]

