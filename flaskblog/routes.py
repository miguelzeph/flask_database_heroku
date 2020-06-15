from flaskblog import app, bcrypt, db
from flask import render_template, flash, url_for, redirect
from flask_login import login_user, logout_user

from flaskblog.forms import RegistrationForm, LoginForm, PostForm
from flaskblog.models import User, Post
@app.route('/')
def index():

    posts = [
        {"title":'First Content','description':'Firts Description'},
        {"title":'Second Content','description':'Second Description'}
    ]
    return render_template('index.html',posts =posts)

@app.route('/about')
def about():
    
    return render_template('about.html',title='About')

@app.route('/register',methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():

        #Class USER -> *Id, username, email, password, *posts
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(
            username = form.username.data,
            email = form.email.data,
            password = hashed_password
        )
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {user.username}','success') 
        return redirect(url_for('login'))
    return render_template('register.html',title='Register', form=form)

@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            flash(f'You are Logged in','success')
            return redirect(url_for('index'))
        else:
            flash(f'Invalid Credentials','danger')

    return render_template('login.html',title='Register', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/create_post',methods=["GET","POST"])
def create_post():
    form = PostForm()
    return render_template('create_post.html',title='Add Post', form = form)