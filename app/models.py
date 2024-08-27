from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class PipelineRun(db.Model):
    # __tablename__ = 'pipeline_run'  # Explicitly define the table name
    id = db.Column(db.Integer, primary_key=True)
    tasks = db.Column(db.String, nullable=False)
    status = db.Column(db.String, nullable=False)
    result = db.Column(db.Text, nullable=True)

    def __init__(self, tasks, status, result=None):
        self.tasks = tasks
        self.status = status
        self.result = result
