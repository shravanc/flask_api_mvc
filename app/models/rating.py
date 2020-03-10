from app import db
from sqlalchemy.dialects.postgresql import JSON


class Rating(db.Model):
  __tablename__ = 'ratings'


  id = db.Column(db.Integer, primary_key=True)
  user_id = db.Column(db.Integer)
  item_id = db.Column(db.Integer)
  rating  = db.Column(db.Integer)


  def __repr__(self):
    return '<id {}>'.format(self.id)



