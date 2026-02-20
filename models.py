"""
Task model with priority and status support.
This is PR #1 in our stack - adds a proper data model.
"""

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum


class Priority(Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class Status(Enum):
    TODO = "todo"
    IN_PROGRESS = "in_progress"
    DONE = "done"


@dataclass
class Task:
    title: str
    priority: Priority = Priority.MEDIUM
    status: Status = Status.TODO
    created_at: datetime = field(default_factory=datetime.now)

    def mark_done(self):
        self.status = Status.DONE

    def __str__(self):
        icon = {"todo": "[ ]", "in_progress": "[~]", "done": "[x]"}
        return f"{icon[self.status.value]} {self.title} ({self.priority.value})"
