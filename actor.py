import math
import numpy as np

from config import config
from tile import Tile
from utils import getRandomPoint, reverseTuple
from state import state

from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

def getZoneBorders(arr):
  y = []
  x = []

  for node in arr:
    y.append(node[1])
    x.append(node[0])

  if len(y) > 0 and len(x) > 0:
    miny = min(y)
    maxy = max(y)
    minx = min(x)
    maxx = max(x)

    return dict(
      min={'x': minx, 'y': miny},
      max={'x': maxx, 'y': maxy}
    )

class Actor(Tile):
  def __init__(self, props, x=0, y=0, random_pos=True):
    Tile.__init__(self, x, y, props.get('color'))
    self.type = props.get('type')
    self.name = props.get('name')
    self.steps = props.get('steps')
    self.minSteps = props.get('steps')
    self.fieldSize = props.get('field')

    self.path = []
    self.pathIndex = 0

    self.target = None
    self.move = False
    self.activeZone = self.setActiveZone()
    self.merge(props)
    if random_pos == True: self.setRandomPosition()

  def setTarget(self, pos):
    position = reverseTuple(pos, lambda a: int(a))
    x, y = position
    try:
      target = state.currentScene[y][x]
      self.target = (y, x)
    except: pass
  
  def setPath(self):
    pos = (self.target[1], self.target[0])
    grid = Grid(matrix=state.currentScene)
    start = grid.node(int(self.x), int(self.y))
    end = grid.node(pos[0], pos[1])

    finder = AStarFinder(diagonal_movement=DiagonalMovement.always)
    path, run = finder.find_path(start, end, grid)

    self.path = path

  def update(self):
    borders = getZoneBorders(self.setActiveZone())
    targets = list(filter(lambda a: a.type != self.type, state.actors))
    
    print(borders)
    # for target in targets:
    #   isInZone = list(filter(lambda a: a[0] == target.y and a[1] == target.x, self.setActiveZone()))
    #   if len(isInZone) > 0:
    #     if state.currentActor.type == 'npc' and state.currentActor.steps != 0:
    #       state.currentActor.setTarget((target.y, target.x))
    #       state.currentActor.setPath()
    #       self.move = True

    if self.steps == 0:
      print("{0} {1} is end his turn!".format(self.type, self.name))
      state.nextActor()

    if state.currentActor.type == 'npc' and state.currentActor.steps != 0 and self.move == False:
      state.currentActor.setTarget(state.currentActor.getRandomPos())
      state.currentActor.setPath()
      self.move = True

    if len(self.path) > 0 and self.steps > 0:
      if self.pathIndex == len(self.path) - 1:
        self.pathIndex = 0
        self.path = []
        self.move = False
      
      try:
        step = self.path[self.pathIndex]
        x, y = step

        self.setPos(step)

        if self.x == x and self.y == y:
          self.pathIndex += 1
          self.steps -= 1
      except: pass
    else:
      self.pathIndex = 0
      self.path = []
      self.move = False

  def reload(self):
    self.steps = self.minSteps
    self.pathIndex = 0
    self.path = []

  def setActiveZone(self):
    arr = []
    scene = state.currentScene
    max = self.fieldSize
    sides = [
      (self.x, (self.y + max) % len(scene)),
      (self.x, (self.y - max) % len(scene)),
      ((self.x + max) % len(scene[0]), self.y),
      ((self.x - max) % len(scene[0]), self.y),
      ((self.x + max) % len(scene[0]), (self.y + max) % len(scene)),
      ((self.x + max) % len(scene[0]), (self.y - max) % len(scene)),
      ((self.x - max) % len(scene[0]), (self.y + max) % len(scene)),
      ((self.x - max) % len(scene[0]), (self.y - max) % len(scene))
    ]

    # for y in range(self.y, sides[0][1]):
    #   arr.append((y, self.x))

    # for y in range(self.y, sides[1][1]):
    #   arr.append((y, self.x))

    
    for side in sides:
      arr.append(reverseTuple(side))

    self.activeZone = arr
    # self.activeZone = map(lambda a: (np.abs(a[0]), np.abs(a[1])), res)
    return self.activeZone

  def getRandomPos(self):
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

    return getRandomPoint(arr)  

  def setRandomPosition(self):
    pos = self.getRandomPos()
    x, y = pos

    self.setPos((y, x))

  def merge(self, data):
    for key in data:
      try: self.__setattr__(key, data.get(key))
      except: pass
