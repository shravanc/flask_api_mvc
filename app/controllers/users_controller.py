from flask import request, jsonify

from . import users_blueprint
from app.models.user import User
from app import mongo


@users_blueprint.route('/users')
def get_users():
    users = User.get()
    return jsonify({'data': users})
