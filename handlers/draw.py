from tkinter import *
import handlers.window as Window
import handlers.grid as Grid
import handlers.sprite as Sprite

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
            self.graphic.create_image(xCoord, yCoord, image=sprite.getImage())
            self.graphic.pack(fill=BOTH, expand=1)
        else:
            print("ERROR: Cannot draw on that position because it does not exist on the grid.")

    def drawOnEachCellInRow(self, row, sprite):
        if self.doesRowExist(row):
            for cell in range(0, self.grid.getHorizontalSize()):
                self.draw(sprite, cell, row)
        else:
            print("ERROR: Cannot draw on that row because it does not exist in the grid.")

    def drawOnEachCellInColumn(self, column, sprite):
        if self.doesColumnExist(column):
            for cell in range(0, self.grid.getVerticalSize()):
                self.draw(sprite, column, cell)
        else:
            print("ERROR: Cannot draw on that column because it does not exist in the grid.")

    def getXCoordinate(self, x):
        cellSize = self.getCellWidth()
        return cellSize/2 + cellSize*x

    def getYCoordinate(self, y):
        cellSize = self.getCellHeight()
        return cellSize/2 + cellSize*y

    def doesRowExist(self, row):
        if row >= 0 and row < self.grid.getVerticalSize():
            return True
        return False

    def doesColumnExist(self, column):
        if column >= 0 and column < self.grid.getHorizontalSize():
            return True
        return False

    def doesCoordinateExists(self, xCoord, yCoord):
        if self.doesRowExist(yCoord):
            if self.doesColumnExist(xCoord):
                return True
        return False

    def getCellWidth(self):
        return self.window.getWidth() / self.grid.getHorizontalSize()

    def getCellHeight(self):
        return self.window.getHeight() / self.grid.getVerticalSize()