import pygame, pprint, math
from pprint import pprint as p

WIN_WIDTH  = 800
WIN_HEIGHT = 640

TILE_SIZE = 32

DISPLAY_SIZE = (WIN_WIDTH, WIN_HEIGHT)
BG_COLOR = "#000000"

def scale_pairs(a, b, size):
  return (a * size, b * size)

class Render():
  def __init__(self, title, state):
    self.state = state
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

  def draw_scene(self):
    scene = self.state.current_scene.data

    for row in scene:
      for node in row:
        pos = scale_pairs(node.x, node.y, self.tile_size)
          
        if node.walkable == False:
          self.draw_rect("red", pos)
        if node.walkable == True:
          self.draw_rect("black", pos)

    mt = self.state.mouse_target

    if mt != None:
      p = scale_pairs(mt[0], mt[1], self.tile_size)
      self.draw_rect("blue", p)

      tar = scene[mt[1]][mt[0]]

      if tar.neighbors != None:
        for np in tar.neighbors:
          pos = scale_pairs(np.x, np.y, self.tile_size)
          self.draw_rect("grey", pos)



