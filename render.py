import pygame, pprint, math
from utils import scale_pairs
from config import Config

config = Config()

FPS = config.fps

TILE_SIZE = config.tile_size

DISPLAY_SIZE = config.screen.size
BG_COLOR = config.colors.background

class Render():
  def __init__(self, title, state):
    pygame.font.init()

    self.state = state
    self.screen = pygame.display.set_mode(config.screen.size)
    self.bg = pygame.Surface(config.screen.size)
    self.font = pygame.font.SysFont(config.font.family, config.font.size)
    self.tile_size = config.tile_size
    self.clock = pygame.time.Clock()
    self.init(title)

  def init(self, title):
    pygame.init()
    pygame.display.set_caption(title)

    self.bg.fill(pygame.Color(config.colors.background))

  def update(self):
    pygame.display.update()

  def loop(self, targets):
    while 1:
      self.clock.tick(config.fps)
      self.screen.blit(self.bg, (0, 0))
      for fn in targets:
        fn()
      self.update()

  def draw_rect(self, color, pos):
    rect = pygame.Surface((config.tile_size, config.tile_size))
    rect.fill(pygame.Color(color))

    self.screen.blit(rect, pos)

  def draw_circle(self, color, pos, radius):
    pygame.draw.circle(self.screen, pygame.Color(color), pos, radius, 2)
    # pygame.display.flip()

  def draw_line(self, color, spos, epos):
    pygame.draw.line(self.screen, pygame.Color(color), spos, epos)
    # pygame.display.flip()

  def draw_text(self, color, content, pos):
    text = self.font.render(str(content), False, pygame.Color(color))
    p = (pos[0] + ((config.tile_size/2) - 9), pos[1] + ((config.tile_size/2) - 5))
    self.screen.blit(text, p)

  def draw_scene_sides(self):
    sides = self.state.current_scene.sides

    for node in sides['top']:
      char, p = node
      pos = scale_pairs(p[0], p[1], config.tile_size)
      self.draw_rect("orange", pos)
      self.draw_text("T", pos)

    for node in sides['left']:
      char, p = node
      pos = scale_pairs(p[0], p[1], config.tile_size)
      self.draw_rect("orange", pos)
      self.draw_text("L", pos)

    for node in sides['right']:
      char, p = node
      pos = scale_pairs(p[0], p[1], config.tile_size)
      self.draw_rect("orange", pos)
      self.draw_text("R", pos)

    for node in sides['bottom']:
      char, p = node
      pos = scale_pairs(p[0], p[1], config.tile_size)
      self.draw_rect("orange", pos)
      self.draw_text("B", pos)

  def draw_scene(self):
    scene = self.state.normalize(self.state.current_scene.data)

    for row in scene:
      for node in row:
        pos = scale_pairs(node.x, node.y, config.tile_size)
          
        if node.walkable == False:
          self.draw_rect(config.colors.walls, pos)
          # self.draw_text(node.char, pos)
        if node.walkable == True:
          self.draw_rect(config.colors.ground, pos)
          # self.draw_text(node.char, pos)

    mt = self.state.mouse_target

    # if mt != None:
    #   p = scale_pairs(mt[0], mt[1], config.tile_size)
    #   self.draw_rect("blue", p)

    players = self.state.current_scene.actors['players']

    for player in players:
      player.update()
      player.draw(self.screen)
      self.draw_text("black", '{0}'.format(int(player.hp)), (player.x*config.tile_size, player.y*config.tile_size))
      # self.draw_rect(player.color, player_pos)

    npcs = self.state.current_scene.actors['npc']

    for npc in npcs:
      npc._update()
      npc.draw(self.screen)
      self.draw_text("black", '{0}'.format(int(npc.hp)), (npc.x*config.tile_size, npc.y*config.tile_size))

      for path in npc.path:
        self.draw_circle(npc.color, scale_pairs(math.floor(path[0]), math.floor(path[1]), config.tile_size), 12)

    # if len(npc.active_zone) > 0:
    #   for node in npc.active_zone:
    #     node_pos = scale_pairs(node[0], node[1], npc.width)
    #     self.draw_rect("purple", node_pos)

    # self.draw_scene_sides()
    self.state.update()



