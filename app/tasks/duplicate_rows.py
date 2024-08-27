import pandas as pd
from .base_task import BaseTask

class DuplicateRowsTask(BaseTask):
    def execute(self, data):
        columns = self.params.get('columns')
        if columns:
            duplicates = data.duplicated(subset=columns).sum()
        else:
            duplicates = data.duplicated().sum()

        return {"duplicates": duplicates}
