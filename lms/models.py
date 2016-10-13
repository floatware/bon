from sqlalchemy import Column, Integer, String
from lms import db

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(50), unique=True)
  email = db.Column(db.String(120), unique=True)

  def __init__(self, username, email):
    self.username = username
    self.email = email

  def __repr__(self):
    return '<User %r>' % (self.username)