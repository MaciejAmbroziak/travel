import os
from os import getenv

from flask import Flask
from travel.server.routes import index_blueprint

from travel.services.login import LOGIN_MANAGER
from travel.db import DB



def create_app() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(index_blueprint)
    app.config['SQLALCHEMY_DATABASE_URI'] = getenv('SQLALCHEMY_DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = os.urandom(15)
    DB.init_app(app)
    DB.create_all(app.app_context().push())
    LOGIN_MANAGER.init_app(app)
    return app

