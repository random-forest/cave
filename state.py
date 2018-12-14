from utils import reverseTuple
from eventHandler import EventHandler

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
  position = reverseTuple(pos, lambda a: int(a))
  y, x = position
  try:
    target = state.currentScene[y][x]
    state.mouseTarget = (y, x)
    print(state.mouseTarget)
  except: pass

@state.event("add_actors")
def addActors(actors):
  arr = []
  for actor in actors:
    try:
      if len(actor) >= 0:
        map(lambda a: arr.append(a), actor)
    except:
      arr.append(actor)
  map(lambda a: state.addActor(a), arr)

@state.event("add_scene")
def addScenes(scene):
  state.addScene(scene)