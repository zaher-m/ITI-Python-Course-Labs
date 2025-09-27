

from Lab_02 import *

def main():
    while True:
        choice = main_menu()
        try:
            task_number = int(choice)
            if choice == "0":
                print("Goodbye!")
                break

            if task_number == 1:
                task1()
            elif task_number == 2:
                length = input("Enter a specific lenght: ")
                start = input("Enter a specific start number: ")
                ranges = task2(length, start)
                print(ranges)

            elif task_number == 3:
                task3()
            elif task_number == 4:
                task4()
            elif task_number == 5:
                task5()
            elif task_number == 6:
                task6()
            elif task_number == 7:
                task7()
            elif task_number == 8:
                task8()
            elif task_number == 9:
                task9()
            else:
                print(f"Task {task_number} is not implemented yet.")
            
        except ValueError:
            print("Invalid input. Please enter a task number or '0' to quit.")


if __name__ == "__main__":
    main()