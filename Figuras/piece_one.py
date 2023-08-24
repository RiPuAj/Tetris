# Cuadrado
import random
from Movements.movements import *
from screen import Screen
from Figuras.piece import Piece
from Icons.icons import Icons

class PieceOne(Piece):

    def __init__(self):
        super().__init__()
        self.firstBlock = (0, random.randrange(0, 9))
        self.secondBlock = (0, self.firstBlock[1]+1)
        self.thirdBlock = (self.firstBlock[0]+1, self.firstBlock[1])
        self.fourthBlock = (self.firstBlock[0]+1, self.firstBlock[1]+1)
        self.oldCoordinates = [self.firstBlock, self.secondBlock, self.thirdBlock, self.fourthBlock]
        self.actualCoordinates = [self.firstBlock, self.secondBlock, self.thirdBlock, self.fourthBlock]
        self.type = 'ONE'
    
    def __del__(self):
        return

    def Position(self) -> list:
        return self.actualCoordinates
    
    def isAlive(self, screen: Screen) -> bool:
        
        if self.thirdBlock[0] == 9:
            return False
        
        elif self.fourthBlock[0] == 9:
            return False

        elif screen.screenList[self.thirdBlock[0]+1][self.thirdBlock[1]] == Icons.BLACK:
            return False
        
        elif screen.screenList[self.fourthBlock[0]+1][self.fourthBlock[1]] == Icons.BLACK:
            return False

        return True

    def printCoordinates(self):
        print(f'1era -> {self.firstBlock}')
        print(f'2a -> {self.secondBlock}')
        print(f'3era -> {self.thirdBlock}')
        print(f'4a -> {self.fourthBlock}')
        

          