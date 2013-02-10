class pherboard:
  #stores the pheramones

  def __init__(self, dim):
    self.dim = dim
    self.arr = [[0.0]*dim for x in range(dim)]
    for i in self.arr:
      print i

  def add_pheromone_trail(self, movelist):
    for x,y in movelist:
      self.arr[x][y] += 1000;

  def decay_pheromones(self):
    for x in range(self.dim):
      for y in range(self.dim):
        val = self.arr[x][y]
        if val != 0:
          self.arr[x][y] = .95 * val
  
  def fetch_pher_strength(self, x, y):
    return self.arr[x][y]

