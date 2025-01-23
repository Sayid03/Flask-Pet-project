from datetime import datetime
from flask_login import UserMixin

from ..extensions import db, login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(80), default='user')
    name = db.Column(db.String(80))
    login = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(200))
    date = db.Column(db.DateTime, default=datetime.utcnow)
    avatar = db.Column(db.String(200))
