from flask import request, jsonify, render_template

from . import user_blueprints
from app.models.user import User
from app import mongo
from app.jobs.user_job import new_task

@user_blueprints.route('/users')
def get_users():
    users = User.get()
    new_task.delay()
    return jsonify({'data': users})

@user_blueprints.route('/home')
def home():
    
    return render_template('index.html')
