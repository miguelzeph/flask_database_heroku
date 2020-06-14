from flaskblog import app
from flask import render_template, flash

from flaskblog.forms import RegistrationForm, LoginForm

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
       flash(f'User Created','sucess') 
    return render_template('register.html',title='Register', form=form)