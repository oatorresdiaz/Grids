from tkinter import *
from PIL import Image, ImageTk

class Sprite:

    image = PhotoImage()
    graphic = None
    xCoord = 0 #Initial value
    yCoord = 0 #Initial value
    type = None #Type of sprite: player, enemy, wall, floor

    def __init__(self, name, imagePath, width, height, anchor):
        self.name = name
        self.imagePath = imagePath
        self.width = width
        self.height = height
        self.anchor = anchor

    def create(self):
        image_file = Image.open(self.imagePath).resize((self.width, self.height))
        self.image = ImageTk.PhotoImage(image_file)

    def getName(self):
        return self.name

    def getImage(self):
        return self.image

    def setGraphic(self, graphic):
        self.graphic = graphic

    def getGraphic(self):
        return self.graphic

    def setType(self, type):
        self.type = type

    def getType(self):
        return self.type

    def setPosition(self, xCoord, yCoord):
        self.xCoord = xCoord
        self.yCoord = yCoord

    def getPosX(self):
        return self.xCoord

    def getPosY(self):
        return self.yCoord

    def setAnchor(self, anchor):
        self.anchor = anchor

    def getAnchor(self):
        return self.anchor