

import random
from  utils import *


def task1() -> None:
    inputs = input("Enter 5 numbers space-separated. e.g: 1 2 3 etc.\n")
    inputs = inputs.split(" ")
    if len(inputs) == 5:
        if is_list_of_numbers(inputs):
            numbers = [float(num) for num in inputs]
            print(f"ASC: {sorted(numbers)}")
            print(f"DESC: {sorted(numbers, reverse=True)}")
            return
    else:
        print("Make sure you're entering only 5 numbers!")
        task1()


def task2(length:str, start:str):
    """Generate a list of sequences 
    args:
        length: length of the range
        start:  start of the sequence

    rturn: 
        a list of the generated sequence

    """
    if is_list_of_numbers([length, start]):
        length, i = int(length), int(start)
        ranges = []
        while i <= (length):
            ranges.append(i)
            i += 1

        return ranges    

    else:
        print("Yo've entered wrong inputs, try again!")
        return


def task3():
    """Prompt user for numbers until 'done', then show total, count, and average."""

    print("Enter a number or 'done' to finish.\n")
    inputs = []
    while True:
        num = input("--> ")
        if num.lower() == "done":
            break
        inputs.append(num)
        
    numbers = only_numbers(inputs)
    print(numbers)
    if numbers:
        out_msg = f""" All entered numbers: {numbers}, Count: {len(numbers)}, Averag: {sum(numbers)/len(numbers)}
        """
        print(out_msg)

    return

def task4():
    inputs = input("Enter a list of numbers space-separated. e.g: 1 2 3 etc.\n --> ")
    inputs = inputs.split(" ")

    if is_list_of_numbers(inputs):
        numbers = [float(num) for num in inputs]
        unique_numbers = set(numbers)
        print(f"Sorted & Unique: {sorted(unique_numbers)}")

    else:
        print("Make sure you're entering all numbers!")
        task4()
    
    return


def task5():
    """Count and display word frequencies in a sentence"""

    sentence = input("Enter a sentence: ")
    if sentence:
        words = sentence.split()
        if len(set(words)) == len(words):
            print("Each word  appeared once!")
            return

        counter = {}
        for word in words:
            if word in counter.keys():
                counter[word] += 1 
            else:
                counter[word] = 1
        
        for word, count in counter.items():
            print(f"Word '{word}' appeared '{count}' times!'")
            
    else:
        print("Nothing entered!")
        task5()

    return

def task6():
    """Collect 5 students' scores and display highest, lowest, and average."""

    student_names, student_scores = [], []
    print("Enter student's name with score. e.g. (Zaher,20)\n")
    for i in range(5):
        student = input(f"{i+1}. --> ")
        if student:
            name, score = student.split(",")
            student_names.append(name)
            student_scores.append(score)
            if is_list_of_numbers(student_scores):
                student_scores = [float(num) for num in student_scores]
            else:
                print("Y've entered wrong score value!")
                continue
        

        else:
            print("Nothing entered!")
            break
    
    if student_names and student_scores:
        out_msg = f"""Highest scoreP: {max(student_scores)}, Minimum score: {min(student_scores)}, Average score: {sum(student_scores)/len(student_scores)}
        """
        print(out_msg)
    else:
        task6()

    return



def task7():
    """Simulate a simple shopping cart system with add, remove, view, and total"""

    def menu():
        print("""
        ==== Shopping Cart Menu ====
        1. Add item
        2. Remove item
        3. View cart
        4. Checkout (show total and exit)
        """)
        return input("--> ")

    cart = {}

    while True:
        choice = menu()

        if choice == "1":
            item = input("Enter item name with price. e.g. (Laptop,3000): ")
            name, price = item.split(",")
            if is_a_number(price):
                cart[name] = float(price)
                print(f"Added '{name}' with price {price}")
            else:
                print("Invalid price, please try again.")

        elif choice == "2":
            item = input("Enter item name to remove: ")
            if item in cart:
                del cart[item]
                print(f"'{item}' removed from the cart")
            else:
                print("Item not found in the cart.")

        elif choice == "3":
            if cart:
                print("\n--- Items in Cart ---")
                print("\nNAME | PRICE\n")
                for name, price in cart.items():
                    print(f"{name}: {price}")
                print("---------------------\n")
            else:
                print("Cart is empty.")

        elif choice == "4":
            if cart:
                print(f"\nTotal cost: {sum(cart.values())}\n")
            else:
                print("Cart is empty!")
            break

        else:
            print("Invalid choice. Select 1–4.")

    return

def task8():
    """Play a number guessing game between 1 and 20 with attempt count"""

    secret = random.randint(1, 20)
    attempts = 0
    print("I'm thinking of a number between 1 and 20...")

    while True:
        guess = input("Enter your guess: ")
        if not is_a_number(guess):
            print("Enter a valid number.")
            continue

        guess = int(guess)
        attempts += 1

        if guess < secret:
            print("Too low! Try again.")
        elif guess > secret:
            print("Too high! Try again.")
        else:
            print(f"Correct! The number was {secret}. Attempts: {attempts}")
            break

    return
