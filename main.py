from render import Render
from events import Events
from state import State

def main():
  state  = State()
  render = Render("((())0", state)
  events = Events(state)

  render.loop([
    events.catch,
    render.draw_scene
  ])

if __name__ == "__main__":
  main()
