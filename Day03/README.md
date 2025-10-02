# Lab 3: Automation Lab

A collection of Python scripts, each solving a different automation task.  
The tasks are modular, implemented in separate `.py` files, and orchestrated via a main menu (`main.py`).  

---

## 📌 Requirements

1. **User input validation**  
   - Every user input must be validated.  
   - If invalid, show an error and ask again until valid.  

2. **Modularity**  
   - Each task is implemented in its own `.py` file.  
   - Each file must expose a function that executes the task.  

3. **Central control**  
   - A `main.py` file imports all task modules.  
   - When run, it displays a **menu** with all tasks and lets the user select one.  
   - Only the chosen task runs.  

4. **Code style**  
   - Use functions to avoid duplication.  
   - Add comments explaining steps.  
   - Automate wherever possible (file creation, processing).  
   - No hardcoding of results.  

5. **Decorators**  
   - Implement a decorator to measure execution time.  
   - Apply it to **at least two tasks**.  
   - Save function name + runtime in `execution_log.txt`.  

---

## Tasks Descriptions

### **1) Math Automation**

- Create a file `math_report.txt`.  
- Ask user for multiple numbers (comma-separated).  
- For each number, calculate:
  - floor  
  - ceil  
  - square root  
  - area of a circle  
- Write results into `math_report.txt`.  
- Confirm file was created and display its contents.  

---

### **2) Regex Log Cleaner**

- Generate a file `access.log` with 10 fake log lines (mix of valid/invalid emails).  
- Extract **valid emails** using regex.  
- Save them into `valid_emails.txt`.  
- Print how many **unique** emails were found.  

---

### **3) Datetime Reminder Script**

- Ask user for a date (YYYY-MM-DD).  
- Calculate how many days remain until that date.  
- If in the past → print `"This date has already passed."`  
- Otherwise → append to `reminders.txt` in format: YYYY-MM-DD -> X days left
- Allow multiple reminders without overwriting.  

- Allow multiple reminders without overwriting.  

### **4) Product Data Transformer**

- Ask user for a list of product names (comma-separated).  
- Ask user for a list of product prices (comma-separated).  
- Process by:
- Pairing each product with its price.  
- Filtering out items with `price <= 0`.  
- Transforming into dictionaries:  

  ```python
  {"product": name, "price": price, "discounted": price * 0.9}
  ```
  
- Save results as JSON in `products.json`.  
- Print a preview of the first 5 items.  

### **5) OS File Manager**

- Ask user for a directory path.  
- Inside it:
- Create a `backup/` folder (if not exists).  
- Copy all `.txt` files into `backup/`.  
- Print summary: how many files were copied.  
- Retry until a valid directory is given.  

---

### **6) Random Data Generator**

- Ask user how many random numbers to generate.  
- Save into `random_numbers.csv` in format:  
- Print:
- Total count of numbers.  
- Average value.  

### **7) Decorators Task**

- Implement a decorator `log_time` that:  
- Records execution time of any function.  
- Saves: `function_name -> runtime` into `execution_log.txt`.  
- Apply it to **at least two tasks** (e.g., Math Automation & Regex Log Cleaner).  
- Verify log file entries are created after execution.  

---

## ▶️ How to Run

1. Clone this repository.  
2. Ensure you have Python 3 installed.  
3. Run the main script:  

 ```bash
 python main.py
```
