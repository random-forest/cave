import time, timeout_decorator, math, asyncio, numpy as np
from timeout_decorator import timeout

from actor import Actor
from event_handler import EventHandler
from utils import scale_pairs, rand

ev = EventHandler()

def get_minmax_borders(arr):
  y = []
  x = []

  for node in arr:
    y.append(node[1])
    x.append(node[0])

  if len(y) > 0 and len(x) > 0:
    miny = min(y)
    maxy = max(y)
    minx = min(x)
    maxx = max(x)

    return dict(
      min={'x': minx, 'y': miny},
      max={'x': maxx, 'y': maxy}
    )

def get_walkable(arr):
  x = y = 0
  res = []

  for row in arr:
    for col in row:
      if col == 1:
        res.append((x, y))
      x += 1
    y += 1
    x = 0

  return res

def get_rand_pos(data):
  return data

class Enemy(Actor):
  def __init__(self, stats, state, lps=("top", (0, 0)), w=32, c="yellow"):
    Actor.__init__(self, lps, w, c)
    self.hp = stats['hp']
    self.lvl = stats['lvl']
    self.global_state = state

  @ev.event("attack")
  def attack(self, target):
    player_hp = target.hp
    
    if len(self.path) > 0:
      last = self.path[len(self.path) - 1]

      if self.x == last[0] and self.y == last[1]:
        player_hp -= 0.01
      
        target.set_hp(player_hp)
        print("attack player! player hp -> %d" % target.hp)

  @ev.event("follow")
  def follow(self, pos):
    self.get_mousepos(pos)
    self.set_path()
    if len(self.path) > 0 : self.path.pop()

  @ev.event("idle")
  def idle(self, data):
    res = []
    arr = get_walkable(data[0])
    pos = data[1]

    for node in arr:
      x, y = node

      if y < pos['max']['y'] and x < pos['max']['x'] and x > pos['min']['x']:
        print('idle')
        res.append(node)

    rand_pos = rand(len(res))
    target = res[rand_pos]

    ev.call("follow", self, target)

  def _update(self):
    scene = self.global_state.current_scene
    player = scene.actors['players'][0]

    borders = get_minmax_borders(self.active_zone)

    if borders != None:
      min = borders['min']
      max = borders['max']

      if player.y < max['y'] and player.x < max['x'] and player.x > min['x']:
        ev.call("follow", self, (player.x, player.y))
        ev.call("attack", self, player)
        self.update()
      else:
        ev.call("idle", self, [scene.data, dict(min=min, max=max)])
        self.update()

