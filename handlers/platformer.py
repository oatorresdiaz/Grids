from tkinter import *

class Platformer:

    player = None
    gravity = 10
    gravityIsOn = True
    collisionSprites = []

    def __init__(self, window, grid, draw):
        self.window = window
        self.grid = grid
        self.draw = draw

    def start(self): #TODO: FIX
        self.draw.moveSprite(self.player, 0, self.gravity)
        collbox =  self.draw.graphic.bbox(self.grid.getSprites(5, 13)[0])
        x1, y1, x2, y2 = self.draw.graphic.bbox(self.player.getGraphic())
        for collSpr in self.collisionSprites:
            for x in range(self.grid.getHorizontalSize()):
                for y in range(self.grid.getVerticalSize()):
                    for spr in self.grid.getSprites(x, y):
                        if spr.getName() == collSpr.getName() and spr.getGraphic() in self.draw.graphic.find_overlapping(x1, y1, x2, y2):
                            self.setGravity(0)

    def setPlayer(self, sprite):
        self.player = sprite

    def getPlayer(self):
        return self.player

    def addCollisionSprite(self, sprite):
        self.collisionSprites.append(sprite)

    def setGravity(self, gravity):
        self.gravity = gravity



