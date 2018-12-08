import numpy as np
import random, pprint, math

from pprint import pprint as p
from heapq import *

from cave import gen_cave
from tile import Tile
from scene import Scene

def scale_pairs(a, b, size):
  return (a * size, b * size)

def heuristic(a, b):
    return (b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2

def astar(array, start, goal):
  neighbors = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]
  
  close_set = set()
  came_from = {}
  gscore = {start:0}
  fscore = {start:heuristic(start, goal)}
  oheap = []

  heappush(oheap, (fscore[start], start))
  
  while oheap:
    current = heappop(oheap)[1]
    if current == goal:
      data = []

      while current in came_from:
        data.append(current)
        current = came_from[current]
      
      return data[::-1]

    close_set.add(current)

    for i, j in neighbors:
      neighbor = current[0] + i, current[1] + j            
      tentative_g_score = gscore[current] + heuristic(current, neighbor)

      if 0 <= neighbor[0] < array.shape[0]:
        if 0 <= neighbor[1] < array.shape[1]:                
          if array[neighbor[0]][neighbor[1]] == 1:
            continue
        else:
          continue
      else:
        continue
                
      if neighbor in close_set and tentative_g_score >= gscore.get(neighbor, 0):
        continue
            
      if  tentative_g_score < gscore.get(neighbor, 0) or neighbor not in [i[1]for i in oheap]:
        came_from[neighbor] = current
        gscore[neighbor] = tentative_g_score
        fscore[neighbor] = tentative_g_score + heuristic(neighbor, goal)
        heappush(oheap, (fscore[neighbor], neighbor))
                
  return []

class State():
  def __init__(self, scene_size=(100, 100)):
    self.scenes = self.build_scenes(scene_size)

    self.index = 0
    self.current_scene = self.scenes[self.index]

    self.mouse_target = None

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
          node = Tile(x, y)
          arr[y].insert(x, node)

        if col == 0:
          node = Tile(x, y, True)
          arr[y].insert(x, node)

        x += 1
      y += 1
      x = 0
    
    for row in arr:
      for col in row:
        self.get_neighbors(col, arr)

    return arr

  def next(self):
    if self.index < len(self.current_scene) - 1:
      self.current_scene = self.normalize(self.scenes[self.index])
      self.index += 1
    else:
      self.index = 0
      self.current_scene = self.normalize(self.scenes[self.index])

  def build_scenes(self, scene_size=(100, 100), fcoef=0.4, iterations=6):
    arr = []
    scenes = self.split(gen_cave(scene_size, fcoef, iterations), 20, 25)

    for scene in scenes:
      y = 0
      x = 0
      i = 0

      if y < len(scene):
        t = []
        b = []
        l = []
        r = []
        
        if y is len(scene): y = 0
        
        if x < len(scene[y]):
          if x is len(scene[y]): x = 0

          if i < len(scene[0]):
            t.append((i, 0))
            b.append((i, len(scene) - 1))
            l.append((0, i))
            r.append((len(scene[0]) - 1, i))

            next = Scene([t, l, b, r], [("players", []), ("npc", [])], self.normalize(scene))
            arr.append(next)

            i += 1
          x += 1
        y += 1

    return arr

  def set_mouse_target(self, target):
    self.mouse_target = target
    
    t = self.current_scene.data[self.mouse_target[1]][self.mouse_target[0]]
    # path = astar(np.array(self.current_scene.data), (1, 7), (t.x, t.y))
    # print(path)

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

