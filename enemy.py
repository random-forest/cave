from utils import reverseTuple
from actor import  Actor
from state import state

class Enemy(Actor):
  def __init__(self, props, x=0, y=0):
    Actor.__init__(self, props, x, y)

    self.health = props.get('health')
    self.neighborIndex = 1

  def getNeighbors(self):
    curr = self.neighborIndex
    max = self.fieldSize
    arr = []

    while curr < max:
      sides = [
        (self.x, self.y + curr),
        (self.x, self.y - curr),
        (self.x + curr, self.y),
        (self.x - curr, self.y),
        (self.x + curr, self.y + curr),
        (self.x + curr, self.y - curr),
        (self.x - curr, self.y + curr),
        (self.x - curr, self.y - curr)
      ]

      for side in sides:
        pos = reverseTuple(side)

        try:
          if state.currentScene[pos[0]][pos[1]] == 1:
            arr.append(pos)
        except: continue

      curr += 1

    self.neighbors = arr
    return self.neighbors

  def update(self):
    self.updateTurn()
    if self.steps != 0 and self.move == False:
      self.neighbors = self.getNeighbors()
      targets = list(filter(lambda a: a.type != self.type, state.actors))

      for target in targets:
        res = list(filter(lambda a: a == (target.y, target.x), self.neighbors))
        
        if len(res) > 0:
          self.setTarget((target.y, target.x))
          self.setPath()
          self.move = True

          target.health -= 1
          print(target.health)
        else:
          self.setTarget(state.currentActor.getRandomPos())
          self.setPath()
          self.move = True

    self.updatePath()