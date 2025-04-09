import pyxel
import math

SCREEN_WIDTH = 220
SCREEN_HEIGHT = 172

SCRENN_LIST = ["modeSelect", "playng", "gameOver"]

class App:
  def __init__(self):
#    self.TRAIN_X = SCREEN_WIDTH / 2
    self.TRAIN_POWER = 0
    self.TRAIN_SPEED = 0
    self.MAX_SPEED = 120
    self.DISTANCE = 0
    self.NEXT_STATION = 0
#    self.SCREEN_VIEW = SCREEN_LIST(0)
    pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT)
    pyxel.load("my_resource.pyxres")
    pyxel.run(self.update, self.draw)

  def update(self):
    if pyxel.btn(pyxel.KEY_Q):
      pyxel.quit()
    #ハンドル操作
    if pyxel.btn(pyxel.KEY_UP) and self.TRAIN_POWER < 5:
      self.TRAIN_POWER = self.TRAIN_POWER + 1
    if pyxel.btn(pyxel.KEY_DOWN) and self.TRAIN_POWER > -5:
      self.TRAIN_POWER = self.TRAIN_POWER - 1
    if  pyxel.btn(pyxel.KEY_E):
      self.TRAIN_POWER = 0
    if self.TRAIN_POWER <= 5 and self.TRAIN_POWER > 0 and self.TRAIN_SPEED < self.MAX_SPEED:
      self.TRAIN_SPEED = self.TRAIN_SPEED + ((self.TRAIN_POWER / 13) ** 2)
    if self.TRAIN_POWER <= 0 and self.TRAIN_SPEED > 0:
      self.TRAIN_SPEED = self.TRAIN_SPEED - ((self.TRAIN_POWER * -1 / 12) ** 2) - 0.007
    if self.TRAIN_SPEED < 0:
      self.TRAIN_SPEED = 0

  def draw(self):
    pyxel.cls(6)
    #背景
    pyxel.blt(SCREEN_WIDTH - 200, SCREEN_HEIGHT / 2, 0, 0, 16, 15, 31, 0, None, 1.5)
    #車両本体
    pyxel.blt(SCREEN_WIDTH - 192, SCREEN_HEIGHT / 2, 0, 8, 0, 216, 16, 0, None, 1)
    pyxel.rect(0, SCREEN_HEIGHT / 2 + 16, SCREEN_WIDTH, SCREEN_HEIGHT + 16, 0)
    #ノッチの処理
    POWER_TEXT = str(self.TRAIN_POWER)
    if self.TRAIN_POWER > 0 and self.TRAIN_POWER <= 5:
      POWER_TEXT = "P" + str(self.TRAIN_POWER)
    if self.TRAIN_POWER == 0:
      POWER_TEXT = " " + str(self.TRAIN_POWER)
    if self.TRAIN_POWER < 0 and self.TRAIN_POWER >= -4:
      POWER_TEXT = "B" + str(self.TRAIN_POWER * -1)
    if self.TRAIN_POWER == -5:
      POWER_TEXT = "EB"
    pyxel.text(4, SCREEN_HEIGHT / 2 + 20, POWER_TEXT, 7)
    # スピード周りの処理
    SPEED_TEXT = str(math.floor(self.TRAIN_SPEED))
    if (self.TRAIN_SPEED == 0):
      SPEED_TEXT = "000"
    elif (self.TRAIN_SPEED < 10):
      SPEED_TEXT = "00" + SPEED_TEXT
    elif (self.TRAIN_SPEED < 100):
      SPEED_TEXT = "0" + SPEED_TEXT
    pyxel.text(SCREEN_WIDTH - 32, SCREEN_HEIGHT /2 +20, str(SPEED_TEXT) + "km/h", 7)

App()
