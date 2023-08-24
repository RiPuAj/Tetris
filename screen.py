from Icons.icons import *
# from Figuras.piece import Piece

class Screen():

    def __init__(self) -> None:
        self.screenList = [[Icons.WHITE.value] * 10 for _ in range(10)]
        self.screenList.append([Icons.BLACK.value]*10)
        self.currentFigure = None
    
    def setCurrent(self, newCurrent):
        self.currentFigure = newCurrent

    def checkLines(self):
        
        completedRow = [Icons.BLACK.value] * 10

        for index, row in enumerate(self.screenList):
            if row == completedRow:
                self.screenList.pop(index)
                self.screenList.insert(0, [Icons.WHITE.value] * 10)

    def printScreen(self):
        for row in self.screenList:
            print(row, '\n')
        print("------------------------------------------------------")