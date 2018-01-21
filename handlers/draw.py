from tkinter import *
import copy

class Draw:

    graphic = Canvas()
    entry = Entry()

    def __init__(self, window, grid):
        self.window = window
        self.grid = grid

    def draw(self, sprite, x, y, anchor):
        if self.doesCoordinateExists(x, y):
            xCoord = self.getXCoordinate(x, anchor)
            yCoord = self.getYCoordinate(y, anchor)
            sprite.setPosition(xCoord, yCoord)
            spr = self.graphic.create_image(xCoord, yCoord, anchor=sprite.getAnchor(), image=sprite.getImage())
            sprite.setGraphic(spr)
            self.grid.addSpriteToCellDictionary(copy.copy(sprite), x, y)
            self.graphic.pack(fill=BOTH, expand=1)
        else:
            print("ERROR: Cannot draw on that position because it does not exist on the grid.")

    def drawOnEachCellInRow(self, sprite, row, anchor):
        if self.doesRowExist(row):
            for cell in range(0, self.grid.getHorizontalSize()):
                self.draw(sprite, cell, row, anchor)
        else:
            print("ERROR: Cannot draw on that row because it does not exist in the grid.")

    def drawOnEachCellInColumn(self, column, sprite, anchor):
        if self.doesColumnExist(column):
            for cell in range(0, self.grid.getVerticalSize()):
                self.draw(sprite, column, cell, anchor)
        else:
            print("ERROR: Cannot draw on that row because it does not exist in the grid.")

    def drawGrid(self):
        verLines = self.grid.getHorizontalSize() - 1
        horLines = self.grid.getVerticalSize() - 1
        for x in range(1, verLines + 1):
            self.graphic.create_line(x*self.getCellWidth(), 0, x*self.getCellWidth(), self.window.getHeight())
        for y in range(1, horLines + 1):
            self.graphic.create_line(0, y*self.getCellHeight(), self.window.getWidth(), y*self.getCellHeight())
        self.graphic.pack(fill=BOTH, expand=1)

    def eraseSprite(self, x, y):
        sprites = self.grid.getSprites(x, y)
        for sprite in sprites:
            self.graphic.delete(sprite.getGraphic())

    def moveSprite(self, sprite, x, y): #TODO: FIX
        img = sprite.getGraphic()
        self.graphic.move(img, x, y)
        self.graphic.update()


    def getXCoordinate(self, x, anchor):
        cellSize = self.getCellWidth()
        if anchor == 'n' or anchor == 'center' or anchor == 's':
            return cellSize/2 + cellSize*x
        elif anchor == 'nw' or anchor == 'w' or anchor == 'sw':
            return cellSize*x
        elif anchor == 'ne' or anchor == 'w' or anchor == 'se':
            return cellSize + cellSize*x
        elif not anchor:
            return self.getXCoordinate(x, 'center') #Default
        return 0

    def getYCoordinate(self, y, anchor):
        cellSize = self.getCellHeight()
        if anchor == 'nw' or anchor == 'n' or anchor == 'ne':
            return cellSize*y
        elif anchor == 'w' or anchor == 'center' or anchor == 'w':
            return cellSize/2 + cellSize*y
        elif anchor == 'sw' or anchor == 's' or anchor == 'se':
            return cellSize + cellSize*y
        elif not anchor:
            return self.getYCoordinate(y, 'center') #Default
        return 0

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

    def getGraphics(self):
        return self.graphic