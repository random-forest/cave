from actor import Actor

class Player(Actor):
  def __init__(self, stats, lps=("top", (0, 0)), w=32, c="grey"):
    Actor.__init__(self, lps, w, c)
    self.hp = stats['hp']
    self.lvl = stats['lvl']

  def set_hp(self, val):
    self.hp = val