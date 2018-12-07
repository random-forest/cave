import pygame

WIN_WIDTH  = 800
WIN_HEIGHT = 640

TILE_SIZE = 32

DISPLAY_SIZE = (WIN_WIDTH, WIN_HEIGHT)
BG_COLOR = "#000000"

class Render():
  def __init__(self, title):
    self.screen = pygame.display.set_mode(DISPLAY_SIZE)
    self.bg = pygame.Surface(DISPLAY_SIZE)

    self.tile_size = TILE_SIZE

    self.init(title)

  def init(self, title):
    pygame.init()
    pygame.display.set_caption(title)

    self.bg.fill(pygame.Color(BG_COLOR))

  def update(self):
    pygame.display.update()

  def loop(self, targets):
    while 1:
      self.screen.blit(self.bg, (0, 0))
      for fn in targets:
        fn()
      self.update()

  def draw_rect(self, color, pos):
    rect = pygame.Surface((TILE_SIZE, TILE_SIZE))
    rect.fill(pygame.Color(color))

    self.screen.blit(rect, pos)