import math, random

from tile import Tile

def rand(size):
  return math.floor(random.uniform(0, size))

class Scene():
  def __init__(self, sides, actors, data):
    self.sides = sides
    self.enter = None
    self.exit = None

    self.actors = actors
    self.data = data
    self.enter_points = list()
    self.ndata = self.normalized()

  def normalized(self):
    x=y=0
    matrix = self.data
    arr = []

    for row in matrix:
      arr.insert(y, [])
      for col in row:
        if col == 1:
          node = Tile(x, y, True, 1)
          arr[y].insert(x, node)

        if col == 0:
          node = Tile(x, y, False, 0)
          arr[y].insert(x, node)

        x += 1
      y += 1
      x = 0
    
    return arr

  def init(self, lp):
    player = self.actors['players'][0]
    player.set_lastpos(lp)

    last_pos = player.last_pos

    l_side = last_pos[0]
    # l_coords = last_pos[1]

    if l_side is 'bottom':
      print('bottom')
    if l_side is 'top':
      print('top')
    if l_side is 'left':
      print('left')
    if l_side is 'right':
      print('right')



