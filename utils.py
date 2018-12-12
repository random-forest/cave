import random
from math import floor
from config import config

def scale_to_pos(x, y):
  return (floor(x / config.tileSize), floor(y / config.tileSize))

def scale_to_draw(x, y):
  return (floor(x * config.tileSize), floor(y * config.tileSize))

def reverseTuple(t, f=None):
  return tuple(map(f, tuple(reversed(t))))

def getRandomPoint(target, min=0):
  if target == None:
    a = int(floor(random.uniform(min, config.levelSize[0])))
    b = int(floor(random.uniform(min, config.levelSize[1])))

    return (a, b)
  else:
    a = int(floor(random.uniform(min, len(target) - 1)))
    b = int(floor(random.uniform(min, len(target[0]) - 1)))

    return (a, b) 
