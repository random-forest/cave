from actor import Actor

class Enemy(Actor):
  def __init__(self, props, x=1, y=1):
    Actor.__init__(self, props, x, y)