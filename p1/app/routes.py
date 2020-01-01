from app import app
from flask import Flask, render_template
from app.forms import LoginForm


@app.route('/login')
def loin():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)
@app.route('/')
@app.route('/index')
def index():
    user = {'username':'Steven'}
    posts = [
        {
            'author': {'username': 'Svengali'},
            'body': 'I am the anti-clown.'
        },
        {
            'author': {'username': 'Bubble-ishus'},
            'body': 'Ba boo, ba ba boo!'

        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)