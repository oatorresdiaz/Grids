from tkinter import *
from PIL import Image, ImageTk

class Sprite:

    image = PhotoImage()
    xCoord = 0 #Initial value
    yCoord = 0 #Initial value

    def __init__(self, imagePath):
        self.imagePath = imagePath

    def create(self):
        image = Image.open(self.imagePath)
        self.image = ImageTk.PhotoImage(image)

    def getImage(self):
        return self.image

    def setPosition(self, xCoord, yCoord):
        self.xCoord = xCoord
        self.yCoord = yCoord

    def getPosX(self):
        return self.xCoord

    def getPosY(self):
        return self.yCoord