import os
from app import celery, create_app, create_celery

app = create_app('development.cfg')
app.app_context().push()

