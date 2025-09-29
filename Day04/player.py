import random 

from abc import ABC, abstractmethod

class Player(ABC):
  def __init__(self, name, symbol):
    self.name = name
    self.symbol = symbol

  @abstractmethod
  def make_move(self, board):
    pass

  @staticmethod
  def is_valid_symbol(symbol):
    return symbol in ["X","O"]

class HumanPlayer(Player):
  def __init__(self, name, symbol):
    super().__init__(name, symbol)

  def make_move(self, board):
    while True:
      move = input(f"\n{self.name} ({self.symbol}), enter your move (row,col) or -1 to exit: ")
      print()
      if move.strip() == "-1":
        return None
      
      if board.is_valid_move(move):
        x, y = map(int, move.split(","))
        board.update((x - 1, y - 1), self.symbol)
        return True
      else:
        print("Invalid move. Try again!\n")

class ComputerPlayer(Player):
  def __init__(self, symbol):
    super().__init__("Computer", symbol)

  def make_move(self, board):
    size = board.get_board_size()
    while True:
      x, y = random.randint(1, size), random.randint(1, size)
      if board.is_valid_move(f"{x},{y}"):
        board.update((x - 1, y - 1), self.symbol)
        print(f"\nComputer placed {self.symbol} at ({x},{y})\n")
        break