import copy

class Grid:

    coord = []
    sprites = {}

    def __init__(self, horSize, verSize):
        self.horSize = horSize
        self.verSize = verSize

    def create(self):
        self.coord = [[[] for x in range(self.horSize)] for y in range(self.verSize)]

    def addSpriteToCellDictionary(self, sprite, x, y):
        self.coord[y][x].append(sprite)

    def getSprites(self, x, y):
        return self.coord[y][x]

    def getHorizontalSize(self):
        return self.horSize

    def getVerticalSize(self):
        return self.verSize

    def clearDictionary(self):
        coordCopy = copy.copy(self.coord)
        self.coord.clear()
        self.create()
        return coordCopy
