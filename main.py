from random import randrange
from screen import Screen
from Figures.piece_one import *
from Figures.piece_two import *
from Figures.piece_three import *
from Figures.piece_four import *
from Movements.movements import *
from pynput import keyboard
from os import system
from time import sleep

def createFigure(screen: Screen):
    randomSelection = randrange(0, 100) % 4

    if randomSelection == 0:
        newPiece = PieceOne()
        newPiece.setPosition(movement=Movements.NONE,
                             screen=screen
                             )
        return newPiece
    
    elif randomSelection == 1:
        newPiece = PieceTwo()
        newPiece.setPosition(movement=Movements.NONE,
                             screen=screen
                             )
        return newPiece
    
    elif randomSelection == 2:
        newPiece = PieceThree()
        newPiece.setPosition(movement=Movements.NONE,
                             screen=screen
                             )
        return newPiece
    
    else:
        newPiece = PieceFour()
        newPiece.setPosition(movement=Movements.NONE,
                             screen=screen
                             )
        return newPiece
    
def on_press(key, currentFigure: Piece, screen: Screen):
    
    if key == keyboard.Key.right:
        currentFigure.setPosition(Movements.RIGHT, screen)

    elif key == keyboard.Key.left:
        currentFigure.setPosition(Movements.LEFT, screen)

    elif key == keyboard.Key.down:
        currentFigure.setPosition(Movements.DOWN, screen)
    
    elif key == keyboard.Key.up:
        currentFigure.setPosition(Movements.ROTATE, screen)
    
    system('cls')
    screen.printScreen()
    # print("ACTUALES:", currentFigure.actualCoordinates, "ROTACION:", currentFigure.rotation)
    # print("--------------------------------------------------------")


def gameOver(currentFigure: Piece, screen: Screen):
    for item in currentFigure.actualCoordinates:
        if item[0] == 0:
            return True
    return False

def main():
    screen = Screen()
    currentFigure = createFigure(screen)
    listenerKeyboard = keyboard.Listener(on_press=lambda key: 
                                         on_press(key,
                                         currentFigure=currentFigure,
                                         screen=screen
                                         )
                                        )
    listenerKeyboard.start()



    while True:

        if currentFigure == None:
            currentFigure = createFigure(screen)
        else:
            if currentFigure.isAlive(screen) == False:
                if gameOver(currentFigure, screen):
                    break
                
                currentFigure = None
                continue
            
            else:
                sleep(1)
                currentFigure.setPosition(Movements.DOWN, screen)

        screen.checkLines()
        system('cls')
        screen.printScreen()
    


if __name__ == "__main__":
    main()
    

