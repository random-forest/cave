import pygame, sys, math

class Events():
  def __init__(self, state):
    self.last = None
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


  def set(self, event):
    self.last = event