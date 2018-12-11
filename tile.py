class Tile():
  def __init__(self, x, y, walkable=False, char=1):
    self.x = x
    self.y = y
    self.walkable = walkable
    self.char = char

  def get_position(self, arr):
    x = self.x
    y = self.y

    if x >= len(arr[0]): x -= 1
    elif y >= len(arr): y -= 1
    elif x < 0: x = 0
    elif y < 0: y = 0
    else:
      return (arr[y][x].x, arr[y][x].y)