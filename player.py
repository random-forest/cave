from actor import Actor

class Player(Actor):
  def __init__(self, lps=("top", (0, 0)), w=32, c="grey"):
    Actor.__init__(self, lps, w, c)