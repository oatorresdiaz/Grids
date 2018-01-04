
class Grid:

    coord = [[]]
    sprites = {} #This would be the sprite dictionary located on each grid cell

    def __init__(self, horSize, verSize):
        self.horSize = horSize
        self.verSize = verSize

    def create(self):
        self.coord = [[self.sprites for xCoord in range(self.horSize)] for yCoord in range(self.verSize)]

    def getHorizontalSize(self):
        return self.horSize

    def getVerticalSize(self):
        return self.verSize