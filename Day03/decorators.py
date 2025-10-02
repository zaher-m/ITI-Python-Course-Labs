from datetime import datetime

def log_time(func):
    """A decorator that logs the excution time of a function"""
    def wrapper(*args, **kwargs):
        start = datetime.now()
        print(f"Function '{func.__name__}' called on: {start.strftime('%Y-%m-%d %H:%M:%S')}")
        func(*args, **kwargs)
        end = datetime.now()
        duration = (end - start).total_seconds()
        print(f"Function '{func.__name__}' finished execution in  {duration:.6f} seconds")

        with open("execution_log.txt", "a") as f:
            f.write(f"{func.__name__} -> {duration:.6f} seconds\n")

    return wrapper