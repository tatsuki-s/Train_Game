import pyxel


SCREEN_WIDTH = 250
SCREEN_HEIGHT = 160

class App:
  def __init__(self):
    self.TRAIN_X = SCREEN_WIDTH / 2
    self.TRAIN_SPEED = 0
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
    if pyxel.btn(pyxel.KEY_UP):
      self.TRAIN_SPEED = self.TRAIN_SPEED + 1

  def draw(self):
    pyxel.cls(6)
    pyxel.blt(SCREEN_WIDTH - 216, SCREEN_HEIGHT / 2, 0, 8, 0, 216, 16, 0, None, 1)
    pyxel.rect(0, SCREEN_HEIGHT / 2 + 16, SCREEN_WIDTH, SCREEN_HEIGHT + 16, 0)
    # スピード周りの処理
    SPEED_TEXT = str(self.TRAIN_SPEED)
    if (self.TRAIN_SPEED == 0):
      SPEED_TEXT = "000"
    elif (self.TRAIN_SPEED < 10):
      SPEED_TEXT = "00" + SPEED_TEXT
    elif (self.TRAIN_SPEED < 100):
      SPEED_TEXT = "0" + SPEED_TEXT
    pyxel.text(4, SCREEN_HEIGHT /2 +20, str(SPEED_TEXT) + "km/h", 7)
#    pyxel.text(SCREEN_WIDTH - 216, SCREEN_HEIGHT / 2, "Hello,pyxel", 7)

App()
