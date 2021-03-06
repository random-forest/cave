TILE_SIZE   = 16
FPS         = 60
WINDOW_SIZE = (1027, 664)

WALL  = 0
FLOOR = 1
START = 2
END   = 3
DOOR  = 4
BOX   = 5

room1 = [
  [0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0],
  [0,1,1,1,1,1,1,0,5,1,1,1,1,1,1,0],
  [0,1,1,1,1,1,1,0,1,1,1,1,1,1,1,0],
  [0,1,1,1,1,1,1,0,1,1,1,1,1,1,1,0],
  [0,1,1,1,1,1,1,0,1,1,1,1,1,1,1,0],
  [0,1,1,0,0,0,0,0,0,0,0,4,0,0,0,0],
  [0,1,1,0,5,1,1,1,1,1,1,1,1,1,1,0],
  [0,1,1,0,1,1,1,1,1,1,1,1,1,1,1,0],
  [0,1,1,0,1,1,1,1,1,1,1,1,1,1,1,0],
  [0,1,1,0,1,1,1,1,1,1,0,0,4,0,0,0],
  [0,1,1,0,0,0,0,1,1,1,0,1,1,1,1,0],
  [0,1,1,1,1,1,1,1,1,1,0,1,1,1,1,0],
  [0,1,1,1,1,1,1,1,1,1,0,1,1,1,1,0],
  [0,1,1,1,1,1,1,1,1,1,0,1,1,1,1,0],
  [0,1,1,1,1,1,1,1,1,1,4,1,1,1,5,0],
  [0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0],
]

LEVEL = [
  room1
]

BLACK      = "#1B120F"
GREY       = "#C9C9C9"
LIGHT_GREY = "#E9E9E9"
ORANGE     = "#F89D13"
RED        = "#8F1D14"
LIGHT_RED  = "#F12D2D"
BLUE       = "#3161A3"
PURPLE     = "#A275E3"
GREEN      = "#B5EDBA"
DARK_GREEN = "#55968F"

TEXT_MARGIN      = 5
TEXT_LINE_HEIGHT = 10