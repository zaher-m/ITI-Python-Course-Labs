
import os
import math
from  utils import *

def math_automation(report_file="math_report.tx"):
    pi = 3.14
    inputs = input("Enter a list of numbers comma-separated. e.g: 1,2,3 etc.\n --> ")
    inputs = inputs.split(",")
    if is_list_of_numbers(inputs):
        numbers = [float(num) for num in inputs]
        floors = [math.floor(num) for num in numbers]
        ceils = [math.ceil(num) for num in numbers]
        squares = [num*num for num in numbers]
        roots = [math.sqrt(num) for num in numbers]
        areas = [pi*num*num for num in numbers]
    else:
        print("Make sure you engtered all numbers correctly!!")
        return math_automation()

    # writing to file (overwrite its content with each new run)
    """
    Number: float | ceil | square | root | area
    """
    with open(report_file, "w", encoding="utf-8") as f:
        print(f"WRITING TO {report_file} FILE!")
        f.write("MATH REPORT\n")  
        f.write("Number: floor | ceil | square | root | area\n")  
        for i in range(len(numbers)):
            f.write(
                f"{numbers[i]:.2f}: {ceils[i]} | {floors[i]} | "
                f"{squares[i]:.2f} | {roots[i]:.2f} | {areas[i]:.2f}\n"
            )
    print(f"Report generated at {report_file}")


    # read back and print 
    print(f"\nREADING FROM {report_file} FILE!\n")
    with open(report_file, "r", encoding="utf-8") as f:
        for line in f:
            print(line.strip())
    return

if __name__  == "__main__":
    math_automation()