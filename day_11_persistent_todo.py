
import json
import os

FILE_NAME = "tasks.json"


def load_tasks():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        except (json.JSONDecodeError, OSError):
            print("Could not read saved tasks. Starting with an empty list.")

    return []


def save_tasks():
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


def add_task():
    name = input("Enter your task: ").strip()

    if name == "":
        print("Task cannot be empty!")
        return

    tasks.append({"name": name, "completed": False})
    save_tasks()
    print("Task added successfully!")


def view_tasks():
    if not tasks:
        print("No tasks saved yet.")
        return

    print("\n===== YOUR TASKS =====")

    for number, task in enumerate(tasks, start=1):
        status = "Completed" if task["completed"] else "Pending"
        print(f"{number}. {task['name']} - {status}")


def complete_task():
    view_tasks()

    if not tasks:
        return

    try:
        number = int(input("Enter task number to complete: "))

        if number < 1 or number > len(tasks):
            print("Invalid task number!")
            return

        tasks[number - 1]["completed"] = True
        save_tasks()
        print("Task marked as completed!")

    except ValueError:
        print("Please enter a valid number!")


def delete_task():
    view_tasks()

    if not tasks:
        return

    try:
        number = int(input("Enter task number to delete: "))

        if number < 1 or number > len(tasks):
            print("Invalid task number!")
            return

        removed_task = tasks.pop(number - 1)
        save_tasks()
        print("Deleted task:", removed_task["name"])

    except ValueError:
        print("Please enter a valid number!")


tasks = load_tasks()

while True:
    print("\n===== PERSISTENT TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Choose an option (1-5): ").strip()

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        complete_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Your tasks are saved. Goodbye!")
        break
    else:
        print("Invalid choice! Please select 1-5.")
