from actor import Actor
from config import START, TILE_SIZE
from utils import nestedFilter, getNeighbors
from pygame import image

class Player(Actor):
  def __init__(self, color, view, spritePos, steps):
    position = getNeighbors(view, nestedFilter(view, START))[0]
    x, y = position

    Actor.__init__(self, x, y, color, view, spritePos, steps)
    self.type = "P"
    self.hp = 10
    self.attack = 0.1

  def update(self):
    self.updatePath()