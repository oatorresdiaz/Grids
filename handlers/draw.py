from tkinter import *
from PIL import Image, ImageTk
import handlers.window as Window
import handlers.grid as Grid
import handlers.sprite as Sprite
import sys

class Draw:

    graphic = Canvas()
    entry = Entry()
    sprites = []

    def __init__(self, window, grid):
        self.window = window
        self.grid = grid

    def draw(self, sprite, x, y):
        if self.doesCoordinateExists(x, y):
            xCoord = self.getXCoordinate(x)
            yCoord = self.getYCoordinate(y)
            sprite.setPosition(xCoord, yCoord)
            self.sprites.append(sprite)
            self.graphic.create_image(xCoord, yCoord, image=self.sprites[len(self.sprites) -1].getImage())
            self.graphic.pack(fill=BOTH, expand=1)
        else:
            print("ERROR: Cannot draw on that position because it does not exist on the grid.")

    def getXCoordinate(self, x):
        cellSize = self.window.getWidth()/self.grid.getHorizontalSize()
        return cellSize/2 + cellSize*x

    def getYCoordinate(self, y):
        cellSize = self.window.getHeight()/self.grid.getVerticalSize()
        return cellSize/2 + cellSize*y

    def doesCoordinateExists(self, xCoord, yCoord):
        if yCoord >= 0 and yCoord < self.grid.getVerticalSize():
            if xCoord >= 0 and xCoord < self.grid.getHorizontalSize():
                return True
        return False


#FOR TESTING. ERASE AFTER USE.
window = Window.Window('Window1', 500, 500)
grid = Grid.Grid(3, 3)
grid.create()
marioImagePath = "/Users/orlandotorres/PycharmProjects/Grids/images/mario.png"
godzillaImagePath = "/Users/orlandotorres/PycharmProjects/Grids/images/godzilla.png"
mario = Sprite.Sprite(marioImagePath, 23, 25)
mario.create()
godzilla = Sprite.Sprite(godzillaImagePath, 73, 48)
godzilla.create()
draw = Draw(window, grid)
draw.draw(mario, 0, 0)
draw.draw(godzilla, 1, 1)
draw.draw(mario, 2, 2)
window.create()