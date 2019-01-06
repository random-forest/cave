import sys 
import math 
import pyxel
import random
from tile import Tile
from game import game

from config import *

class Render:
  def __init__(self):
    pyxel.init(255, 255, caption="((((((((()))")
    pyxel.mouse(True)
    game.setCurrentActor()
    
    self.tiles = []

    for y in range(len(game.currentRoom)):
      for x in range(len(game.currentRoom[0])):
        target = game.currentRoom[y][x]

        if target == FLOOR:
          self.tiles.append(Tile(x*TILE_SIZE, y*TILE_SIZE, 'F', 13))
        if target == WALL:
          self.tiles.append(Tile(x*TILE_SIZE, y*TILE_SIZE, 'W', 8))
        if target == DOOR:
          self.tiles.append(Tile(x*TILE_SIZE, y*TILE_SIZE, 'D', 3))
        if target == START:
          self.tiles.append(Tile(x*TILE_SIZE, y*TILE_SIZE, 'S', 3))
        if target == END:
          self.tiles.append(Tile(x*TILE_SIZE, y*TILE_SIZE, 'E', 3))
        if target == BOX:
          self.tiles.append(Tile(x*TILE_SIZE, y*TILE_SIZE, 'B', 11))

    pyxel.run(self.update, self.draw)

  def update(self):
    if pyxel.btnp(pyxel.KEY_Q):
      pyxel.quit()
      
    if pyxel.btnp(pyxel.KEY_SPACE):
      game.nextActorIndex()
      game.setCurrentActor()

    if pyxel.btnp(pyxel.KEY_TAB):
      game.toggleStatsMenu()

    if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
      pos = tuple(map(lambda a: math.floor(a/TILE_SIZE), (pyxel.mouse_x, pyxel.mouse_y)))
      game.player.setTarget(pos)
      game.player.setPath()

  def draw(self):
    pyxel.cls(0)

    if game.showStatsMenu:
      game.player.update()

      pyxel.text(TEXT_MARGIN, TEXT_MARGIN, 'hp: {0}'.format(game.player.hp), 7)
      pyxel.text(TEXT_MARGIN, TEXT_LINE_HEIGHT + TEXT_MARGIN, 'steps: {0}'.format(game.player.steps), 7)
      
    else:
      for tile in self.tiles:
        pyxel.rect(tile.pos.x, tile.pos.y, tile.pos.x+TILE_SIZE, tile.pos.y+TILE_SIZE, tile.color)
        pyxel.text(tile.pos.x+7, tile.pos.y + 6, tile.type, 1)

      for actor in game.actors:
        pyxel.rect(actor.pos.x, actor.pos.y, actor.pos.x+TILE_SIZE, actor.pos.y+TILE_SIZE, actor.color)
        pyxel.text(actor.pos.x+7, actor.pos.y + 6, actor.type, 1)
        
        # for n in actor.neighbors:
        #   pyxel.rectb(n[0], n[1], n[0]+TILE_SIZE, n[1]+TILE_SIZE, actor.color)

        for p in actor.path:
          pyxel.rectb(p[0], p[1], p[0]+TILE_SIZE, p[1]+TILE_SIZE, actor.color)

        if game.currentActor: 
          game.currentActor.update()