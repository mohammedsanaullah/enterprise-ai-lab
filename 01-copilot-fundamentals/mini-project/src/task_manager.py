from typing import List, Optional

from task import Task


class TaskManager:
    def __init__(self, tasks: Optional[List[Task]] = None):
        self.tasks = tasks[:] if tasks else []

    def _next_id(self) -> int:
        if not self.tasks:
            return 1
        return max(task.task_id for task in self.tasks) + 1

    def add_task(self, title: str) -> Task:
        new_task = Task(task_id=self._next_id(), title=title)
        self.tasks.append(new_task)
        return new_task

    def list_tasks(self) -> List[Task]:
        return list(self.tasks)

    def get_task(self, task_id: int) -> Optional[Task]:
        for task in self.tasks:
            if task.task_id == task_id:
                return task
        return None

    def mark_complete(self, task_id: int) -> bool:
        task = self.get_task(task_id)
        if task is None:
            return False
        task.mark_complete()
        return True

    def delete_task(self, task_id: int) -> bool:
        task = self.get_task(task_id)
        if task is None:
            return False
        self.tasks.remove(task)
        return True

    def to_dict_list(self) -> List[dict]:
        return [task.to_dict() for task in self.tasks]

    @classmethod
    def from_dict_list(cls, data_list: List[dict]) -> "TaskManager":
        tasks = [Task.from_dict(data) for data in data_list]
        return cls(tasks=tasks)