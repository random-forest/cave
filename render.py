import pygame, sys

from config import config
from state import state
from eventHandler import EventHandler
from tile import Tile
from utils import scale_to_pos, getRandomPoint

class Render(EventHandler):
  def __init__(self):
    EventHandler.__init__(self)

    self.init()
    self.screen = pygame.display.set_mode((config.levelSize[1] * config.tileSize, config.levelSize[0] * config.tileSize))
    self.font = pygame.font.SysFont(config.font[0], config.font[1])

    self.loopRunning = True
    self.loop()

  def init(self):
    pygame.font.init()
    pygame.init()

  def update(self):
    pygame.display.flip()

  def drawRect(self, target):
    pygame.draw.rect(self.screen, target.color, target.rect)

  def loop(self):
    while self.loopRunning:
      self.listenKeyboard()
      self.drawScene()
      self.drawActors()
      self.update()

  def listenKeyboard(self):
    for e in pygame.event.get():
      if e.type == pygame.QUIT: sys.exit(0)
      if e.type == pygame.MOUSEBUTTONDOWN:
        if e.button == 1:
          x,y = e.pos
          state.call("set_mouse_target", scale_to_pos(x, y))

  def drawActors(self):
    for actor in state.actors:
      self.drawRect(actor)

  def drawScene(self):
    x = y = 0

    for row in state.currentScene:
      for char in row:
        if char == 1:
          self.drawRect(Tile(x, y, "black", False))
        if char == 0:
          self.drawRect(Tile(x, y, "grey", True))
        x += 1
      y += 1
      x = 0
    # y = 0

