
import os
import shutil

def os_file_manager():
    
    while True:
        pt = input("Enter directory path in ('/path/to/your/directory') format: ").strip()

        if not os.path.isdir(pt):  # ensure it's a directory
            print("Invalid path, try again!")
            continue

        # backup directory
        backup_dir = os.path.join(pt, "backup")
        # create backup directory if not exists
        os.makedirs(backup_dir, exist_ok=True)

        # get all .txt files in directory
        txt_files = [f for f in os.listdir(pt) if f.endswith(".txt") and os.path.isfile(os.path.join(pt, f))]

        copied_count = 0
        for file in txt_files:
            src = os.path.join(pt, file)
            dst = os.path.join(backup_dir, file)
            shutil.copy(src, dst)
            copied_count += 1

        print(f"Copied {copied_count} .txt file(s) into '{backup_dir}'.")
        break

if __name__ == "__main__":
    print("\nRunning Task 5: OS File Manager (backup .txt files)")
    os_file_manager()