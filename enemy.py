import random, time, math

from config import *
from game import game
from actor import Actor
from utils import getRandomPosition

class Enemy(Actor):
  def __init__(self, color, view, spritePos, steps):
    self.setPosition(getRandomPosition(view))
    Actor.__init__(self, self.x, self.y, color, view, spritePos, steps)

    self.type = "A"
    self.hp = 5
    self.attack = 0.01

  def update(self):
    if self.steps > 0:
      self.setTarget(getRandomPosition(self.view))
      self.setPath()
      self.updatePath()

      # selfPos = (self.x, self.y)
      # playerPos = (game.player.x, game.player.y)

      # if playerPos in self.neighbors:
      #   if playerPos[0] < self.x:
      #     playerPos = (playerPos[0] + 1, playerPos[1])
      #   else:
      #     playerPos = (playerPos[0] - 1, playerPos[1])

      #   if playerPos[1] < self.y:
      #     playerPos = (playerPos[0], playerPos[1] - 1)
      #   else:
      #     playerPos = (playerPos[0], playerPos[1] + 1)

      #   self.isMoving = False
      #   self.setTarget(playerPos)
      #   self.setPath()

        # if self.x == playerPos[0] and self.y == playerPos[1]:
        #   # self.isMoving = True
        #   print('attack')
        #   self._attack()
        # else:
        #   self.isMoving = True
        #   self.updatePath()

    else:
      self.cleanPath()
      game.nextTurn()

