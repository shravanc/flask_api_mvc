from flask import Blueprint

user_blueprints = Blueprint('users', 'api')

from . import users_controller
