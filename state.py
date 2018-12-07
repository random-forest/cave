import numpy as np

from cave import gen_cave
from tile import Tile

class State():
  def __init__(self, stage_size=(100, 100)):
    self.stages = self.split(gen_cave(stage_size, 0.4, 6), 20, 25)

    self.index = 0
    self.current_stage = self.normalize(self.stages[self.index])

  def split(self, array, nrows, ncols):
    r, h = array.shape

    return (array.reshape(h//nrows, nrows, -1, ncols)
              .swapaxes(1, 2)
              .reshape(-1, nrows, ncols))

  def normalize(self, matrix):
    x=y=0
    arr = []

    for row in matrix:
      arr.insert(y, [])
      for col in row:
        if col == 1:
          arr[y].insert(x, Tile(x, y))
        if col == 0:
          arr[y].insert(x, Tile(x, y, True))

        x += 1
      y += 1
      x = 0
    
    return arr

  def next(self):
    if self.index < len(self.current_stage) - 1:
      self.current_stage = self.normalize(self.stages[self.index])
      self.index += 1
    else:
      self.index = 0
      self.current_stage = self.normalize(self.stages[self.index])

  