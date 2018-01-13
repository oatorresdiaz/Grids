
class Grid:

    coord = []
    sprites = []

    def __init__(self, horSize, verSize):
        self.horSize = horSize
        self.verSize = verSize

    def create(self):
        #self.coord = [[None for xCoord in range(self.horSize)] for yCoord in range(self.verSize)]
        self.coord = [[[] for x in range(self.horSize)] for y in range(self.verSize)]

    def addSpriteToCellDictionary(self, sprite, x, y):
        self.coord[y][x].append(sprite)
        self.sprites.append(sprite)

    def getSprites(self, x, y):
        return self.coord[y][x]

    def getHorizontalSize(self):
        return self.horSize

    def getVerticalSize(self):
        return self.verSize
