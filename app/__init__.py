from flask import Flask

from flask_pymongo import PyMongo


mongo = PyMongo()

def create_app(config_filename=None):
    application = Flask(__name__, instance_relative_config=True)
    application.config.from_pyfile(config_filename)
    initialize_extensions(application)
    register_blueprints(application)
    return application

def initialize_extensions(application):
    mongo.init_app(application)
    from app.models.user import User


def register_blueprints(application):
    from app.controllers import users_blueprint

    application.register_blueprint(users_blueprint)


