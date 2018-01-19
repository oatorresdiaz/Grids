
class Platformer:

    gravity = 10
    player = None
    collisionSprites = []

    def __init__(self, window, grid, draw):
        self.window = window
        self.grid = grid
        self.draw = draw

    def start(self):
        self.draw.moveSprite(self.player, 0, self.gravity)

    def setPlayer(self, sprite):
        self.player = sprite

    def addCollisionSprite(self, sprite):
        self.collisionSprites.append(sprite)

    def setGravity(self, gravity):
        self.gravity = gravity

    def getPlayer(self):
        return self.player



