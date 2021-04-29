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
    moment.init_app(app)

    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    login_manager.login_message = 'You do not have access to this page. Please log in.'
    login_manager.login_message_category = 'warning'


    from app.blueprints.authentication import bp as auth
    app.register_blueprint(auth)

    from app.blueprints.main import bp as main
    app.register_blueprint(main)

    from .import models

    with app.app_context():
        from .import context_processors
        
        from app.blueprints.shop import bp as shop
        app.register_blueprint(shop)

        from .import seed

        
    return app