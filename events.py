import pygame, sys

class Events():
  def __init__(self):
    self.last = None

  def catch(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        self.set("QUIT")
        sys.exit(0)

  def set(self, event):
    self.last = event