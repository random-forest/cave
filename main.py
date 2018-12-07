from render import Render
from events import Events
from state import State

def scale_pairs(a, b, size):
  return (a * size, b * size)

def main():
  render = Render("((())0")
  events = Events()
  state  = State()

  def draw_stage():
    for row in state.current_stage:
      for node in row:
        pos = scale_pairs(node.x, node.y, render.tile_size)

        if node.walkable == False:
          render.draw_rect("red", pos)
        if node.walkable == True:
          render.draw_rect("black", pos)

  render.loop([
    events.catch,
    draw_stage
  ])

if __name__ == "__main__":
  main()
