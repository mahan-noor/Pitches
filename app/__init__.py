from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from config import config_options

bootstrap = Bootstrap()
db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)

    # Setting up configuration
    app.config.from_object(DevConfig)
    app.config.from_pyfile("config.py")

    # Initializing Flask Extensions
    bootstrap.init_app(app)
    db.init_app(app)

    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # setting config
    from .requests import configure_request
    configure_request(app)

    return app

