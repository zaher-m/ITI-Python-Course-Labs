# Lab 4: Tic-Tac-Toe (OOP)

## Description

Design and implement a **Tic-Tac-Toe** game in Python using **Object-Oriented Programming (OOP)** concepts.  
The game should allow the player to choose whether to play with a **friend (human vs. human)** or **against the computer (human vs. computer)**.

---

## 📌 Requirements

### 1. Core Classes

- **Player**
  - Attributes: `name`, `symbol` (X or O)
  - Methods: `make_move(board)`
- **HumanPlayer** (inherits from `Player`)
  - Implements `make_move()` by asking the user for input.
- **ComputerPlayer** (inherits from `Player`)
  - Implements `make_move()` by choosing a move automatically (random or simple strategy).
- **Board**
  - Attributes: 3x3 grid.
  - Methods:
    - `display()`
    - `update(position, symbol)`
    - `check_winner()`
    - `is_full()`
- **Game**
  - Attributes: `players`, `board`, `current_turn`
  - Methods:
    - `play()`
    - `switch_turns()`

---

### 2. OOP Concepts to Use

- **Encapsulation** → Keep the board grid private, only modify it using methods.
- **Inheritance** → `HumanPlayer` and `ComputerPlayer` inherit from `Player`.
- **Polymorphism** → `make_move()` behaves differently depending on the type of player.
- **Special Methods** → Implement `__str__()` for board display formatting.

---

### 3. Game Flow

1. The program starts by asking:
2. If option **1** → two human players enter their names.  
3. If option **2** → one human player enters their name, and the opponent is the computer.  
4. Players take turns placing **X** or **O** on the grid.  
5. After each move, the board is displayed.  
6. The game checks if a player has **won** or if the board is **full (draw)**.  
7. Print the **winner** or `"It’s a draw!"` at the end.
