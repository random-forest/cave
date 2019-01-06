import random, math
from config import FLOOR

def getRandomPosition(matrix):
  y = math.floor(random.uniform(0, len(matrix)))
  x = math.floor(random.uniform(0, len(matrix[0])))

  if matrix[y][x] is FLOOR:
    return (x, y)
  else:
    return getRandomPosition(matrix)

def nestedFilter(matrix, target):
  x = 0
  y = 0

  for row in matrix:
    for col in row:
      if col == target:
        return (x, y)
      else:
        continue
      x += 1
    y += 1
    x = 0
  y = 0

def getNeighbors(matrix, target):
  arr = []
  nei = [
    (target[0], (target[1] - 1) % len(matrix)), 
    (target[0], (target[1] + 1) % len(matrix)),
    ((target[0] - 1) % len(matrix[0]), target[1]), 
    ((target[0] + 1) % len(matrix[0]), target[1]),
    ((target[0] + 1) % len(matrix[0]), (target[1] - 1) % len(matrix)), 
    ((target[0] - 1) % len(matrix[0]), (target[1] + 1) % len(matrix)),
    ((target[0] + 1) % len(matrix[0]), (target[1] + 1) % len(matrix)), 
    ((target[0] - 1) % len(matrix[0]), (target[1] - 1) % len(matrix))
  ]

  for n in nei:
    if matrix[n[0]][n[1]] is FLOOR:
      arr.append(n)
    else:
      continue

  return arr