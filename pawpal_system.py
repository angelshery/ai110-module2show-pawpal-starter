class Owner:
    def __init__(self, name, time_available, preferences):
        self.name = name
        self.time_available = time_available
        self.preferences = preferences

    def update_preferences(self, preferences):
        self.preferences = preferences

    def set_time_available(self, time_available):
        self.time_available = time_available


class Pet:
    def __init__(self, name, species, age, breed):
        self.name = name
        self.species = species
        self.age = age
        self.breed = breed

    def get_pet_info(self):
        return {
            "name": self.name,
            "species": self.species,
            "age": self.age,
            "breed": self.breed
        }

    def update_pet_info(self, name, species, age, breed):
        self.name = name
        self.species = species
        self.age = age
        self.breed = breed


class Task:
    def __init__(self, task_name, duration, priority, task_type, is_completed=False):
        self.task_name = task_name
        self.duration = duration
        self.priority = priority
        self.task_type = task_type
        self.is_completed = is_completed

    def mark_completed(self):
        self.is_completed = True

    def update_task(self, task_name, duration, priority, task_type):
        self.task_name = task_name
        self.duration = duration
        self.priority = priority
        self.task_type = task_type

    def get_task_details(self):
        return {
            "task_name": self.task_name,
            "duration": self.duration,
            "priority": self.priority,
            "task_type": self.task_type,
            "completed": self.is_completed
        }


class Scheduler:
    def __init__(self, tasks, time_available):
        self.tasks = tasks
        self.time_available = time_available
        self.daily_plan = []

    def add_task(self, task):
        self.tasks.append(task)

    def edit_task(self, index, updated_task):
        self.tasks[index] = updated_task

    def generate_plan(self):
        pass  # we will implement this next

    def explain_plan(self):
        pass