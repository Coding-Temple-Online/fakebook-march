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

@main.route('/profile', methods=['GET', 'POST'])
def profile():
    if request.method == 'POST':
        user = User.query.get(current_user.id)
        if user is not None:
            user.first_name = request.form.get('first_name')
            user.last_name = request.form.get('last_name')
            user.set_email()


            if request.form.get('password') and request.form.get('confirm_password') and request.form.get('password') == request.form.get('confirm_password'):
                user.password = request.form.get('password')
            elif not request.form.get('password') and not request.form.get('confirm_password'):
                pass
            else:
                flash('There was an issue updating your information. Please try again.', 'warning')
                return redirect(url_for('main.profile'))
            db.session.commit()
            flash('User updated successfully', 'success')
            return redirect(url_for('main.profile'))
    return render_template('profile.html')