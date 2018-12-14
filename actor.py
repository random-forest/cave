from config import config

from tile import Tile
from utils import getRandomPoint 

from state import state

class Actor(Tile):
  def __init__(self, props, x=0, y=0, random_pos=True):
    Tile.__init__(self, x, y, props.get('color'))

    self.merge(props)
    if random_pos == True: self.setRandomPosition()
  
  def setPath(self):
    print(vars(self))

  def setRandomPosition(self):
    arr = []
    x = y = 0
    for row in state.currentScene:
      for col in row:
        if col == 1: arr.append((y, x))
        if col == 0: pass
        x += 1
      y += 1
      x = 0
    y = 0

    pos = getRandomPoint(arr)
    x, y = pos

    self.setPos((y, x))

  def merge(self, data):
    for key in data:
      try: self.__setattr__(key, data.get(key))
      except: continue
