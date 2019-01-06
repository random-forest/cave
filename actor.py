import random, time, math

from pygame import Rect, Surface, Color, sprite, image, transform
from config import TILE_SIZE, FLOOR
from game import game
from tile import Tile

from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

# red (71, 51)
# green (35, 51)
# yellow (64, 142)
# purple (96, 118)

# tree1 (30, 155)
# tree2 (102, 5)
# blood (102,45)

#floor (1,1)

class Actor(Tile, sprite.Sprite):
  def __init__(self, x, y, color, view, spritePos, steps):
    Tile.__init__(self, x*TILE_SIZE, y*TILE_SIZE, "npc", color)
    sprite.Sprite.__init__(self)

    self.x = x
    self.y = y

    self.speed = 2

    self.steps = steps
    self._steps = steps

    self.view = view

    self.target = None

    self.neighbors = []

    self.pathIndex = 0
    self.path = []

    self.isMoving = False
    self.isAlive = True

  def death(self):
    self.isAlive = False

  def _attack(self):
    critCoef = random.uniform(0, 1)
    
    if critCoef > 0.5:
      coef = ((0.5 + self.attack) * critCoef)
      game.player.hp -= coef
      # return False
    else:
      coef = ((0.5 + self.attack) / critCoef)
      game.player.hp -= coef
      # return False

  def setPosition(self, nextPos):
    self.x = nextPos[0]
    self.y = nextPos[1]

  def setTarget(self, value):
    x, y = value

    if self.isMoving == False:
      try:
        self.view[y][x]
        self.target = value
      except IndexError:
        self.target = None

  def setPath(self):
      grid = Grid(matrix=self.view)
      start = grid.node(self.x, self.y)
      end = grid.node(self.target[0], self.target[1])

      finder = AStarFinder(diagonal_movement=DiagonalMovement.only_when_no_obstacle)
      path, runs = finder.find_path(start, end, grid)

      self.path = list(map(lambda a: list(map(lambda b: b*TILE_SIZE, a)), path))
      self.isMoving = True

  def cleanPath(self):
    self.path = []
    self.pathIndex = 0
    self.isMoving = False

  def updatePath(self):
    self.neighbors = self.getNeighbors()

    if self.isMoving == True and self.pathIndex < len(self.path):
      print('{0} is move'.format(self.type))
      step = tuple(map(lambda a: math.floor(a/TILE_SIZE), self.path[self.pathIndex]))

      if step == (self.x, self.y):
        self.pathIndex += 1
        self.steps -= 1
      else:
        self.updateStep(step)
    else:
      self.cleanPath()

  def updateStep(self, step):
    if self.pos.x < step[0]*TILE_SIZE:
      self.pos.x += self.speed

    if self.pos.x > step[0]*TILE_SIZE:
      self.pos.x -= self.speed

    if self.pos.y < step[1]*TILE_SIZE:
      self.pos.y += self.speed

    if self.pos.y > step[1]*TILE_SIZE:
      self.pos.y -= self.speed
          
    self.x = math.floor(self.pos.x/TILE_SIZE)
    self.y = math.floor(self.pos.y/TILE_SIZE)

  def getNeighbors(self):
    return [
      (self.x, (self.y - 1) % len(self.view)), 
      (self.x, (self.y + 1) % len(self.view)),
      ((self.x - 1) % len(self.view[0]), self.y), 
      ((self.x + 1) % len(self.view[0]), self.y),
      ((self.x + 1) % len(self.view[0]), (self.y - 1) % len(self.view)), 
      ((self.x - 1) % len(self.view[0]), (self.y + 1) % len(self.view)),
      ((self.x + 1) % len(self.view[0]), (self.y + 1) % len(self.view)), 
      ((self.x - 1) % len(self.view[0]), (self.y - 1) % len(self.view))
    ]