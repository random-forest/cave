import pygame, pprint, math
from utils import scale_pairs

WIN_WIDTH  = 800
WIN_HEIGHT = 640

TILE_SIZE = 32

DISPLAY_SIZE = (WIN_WIDTH, WIN_HEIGHT)
BG_COLOR = "#000000"

class Render():
  def __init__(self, title, state):
    pygame.font.init()

    self.state = state
    self.screen = pygame.display.set_mode(DISPLAY_SIZE)
    self.bg = pygame.Surface(DISPLAY_SIZE)
    self.font = pygame.font.SysFont('Arial', 18)
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

  def draw_text(self, content, pos):
    text = self.font.render(str(content), False, (250, 250, 250))
    p = (pos[0] + ((self.tile_size/2) - 9), pos[1] + ((self.tile_size/2) - 5))
    self.screen.blit(text, p)

  def draw_scene_sides(self):
    sides = self.state.current_scene.sides

    for node in sides['top']:
      char, p = node
      pos = scale_pairs(p[0], p[1], self.tile_size)
      self.draw_rect("orange", pos)
      self.draw_text("T", pos)

    for node in sides['left']:
      char, p = node
      pos = scale_pairs(p[0], p[1], self.tile_size)
      self.draw_rect("orange", pos)
      self.draw_text("L", pos)

    for node in sides['right']:
      char, p = node
      pos = scale_pairs(p[0], p[1], self.tile_size)
      self.draw_rect("orange", pos)
      self.draw_text("R", pos)

    for node in sides['bottom']:
      char, p = node
      pos = scale_pairs(p[0], p[1], self.tile_size)
      self.draw_rect("orange", pos)
      self.draw_text("B", pos)

  def draw_scene(self):
    scene = self.state.normalize(self.state.current_scene.data)

    for row in scene:
      for node in row:
        pos = scale_pairs(node.x, node.y, self.tile_size)
          
        if node.walkable == False:
          self.draw_rect("red", pos)
          self.draw_text(node.char, pos)
        if node.walkable == True:
          self.draw_rect("black", pos)
          self.draw_text(node.char, pos)

    mt = self.state.mouse_target

    if mt != None:
      p = scale_pairs(mt[0], mt[1], self.tile_size)
      self.draw_rect("blue", p)

    player = self.state.current_scene.actors['players'][0]
    player_pos = scale_pairs(player.x, player.y, player.width)
      
    player.update()
    self.draw_rect(player.color, player_pos)

    # if len(player.active_zone) > 0:
    #   for node in player.active_zone:
    #     node_pos = scale_pairs(node[0], node[1], player.width)
    #     self.draw_rect("purple", node_pos)

    npc = self.state.current_scene.actors['npc'][0]
    npc_pos = scale_pairs(npc.x, npc.y, npc.width)
      
    npc.update()
    npc._update()
    self.draw_rect(npc.color, npc_pos)

    self.draw_scene_sides()
    self.state.update()



