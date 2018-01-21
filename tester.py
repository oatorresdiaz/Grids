from tkinter import *
import handlers.window as Window
import handlers.grid as Grid
import handlers.draw as Draw
import handlers.sprite as Sprite
import handlers.action as Action
import handlers.controller as Controller

# window = Window.Window("Sandbox", 500, 500)
#
# grid = Grid.Grid(15, 15)
# grid.create()
#
# godzilla = Sprite.Sprite("/Users/orlandotorres/PycharmProjects/Grids/images/godzilla.png", 120, 79, 's')
# godzilla.create()
#
# mario = Sprite.Sprite("/Users/orlandotorres/PycharmProjects/Grids/images/mario.png", 25, 36, 's')
# mario.create()
#
# platform = Sprite.Sprite("/Users/orlandotorres/PycharmProjects/Grids/images/platform.png", 33, 33, 'center')
# platform.create()
#
# controller = Controller.Controller(window, grid)
# controller.draw.drawOnEachCellInRow(platform, 13, 'center')
# controller.draw.drawOnEachCellInRow(platform, 14, 'center')
# controller.draw.draw(godzilla, 5, 12, 's')
# controller.draw.drawGrid()
# controller.drawIfLeftMouseClickedAndNoOverlapping(platform, 'center')
# #controller.drawIfLeftMouseClicked(platform, 'center')
# #controller.eraseIfLeftMouseClicked()
# controller.moveSpriteIfKeyPressed()
# controller.start()

window = Window.Window("Game Board", 500, 500)

grid = Grid.Grid(3,3)
grid.create()

sprite_x = Sprite.Sprite("uprm.png", 150, 150, 'center')
sprite_x.create()

controller = Controller.Controller(window, grid)
controller.draw.drawGrid()
controller.drawIfLeftMouseClickedAndNoOverlapping(sprite_x, 'center')
controller.start()
