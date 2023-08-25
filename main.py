from random import randrange
from screen import Screen
from Figuras.piece_one import *
from Figuras.piece_two import *
from Figuras.piece_three import *
from Figuras.piece_four import *
from Movements.movements import *
from pynput import keyboard
from time import sleep

def createFigure(screen: Screen):
    randomSelection = randrange(0, 3)

    if randomSelection == 0:
        newPiece = PieceOne()
        newPiece.setPosition(None, screen=screen)
        return newPiece
    
    elif randomSelection == 1:
        newPiece = PieceTwo()
        newPiece.setPosition(None, screen=screen)
        return newPiece
    
    elif randomSelection == 2:
        newPiece = PieceThree()
        newPiece.setPosition(None, screen=screen)
        return newPiece
    
    else:
        newPiece = PieceFour()
        newPiece.setPosition(None, screen=screen)
        return newPiece
    
def on_press(key):
    
    if key == keyboard.Key.right:


screen = Screen()
figura = PieceOne()
figura.setPosition(None, screen=screen)
screen.setCurrent(figura)

while True:

    # if screen.currentFigure == None:
    #     screen.setCurrent(createFigure())

    # else:
    #     if screen.currentFigure.isAlive == False:
    #         del screen.currentFigure
    #         screen.setCurrent(None)
    #         continue
    #     else:

    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    

