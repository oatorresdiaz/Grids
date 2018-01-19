from tkinter import *

class Window:

    window = Tk()

    def __init__(self, name, width, height):
        self.name = name
        self.width = width
        self.height = height


    def create(self):
        self.window.wm_title(self.name)
        self.window.minsize(self.width, self.height)
        self.window.mainloop()

    def getWindow(self):
        return self.window

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

