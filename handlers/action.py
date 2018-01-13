from tkinter import *
import math as math
import handlers.draw as Draw

class Action:

    x, y = 0, 0 #Defines the position where the mouse was clicked
    leftMouseClicked = False
    drawIfLeftMouseClickedEnabled = False
    keyPressed = False

    def __init__(self, window, grid):
        self.window = window
        self.grid = grid
        self.draw = Draw.Draw(window, grid)
        self.windowTk = window.getWindow()
        self.windowTk.bind('<Button-1>', self.leftMouseClick)
        self.windowTk.bind('<ButtonRelease-1>', self.leftMouseRelease)
        self.windowTk.bind('<KeyPress>', self.keyPress)
        self.windowTk.bind('<KeyRelease>', self.keyRelease)

    def leftMouseClick(self, event):
        relx = self.windowTk.winfo_pointerx() - self.windowTk.winfo_rootx()
        rely = self.windowTk.winfo_pointery() - self.windowTk.winfo_rooty()
        x = relx/(self.window.getWidth()/self.grid.getHorizontalSize())
        y = rely/(self.window.getHeight()/self.grid.getVerticalSize())
        x = math.floor(x)
        y = math.floor(y)
        self.setXY(x, y)
        self.leftMouseClicked = True

    def leftMouseRelease(self, event):
        self.leftMouseClicked = False
        return self.getXY()

    def keyPress(self, event):
        print("Key is pressed")
        self.keyPressed = event.keysym

    def keyRelease(self, event):
        print("Key is released")
        self.keyPressed = None

    def isLeftMouseClicked(self):
        return self.leftMouseClicked

    def getKeyPressed(self):
        return self.keyPressed

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

    def setXY(self, x, y):
        self.x, self.y = x, y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getXY(self):
        return self.x, self.y


