from app import app
from flask import Flask, render_template

@app.route('/')
@app.route('/index')
def index():
    user = {'username':'Steven'}
    return render_template('index.html', title='Home', user=user)