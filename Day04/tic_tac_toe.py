
from board import Board
from game import Game
from player import Player, HumanPlayer, ComputerPlayer 

def initiate_game():

   while True:
    choice = input("Do you want to play with a friend (1) or vs computer (2)? ")
    if choice not in ["1", "2"]:
      print("Invalid choice. Try again!")
      continue

    player_one_name = input("Enter first player's name: ")
    player_one_symbol = input(f"Enter {player_one_name}'s favorite synbol 'X' or 'O' -> ").upper()

    if not Player.is_valid_symbol(player_one_symbol):
      print("Invalid symbol. Must be X or O.")
      continue

    if choice == "1":
      player_two_name = input("Enter second player's name: ")
      player_two_symbol = "O" if player_one_symbol == "X" else "X"
      player_two = HumanPlayer(player_two_name, player_two_symbol)
    else:
      computer_symbol = "O" if player_one_symbol == "X" else "X"
      player_two = ComputerPlayer(computer_symbol)

    player_one = HumanPlayer(name=player_one_name, symbol=player_one_symbol)
    board = Board()
    game = Game(players=[player_one, player_two], board=board, current_turn=1)
    return game

def main():
  while True:

    print("\n====== Main Menu ======")
    print("Welcome to Tic Tac Toe!")
    print("1. Start Game")
    print("2. Quit")
    choice = input("Enter choice: ")

    if choice == "1":
      game = initiate_game()
      game.play()
    elif choice == "2":
      print("Goodbye!")
      break
    else:
      print("Invalid option. Try again.")


if __name__ == "__main__":
    main()