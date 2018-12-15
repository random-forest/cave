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
    self.screen = pygame.display.set_mode(config.windowSize)
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
      state.currentActor.update()
      self.drawActorPath()
      self.drawActiveZone()
      self.update()

  def listenKeyboard(self):
    for e in pygame.event.get():
      if e.type == pygame.QUIT: sys.exit(0)
      if e.type == pygame.KEYDOWN:
        if e.key == 32:
          state.nextActor()

      if e.type == pygame.MOUSEBUTTONDOWN:
        if e.button == 1:
          x,y = e.pos

          if state.currentActor != False:
            if state.currentActor.type == 'player':
              state.currentActor.setTarget(scale_to_pos(y, x))
              state.currentActor.setPath()

  def drawActors(self):
    for actor in state.actors:
      self.drawRect(actor)

  def drawActiveZone(self):
    target = state.currentActor

    for node in target.activeZone:
      self.drawRect(Tile(node[1], node[0], "green"))

  def drawActorPath(self):
    path = state.currentActor.path

    if len(path) > 0:
      for p in path:
        self.drawRect(Tile(p[0], p[1], "orange"))

  def drawScene(self):
    x = y = 0

    for row in state.currentScene:
      for char in row:
        if char == 1:
          self.drawRect(Tile(x, y, "grey", True))
        if char == 0:
          self.drawRect(Tile(x, y, "black", False))
        x += 1
      y += 1
      x = 0

