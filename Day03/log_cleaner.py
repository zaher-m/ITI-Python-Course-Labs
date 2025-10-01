import re
import os

def log_cleaner(log_file="access.log", cleaned_file="valid_emails.txt"):
    email_pattern = re.compile("[^@]+@[^@]+\.[^@]+") # only one '@' and '.' plus anyyhing else between
    valid_emails = set()

    with open(log_file,"r",encoding="utf-8") as f:
        lines = f.read().splitlines()
        
    for line in lines:
        email = line.split(": ")[1]
        if email_pattern.match(email):
            valid_emails.add(email)
    
    with open(cleaned_file, "w", encoding="utf-8") as f:
        f.write("\n".join(valid_emails))
    
    print(f"Number of unique emails: {len(valid_emails)}")

        
if __name__ == "__main__":
    log_cleaner()
