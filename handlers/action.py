from tkinter import *
import math as math

class Action:

    def __init__(self, window, grid):
        self.window = window
        self.grid = grid
        self.windowTk = window.getWindow()
        self.windowTk.bind('<Button-1>', self.leftMouseClick)

    def leftMouseClick(self, event):
        relx = self.windowTk.winfo_pointerx() - self.windowTk.winfo_rootx()
        rely = self.windowTk.winfo_pointery() - self.windowTk.winfo_rooty()
        x = relx/(self.window.getWidth()/self.grid.getHorizontalSize())
        y = rely/(self.window.getHeight()/self.grid.getVerticalSize())
        x = math.floor(x)
        y = math.floor(y)
        print(x, y) #TODO: DELETE



