from flask import Blueprint, render_template, request, redirect
from ..models.post import Post
from ..extensions import db

post = Blueprint('post', __name__)

@post.route('/post/create', methods=['POST', 'GET'])
def create():
    if request.method == 'POST':
        teacher = request.form.get('teacher')
        subject = request.form.get('subject')
        student = request.form.get('student')

        post = Post(teacher=teacher, subject=subject, student=student)
        
        try:
            db.session.add(post)
            db.session.commit()
            return redirect('/')
        except Exception as e:
            print(str(e))

    else:
        return render_template('post/create.html')