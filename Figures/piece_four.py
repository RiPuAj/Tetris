# Zig zag
from Figures.piece import Piece
from random import randrange

class PieceFour(Piece):

    def __init__(self):
        self.firstBlock = (0, randrange(2, 9))
        self.secondBlock = (self.firstBlock[0], self.firstBlock[1] -1)
        self.thirdBlock = (self.secondBlock[0] + 1, self.secondBlock[1])
        self.fourthBlock = (self.thirdBlock[0], self.thirdBlock[1]-1)
        self.oldCoordinates = [self.firstBlock, self.secondBlock, self.thirdBlock, self.fourthBlock]
        self.actualCoordinates = [self.firstBlock, self.secondBlock, self.thirdBlock, self.fourthBlock]
        self.type = 'FOUR'
        self.rotation = 0