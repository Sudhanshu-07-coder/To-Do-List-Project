# Importing necessary libraries
import json
import os

# Defining the file name for storing tasks
fileName = "tasks.json"

# Function to load tasks from the JSON file
def load_tasks():
    if not os.path.exists(fileName):
        return []
    try:
        with open(fileName, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []

# Function to save tasks to the JSON file
def save_tasks(tasks):
    with open(fileName, "w") as file:
        json.dump(tasks, file, indent=4)

# Function to add a new task
def add_task(tasks):
    task_name = input("Enter task description: ").strip()
    if task_name == "":
        print("Task cannot be empty.")
        return

    task = {
        "title": task_name,
        "completed": False
    }
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully.")

# Function to list all tasks
def list_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return

    print("\nYour Tasks:")
    for index, task in enumerate(tasks, start=1):
        status = "✔ Done" if task["completed"] else "✘ Pending"
        print(f"{index}. {task['title']} [{status}]")

# Function to delete a task
def delete_task(tasks):
    list_tasks(tasks)
    if not tasks:
        return

    try:
        task_no = int(input("Enter task number to delete: "))
        if task_no < 1 or task_no > len(tasks):
            print("Invalid task number.")
            return

        removed_task = tasks.pop(task_no - 1)
        save_tasks(tasks)
        print(f"Task '{removed_task['title']}' deleted.")
    except ValueError:
        print("Please enter a valid number.")

# Function to mark a task as completed
def mark_task_done(tasks):
    list_tasks(tasks)
    if not tasks:
        return

    try:
        task_no = int(input("Enter task number to mark as done: "))
        if task_no < 1 or task_no > len(tasks):
            print("Invalid task number.")
            return

        tasks[task_no - 1]["completed"] = True
        save_tasks(tasks)
        print("Task marked as completed.")
    except ValueError:
        print("Please enter a valid number.")

# Main function to run the to-do list application
def main():
    tasks = load_tasks()

    while True:
        print("\n--- To-Do List Menu ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Mark Task as Done")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            list_tasks(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            mark_task_done(tasks)
        elif choice == "5":
            print("Exiting To-Do List. Goodbye!")
            break
        else:
            print("Invalid choice. Please select between 1 and 5.")

# Entry point of the application
if __name__ == "__main__":
    main()
