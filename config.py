class Config():
  def __init__(self):
    self.tileSize = 32
    self.levelSize = (19, 25)
    self.font = ("Arial", 21)
    self.actors = {
      'player': {
        'name': 'nikto',
        'race': 'goblin',
        'clas': 'rogue',
        'color': 'red',
        'health': 100,
        'field': 8,
        'steps': 15,
        'exp': 0
      },

      'npc': [
        {
          'name': 'ahgrakhnak',
          'race': 'goblin',
          'clas': 'warrior',
          'color': 'blue',
          'health': 10,
          'field': 4,
          'steps': 10,
          'exp': 11
        }
      ]
    }

config = Config()