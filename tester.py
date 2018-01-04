import handlers.window as Window
import handlers.grid as Grid
import handlers.draw as Draw
import handlers.sprite as Sprite

window = Window.Window("Sandbox", 500, 500)
grid = Grid.Grid(15, 15)
grid.create()
godzilla = Sprite.Sprite("/Users/orlandotorres/PycharmProjects/Grids/images/godzilla.png", 120, 79)
godzilla.create()
mario = Sprite.Sprite("/Users/orlandotorres/PycharmProjects/Grids/images/mario.png", 25, 22)
mario.create()
platform = Sprite.Sprite("/Users/orlandotorres/PycharmProjects/Grids/images/platform.png", 33, 33)
platform.create()
draw = Draw.Draw(window, grid)
#draw.drawOnEachCellInRow(1, godzilla)
#draw.drawOnEachCellInColumn(0, mario)
draw.drawOnEachCellInRow(12, platform)
draw.drawOnEachCellInRow(13, platform)
draw.drawOnEachCellInRow(14, platform)
window.create()