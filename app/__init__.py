# função de fábrica

from flask import Flask
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from config import config


login_manager = LoginManager()
bootstrap = Bootstrap()
db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    db.init_app(app)
    bootstrap.init_app(app)
    login_manager.init_app(app)

    from .controllers.home import teste as home_blueprint
    app.register_blueprint(home_blueprint)

    from .controllers.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    return app
