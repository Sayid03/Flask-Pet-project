from datetime import datetime
from ..extensions import db

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    teacher = db.Column(db.String(258))
    subject = db.Column(db.String(258))
    student = db.Column(db.String(258))
    date = db.Column(db.DateTime, default=datetime.utcnow)
