
import random
from utils import is_a_number
from decorators import log_time


@log_time
def random_data_gen(save_file="random_numbers.csv"):
    while True:    
        n_rand = input("How many random numbers to generate or 'q' to quit: ").lower()
        
        if n_rand== 'q':
            print("Quitting!!!")
            return
        
        if not is_a_number(n_rand) or  int(n_rand) < 0:
            print("Invalid input, try again!")
            continue

        n_rand = int(n_rand)
        # generate random integer (without predefined range) of length n bits
        rand_nums = [random.getrandbits(5) for _ in range(n_rand)]

        try:
            with open(save_file, "w", encoding="utf-8") as f:
                f.write("index, value\n")
                for i, val in enumerate(rand_nums):
                    row = f"{str(i+1)}, {str(val)}\n"
                    f.write(row)
            
            print("\nSUMMARY")
            print("-"*30)
            # str_rand_numbers = [str(num) for num in rand_nums]
            # print(f"Numbers: {','.join(str_rand_numbers)}")
            avg = sum(rand_nums)/n_rand
            print(f"Total count: {n_rand}")
            print(f"Average: {avg:.2}")

        except Exception as e:
            print(f"An error occurred! -> {e}")      
            return False


if __name__ == "__main__":
    print("\nRunning Task 6: Random Data Generator (save random numbers to CSV)")
    random_data_gen()