import json
import os

DATA_FILE = "todo_data.json"

def load_tasks():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_tasks(tasks):
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def add_task():
    task_name = input("Enter task: ").strip()
    if task_name:
        tasks = load_tasks()
        tasks.append({"task": task_name, "completed": False})
        save_tasks(tasks)
        print(f"Task '{task_name}' added.")
    else:
        print("Task cannot be empty.")

def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return
    print("\nTo-Do List:")
    for idx, task in enumerate(tasks, 1):
        status = "✅" if task["completed"] else "❌"
        print(f"{idx}. [{status}] {task['task']}")
    print()

def mark_task_complete():
    tasks = load_tasks()
    view_tasks()
    try:
        task_num = int(input("Enter task number to mark as complete: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]["completed"] = True
            save_tasks(tasks)
            print("Task marked as complete.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task():
    tasks = load_tasks()
    view_tasks()
    try:
        task_num = int(input("Enter task number to delete: "))
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            save_tasks(tasks)
            print(f"Deleted task: {removed['task']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    while True:
        print("\n--- To-Do List Manager ---")
        print("1. View tasks")
        print("2. Add task")
        print("3. Mark task as complete")
        print("4. Delete task")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == '1':
            view_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            mark_task_complete()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 5.")

if __name__ == "__main__":
    main()
