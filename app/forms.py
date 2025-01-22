from flask_wtf import FlaskForm
from wtforms import StringField

class RegistrationForm(FlaskForm):
    name = StringField()