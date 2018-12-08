class Tile():
  def __init__(self, x, y, walkable=False):
    self.x = x
    self.y = y
    self.walkable = walkable

    self.neighbors = None

  def set_neighbors(self, value):
    self.neighbors = value