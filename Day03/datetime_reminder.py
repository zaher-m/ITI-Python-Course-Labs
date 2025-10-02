import re 
from datetime import datetime

def reminder(reminder_file="reminders.txt"):

    def match_date(date):
        date_pattern = re.compile(r'^\d{4}-\d{2}-\d{2}$') 
        return date_pattern.match(date)
    
    while True:
        date = input("Please, enter a date (YYYY-MM-DD) or q to quit: ")
        if date.lower() == "q":
            break
        if match_date(date):
            try:
                datetime_object = datetime.strptime(date,"%Y-%m-%d") 
                if datetime_object < datetime.now():
                    print("You've entered past date. Please, try again!")
                    continue
            except ValueError:
                print("Wrong entry!")
                continue
        else:
            print("You've entered wrong date. Please, try again!")
            continue
        
        with open(reminder_file, "a", encoding="utf-8") as f:
            try:
                print(datetime_object.day, datetime_object.month, datetime_object.year )
                today = datetime.today()
                n_days_left = (datetime_object.date() - today.date()).days

                obj = f"{datetime_object.strftime('%Y-%m-%d')} -> {n_days_left} days left.\n"
                f.write(obj)
            except ValueError:
                print("Error encountered, please, try again!")
                continue
        
if __name__ == "__main__":
    print("\nRunning Task 3: Datetime Reminder (days until date)")
    reminder()

