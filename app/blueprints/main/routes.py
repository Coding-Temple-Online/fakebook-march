from app import db
from flask import render_template, request, redirect, url_for, flash
from app.blueprints.main import bp as main
from app.models import Post
from app.blueprints.authentication.models import User
from flask_login import login_user, logout_user, current_user

@main.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        p = Post(email='derekh@codingtemple.com', body=request.form.get('body_text'), user_id=current_user.get_id())
        db.session.add(p)
        db.session.commit()
        flash('Blog post created successfully', 'info')
        return redirect(url_for('main.home'))
    context = {
        'posts': [p.to_dict() for p in Post.query.filter_by(user_id=current_user.get_id()).all()]
    }
    return render_template('index.html', **context)


@main.route('/contact')
def contact():
    context = {
        'help': 'yes',
        'page': 124567,
        'yellow': 'jaune'
    }
    return render_template('contact.html', **context)

@main.route('/blog')
def blog():
    context = {
        'posts': [p.to_dict() for p in Post.query.all()]
    }
    return render_template('blog.html', **context)