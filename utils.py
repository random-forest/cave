import math, random

def scale_pairs(a, b, size):
  return (a * size, b * size)

def rand(size):
  return math.floor(random.uniform(0, size))