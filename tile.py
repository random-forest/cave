class Tile():
  def __init__(self, x, y, walkable=False):
    self.x = x
    self.y = y
    self.walkable = walkable

    self.neighbors = []
    self.g = 0
    self.h = 0
    self.f = 0