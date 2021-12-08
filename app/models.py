from flask_login import UserMixin
from app import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(500))




"""
class Assessment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), index=True, nullable=False)
    code = db.Column(db.String(10), index=True, nullable=False)
    deadline = db.Column(db.DateTime)
    description = db.Column(db.String(1500), index=True)
    complete = db.Column(db.Boolean, default=False)
"""