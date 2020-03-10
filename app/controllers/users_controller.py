from flask import request, jsonify, render_template

#from . import user_blueprints
from app.models.user import User
from app.models.rating import Rating

from app import mongo
from app.jobs.user_job import new_task
import app.helpers.user_service as us

#@user_blueprints.route('/users')
def index():
    users = User.get()
    new_task.delay()
    us.say_hello('hello')
    return jsonify({'data': users})


def ratings():
  user_ratings = Rating.query.all()
  ratings = []
  for rating in user_ratings:
    d1 = {}
    d1["user_id"] = rating.user_id
    d1["item_id"] = rating.item_id
    d1["rating"]  = rating.rating
    ratings.append(d1)
  return jsonify({'data': ratings})


#@user_blueprints.route('/home')
def home():
    return render_template('index.html')

