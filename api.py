"""
REST API for Task Tracker.
This is PR #2 in our stack - depends on models from PR #1.
"""

from models import Task, Priority, Status

# In-memory store
TASKS: dict[str, Task] = {}
_next_id = 1


def create_task(title: str, priority: str = "medium") -> dict:
    global _next_id
    task = Task(title=title, priority=Priority(priority))
    task_id = str(_next_id)
    TASKS[task_id] = task
    _next_id += 1
    return {"id": task_id, "task": str(task)}


def list_tasks(status_filter: str | None = None) -> list[dict]:
    results = []
    for task_id, task in TASKS.items():
        if status_filter and task.status.value != status_filter:
            continue
        results.append({"id": task_id, "task": str(task)})
    return results


def complete_task(task_id: str) -> dict:
    if task_id not in TASKS:
        raise KeyError(f"Task {task_id} not found")
    TASKS[task_id].mark_done()
    return {"id": task_id, "task": str(TASKS[task_id])}
