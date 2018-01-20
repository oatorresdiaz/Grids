from tkinter import *

class Platformer:

    player = None
    gravity = 10
    gravityIsOn = True
    collisionGraphics = []


    def __init__(self, window, grid, draw):
        self.window = window
        self.grid = grid
        self.draw = draw

    def start(self): #TODO: FIX BUG LATER
        self.draw.moveSprite(self.player, 0, self.gravity)
        x1, y1, x2, y2 = self.draw.graphic.bbox(self.player.getGraphic())
        for graphic in self.draw.graphic.find_overlapping(x1, y1, x2, y2):
            if graphic in self.collisionGraphics:
                self.setGravity(0)
                break
            else:
                self.setGravity(10)
                break

    def setPlayer(self, sprite):
        self.player = sprite

    def getPlayer(self):
        return self.player

    def addCollisionSprite(self, sprite):
        self.findAllColissionsInGrid(sprite)
        print(sprite.getName(), self.collisionGraphics)

    def setGravity(self, gravity):
        self.gravity = gravity

    def findAllColissionsInGrid(self, sprite):
        for x in range(self.grid.getHorizontalSize()):
            for y in range(self.grid.getVerticalSize()):
                for spr in self.grid.getSprites(x, y):
                    if spr.getName() == sprite.getName():
                        self.collisionGraphics.append(spr.getGraphic())




