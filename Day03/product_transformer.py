
import json
import os, sys 
from collections import defaultdict
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from Helpers.utils import is_list_of_names, is_list_of_numbers

def product_transformer(save_file="products.json"):
    
    def is_valid_product_data(names=None,prices=None):
        
        try:
            names = names.split(",")
            prices = prices.split(",")
            if not names or not is_list_of_names(names):
                print("Incorrect product names. Please, try again!")
                return False
            
            if  not prices or not is_list_of_numbers(prices):
                print("Incorrect product prices. Please, try again!")
                return False
            
            if len(names) != len(prices):
                print("Names and prices count mismatch!")
                return False
            
        except Exception as e:
            print(f"An error occurred! -> {e}")      
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
            if p_price <= 0:
                continue
            try:
                product["product"].append(p_name)
                product["price"].append(str(p_price))
                product["discount"].append(str(round(p_price*0.8)))

            except Exception as e:
                print(f"An error occurred! -> {e}")

        # writing to save_file file
        with open(save_file, "w", encoding='utf-8') as f:
            try:
                json.dump(product, f, indent=4)
            except Exception as e:
                print(f"An error occurred! -> {e}")
                print("Returning!!!")
                continue
        
        # reading from save_file file
        with open(save_file, "r", encoding='utf-8') as f:
            try:
                data = json.load(f)
                idx = 0
                dict_keys = data.keys()
                print(f" {' | '.join([col.upper() for col in dict_keys])}")

                dict_values = data.values() # list of lists of values
                zipped_values = zip(*dict_values) #[["prodAName", "prodAPrice", "prodADiscount"], ["prodBName",....], ....]

                for row in list(zipped_values):
                    if idx < 6 :
                        print(f" {' | '.join(row)}")
                        idx += 1
                    else:
                        break
            except FileNotFoundError:
                print(f"Error: The file '{save_file}' was not found.")
                continue

        
if __name__ == "__main__":
    print("\nRunning Task 4: Product Data Transformer (filter & discount products)")
    product_transformer()