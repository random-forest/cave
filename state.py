import numpy as np
import random, pprint, math

from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

from pprint import pprint as p

from cave import gen_cave
from tile import Tile
from scene import Scene
from actor import Actor

def scale_pairs(a, b, size):
  return (a * size, b * size)

def rand(size):
  return math.floor(random.uniform(0, size))
                
class State():
  def __init__(self, scene_size=(100, 100)):
    self.index = 0
    self.mouse_target = None
    self.scenes = self.build_scenes(scene_size)
    
    self.current_scene = self.scenes[self.index]

  def split(self, array, nrows, ncols):
    r, h = array.shape
    return (array.reshape(h//nrows, nrows, -1, ncols).swapaxes(1, 2).reshape(-1, nrows, ncols))

  def normalize(self, matrix):
    x=y=0
    arr = []

    for row in matrix:
      arr.insert(y, [])
      for col in row:
        if col == 1:
          node = Tile(x, y, True, col)
          arr[y].insert(x, node)

        if col == 0:
          node = Tile(x, y, False, col)
          arr[y].insert(x, node)

        x += 1
      y += 1
      x = 0
    
    # for row in arr:
    #   for col in row:
    #     self.get_neighbors(col, arr)

    self.current_scene.actors[0][1][0].set_grid(self.current_scene.data)
    return arr

  def next(self, pos):
    scenes = self.scenes
    x, y = pos

    # print(scenes[y])
    if self.index < len(self.current_scene.data) - 1:
      self.current_scene = self.scenes[self.index]
      self.index += 1
    else:
      self.index = 0
      self.current_scene = self.scenes[self.index]

  def build_scenes(self, scene_size=(100, 100), fcoef=0.4, iterations=7):
    x=y=0
    arr=[]
    scenes = self.split(gen_cave(scene_size, fcoef, iterations), 20, 25)
    for scene in scenes:
      top = list()
      bottom = list()
      right = list()
      left = list()
      rand_points = list()


      for row in scene:
        for col in row:
          top.append((scene[0][x], (x, 0)))
          bottom.append((scene[len(scene) - 1][x], (x, len(scene) - 1)))
          right.append((scene[y][len(scene[0]) - 1], (len(scene[0]) - 1, y)))
          left.append((scene[y][0], (0, y)))
          if col == 1:
            pos = (x, y)
            rand_points.append(pos)

          x+=1
        y+=1
        x=0
      y=0

      rand_pos = rand_points[rand(len(rand_points))]
      sides = dict(top=top,left=left,bottom=bottom,right=right)
      
      actors = [("players", [Actor(rand_pos[0], rand_pos[1])]), ("npc", [])]
      next = Scene(sides, actors, scene)
      arr.append(next)

    return arr

  def set_mouse_target(self, target):
    self.mouse_target = target
    self.current_scene.actors[0][1][0].get_mousepos(self.mouse_target)
    
  def get_neighbors(self, t, arr):
    neighbors = []
    
    for x, y in [(t.x,t.y + 1),(t.x,t.y-1),(t.x + 1,t.y),(t.x-1,t.y),(t.x+1,t.y+1),(t.x+1,t.y-1),(t.x-1,t.y+1),(t.x-1,t.y-1)]:
      if x >= len(arr[0]): continue
      elif y >= len(arr): continue
      elif x < 0: x = 0
      elif y < 0: y = 0
      else:
        tt = arr[y][x]
        neighbors.append(tt)

    t.set_neighbors(neighbors)

  def update(self):
    sides = self.current_scene.sides
    top = sides['top']
    left = sides['left']
    bottom = sides['bottom']
    right = sides['right']

    x = self.current_scene.actors[0][1][0].x
    y = self.current_scene.actors[0][1][0].y

    tf = filter(lambda a: a[1] == (x, y), top)
    bf = filter(lambda a: a[1] == (x, y), bottom)
    lf = filter(lambda a: a[1] == (x, y), left)
    rf = filter(lambda a: a[1] == (x, y), right)

    if len(list(bf)) > 0:
      self.next((x, y))
      self.mouse_target = None
    if len(list(tf)) > 0:
      self.next((x, y))
      self.mouse_target = None
    if len(list(lf)) > 0:
      self.next((x, y))
      self.mouse_target = None
    if len(list(rf)) > 0:
      self.next((x, y))
      self.mouse_target = None
    

      