from config import config
from caveGen import generateCave
from state import state
from render import Render
from player import Player
from enemy import Enemy

state.call("add_scene", generateCave(config.levelSize, 0.4, 7))
state.call("add_actors", [Player(config.actors.get('player')), map(lambda a: Enemy(a), config.actors.get('npc'))])

def main():
  Render()

if __name__ == "__main__":
  main()
