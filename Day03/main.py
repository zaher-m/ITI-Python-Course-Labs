import math_automation
import log_cleaner
import datetime_reminder
import product_transformer
import os_file_manager
import rand_data_gen


def display_menu():
    print("\n================= TASK MENU =================")
    print("1) Math Automation")
    print("2) Regex Log Cleaner")
    print("3) Datetime Reminder Script")
    print("4) Product Data Transformer")
    print("5) OS File Manager")
    print("6) Random Data Generator")
    print("0) Exit")
    print("============================================")


def get_user_choice():
    """validate user input and return a valid task number"""
    while True:
        choice = input("Enter the task number (0-6): ").strip()
        if choice.isdigit():
            choice = int(choice)
            if 0 <= choice <= 6:
                return choice
        print("\nInvalid input. Please enter a number between 0 and 6\n")



def main():
    task_map = {
        1: math_automation.math_automation,
        2: log_cleaner.log_cleaner,
        3: datetime_reminder.reminder,
        4: product_transformer.product_transformer,
        5: os_file_manager.os_file_manager,
        6: rand_data_gen.random_data_gen,
    }
    while True:
        display_menu()
        choice = get_user_choice()
        if choice == 0:
            print("Exiting program...")
            break
        task_map[choice]()

if __name__ == "__main__":
    main()
