from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .api import api
from .models import db

# db = SQLAlchemy()
migrate = Migrate()

def create_app():

    app = Flask(__name__)

    # Load configuration
    app.config.from_object('config.Config')

    # Initialize SQLAlchemy with the app
    db.init_app(app)
    migrate.init_app(app, db)

    # Import and register your routes or blueprints
    app.register_blueprint(api)

    # In your create_app function
    app.logger.debug(f"App created: {app}")
    app.logger.debug(f"DB initialized: {db}")


    return app
