import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from task_manager import TaskManager
from task import Task


class TestTaskManager:
    def test_add_task_increases_count_and_assigns_id(self):
        manager = TaskManager()
        task = manager.add_task("Write docs")

        assert task.task_id == 1
        assert task.title == "Write docs"
        assert task.completed is False
        assert manager.list_tasks() == [task]

    def test_list_tasks_returns_copy_of_tasks(self):
        manager = TaskManager()
        manager.add_task("Task A")

        tasks = manager.list_tasks()
        tasks.append(Task(99, "Fake"))

        assert len(manager.list_tasks()) == 1

    def test_get_task_returns_task_by_id_or_none(self):
        manager = TaskManager()
        manager.add_task("Task A")

        assert manager.get_task(1) is not None
        assert manager.get_task(2) is None

    def test_mark_complete_updates_status_and_returns_true(self):
        manager = TaskManager()
        manager.add_task("Task A")

        result = manager.mark_complete(1)
        task = manager.get_task(1)

        assert result is True
        assert task is not None
        assert task.completed is True

    def test_mark_complete_returns_false_for_missing_id(self):
        manager = TaskManager()

        assert manager.mark_complete(999) is False

    def test_delete_task_removes_task_and_returns_true(self):
        manager = TaskManager()
        manager.add_task("Task A")

        result = manager.delete_task(1)

        assert result is True
        assert manager.get_task(1) is None
        assert manager.list_tasks() == []

    def test_delete_task_returns_false_for_missing_id(self):
        manager = TaskManager()

        assert manager.delete_task(5) is False

    def test_to_dict_list_and_from_dict_list_roundtrip(self):
        manager = TaskManager()
        manager.add_task("Task A")
        manager.mark_complete(1)

        data = manager.to_dict_list()
        new_manager = TaskManager.from_dict_list(data)
        loaded = new_manager.get_task(1)

        assert len(new_manager.list_tasks()) == 1
        assert loaded is not None
        assert loaded.title == "Task A"
        assert loaded.completed is True