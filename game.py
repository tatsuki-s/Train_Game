import pyxel


SCREEN_WIDTH = 250
SCREEN_HEIGHT = 160

class App:
  def __init__(self):
    self.TRAIN_X = SCREEN_WIDTH / 2
    pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT)
    pyxel.load("my_resource.pyxres")
    pyxel.run(self.update, self.draw)

  def update(self):
    if pyxel.btn(pyxel.KEY_Q):
      pyxel.quit()
    if pyxel.btn(pyxel.KEY_RIGHT):
      self.TRAIN_X = self.TRAIN_X + 1
    if pyxel.btn(pyxel.KEY_LEFT):
      self.TRAIN_X = self.TRAIN_X - 1

  def draw(self):
    pyxel.cls(6)
    pyxel.blt(SCREEN_WIDTH - 216, SCREEN_HEIGHT / 2, 0, 8, 0, 216, 16, 0, None, 1)
#    pyxel.text(SCREEN_WIDTH - 216, SCREEN_HEIGHT / 2, "Hello,pyxel", 7)

App()
