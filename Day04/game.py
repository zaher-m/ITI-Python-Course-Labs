class Game:
  def __init__(self, players, board, current_turn):
      self.players = players
      self.__current_player = self.players[0]
      self.__current_turn = current_turn  # 1 or 2
      self.__total_plays = 0
      self.board = board
      self.start_game()

  def play(self):

    while True:
      state = self.current_player.make_move(self.board)
      if state is None:
        print("Game terminated.")
        break
      
      self.__total_plays += 1
      self.board.display()

      winner = self.board.check_winner()
      if winner:
        print(f"\n {self.current_player.name} ({winner}) wins!!")
        break
      if self.board.is_full():
        print("\nIt's a draw!!!")
        break

      self.switch_turns()

  @property
  def current_turn(self):
    return self.__current_turn
  @current_turn.setter
  def current_turn(self, turn):
    self.__current_turn = turn

  @property
  def current_player(self):
    return self.__current_player

  @current_player.setter
  def current_player(self, player):
    self.__current_player = player

  def switch_turns(self):
    self.current_turn = 2 if self.current_turn == 1 else 1
    self.current_player = self.players[self.current_turn - 1]

  def start_game(self):
      print(f"""
{"=" * 40}
Welcome to Tic Tac Toe
{"=" * 40}
Instructions:
1. The game is played on a 3x3 board.
2. Player: {self.players[0].name} and Player: {self.players[0].name}. take turns placing their symbol (X or O).
3. The first player to align three symbols (row, column, or diagonal) wins.
4. If all cells are filled and no one wins, it's a draw.

How to choose a move:
- Use row and column numbers as positions.
- Example: to place a symbol in the top-left corner, enter (1,1).
{"=" * 40}
Below is the initial board:
""")
      print(self.board)   # show empty board
      print()