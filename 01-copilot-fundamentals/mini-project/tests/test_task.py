import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from task import Task


class TestTask:
    def test_to_dict_and_from_dict_roundtrip(self):
        task = Task(task_id=1, title="Write docs")
        data = task.to_dict()

        assert data == {"id": 1, "title": "Write docs", "completed": False}

        loaded = Task.from_dict(data)
        assert loaded.task_id == 1
        assert loaded.title == "Write docs"
        assert loaded.completed is False

    def test_mark_complete_sets_completed_true(self):
        task = Task(task_id=2, title="Review design")

        task.mark_complete()

        assert task.completed is True
        assert "✅" in str(task)

    def test_str_representation_includes_id_title_and_status(self):
        task = Task(task_id=3, title="Refactor code")

        output = str(task)

        assert "[3]" in output
        assert "Refactor code" in output
        assert "⬜" in output