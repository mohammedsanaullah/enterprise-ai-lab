import json
from pathlib import Path

from task_manager import TaskManager


def save_tasks(task_manager: TaskManager, filename: str = "tasks.json") -> None:
    path = Path(filename)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as file:
        json.dump(task_manager.to_dict_list(), file, indent=2)


def load_tasks(filename: str = "tasks.json") -> TaskManager:
    path = Path(filename)
    if not path.exists():
        return TaskManager()
    with path.open("r", encoding="utf-8") as file:
        data = json.load(file)
    return TaskManager.from_dict_list(data)