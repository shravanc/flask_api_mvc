import os
from flask import Blueprint, current_app

from app.controllers.users_controller import index as users_index
from app.controllers.users_controller import home as users_home



template_dir = os.path.abspath('app/views/users')

user_blueprints = Blueprint('users', 'api', template_folder=template_dir)
user_blueprints.add_url_rule('/users', view_func=users_index, methods=['GET'])
user_blueprints.add_url_rule('/home', view_func=users_home, methods=['GET'])



