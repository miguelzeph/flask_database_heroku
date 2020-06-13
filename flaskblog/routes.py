from flaskblog import app
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    title = 'About'
    return render_template('about.html',title=title)