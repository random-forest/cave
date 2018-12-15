from actor import  Actor

class Player(Actor):
  def __init__(self, props, x=0, y=0):
    Actor.__init__(self, props, x, y)