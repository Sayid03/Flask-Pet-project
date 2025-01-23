from datetime import datetime

from ..extensions import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(80), default='user')
    name = db.Column(db.String(80))
    login = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(200))
    date = db.Column(db.DateTime, default=datetime.utcnow)
    avatar = db.Column(db.String(200))
