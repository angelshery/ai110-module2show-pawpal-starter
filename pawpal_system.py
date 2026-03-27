from dataclasses import dataclass, field
from typing import List


@dataclass
class Task:
    name: str
    type: str        # e.g. "feeding", "walking", "medication"
    duration: int    # in minutes
    priority: int    # 1 = highest priority

    def get_details(self) -> str:
        pass


@dataclass
class Pet:
    name: str
    species: str
    age: int
    breed: str
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, _task: Task) -> None:
        pass

    def get_tasks(self) -> List[Task]:
        pass


class Owner:
    def __init__(self, name: str, available_time: int, preferences: List[str]):
        self.name = name
        self.available_time = available_time  # in minutes
        self.preferences = preferences
        self.pets: List[Pet] = []

    def add_pet(self, pet: Pet) -> None:
        pass

    def get_available_time(self) -> int:
        pass


class Scheduler:
    def __init__(self):
        self.plan: List[Task] = []

    def generate_plan(self, owner: Owner, pet: Pet) -> List[Task]:
        pass

    def explain_plan(self) -> str:
        pass
