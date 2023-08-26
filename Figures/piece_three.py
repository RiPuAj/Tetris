# Palo
from Figures.piece import Piece
from random import randrange

class PieceThree(Piece):
    
    def __init__(self):
        self.firstBlock = (0, randrange(0, 9))
        self.secondBlock = (1, self.firstBlock[1])
        self.thirdBlock = (2, self.firstBlock[1])
        self.fourthBlock = (3, self.firstBlock[1])
        self.oldCoordinates = [self.firstBlock, self.secondBlock, self.thirdBlock, self.fourthBlock]
        self.actualCoordinates = [self.firstBlock, self.secondBlock, self.thirdBlock, self.fourthBlock]
        self.type = 'THREE'
        self.rotation = 0