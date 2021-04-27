from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

# flask-sqlalchemy- "Flaskifies" our sqlalchemy functionality
    # sqlalchemy  - Handles connecting to the database and building models
# flask-migrate   - Handles the action of updating our database.
# pyscopg2-binary - Handles the actual queries that we'll run against our database


app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)

from .import routes, models