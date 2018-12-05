from flask import Blueprint

users_blueprint = Blueprint('users', __name__)
from . import users_controller
