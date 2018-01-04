from tkinter import *
from PIL import Image, ImageTk

class Sprite:

    image = PhotoImage()
    xCoord = 0 #Initial value
    yCoord = 0 #Initial value

    def __init__(self, imagePath, width, height):
        self.imagePath = imagePath
        self.width = width
        self.height = height

    def create(self):
        image_file = Image.open(self.imagePath).resize((self.width, self.height))
        self.image = ImageTk.PhotoImage(image_file)

    def getImage(self):
        return self.image

    def setPosition(self, xCoord, yCoord):
        self.xCoord = xCoord
        self.yCoord = yCoord

    def getPosX(self):
        return self.xCoord

    def getPosY(self):
        return self.yCoord