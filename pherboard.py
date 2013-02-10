class pherboard:
  #stores the pheramones

  def __init__(self, dim):
    self.dim = dim
    self.arr = [[0]*dim for x in range(dim)]
    for i in self.arr:
      print i

  def add_pheromone_trail(self, movelist):
    for x,y in movelist:
      self.arr[x][y] -= 1000;

  def decay_pheromones(self):
    for x in range(self.dim):
      for y in range(self.dim):
        self.arr[x][y] = (int) (.95 *  self.arr[x][y])




p = pherboard(5)

