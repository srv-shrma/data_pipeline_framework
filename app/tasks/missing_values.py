import pandas as pd
from .base_task import BaseTask

class MissingValuesTask(BaseTask):
    def execute(self, data):
        columns = self.params.get('columns')
        threshold = self.params.get('threshold', 0.0)
        missing_report = {}
        
        for column in columns:
            missing_percentage = data[column].isnull().mean()
            missing_report[column] = {
                "missing_percentage": missing_percentage,
                "is_above_threshold": missing_percentage > threshold
            }
        
        return missing_report
