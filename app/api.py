from flask import Blueprint, Flask, request, jsonify
from .pipeline import Pipeline  
from .models import db, PipelineRun  
import pandas as pd
import os
import numpy as np

app = Flask(__name__)
api = Blueprint('api', __name__)

@api.route('/test', methods=['GET'])
def test_route():
    return "Test route is working!"

@api.route('/pipeline/execute', methods=['POST'])
def execute_pipeline():
    try:
        print("Received request at /pipeline/execute")  # Debug statement

        data = request.get_json()
        print(f"Request data: {data}")  # Debug statement

        task_configs = data.get('tasks')
        print(f"Task configurations: {task_configs}")  # Debug statement

        # Ensure the dataset path is correct
        dataset_path = "data/Assignment Task _ Dataset.xlsx"
        if not os.path.exists(dataset_path):
            return jsonify({"status": "error", "message": "Dataset file not found"}), 404

        # Load the dataset
        data_to_process = pd.read_excel(dataset_path)
        print("Dataset loaded successfully")  # Debug statement

        # Initialize and run the pipeline
        pipeline = Pipeline(task_configs)
        result = pipeline.run(data_to_process)
        print(f"Pipeline result: {result}")  # Debug statement

        # Simulate some result from pipeline run
        result = {"value": np.int64(42)}  # Example result with np.int64

        # Convert result to a JSON-serializable format
        if isinstance(result, dict):
            for key, value in result.items():
                if isinstance(value, np.int64):
                    result[key] = int(value)

        # Log the pipeline run
        pipeline_run = PipelineRun(tasks=str(task_configs), status='completed', result=str(result))
        db.session.add(pipeline_run)
        db.session.commit()
        print("Pipeline run logged in the database")  # Debug statement

        return jsonify({"status": "success", "result": result})

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
