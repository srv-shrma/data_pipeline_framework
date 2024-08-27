from .tasks.missing_values import MissingValuesTask
from .tasks.duplicate_rows import DuplicateRowsTask

class Pipeline:
    TASK_MAPPING = {
        "missing_values": MissingValuesTask,
        "duplicate_rows": DuplicateRowsTask
    }

    def __init__(self, task_configs):
        self.task_configs = task_configs
        self.tasks = self._load_tasks()

    def _load_tasks(self):
        tasks = []
        for task_config in self.task_configs:
            task_name = task_config["task"]
            params = task_config["params"]
            task_class = self.TASK_MAPPING.get(task_name)
            if task_class:
                tasks.append(task_class(params))
        return tasks

    def run(self, data):
        results = {}
        for task in self.tasks:
            task_result = task.execute(data)
            results[task.__class__.__name__] = task_result
        return results
