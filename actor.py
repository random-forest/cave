from config import config

from tile import Tile
from utils import getRandomPoint 
from eventHandler import EventHandler

class Actor(Tile, EventHandler):
  def __init__(self, props, x=0, y=0):
    Tile.__init__(self, x, y, props.get('color'))
    EventHandler.__init__(self)

    self.merge(props)

  def merge(self, data):
    for key in data:
      try: self.__setattr__(key, data.get(key))
      except: continue
