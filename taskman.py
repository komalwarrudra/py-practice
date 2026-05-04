import json

def load_task():
    try:
        with open('task.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

def save_task(tasks):
    with open('task.json', 'w') as file:
        json.dump(tasks, file, indent=2)

def add_task(task):
    tasks = load_task()
    tasks.append(task)
    save_task(tasks)    

def view_tasks():
    tasks = load_task()
    if not tasks:
        print("No tasks found.")
    else:
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")

def remove_task(task_number):
    tasks = load_task()
    if 0 < task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        save_task(tasks)
        print(f"Removed task: {removed_task}")
    else:
        print("Invalid task number.")

while True:
    print("\nTask Manager")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        task = input("Enter the task: ")
        add_task(task)
        print("Task added successfully.")
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        try:
            task_number = int(input("Enter the task number to remove: "))
            remove_task(task_number)
        except ValueError:
            print("Please enter a valid number.")
    elif choice == '4':
        print("Exiting Task Manager. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")