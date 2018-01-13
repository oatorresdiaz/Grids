from tkinter import *
import handlers.draw as Draw
import handlers.action as Action

class Controller:

    sprite = None
    anchor = None

    def __init__(self, window, grid):
        self.window = window
        self.grid = grid
        self.draw = Draw.Draw(window, grid)
        self.action = Action.Action(window, grid)

    def start(self):
        self.window.create()

    def drawIfLeftMouseClicked(self, sprite, anchor):
        if self.action.isLeftMouseClicked():
            x, y = self.action.getXY()
            self.draw.draw(sprite, x, y, anchor)
            print(self.grid.coord[y][x])
            self.action.leftMouseClicked = False
        self.window.window.after(50, self.drawIfLeftMouseClicked, sprite, anchor)

    def eraseIfLeftMouseClicked(self):
        if self.action.isLeftMouseClicked():
            x, y = self.action.getXY()
            self.draw.eraseSprite(x, y)
            self.action.leftMouseClicked = False
        self.window.window.after(50, self.eraseIfLeftMouseClicked)

    def setSpriteAndAnchor(self, sprite, anchor):
        self.sprite = sprite
        self.anchor = anchor

