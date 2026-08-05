from typing import Optional

from task_manager import TaskManager
from storage import load_tasks, save_tasks


def display_menu() -> None:
    print("\nTask Manager")
    print("1. Add task")
    print("2. List tasks")
    print("3. Complete task")
    print("4. Delete task")
    print("5. Exit")


def prompt_choice() -> str:
    return input("Choose an option: ").strip()


def prompt_title() -> str:
    return input("Task title: ").strip()


def prompt_task_id() -> Optional[int]:
    raw = input("Task ID: ").strip()
    if not raw:
        print("Task ID is required.")
        return None
    if not raw.isdigit():
        print("Please enter a numeric task ID.")
        return None
    return int(raw)


def handle_add(manager: TaskManager) -> None:
    title = prompt_title()
    if not title:
        print("Task title cannot be empty.")
        return
    task = manager.add_task(title)
    print(f"Added task {task.task_id}: {task.title}")


def handle_list(manager: TaskManager) -> None:
    tasks = manager.list_tasks()
    if not tasks:
        print("No tasks found.")
        return
    for task in tasks:
        print(task)


def handle_complete(manager: TaskManager) -> None:
    task_id = prompt_task_id()
    if task_id is None:
        return
    if manager.mark_complete(task_id):
        print(f"Task {task_id} marked complete.")
    else:
        print(f"Task {task_id} not found.")


def handle_delete(manager: TaskManager) -> None:
    task_id = prompt_task_id()
    if task_id is None:
        return
    if manager.delete_task(task_id):
        print(f"Task {task_id} deleted.")
    else:
        print(f"Task {task_id} not found.")


def main() -> None:
    manager = load_tasks()
    print("Loaded tasks from file.")
    while True:
        display_menu()
        choice = prompt_choice()
        if choice == "1":
            handle_add(manager)
        elif choice == "2":
            handle_list(manager)
        elif choice == "3":
            handle_complete(manager)
        elif choice == "4":
            handle_delete(manager)
        elif choice == "5" or choice.lower() == "exit":
            save_tasks(manager)
            print("Saved tasks and exiting.")
            break
        else:
            print("Invalid option. Enter 1-5.")


if __name__ == "__main__":
    main()