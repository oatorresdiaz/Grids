import handlers.draw as Draw
import handlers.action as Action
import handlers.rule as Rule


class Controller:

    player = 0

    def __init__(self, window, grid, gb, winPos):
        self.window = window
        self.grid = grid
        self.draw = Draw.Draw(window, grid)
        self.action = Action.Action(window, grid)
        self.gb = gb
        self.winPos = winPos
        self.rule = Rule.Rule(self.winPos)

    def start(self):
        self.window.create()

    def drawIfLeftMouseClicked(self, sprite1, sprite2, anchor):
        if self.action.isLeftMouseClicked():
            if self.player == 0:
                x, y = self.action.getXY()
                self.draw.draw(sprite1, x, y, anchor)
                print(self.grid.coord[y][x])
                self.action.leftMouseClicked = False
                self.player = 1
            else:
                x, y = self.action.getXY()
                print(type(sprite2))
                self.draw.draw(sprite2, x, y, anchor)
                print(self.grid.coord[y][x])
                self.action.leftMouseClicked = False
                self.player = 0
        self.window.window.after(50, self.drawIfLeftMouseClicked, sprite1, sprite2, anchor)

    def drawIfLeftMouseClickedAndNoOverlapping(self, sprite, anchor):
        if self.action.isLeftMouseClicked():
            x, y = self.action.getXY()
            if len(self.grid.getSprites(x,y)) > 0:
                print("Cannot draw here because sprite exists.")
            else:
                self.draw.draw(sprite, x, y, anchor)
                print(self.grid.coord[y][x])
            self.action.leftMouseClicked = False
        self.window.window.after(50, self.drawIfLeftMouseClickedAndNoOverlapping, sprite, anchor)

    def drawIfLeftMouseClickedAndNoOverlapping2(self, sprite1, sprite2):
        if self.action.isLeftMouseClicked():
            x, y = self.action.getXY()
            if len(self.grid.getSprites(x,y)) > 0:
                print("Cannot draw here because sprite exists.")
            else:
                if self.player == 0:
                    self.draw.draw(sprite1, x, y, "center")
                    print(self.grid.coord[y][x])
                    self.action.leftMouseClicked = False
                    self.player = 1
                    self.gb[str(x) + ',' + str(y)] = sprite1.imagePath
                    if self.rule.winByEquality3(self.gb):
                        print('Player 1 has won!')
                else:
                    self.draw.draw(sprite2, x, y, "center")
                    print(self.grid.coord[y][x])
                    self.action.leftMouseClicked = False
                    self.player = 0
                    self.gb[str(x) + ',' + str(y)] = sprite2.imagePath
                    if self.rule.winByEquality3(self.gb):
                        print('Player 2 has won!')


        self.window.window.after(50, self.drawIfLeftMouseClickedAndNoOverlapping2, sprite1, sprite2)



    def eraseIfLeftMouseClicked(self):
        if self.action.isLeftMouseClicked():
            x, y = self.action.getXY()
            self.draw.eraseSprite(x, y)
            self.action.leftMouseClicked = False
        self.window.window.after(50, self.eraseIfLeftMouseClicked)

    def moveSpriteIfKeyPressed(self):
        if self.action.getKeyPressed() == 'd':
            self.draw.moveSprite(5, 0)
        elif self.action.getKeyPressed() == 'a':
            self.draw.moveSprite(-5,0)
        self.window.window.after(50, self.moveSpriteIfKeyPressed)



