class Board:
  def __init__(self, size=3):
    self.size = size
    self.__blanck = "_"
    self.__grid = [[self.__blanck]*self.size for _ in range(self.size)]

  def __str__(self):
    # for row in self.grid:
    #   print(*row)
    return "\n".join(" ".join(row) for row in self.__grid)

  def display(self):
    print(self)

  def get_board_size(self):
    return self.size

  # pos: is a tuple contains ith and jth indices of that specific position
  def update(self, pos, symbol):
    i, j = pos
    # using setter instead of directlly
    # getter -> logic -> setter
    new_grid = self.grid
    new_grid[i][j] = symbol
    self.grid = new_grid

  def check_winner(self):

    lines = []
    # rows and columns
    lines.extend(self.__grid)
    lines.extend([[self.__grid[r][c] for r in range(self.size)] for c in range(self.size)])

    # diagonals
    lines.append([self.__grid[i][i] for i in range(self.size)])
    lines.append([self.__grid[i][self.size - i - 1] for i in range(self.size)])

    for line in lines:
      if line.count(line[0]) == self.size and line[0] != self.__blanck:
        return line[0]  # return winning symbol
    return None

  def is_full(self):
    return all(self.__blanck not in row for row in self.grid)

  def is_valid_move(self, move):

    try:
      x, y = map(int, move.split(","))
      if 1 <= x <= self.size and 1 <= y <= self.size:
        return self.grid[x - 1][y - 1] == self.__blanck
    except Exception:
      return False   
    return False
 
  @property
  def grid(self):
    return self.__grid

  @grid.setter
  def grid(self, grid):
    self.__grid = grid
