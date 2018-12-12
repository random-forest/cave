from pygame import Rect, Color
from config import config

class Tile():
  def __init__(self, x, y, color="white", walkable=True):
    self.x = x
    self.y = y
    self.color = Color(color)
    self.walkable = walkable

    self.rect = Rect(self.x*config.tileSize, self.y*config.tileSize, config.tileSize, config.tileSize)

  def setPos(self, pos):
    self.x = pos[0]
    self.y = pos[1]
    self.rect.left = self.x*config.tileSize
    self.rect.top = self.y*config.tileSize