# Lab 02 – Python Practice Tasks  

## Description

Design and implement a set of **Python practice tasks** focusing on input handling, data structures, and modular programming.  
Each task is menu-driven and must run only when selected by the user.  

---

## Requirements  

1. **Program Structure**  
   - Everything must be written inside functions.  
   - The file should run as a script.  
   - On start, the program displays a numbered menu of scenarios.  
   - The user selects a number → the corresponding function runs.  
   - Invalid input should:  
     - Show an error message  
     - Explain valid input  
     - Prompt again (program must not crash)  

2. **Tasks**  
   - **Task 1:** Enter 5 numbers → display in ascending and descending order.  
   - **Task 2:** Generate a sequence given `(length, start)`.  
   - **Task 3:** Keep asking for numbers until `"done"` → show total, count, and average.  
   - **Task 4:** Enter a list of numbers → remove duplicates, sort, and display.  
   - **Task 6:** Enter a sentence → count word occurrences.  
   - **Task 7:** Gradebook system for 5 students → highest, lowest, and average score.  
   - **Task 8:** Shopping cart system → add, remove, view items, and show total cost.  
   - **Task 9:** Number guessing game (1–20) → hints until correct, show attempts.  

---

## Program Flow  

1. Display main menu with numbered options.  
2. User selects a task number.  
3. Run the chosen function.  
4. Return to menu after completion.  
5. Handle invalid input gracefully at every stage.  
