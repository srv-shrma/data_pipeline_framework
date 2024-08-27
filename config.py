# config.py

class Config:
    # Flask settings
    SECRET_KEY = 'your_secret_key_here'
    SQLALCHEMY_DATABASE_URI = 'sqlite:////Users/neha/Desktop/work/data_pipeline_framework/instance/data_pipeline.db'  
    # /Users/neha/Desktop/work/data_pipeline_framework/instance/your_database.db
    # instance/your_database.db# Update with your actual database URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
