from app import create_app, db
from app.models import PipelineRun
# from . import routes

app = create_app()

# with app.app_context():
#     # Now you can safely interact with the database
#     db.create_all()  # This will create all tables
#     pipeline_runs = PipelineRun.query.all()  # Example query
#     print(pipeline_runs)

if __name__ == "__main__":
    app.run(debug=True)
