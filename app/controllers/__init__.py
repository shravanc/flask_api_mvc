import os
from flask import Blueprint, current_app

template_dir = os.path.abspath('app/views/users')
user_blueprints = Blueprint('users', 'api', template_folder=template_dir)

from . import users_controller
