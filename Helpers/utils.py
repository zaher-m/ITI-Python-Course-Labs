def is_a_number(inp: str) -> bool:
    """Check if the input string is a valid integer or float number"""
    try:
        float(inp)
        return True
    except ValueError:
        return False
    
def is_list_of_numbers(inp:list) -> bool:
    """Check if the input list is a valid list of numbers"""

    for i in inp:
        if not is_a_number(i):
            return False
    return True

def only_numbers(inp:list) -> list:
    """Filters a list to include only numeric elements (integers and floats)"""
    
    res = []
    for ele in inp:
        if is_a_number(ele):
            res.append(float(ele))
    return res

def is_list_of_names(inp:list) -> bool:
    """Check if the input list is a valid list of product names
    a product name is not correct neme if it contains non-alphanumeric characters
    """

    if is_list_of_numbers(inp):
        return False
    for p in inp:
        if not all(char.isalpha() for char in p):
            return False
    return True

def main_menu():
    """Display the main menu of tasks"""
    tasks_menu = {
        0: "quit",
        1: "Enter 5 numbers and display them in ascending and descending order",
        2: "Generate a sequence of numbers from a start value with given length",
        3: "Keep entering numbers until 'done', then show total, count, and average",
        4: "Enter a list of numbers, remove duplicates, sort, and display",
        5: "Enter a sentence and count how many times each word appears",
        6: "Enter 5 students' names and scores, then show highest, lowest, and average",
        7: "Simulate a shopping cart with add, remove, view, and total cost",
        8: "Play a number guessing game between 1 and 20 with attempt count",
    }

    print("\n=== Main Menu ===")
    for key, desc in tasks_menu.items():
        print(f"{key}. {desc}")

    choice = input("\nSelect a task number: ")
    return choice