from vec2d import Vec2

class Tile:
  def __init__(self, x, y, type, color):
    self.type = type
    self.pos = Vec2(x, y)
    self.color = color

  def update(self):
    pass