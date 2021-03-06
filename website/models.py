#create db models
# importing from de current package
from datetime import timezone
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    #func.now is the current dayTime
    date = db.Column(db. DateTime(timezone=True), default=func.now())

    #foreign key
    #one to many relationship
    #one user can have many notes
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
class User(db.Model, UserMixin):
    #creating columns
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    first_name = db.Column(db.String(150), nullable=False)

    notes = db.relationship('Note')