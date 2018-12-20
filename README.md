# flask_api_mvc

Steps to add new Resource

Models

Controllers

App

1.
# inside initialize_extensions
from app.models import NewModel

2.
# inside register_blueprints
from app.controllers import new_controller

Run application:

export FLASK_APP=main.py
flask run
