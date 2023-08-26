from screen import Screen
from Movements.movements import Movements
from Icons.icons import Icons


class Piece():

    def __init__(self):
        self.firstBlock = ()
        self.secondBlock = ()
        self.thirdBlock = ()
        self.fourthBlock = ()
        self.oldCoordinates = []
        self.actualCoordinates = []
        self.type = None
        self.rotation = 0

    def setPosition(self, movement: Movements, screen: Screen):

        self.oldCoordinates = self.actualCoordinates
        self.actualCoordinates = []
        
        if movement == Movements.ROTATE:
            
            movementList = movement.value.get(self.type)[self.rotation]
            self.rotation = 0 if self.rotation == 3 else self.rotation + 1
        
        else:
            movementList = movement.value.get(self.type)

        
        for index, item in enumerate(movementList):

            (x, y) = (self.oldCoordinates[index][0] + item[0], self.oldCoordinates[index][1] + item[1])
            
            if x < 0 or x > 9:
                self.actualCoordinates = self.oldCoordinates
                if movement == Movements.ROTATE:
                    self.rotation = self.rotation - 1 if self.rotation > 0 else 3
                return
            
            elif y < 0 or y > 9:
                self.actualCoordinates = self.oldCoordinates
                if movement == Movements.ROTATE:
                    self.rotation = self.rotation -1 if self.rotation > 0 else 3
                return
            
            elif screen.screenList[x][y] == Icons.BLACK.value and (x, y) not in self.oldCoordinates:
                
                self.actualCoordinates = self.oldCoordinates
                if movement == Movements.ROTATE:
                    self.rotation = self.rotation - 1 if self.rotation > 0 else 3
                return

            else:
                self.actualCoordinates.append((x, y))

        for item in self.oldCoordinates:
            screen.screenList[item[0]][item[1]] = Icons.WHITE.value
        
        for item in self.actualCoordinates:
            screen.screenList[item[0]][item[1]] = Icons.BLACK.value

        self.firstBlock = self.actualCoordinates[0]
        self.secondBlock = self.actualCoordinates[1]
        self.thirdBlock = self.actualCoordinates[2]
        self.fourthBlock = self.actualCoordinates[3]

    def isAlive(self, screen: Screen) -> bool:
        
        if self.firstBlock[0] == 9:
            return False

        elif self.secondBlock[0] == 9:
            return False

        elif self.thirdBlock[0] == 9:
            return False
        
        elif self.fourthBlock[0] == 9:
            return False

        for item in self.actualCoordinates:
            x = item[0] + 1
            y = item[1]
            
            if (x, y) not in self.actualCoordinates:
                if screen.screenList[x][y] == Icons.BLACK.value:
                    return False

        return True

