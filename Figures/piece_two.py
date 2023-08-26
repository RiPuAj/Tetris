# Ele
from Figures.piece import Piece
from screen import Screen
from Icons.icons import Icons
from random import randrange

class PieceTwo(Piece):
    
    def __init__(self):
        self.firstBlock = (0, randrange(0, 7))
        self.secondBlock = (1, self.firstBlock[1])
        self.thirdBlock = (1, self.firstBlock[1] + 1)
        self.fourthBlock = (1, self.firstBlock[1] + 2)
        self.oldCoordinates = [self.firstBlock, self.secondBlock, self.thirdBlock, self.fourthBlock]
        self.actualCoordinates = [self.firstBlock, self.secondBlock, self.thirdBlock, self.fourthBlock]
        self.type = 'TWO'
        self.rotation = 0
    
    def __del__(self):
        return
        