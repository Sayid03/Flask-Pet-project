from flask import Blueprint, render_template, redirect

from ..functions import save_picture
from ..forms import RegistrationForm
from ..models.user import User
from ..extensions import db, bcrypt

user = Blueprint('user', __name__)

@user.route('/user/register', methods=['POST', 'GET'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        avatar_filename = save_picture(form.avatar.data)
        user = User(name= form.name.data,
                    login= form.login.data,
                    avatar= avatar_filename,
                    password= hashed_password)
        db.session.add(user)
        db.session.commit()
        print(f"User - {form.name.data} has signed up!")
        return redirect('/')
    else:
        print('Registration Error')
    return render_template('user/register.html', form=form)