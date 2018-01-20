from tkinter import *
import copy
import handlers.draw as Draw
import handlers.action as Action
import handlers.platformer as Platformer

class Controller:

    gameMode = None

    def __init__(self, window, grid):
        self.window = window
        self.grid = grid
        self.draw = Draw.Draw(window, grid)
        self.action = Action.Action(window, grid)
        self.platformer = Platformer.Platformer(window, grid, self.draw, self.action)

    def start(self):
        self.window.create()

    def drawIfLeftMouseClicked(self, sprite, anchor):
        if self.action.isLeftMouseClicked():
            x, y = self.action.getXY()
            sprite.setNativeTo(False)
            self.draw.draw(sprite, x, y, anchor)
            print(self.grid.coord[y][x])
            self.action.leftMouseClicked = False
        self.window.window.after(50, self.drawIfLeftMouseClicked, sprite, anchor)

    def drawIfLeftMouseClickedAndNoOverlapping(self, sprite, anchor):
        if self.action.isLeftMouseClicked():
            x, y = self.action.getXY()
            if len(self.grid.getSprites(x,y)) > 0:
                print("Cannot draw here because sprite exists.")
            else:
                sprite.setNativeTo(False)
                self.draw.draw(sprite, x, y, anchor)
                print(self.grid.coord[y][x])
            self.action.leftMouseClicked = False
        self.window.window.after(50, self.drawIfLeftMouseClickedAndNoOverlapping, sprite, anchor)

    def eraseIfLeftMouseClicked(self):
        if self.action.isLeftMouseClicked():
            x, y = self.action.getXY()
            self.draw.eraseSprite(x, y)
            self.action.leftMouseClicked = False
        self.window.window.after(50, self.eraseIfLeftMouseClicked)

    def usePlatformer(self):
        self.gameMode = 'platformer'
        self.platformer.start()
        self.window.window.after(50, self.usePlatformer)

    def restart(self):
        if self.action.getKeyPressed() == 'q': #THIS LINE IS FOR TESTING PURPOSES. REMOVE.
            self.draw.getGraphics().delete("all")
            sprites =  self.grid.clearDictionary()
            for x in range(self.grid.getHorizontalSize()):
                for y in range(self.grid.getVerticalSize()):
                    for spr in sprites[y][x]:
                        if not spr.isNative():
                            sprites[y][x].remove(spr)
                        else:
                            self.draw.draw(spr, x, y, spr.getAnchor())
            if self.gameMode == 'platformer':
                self.platformer.restart()
            self.draw.drawGrid()
        self.window.window.after(50, self.restart)




