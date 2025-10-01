
import json
from collections import defaultdict
from utils import *
# 4) Product Data Transformer (lambda, map, filter, zip)
#    - Ask user for a list of product names (comma-separated).
#    - Ask user for a list of product prices (comma-separated).
#    - Process them by:
#         - Pairing product with price.
#         - Filtering out items where price <= 0.
#         - Transforming each pair into a dictionary {"product": name, "price": price, "discounted": price * 0.9}.
#    - Save the final result as JSON into "products.json".
#    - Print a preview of the first 5 results.


def product_transformer(save_file="products.json"):
    
    def is_valid_product_data(names=None,prices=None):
        
        if not names or not prices:
            return False

        if isinstance(names, str):
            names = names.split(",")
        if isinstance(prices, str):
            prices = prices.split(",")

        if not names or not is_list_of_names(names):
            print("Incorrect product names. Please, try again!")
            return False
        if not prices or not is_list_of_numbers(prices):
            print("Incorrect product prices. Please, try again!")
            return False
        
        if len(names) != len(prices):
            print("Names and prices count mismatch!")
            return False
        
        return True


    while True:
        product = defaultdict(list)
        choice = input("Enter 'q' to quit os any key to start: ").lower()
        if choice == 'q':
            print("Quitting.....")
            return

        prod_names = input("Please, enter your product names comma-separated (laptop,headphone,etc): ")
        prod_prices = input("Please, enter your product prices comma-separated (1500,100,etc): ")
        if not is_valid_product_data(names=prod_names, prices=prod_prices):
            continue
        # convert both to list 
        prod_names = prod_names.split(",")
        prod_prices = list(map(float, prod_prices.split(",")))

        for p_name, p_price in zip(prod_names, prod_prices):
            if float(p_price) <= 0:
                continue
            try:
                product["product"].append(p_name)
                product["price"].append(float(p_price))
                product["discount"].append(float(p_price)*0.8)
            except Exception as e:
                print(f"An error occurred! -> {e}")

        with open(save_file, "a", encoding='utf-8') as f:
            try:
                json.dump([product], f, indent=4)
            except:
                print("Some error occurred!!!")
                print("Returning!!!")
                continue
    
    with open(save_file, "r", encoding='utf-8') as f:
        try:
            data = json.load(f)
            for item in data[:5]:
                print(item)
        except FileNotFoundError:
            print(f"Error: The file '{save_file}' was not found.")

        
if __name__ == "__main__":
    product_transformer()