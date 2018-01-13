from tkinter import *
import handlers.window as Window
import handlers.grid as Grid
import handlers.draw as Draw
import handlers.sprite as Sprite
import handlers.action as Action
import handlers.controller as Controller

window = Window.Window("Sandbox", 500, 500)

grid = Grid.Grid(15, 15)
grid.create()

godzilla = Sprite.Sprite("/Users/orlandotorres/PycharmProjects/Grids/images/godzilla.png", 120, 79, 's')
godzilla.create()

mario = Sprite.Sprite("/Users/orlandotorres/PycharmProjects/Grids/images/mario.png", 25, 36, 's')
mario.create()

platform = Sprite.Sprite("/Users/orlandotorres/PycharmProjects/Grids/images/platform.png", 33, 33, 'center')
platform.create()

controller = Controller.Controller(window, grid)
controller.draw.draw(platform, 5, 12, 'center')
controller.draw.draw(platform, 5, 12, 'center')
controller.draw.draw(platform, 5, 12, 'center')
controller.draw.drawOnEachCellInRow(platform, 13, 'center')
controller.draw.drawOnEachCellInRow(platform, 14, 'center')
controller.draw.drawGrid()
# draw = Draw.Draw(window, grid)
# draw.draw(platform, 12, 10, 'center')
# draw.draw(platform, 11, 11, 'center')
# draw.draw(platform, 12, 11, 'center')
# draw.draw(platform, 12, 12, 'center')
# draw.draw(platform, 10, 12, 'center')
# draw.draw(platform, 11, 12, 'center')
# draw.draw(platform, 12, 12, 'center')
# draw.draw(platform, 12, 12, 'center')
# draw.drawOnEachCellInRow(platform, 13, 'center')
# draw.drawOnEachCellInRow(platform, 14, 'center')
# draw.draw(mario, 2, 12, 's')
# draw.draw(godzilla, 7, 12, 's')
# draw.drawGrid()
#action = Action.Action(window, grid)
#window.create()
controller.drawIfLeftMouseClicked(platform, 'center')
#controller.eraseIfLeftMouseClicked()
controller.start()