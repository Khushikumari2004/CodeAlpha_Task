import os
import shutil
import tempfile
import functools
import time

# --- Decorator for Logging Task Completion ---
def task_logger(task_name):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f"\nStarting {task_name}...")
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            print(f"Completed {task_name} in {round(end_time - start_time, 2)}s!")
            return result
        return wrapper
    return decorator

# --- Task 1: File Organization ---
file_types = {
    "Text Files": ['.txt', '.docx'],
    "Images": ['.jpg', '.jpeg', '.png', '.gif'],
    "PDFs": ['.pdf'],
    "Spreadsheets": ['.xlsx', '.csv'],
    "Presentations": ['.pptx'],
    "Scripts": ['.py', '.js', '.html', '.css']
}

@task_logger("File Organization")
def organize_files(directory):
    if not os.path.exists(directory):
        print(f"Directory '{directory}' does not exist.")
        return
    
    print(f"Organizing files in '{directory}'...")
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            _, ext = os.path.splitext(filename)
            moved = False
            for folder, extensions in file_types.items():
                if ext in extensions:
                    folder_path = os.path.join(directory, folder)
                    if not os.path.exists(folder_path):
                        os.makedirs(folder_path)
                    shutil.move(file_path, folder_path)
                    print(f"Moved {filename} to {folder}")
                    moved = True
                    break
            if not moved:
                others_folder = os.path.join(directory, "Others")
                if not os.path.exists(others_folder):
                    os.makedirs(others_folder)
                shutil.move(file_path, others_folder)
                print(f"Moved {filename} to Others")

# --- Task 2: Data Cleaning ---
@task_logger("Data Cleaning")
def clean_txt_files(directory):
    print(f"Cleaning .txt files in '{directory}'...")
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            file_path = os.path.join(directory, filename)
            with open(file_path, 'r') as file:
                lines = file.readlines()
            cleaned_lines = [line.strip() for line in lines if line.strip()]
            with open(file_path, 'w') as file:
                file.write('\n'.join(cleaned_lines))
            print(f"Cleaned {filename}")

# --- Task 3: System Maintenance (clearing temporary files) ---
@task_logger("System Maintenance")
def clear_temp_files():
    temp_dir = tempfile.gettempdir()
    print(f"Clearing temporary files in '{temp_dir}'...")
    for filename in os.listdir(temp_dir):
        file_path = os.path.join(temp_dir, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
                print(f"Deleted {filename}")
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
                print(f"Deleted folder {filename}")
        except Exception as e:
            print(f"Error deleting {filename}: {e}")

# --- Main Function to Run All Tasks ---
def automate_tasks():
    print("\n=== Task Automation ===")
    directory = input("Enter the directory path to organize and clean: ")

    # Execute all tasks
    organize_files(directory)
    clean_txt_files(directory)
    clear_temp_files()

    print("\nAll tasks completed successfully!")

if __name__ == "__main__":
    automate_tasks()
