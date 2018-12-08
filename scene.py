import math, random

def rand(size):
  return math.floor(random.uniform(0, size))

class Scene():
  def __init__(self, sides, actors, data):
    self.top = sides[0]
    self.left = sides[1]
    self.bottom = sides[2]
    self.right = sides[3]

    self.start = None
    self.end = None

    self.actors = actors
    self.data = data

    self.init()

  def init(self):
    sides = [
      ('top', self.top),
      ('left', self.left),
      ('bottom', self.bottom),
      ('right', self.right)
    ]
