from flask import Flask
from .extentions import db


def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'

    db.init_app(app)
    with app.app_context():
        db.create_all()

    return app