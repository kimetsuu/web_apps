import os

from flask import Flask
import dotenv

# Things to import at the beginning
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

# Declarations to insert before the create_app function:
class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)

def create_app(test_config=None):
    app = Flask(__name__)

    dotenv.load_dotenv()

    # A secret for signing session cookies
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("SQLALCHEMY_DATABASE_URI")   

    db.init_app(app)

    # Register blueprints
    # (we import main from here to avoid circular imports in the next lab)
    from . import main

    app.register_blueprint(main.bp)
    return app
