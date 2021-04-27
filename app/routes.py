from app import app, db
from flask import render_template, request, redirect, url_for, flash
from app.models import Post, User
from flask_login import login_user, logout_user

# Testing - 
# Development - 
# Production - 

# file-watcher

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        p = Post(email='derekh@codingtemple.com', body=request.form.get('body_text'))
        db.session.add(p)
        db.session.commit()
        flash('Blog post created successfully', 'info')
        return redirect(url_for('home'))
    return render_template('index.html')


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