from Icons.icons import *


class Screen():

    def __init__(self) -> None:
        self.screenList = [[Icons.WHITE.value] * 10 for _ in range(10)]


    def checkLines(self):
        
        completedRow = [Icons.BLACK.value] * 10

        for index, row in enumerate(self.screenList):
            if row == completedRow:
                self.screenList.pop(index)
                self.screenList.insert(0, [Icons.WHITE.value] * 10)

    def printScreen(self):

        for row in self.screenList:
            print(row, '\n')
