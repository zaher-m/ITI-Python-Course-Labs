# ITI Python Labs – Repository Overview

This repository contains hands-on Python labs and lecture materials spanning fundamental programming, automation, and object‑oriented programming. Each lab is self‑contained with its own `README.md`, while this root README provides a high‑level map and quick start.

---

## Structure

- `Day02/` – Lab 02: function‑based practice tasks with a menu‑driven runner
- `Day03/` – Lab 03: automation scripts orchestrated by `main.py`
  - Tasks: math report, regex log cleaner, datetime reminder, product transformer, OS file manager, random data generator, decorators
- `Day04/` – Lab 04: Tic‑Tac‑Toe using OOP (players, board, game loop)
- `Helpers/` – Reusable utilities under `utils.py`

---

## Day02 – Lab 02 (Practice Tasks)

- Menu‑driven app where each option runs a function‑scoped task.
- Focus areas: input validation, lists/sets/dicts, sequences, sort, word counts, simple games, small systems (gradebook, cart).
- See `Day02/README.md` for the full task list and rules.

## Day03 – Lab 03 (Automation)

- Multiple standalone automation scripts imported and run from `main.py` with a user menu.
- Key features: strict input validation, modular functions, a `log_time` decorator that records runtimes to `backup/execution_log.txt`.
- See `Day03/README.md` for task details and run instructions.

## Day04 – Lab 04 (OOP Tic‑Tac‑Toe)

- OOP design with `Player` (Human/Computer), `Board`, and `Game` classes.
- Supports human vs human and human vs computer play modes.
- See `Day04/README.md` for class responsibilities and game flow.

---


### Clone the repository

Use Git to clone locally, then move into the project root:

```bash
git clone https://github.com/zaher-m/ITI-Python-Course-Labs.git iti-python-course-labs
cd iti-python-labs
```

Clone and run any lab from its directory:

```bash
cd Day02
python main.py

cd ../Day03
python main.py

cd ../Day04
python tic_tac_toe.py 
```

---

## Next steps

- Improve the computer strategy (optional):
  - Add basic heuristics: play winning moves; block opponent wins.
  - Add difficulty modes: Easy (random), Medium (random + block/win), Hard (minimax or scoring).
