# Mini Project

This mini project is a small CLI Task Manager built to explore Copilot fundamentals and Python application structure.

## Project overview

The mini project implements a simple task manager that can:
- add tasks
- list tasks
- mark tasks complete
- delete tasks
- save tasks to a JSON file
- load tasks when the application starts

## Structure

- `src/` - application source code
  - `main.py` - CLI entry point and user interaction
  - `task.py` - task domain model
  - `task_manager.py` - business logic for task operations
  - `storage.py` - JSON persistence layer
- `tests/` - automated tests for validating functionality
- `.github/copilot-instructions.md` - guidance for Copilot use in the mini project

## Prerequisites

- Python 3.10+ recommended
- No external dependencies are required for the application itself
- `pytest` is used for running tests

## Running the app

From the `mini-project` folder:

```bash
python src/main.py
```

This will start the CLI and automatically load tasks from `tasks.json` if it exists. Tasks are saved back to `tasks.json` when you exit.

## How to run tests

1. Open a terminal in the repository root:
   ```bash
   cd 01-copilot-fundamentals/mini-project
   ```

2. (Optional but recommended) create and activate a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Install pytest if needed:
   ```bash
   pip install pytest
   ```

4. Run the test suite:
   ```bash
   pytest tests/
   ```

You should see output indicating the number of tests run, for example:
- `7 passed`

## Notes

- `tasks.json` is the persisted data file for tasks.
- `tests/` contains unit tests for the model, manager, and storage logic.
- The project is intended to stay beginner-friendly and modular.