# GitHub Copilot Fundamentals

## Purpose

This folder captures the learning journey around GitHub Copilot and beginner Python application design. It includes:
- Copilot fundamentals notes
- prompt patterns and examples
- simple Python examples
- a mini-project that applies the concepts in a real implementation

## Repository structure

- `notes/`
  - learning notes on Copilot features, inline completion, chat, best practices, and limitations
- `prompts/`
  - prompt examples for code review, refactoring, debugging, and architecture
- `examples/`
  - small Python examples demonstrating calculator logic, loops, classes, and file handling
- `mini-project/`
  - a beginner-friendly CLI Task Manager implementation
  - `src/` contains the application code
  - `tests/` contains unit tests
  - `.github/copilot-instructions.md` captures guidance for Copilot use

## Mini project overview

The `mini-project` is a simple CLI Task Manager implemented in Python. It demonstrates:
- a domain model in `src/task.py`
- business logic in `src/task_manager.py`
- JSON persistence in `src/storage.py`
- CLI flow in `src/main.py`
- automated tests in `tests/`

## How to run the mini project

From the `01-copilot-fundamentals/mini-project` folder:

```bash
python src/main.py
```

This will start the CLI and load existing tasks from `tasks.json` if present.

## How to run tests

From `01-copilot-fundamentals/mini-project`:

```bash
pytest tests/
```

## Notes

- The project is intentionally beginner-friendly and modular.
- `tasks.json` is used to persist task data between runs.
- The structure is designed to separate learning notes, prompt guidance, example code, and a practical mini-project.