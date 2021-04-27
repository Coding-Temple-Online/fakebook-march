from app import app, db
from flask import render_template, request, redirect, url_for, flash
from app.models import Post, User
from flask_login import login_user, logout_user, current_user

# Testing - 
# Development - 
# Production - 

# file-watcher

# How to do routing in <framework>
# How to create models using <framework>
# How to do user authentication in <framework>

@app.route('/', methods=['GET', 'POST'])
def home():
    # print("Current User:", current_user.is_authenticated)
    # print("Current User:", current_user.is_active)
    # print("Current User:", current_user.is_anonymous)
    # print("Current User:", current_user.get_id())
    if request.method == 'POST':
        p = Post(email='derekh@codingtemple.com', body=request.form.get('body_text'), user_id=current_user.get_id())
        db.session.add(p)
        db.session.commit()
        flash('Blog post created successfully', 'info')
        return redirect(url_for('home'))
    context = {
        'posts': [p.to_dict() for p in Post.query.filter_by(user_id=current_user.get_id()).all()]
    }
    return render_template('index.html', **context)


@app.route('/contact')
def contact():
    context = {
        'help': 'yes',
        'page': 124567,
        'yellow': 'jaune'
    }
    return render_template('contact.html', **context)

@app.route('/blog')
def blog():
    context = {
        'posts': [p.to_dict() for p in Post.query.all()]
    }
    return render_template('blog.html', **context)

@app.route('/logout')
def logout():
    logout_user()
    flash('You have logged out successfully.', 'warning')
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(email=request.form.get('email')).first()
        if user is None or not user.check_password(request.form.get('password')):
            flash('Either that user does not exist or the password is incorrect. Try again.', 'warning')
            return redirect(url_for('login'))
        remember_me = True if request.form.get('checked') is not None else False
        login_user(user, remember=remember_me)
        flash(f'Welome, {user.first_name} {user.last_name}! You have successfully logged in!', 'success')
        return redirect(url_for('home'))
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        u = User()
        u.from_dict(request.form)
        u.save()
        flash('Blog post created successfully', 'info')
        return redirect(url_for('login'))
    return render_template('register.html')