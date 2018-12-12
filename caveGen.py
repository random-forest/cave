import random, numpy as np

WALL  = 0
FLOOR = 1
        
def generateCave(size, fill_coef, cycles):
  shape = size
  fill_prob = fill_coef

  new_map = np.ones(shape)
  for i in range(shape[0]):
    for j in range(shape[1]):
      choice = random.uniform(0, 1)
      new_map[i][j] = WALL if choice < fill_prob else FLOOR

  generations = cycles
  for generation in range(generations):
    for i in range(shape[0]):
      for j in range(shape[1]):
        submap = new_map[max(i-1, 0):min(i+2, new_map.shape[0]),max(j-1, 0):min(j+2, new_map.shape[1])]
        wallcount_1away = len(np.where(submap.flatten() == WALL)[0])
        submap = new_map[max(i-2, 0):min(i+3, new_map.shape[0]),max(j-2, 0):min(j+3, new_map.shape[1])]
        wallcount_2away = len(np.where(submap.flatten() == WALL)[0])

        if generation < 5:
          if wallcount_1away >= 5 or wallcount_2away <= 7:
            new_map[i][j] = WALL
          else:
            new_map[i][j] = FLOOR
          if i==0 or j == 0 or i == shape[0]-1 or j == shape[1]-1:
            new_map[i][j] = WALL

        else:
          if wallcount_1away >= 5:
            new_map[i][j] = WALL
          else:
            new_map[i][j] = FLOOR

  return new_map
