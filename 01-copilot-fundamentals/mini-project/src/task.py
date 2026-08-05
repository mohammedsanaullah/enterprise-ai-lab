class Task:
    def __init__(self, task_id: int, title: str, completed: bool = False):
        self.task_id = task_id
        self.title = title
        self.completed = completed

    def mark_complete(self):
        self.completed = True

    def to_dict(self):
        return {
            "id": self.task_id,
            "title": self.title,
            "completed": self.completed,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            task_id=data["id"],
            title=data["title"],
            completed=data.get("completed", False),
        )

    def __str__(self):
        status = "✅" if self.completed else "⬜"
        return f"{status} [{self.task_id}] {self.title}"

task1 = Task(1,"Learn Python")

print(task1)