from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_moment import Moment

# flask-sqlalchemy- "Flaskifies" our sqlalchemy functionality
    # sqlalchemy  - Handles connecting to the database and building models
# flask-migrate   - Handles the action of updating our database.
# pyscopg2-binary - Handles the actual queries that we'll run against our database
db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
moment = Moment()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    moment.init_app(app)

    from app.blueprints.authentication import bp as auth
    app.register_blueprint(auth)

    from app.blueprints.main import bp as main
    app.register_blueprint(main)

    from .import models

    return app