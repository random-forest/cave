import numpy as np
import pygame

from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

class Actor(pygame.sprite.Sprite):
  def __init__(self, lps=("top", (0, 0)), w=32, c="grey"):
    pygame.sprite.Sprite.__init__(self)

    self.x = lps[1][0]
    self.y = lps[1][1]
    self.width = w
    self.color = c
    
    self.grid = None
    self.mouse_pos = None
    self.start = None
    self.end = None

    self.image = pygame.Surface((w,w))
    self.image.fill(pygame.Color(c))
    
    self.rect = pygame.Rect(self.x, self.y, w, w)

    self.index = 0
    self.path = []

    self.active_zone = []

    self.last_pos = lps

  def set_grid(self, grid):
    self.grid = Grid(matrix=np.array(grid))
    self.start = self.grid.node(self.x, self.y)
    

  def get_mousepos(self, pos):
    self.mouse_pos = pos
    self.end = self.grid.node(self.mouse_pos[0], self.mouse_pos[1])

  def set_pos(self, x, y):
    self.x = x
    self.y = y
    self.rect.x = x
    self.rect.y = y

  def set_lastpos(self, data):
    self.last_pos = data

  def set_path(self):
    finder = AStarFinder(diagonal_movement=DiagonalMovement.always)
    path, run = finder.find_path(self.start, self.end, self.grid)

    self.path = path

  def get_active_zone(self, arr):
    max = 4
    sides = [(self.x,self.y + max),(self.x,self.y-max),(self.x + max,self.y),(self.x-max,self.y),(self.x+max,self.y+max),(self.x+max,self.y-max),(self.x-max,self.y+max),(self.x-max,self.y-max)]
    res = []

    for side in sides:
      res.append(side)

    self.active_zone = res

  def update(self):
    index = self.index
    path = self.path

    if index < len(path):
      step = path[index]
      rev = (step[0], step[1])

      if self.x > rev[0]:
        self.x -= 1
        self.rect.x = self.x
      if self.x < rev[0]:
        self.x += 1
        self.rect.x = self.x

      if self.y > rev[1]:
        self.y -= 1
        self.rect.y = self.y
      if self.y < rev[1]:
        self.y += 1
        self.rect.y = self.y

      if self.x == rev[0] and self.y == rev[1]:
        self.index += 1

    else:
      if len(path) > 0:
        self.path = []
        self.index = 0