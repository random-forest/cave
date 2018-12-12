class Object():
  def __init__(self, props):
    for key in props:
      self.__setattr__(key, props.get(key))

class Config():
  def __init__(self):
    self.tile_size = 32
    self.fps = 30
    self.font = Object(dict(
      family="Roboto Mono", 
      size=18
    ))
    self.screen = Object(dict(
      size=(800, (600 + self.tile_size)), 
      title="((((((((())"
    ))
    self.colors = Object(dict(
      background="black",
      ground="darkgrey",
      walls="black",
      player="red",
      enemies=Object(dict(
        orange="orange", 
        green="green", 
        blue="blue"
      ))
    ))
    self.actors=Object(dict(
      player=Object(dict(
        name="test",
        clas="rogue",
        hp=10,
        atk=0.3,
        dfs=0.4,
        pts=10,
        lvl=0,
        exp=0
      )),
      enemies=[
        Object(dict(
          name="goblin 1",
          clas="warrior",
          hp=5,
          atk=0.1,
          dfs=0.1,
          pts=5,
          lvl=0,
          exp=10
        )),
        Object(dict(
          name="goblin 2",
          clas="warrior",
          hp=6,
          atk=0.2,
          dfs=0.3,
          pts=5,
          lvl=0,
          exp=23
        ))
      ]
    ))
