from screen import Screen
from Movements.movements import Movements
from Icons.icons import Icons

class Piece(object):

    def __init__(self):
        self.firstBlock = ()
        self.secondBlock = ()
        self.thirdBlock = ()
        self.fourthBlock = ()
        self.oldCoordinates = []
        self.actualCoordinates = []
        self.type = None

    def setPosition(self, movement: Movements, screen: Screen) -> list:

        movementList = movement.value.get(self.type)
        self.oldCoordinates = self.actualCoordinates
        self.actualCoordinates = []

        for index, item in enumerate(movementList):

            (x, y) = (self.oldCoordinates[index][0] + item[0], self.oldCoordinates[index][1] + item[1])
            
            if x < 0 or x > 9:
                self.actualCoordinates = self.oldCoordinates
                return []
            
            elif y < 0 or y > 9:
            
                self.actualCoordinates = self.oldCoordinates
                print("TE HAS SALIDO DEL TABLERO")
                return []
            
            else:
                self.actualCoordinates.append((x, y))
        
        board = screen.screenList

        for item in self.oldCoordinates:

            board[item[0]][item[1]] = Icons.WHITE.value

        for item in self.actualCoordinates:

            if board[item[0]][item[1]] == Icons.BLACK.value:
                break
            else:
                board[item[0]][item[1]] = Icons.BLACK.value

        screen.screenList = board
        self.firstBlock = self.actualCoordinates[0]
        self.secondBlock = self.actualCoordinates[1]
        self.thirdBlock = self.actualCoordinates[2]
        self.fourthBlock = self.actualCoordinates[3]
