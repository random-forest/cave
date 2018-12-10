import numpy as np
import pygame, sys, math

from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

class Events():
  def __init__(self, state):
    self.state = state

  def catch(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        sys.exit(0)
      if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
          x, y = event.pos
          pos = (math.floor(x/32), math.floor(y/32))

          self.state.set_mouse_target(pos)
          
          player = self.state.current_scene.actors[0][1][0]
          player.set_path()
          