from tkinter import *
import handlers.draw as Draw
import handlers.action as Action
import handlers.platformer as Platformer

class Controller:

    def __init__(self, window, grid):
        self.window = window
        self.grid = grid
        self.draw = Draw.Draw(window, grid)
        self.action = Action.Action(window, grid)
        self.platformer = Platformer.Platformer(window, grid, self.draw)

    def start(self):
        self.window.create()

    def drawIfLeftMouseClicked(self, sprite, anchor):
        if self.action.isLeftMouseClicked():
            x, y = self.action.getXY()
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

    # def moveSpriteIfKeyPressed(self):
    #     if self.action.getKeyPressed() == 'd':
    #         self.draw.moveSprite(5, 0)
    #     elif self.action.getKeyPressed() == 'a':
    #         self.draw.moveSprite(-5,0)
    #     self.window.window.after(50, self.moveSpriteIfKeyPressed)

    def usePlatformer(self):
        self.platformer.start()
        self.window.window.after(50, self.usePlatformer)




