from __future__ import print_function

import pyxel
from config import *

from render import Render
from player import Player
from enemy import Enemy
from game import game

game.setPlayer(Player(10, game.currentRoom, (71, 51), 15))
game.addActor(Enemy(7, game.currentRoom, (96, 118), 3))
game.addActor(Enemy(2, game.currentRoom, (64, 142), 3))

def main():
  Render()

if __name__ == "__main__":
  main()