import time

from actor import Actor
from event_handler import EventHandler
from utils import scale_pairs, rand

ev = EventHandler()

class Enemy(Actor):
  def __init__(self, state, lps=("top", (0, 0)), w=32, c="yellow"):
    Actor.__init__(self, lps, w, c)
    self.global_state = state

  def _update(self):
    scene = self.global_state.current_scene
    player = scene.actors['players'][0]

    ff = filter(lambda a: a == (player.x, player.y), self.active_zone)

    def get_rand_pos(scene):
      x=y=0
      ff = []

      for row in scene.data:
        for col in row:
          if col == 1:
            ff.append((col, (x, y)))
          x+=1
        y+=1
        x=0

      return ff[rand(len(ff))][1]

    # if len(self.path) > 0:
    #   last = self.path[len(self.path) - 1]

    #   if self.x == last[0] and self.y == last[1]:

        
    if len(self.path) == 0:      
      if len(list(ff)) > 0:
        print('attack!')
        for p in list(ff):
          self.get_mousepos((p[1], p[0]))
        self.set_path()
      else:
        rp = get_rand_pos(scene)
        print('idle!')
        self.get_mousepos(rp)

        self.set_path()

