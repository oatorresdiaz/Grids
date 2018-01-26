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

godzilla = Sprite.Sprite('godzilla', "/Users/orlandotorres/PycharmProjects/Grids/images/godzilla.png", 120, 79, 's')
godzilla.create()

mario = Sprite.Sprite('mario', "/Users/orlandotorres/PycharmProjects/Grids/images/mario.png", 25, 36, 's')
mario.create()

platform = Sprite.Sprite('platform', "/Users/orlandotorres/PycharmProjects/Grids/images/platform.png", 33, 33, 'center')
platform.create()

controller = Controller.Controller(window, grid)
controller.draw.drawOnEachCellInRow(platform, 13, 'center')
controller.draw.drawOnEachCellInRow(platform, 14, 'center')
controller.draw.draw(godzilla, 5, 8, 's')
controller.draw.drawGrid()
#controller.drawIfLeftMouseClickedAndNoOverlapping(platform, 'center')
#controller.drawIfLeftMouseClicked(platform, 'center')
controller.eraseIfLeftMouseClicked()
#controller.moveSpriteIfKeyPressed(godzilla)
controller.platformer.setPlayer(godzilla)
controller.platformer.addCollisionSprite(platform)
controller.usePlatformer()
controller.restart()
controller.start()

# window = Window.Window("Game Board", 300, 300)
#
# grid = Grid.Grid(3,3)
# grid.create()
#
# sprite_x = Sprite.Sprite("x", "/Users/orlandotorres/PycharmProjects/Grids/images/x.png", 50, 50, 'center')
# sprite_x.create()
# sprite_zero = Sprite.Sprite("zero", "/Users/orlandotorres/PycharmProjects/Grids/images/zero.png", 50, 50, 'center')
# sprite_zero.create()
#
# controller = Controller.Controller(window, grid)
# controller.draw.drawGrid()
# controller.drawIfLeftMouseClickedAndNoOverlapping(sprite_x, 'center')
# controller.restart()
# controller.start()