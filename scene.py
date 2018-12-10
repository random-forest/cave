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

    self.init()

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

  def init(self):
    pass
    # ndata = self.ndata
    # narr = self.enter_points

    # r1 = rand(len(ndata))
    # r2 = rand(len(ndata[0]))

    # if ndata[r1][r2].walkable == False:
    #   narr.append(ndata[r1][r2])

    #   r1 = rand(len(ndata))
    #   r2 = rand(len(ndata[0]))
    #   narr.append(ndata[r1][r2])
    # else:
    #   pass
    # else:
    #   return False

      

      
    # arr = []
    # data = self.data
    # y = 0
    # x = 0

    # for line in data:
    #   for node in line:
    #     if node == 1: continue
    #     if node == 0: arr.append((x, y))

    #     x += 1
    #   y += 1
    #   x = 0

    # t = list(filter(lambda x: x[1] == 0, arr))
    # b = list(filter(lambda x: x[1] == len(data) - 1, arr))
    # l = list(filter(lambda x: x[0] == 0 and x[1] < len(data) - 1, arr))
    # r = list(filter(lambda x: x[0] == (len(data[0]) - 1) and x[1] < len(data) - 1, arr))

    # t_pos = rand(len(t) - 1)

    # if t_pos >= len(t): t_pos -= 1
    # else:
    #   try:
    #     self.enter = t[t_pos]
    #     # e_tar = self.data[self.enter[0]][self.enter[1]]

    #     # if e_tar == 0: self.enter = t[t_pos]
    #     # else: self.enter = t[t_pos]

    #     b_pos = rand(len(b) - 1)
    #     if b_pos >= len(b): b_pos -= 1
    #     else:
    #       try:
    #         self.exit = b[b_pos]
    #       except:
    #         pass
    #   except:
    #     pass
    # # self.enter = l[1]
    # # self.exit = b[rand(19)]



