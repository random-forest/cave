from config import config
from caveGen import generateCave
from utils import reverseTuple, getRandomPoint
from eventHandler import EventHandler
from player import Player
from enemy import Enemy

class State(EventHandler):
  def __init__(self, scenes=[], actors=[]):
    EventHandler.__init__(self)

    self.scenes = scenes
    self.sceneIndex = 0
    self.currentScene = self.getCurrentScene()

    self.actors = actors
    self.actorIndex = 0
    self.currentActor = self.getCurrentActor()

    self.mouseTarget = False

  def getCurrentScene(self):
    try: return self.scenes[self.sceneIndex]
    except: return False

  def addScene(self, scene):
    self.scenes.append(scene)
    self.currentScene = self.getCurrentScene()

  def getCurrentActor(self):
    try: return self.actors[self.actorIndex]
    except: return False

  def addActor(self, actor):
    self.actors.append(actor)
    self.currentActor = self.getCurrentActor()

  def nextScene(self):
    self.sceneIndex += 1

  def nextActor(self):
    self.actorIndex += 1

state = State()

@state.event("set_mouse_target")
def setMouseTarget(pos):
  state.mouseTarget = reverseTuple(pos, lambda a: int(a))

@state.event("add_actors")
def addActors(actors):
  state.addActor(Player(actors.get('player')))
  map(lambda a: state.addActor(Enemy(a)), actors.get('npc'))


@state.event("add_scene")
def addScenes(scene):
  state.addScene(scene)

state.call("add_scene", generateCave(config.levelSize, 0.4, 6))
state.call("add_actors", config.actors)