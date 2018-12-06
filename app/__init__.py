from flask import Flask

from flask_pymongo import PyMongo
from celery import Celery

mongo = PyMongo()
celery = Celery('flask_api')

def create_app(config_filename=None):
    application = Flask(__name__, instance_relative_config=True)
    application.config.from_pyfile(config_filename)
    initialize_extensions(application)
    register_blueprints(application)
    create_celery(application)
    return application

def create_celery(application):
    celery.conf.update(application.config) 
    return celery

def initialize_extensions(application):
    mongo.init_app(application)
    from app.models.user import User


def register_blueprints(application):
    from app.controllers import user_blueprints
    application.register_blueprint(user_blueprints)


